import os
import torch
import torch_nebula

from deepspeed.runtime.checkpoint_engine.checkpoint_engine import \
    CheckpointEngine
from deepspeed.utils import logger, log_dist
from deepspeed.nebula.constants import *


def _get_tag_from_path(path):
    return os.path.basename(os.path.dirname(path))


class NebulaCheckpointEngine(CheckpointEngine):
    def __init__(self, config_params=None):
        super().__init__(config_params)
        self.checkpoint = None
        self.tag_flag = None
        self.enable_nebula_load = config_params.enable_nebula_load
        self.nebula_load_path = config_params.load_path
        if self.nebula_load_path is None:
            self.nebula_load_path = config_params.persistent_storage_path

        nebula_config_params = {
            NEBULA_PERSISTENT_STORAGE_PATH: config_params.persistent_storage_path,
            NEBULA_PERSISTENT_TIME_INTERVAL: config_params.persistent_time_interval,
            NEBULA_NUM_OF_VERSION_IN_RETENTION:
            config_params.num_of_version_in_retention,
        }
        torch_nebula.init(**nebula_config_params)

    def create(self, tag):
        log_dist(f"[Nebula] Start Checkpoint for tag:{tag}", ranks=[0])
        # -2 means: customer needs to  explicitly tell nebula
        # current checkpoint is complete by commit methond.
        self.checkpoint = torch_nebula.Checkpoint(tag, -2)

    def save(self, state_dict, path: str):
        tag = _get_tag_from_path(path)
        partititon_name = os.path.basename(path)
        logger.info(f"[Nebula] Saving {partititon_name} under tag{tag}...")
        self.checkpoint.save(partititon_name, state_dict)
        logger.info(f"[Nebula] Saved {partititon_name} under tag{tag}.")
        return None

    def load(self, path: str, map_location=None):
        tag = _get_tag_from_path(path)
        first_load_flag = self.tag_flag is None or self.tag_flag == tag
        if not self.enable_nebula_load and first_load_flag:
            self.tag_flag = tag
            logger.info(
                f"[Nebula] Disable nebula load. Loading checkpoint from {path}...")
            partition = torch.load(path, map_location=map_location)
            logger.info(
                f"[Nebula] Disable nebula load. Loaded checkpoint from {path}...")
            return partition

        partititon_name = os.path.basename(path)
        logger.info(
            f"[Nebula] Loading {path} under tag{tag} from {self.nebula_load_path}...")

        checkpoint = None
        if tag is None:
            checkpoint = torch_nebula.get_latest_checkpoint(
                persist_path=self.nebula_load_path)
            if checkpoint is None or (checkpoint is not None and checkpoint.tag == ''):
                logger.warning(f"Unable to find latest valid checkpoint from Nebula!")
                return None
        else:
            checkpoint = torch_nebula.get_checkpoint(tag=tag,
                                                     persist_path=self.nebula_load_path)
        partition = checkpoint.load(partititon_name, map_location=map_location)
        logger.info(
            f"[Nebula] Loaded {path} under tag{tag} from {self.nebula_load_path}.")
        return partition

    def commit(self, tag):
        # nebula commit will be call when all files under give tag are ready to be persisted in the async way.
        logger.info(
            f"[Nebula] all files for {tag} are saved in tier1. It is ready to start persisting"
        )
        commit_rls = self.checkpoint.commit()
        if not commit_rls:
            logger.error(
                f"[Nebula] failed to commit the checkpoint, please check the log.")
            return False
        return commit_rls
