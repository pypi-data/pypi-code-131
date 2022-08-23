'''
Copyright 2021 The Microsoft DeepSpeed Team
'''
from deepspeed import utils

from .utils import *
from .backend import *
from .comm import *


class TorchBackend(Backend):
    """
        A light-weight wrapper class for torch.distributed API.
        Only a subset of functions are wrapped. Once the init_process_group
        is initialized, standard torch.distributed.* can be used directly
        so no need to wrap all the functions. We can keep adding wrappers as
        needed.
    """
    def __init__(self, backend, timeout, init_method, name='torch'):
        super(TorchBackend, self).__init__()
        self.torch_version_before_18 = older_torch()
        self.has_allgather_base = has_allgather_base()
        self.has_reduce_scatter_base = has_reduce_scatter_base()
        self.initialized = True
        self.name = name
        # Future functionality to support ds.initialize() on a single GPU
        # The idea is to fake that dist backend is initialized even when
        # it is not so we can run on a single GPU without doing any init_process_group
        self.single_gpu_mode = True
        self.init_process_group(backend, timeout, init_method)

    def init_process_group(self, backend, timeout, init_method):
        if not torch.distributed.is_initialized():
            torch.distributed.init_process_group(backend,
                                                 timeout=timeout,
                                                 init_method=init_method)
        self.using_mpi = torch.distributed.get_backend() == 'mpi'

    def all_reduce(self,
                   tensor,
                   op=torch.distributed.ReduceOp.SUM,
                   group=None,
                   async_op=False):
        op = self._reduce_op(op)
        return torch.distributed.all_reduce(tensor=tensor,
                                            op=op,
                                            group=group,
                                            async_op=async_op)

    def reduce(self, tensor, dst, op=ReduceOp.SUM, group=None, async_op=False):
        return torch.distributed.reduce(tensor=tensor,
                                        dst=dst,
                                        op=self._reduce_op(op),
                                        group=group,
                                        async_op=async_op)

    def reduce_scatter(self,
                       output,
                       input_list,
                       op=ReduceOp.SUM,
                       group=None,
                       async_op=False):
        return torch.distributed.reduce_scatter(output=output,
                                                input_list=input_list,
                                                op=self._reduce_op(op),
                                                group=group,
                                                async_op=async_op)

    def broadcast(self, tensor, src, group=None, async_op=False):
        return torch.distributed.broadcast(tensor=tensor,
                                           src=src,
                                           group=group,
                                           async_op=async_op)

    def all_gather(self, tensor_list, tensor, group=None, async_op=False):
        return torch.distributed.all_gather(tensor_list=tensor_list,
                                            tensor=tensor,
                                            group=group,
                                            async_op=async_op)

    def all_gather_base(self, output_tensor, input_tensor, group=None, async_op=False):
        if self.has_allgather_base:
            return torch.distributed.distributed_c10d._all_gather_base(
                output_tensor=output_tensor,
                input_tensor=input_tensor,
                group=group,
                async_op=async_op)
        else:
            utils.logger.warning(
                "unable to find torch.distributed._all_gather_base. will fall back to "
                "torch.distributed.reduce_scatter which will result in suboptimal performance. "
                "please consider upgrading your pytorch installation.")
            pass

    def reduce_scatter_base(self,
                            output_tensor,
                            input_tensor,
                            group=None,
                            async_op=False):
        if self.has_reduce_scatter_base:
            return torch.distributed._reduce_scatter_base(output_tensor,
                                                          input_tensor,
                                                          group=group,
                                                          async_op=async_op)
        else:
            utils.logger.warning(
                "unable to find torch.distributed._reduce_scatter_base. will fall back to "
                "torch.distributed.reduce_scatter which will result in suboptimal performance. "
                "please consider upgrading your pytorch installation.")
            pass

    def all_to_all_single(self,
                          output,
                          input,
                          output_split_sizes=None,
                          input_split_sizes=None,
                          group=None,
                          async_op=False):
        return torch.distributed.all_to_all_single(output=output,
                                                   input=input,
                                                   output_split_sizes=output_split_sizes,
                                                   input_split_sizes=input_split_sizes,
                                                   group=group,
                                                   async_op=async_op)

    def send(self, tensor, dst, group=None, tag=0):
        return torch.distributed.send(tensor=tensor, dst=dst, group=group, tag=tag)

    def recv(self, tensor, src=None, group=None, tag=0):
        return torch.distributed.recv(tensor=tensor, src=src, group=group, tag=tag)

    def isend(self, tensor, dst, group=None, tag=0):
        return torch.distributed.isend(tensor=tensor, dst=dst, group=group, tag=tag)

    def irecv(self, tensor, src=None, group=None, tag=0):
        return torch.distributed.irecv(tensor=tensor, src=src, group=group, tag=tag)

    def gather(self, tensor, gather_list=None, dst=0, group=None, async_op=False):
        return torch.distributed.gather(tensor=tensor,
                                        gather_list=gather_list,
                                        dst=dst,
                                        group=group,
                                        async_op=async_op)

    def scatter(self, tensor, scatter_list=None, src=0, group=None, async_op=False):
        return torch.distributed.scatter(tensor=tensor,
                                         scatter_list=scatter_list,
                                         src=src,
                                         group=group,
                                         async_op=async_op)

    def barrier(self):
        return torch.distributed.barrier()

    def get_rank(self, group=None):
        return torch.distributed.get_rank(group=group)

    def get_world_size(self, group=None):
        return torch.distributed.get_world_size(group=group)

    def is_initialized(self):
        return torch.distributed.is_initialized()

    def get_backend(self, group=None):
        return torch.distributed.get_backend(group=group)

    def new_group(self, ranks):
        return torch.distributed.new_group(ranks)

    def get_global_rank(self, group, group_rank):
        return torch.distributed.distributed_c10d._get_global_rank(group, group_rank)

    def get_world_group(self):
        return torch.distributed.group.WORLD

    def destroy_process_group(self, group=None):
        return torch.distributed.destroy_process_group(group=group)

    def _reduce_op(self, op):
        '''
            Helper function. If the op provided is not a torch.dist.ReduceOp, convert it and return
        '''
        if not isinstance(op, torch.distributed.ReduceOp):
            if op == ReduceOp.SUM:
                op = torch.distributed.ReduceOp.SUM
            elif op == ReduceOp.PRODUCT:
                op = torch.distributed.ReduceOp.PRODUCT
            elif op == ReduceOp.AVG:
                op = torch.distributed.ReduceOp.AVG
            elif op == ReduceOp.MIN:
                op = torch.distributed.ReduceOp.MIN
            elif op == ReduceOp.MAX:
                op = torch.distributed.ReduceOp.MAX
            elif op == ReduceOp.BAND:
                op = torch.distributed.ReduceOp.BAND
            elif op == ReduceOp.BOR:
                op = torch.distributed.ReduceOp.BOR
            elif op == ReduceOp.BXOR:
                op = torch.distributed.ReduceOp.BXOR
        return op


# This will become a light-weight wrapper around torch.distributed functions
# TODO: create some example to show how this wrapper can help profile communication
# TODO: make sure there is no performance regression with this approach
# TODO: explore monkey-patching if this does not work
