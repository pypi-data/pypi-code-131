from .utils import check_wandb_availability
from .monitor import Monitor

import deepspeed.comm as dist


class WandbMonitor(Monitor):
    def __init__(self, monitor_config):
        super().__init__(monitor_config)
        check_wandb_availability()
        import wandb

        self.enabled = monitor_config.wandb_config.enabled
        self.group = monitor_config.wandb_config.group
        self.team = monitor_config.wandb_config.team
        self.project = monitor_config.wandb_config.project

        if self.enabled and dist.get_rank() == 0:
            wandb.init(project=self.project, group=self.group, entity=self.team)

    def log(self, data, step=None, commit=None, sync=None):
        if self.enabled and dist.get_rank() == 0:
            import wandb
            return wandb.log(data, step=step, commit=commit, sync=sync)

    def write_events(self, event_list):
        if self.enabled and dist.get_rank() == 0:
            for event in event_list:
                label = event[0]
                value = event[1]
                step = event[2]
                self.log({label: value}, step=step)
