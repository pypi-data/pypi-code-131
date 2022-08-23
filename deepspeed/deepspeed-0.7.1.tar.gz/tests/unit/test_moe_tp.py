import torch
import deepspeed
import pytest
from .common import distributed_test
from .simple_model import args_from_dict
from .util import required_torch_version
from deepspeed.moe.layer import MoE


@pytest.mark.parametrize("ep_size, tp_size, enable_expert_tp, use_residual",
                         [
                             (1,
                              2,
                              False,
                              False),
                             (1,
                              2,
                              True,
                              False),
                             (1,
                              2,
                              False,
                              True),
                             (1,
                              2,
                              True,
                              True),
                             (1,
                              4,
                              False,
                              False),
                             (1,
                              4,
                              True,
                              False),
                             (1,
                              4,
                              False,
                              True),
                             (1,
                              4,
                              True,
                              True),
                             (2,
                              2,
                              False,
                              False),
                             (2,
                              2,
                              True,
                              False),
                             (2,
                              2,
                              False,
                              True),
                             (2,
                              2,
                              True,
                              True),
                         ])
def test_moe_tensor_parallel(tmpdir, ep_size, tp_size, enable_expert_tp, use_residual):
    if not required_torch_version():
        pytest.skip("DeepSpeed MoE tests need torch 1.8 or higher to run correctly")

    config_dict = {
        "train_batch_size": 8,
        "steps_per_print": 1,
        "fp16": {
            "enabled": True
        }
    }
    args = args_from_dict(tmpdir, config_dict)
    hidden_dim = 16

    class MPU():
        def __init__(self, tp_world_size):
            self.rank = deepspeed.comm.get_rank()
            self.world_size = deepspeed.comm.get_world_size()
            self.tp_world_size = tp_world_size

            for i in range(0, self.world_size, tp_world_size):
                ranks = range(i, i + tp_world_size)
                group = deepspeed.comm.new_group(ranks)
                if self.rank in ranks:
                    self.tp_group = group

            for i in range(0, tp_world_size):
                ranks = range(i, self.world_size, tp_world_size)
                group = deepspeed.comm.new_group(ranks)
                if self.rank in ranks:
                    self.dp_group = group

        def get_model_parallel_rank(self):
            return self.rank % self.tp_world_size

        def get_model_parallel_world_size(self):
            return self.tp_world_size

        def get_data_parallel_rank(self):
            return self.rank // self.tp_world_size

        def get_data_parallel_world_size(self):
            return self.world_size // self.tp_world_size

        def get_data_parallel_group(self):
            return self.dp_group

        def get_model_parallel_group(self):
            return self.tp_group

    @distributed_test(world_size=[4])
    def _test_moe(args, hidden_dim, ep_size, tp_size, enable_expert_tp, use_residual):

        # TODO: replace this with a true parallel mlp in the future
        # and run convergence tests

        tensor_parallel_expert = torch.nn.Sequential(
            torch.nn.Linear(hidden_dim,
                            4 * hidden_dim // tp_size),
            torch.nn.ReLU(),
            torch.nn.Linear(4 * hidden_dim // tp_size,
                            hidden_dim))

        # set num experts to world size
        world_size = deepspeed.comm.get_world_size()
        model = MoE(
            hidden_size=hidden_dim,
            expert=tensor_parallel_expert,
            num_experts=world_size,
            ep_size=ep_size,
            use_residual=use_residual,
            enable_expert_tensor_parallelism=enable_expert_tp,
        )
        optimizer = torch.optim.AdamW(params=model.parameters())
        model, _, _, _ = deepspeed.initialize(args=args,
                                              model=model,
                                              optimizer=optimizer,
                                              dist_init_required=False,
                                              mpu=MPU(tp_size))

        assert model.num_local_experts == world_size // ep_size
        if enable_expert_tp:
            assert deepspeed.utils.groups._get_expert_model_parallel_world_size(
            ) == tp_size
        else:
            assert deepspeed.utils.groups._get_expert_model_parallel_world_size() == 1

    _test_moe(args=args,
              hidden_dim=hidden_dim,
              ep_size=ep_size,
              tp_size=tp_size,
              enable_expert_tp=enable_expert_tp,
              use_residual=use_residual)
