# TODO: add tests with model parallelism for activation partitioning and other features.

from copy import deepcopy

import pytest

import torch

import deepspeed

ckpt = deepspeed.checkpointing.checkpoint

from .common import distributed_test


def _compute(module, *inputs, do_checkpoint=False):
    if do_checkpoint:
        outputs = ckpt(module, *inputs)
    else:
        outputs = module(*inputs)

    if torch.is_tensor(outputs):
        outputs = (outputs, )

    sum(o.sum() for o in outputs if torch.is_tensor(o) and o.requires_grad).backward()

    grads = [p.grad for p in module.parameters()]
    input_grads = [inp.grad for inp in inputs if torch.is_tensor(inp)]

    return {
        'outputs': outputs,
        'module_grads': grads,
        'input_grads': input_grads,
    }


def _prep_inputs(*inputs):
    _inputs = []

    for inp in inputs:
        inp = deepcopy(inp)
        if torch.is_tensor(inp):
            inp = inp.cuda()
        _inputs.append(inp)

    return tuple(_inputs)


def _match_outputs(ref, tgt):
    assert type(ref) == type(tgt)
    if type(ref) in [list, tuple]:
        for x, y in zip(ref, tgt):
            _match_outputs(x, y)
    elif not torch.is_tensor(ref):
        assert ref == tgt
    elif ref.is_floating_point():
        assert torch.allclose(ref, tgt)
    else:
        assert torch.equal(ref, tgt)


# This is distributed because checkpoint() assumes that deepspeed.comm is initialized.
# deepspeed.comm is used with activation partitioning, but not for these simple cases.
@distributed_test(world_size=1)
def _test_activation_checkpoint(module, *inputs):
    # Move to device
    module.cuda()

    # Get rid of dropouts until we fork the RNG between tests.
    module.eval()

    module_ = deepcopy(module)
    inputs_ = _prep_inputs(*inputs)
    base = _compute(module_, *inputs_, do_checkpoint=False)

    module_ = deepcopy(module)
    inputs_ = _prep_inputs(*inputs)
    test = _compute(module_, *inputs_, do_checkpoint=True)

    for group in base.keys():
        for b, t in zip(base[group], test[group]):
            _match_outputs(b, t)


# This is distributed because checkpoint() assumes that deepspeed.comm is initialized.
# deepspeed.comm is used with activation partitioning, but not for these simple cases.
@distributed_test(world_size=1)
def _test_activation_checkpoint_ordering(module, expected_ordering, *inputs):
    # Move to device
    module.cuda()

    # Get rid of dropouts until we fork the RNG between tests.
    module.eval()

    module_ = deepcopy(module)
    inputs_ = _prep_inputs(*inputs)
    test = _compute(module_, *inputs_, do_checkpoint=True)

    outputs = test['outputs']
    test_ordering = []
    for item in outputs:
        if type(item) in [list, tuple]:
            test_ordering += [torch.is_tensor(t) for t in item]
        else:
            test_ordering += [torch.is_tensor(item)]

    assert expected_ordering == test_ordering


#
# Helpers
#


class MaskedLinear(torch.nn.Linear):
    def forward(self, x, mask):
        out = super().forward(x)
        if mask.is_floating_point():
            out = out * mask
        else:
            # must cast BoolTensor in older torch versions
            out = out * mask.type_as(out)
        return out


class MaskedLinearSeq(MaskedLinear):
    """Tests pipeline modules by also returning the mask."""
    def forward(self, x, mask):
        return super().forward(x, mask), mask


class MaskedLinearSeqDup(MaskedLinearSeq):
    """MaskedLinearSeq, but with more outputs than inputs and in a different order."""
    def forward(self, x, mask):
        dup = x.clone().detach() * 1.38  # just an arbitrary scaling
        x, mask = super().forward(x, mask)
        return dup, x, mask


HIDDEN_DIM = 20


def _mixed_mask(size=HIDDEN_DIM):
    entries = torch.randn(size)
    mask = torch.where(entries > 0, torch.ones(size), torch.zeros(size))
    mask = mask.bool()
    return mask


def _bool_to_float(btensor, dtype=torch.float32):
    """Converts a torch.BoolTensor to an equivalent dtype. """
    ones = torch.ones(size=btensor.size(), dtype=dtype)
    zeros = torch.zeros(size=btensor.size(), dtype=dtype)
    return torch.where(btensor, ones, zeros)


#
# Tests
#


def test_ckpt_inputs1_outputs1():
    module = torch.nn.Linear(HIDDEN_DIM, HIDDEN_DIM)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs)


# both bool and float are important, as bool is not differentiable
@pytest.mark.parametrize('mask',
                         [
                             _mixed_mask(),
                             _bool_to_float(_mixed_mask()),
                         ])
def test_ckpt_inputs2_outputs1(mask):
    module = MaskedLinear(HIDDEN_DIM, HIDDEN_DIM)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs, mask)


@pytest.mark.parametrize('mask',
                         [
                             _mixed_mask(),
                             _bool_to_float(_mixed_mask()),
                         ])
def test_ckpt_inputs2_outputs2(mask):
    module = MaskedLinearSeq(HIDDEN_DIM, HIDDEN_DIM)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs, mask)


@pytest.mark.parametrize('mask',
                         [
                             _mixed_mask(),
                             _bool_to_float(_mixed_mask()),
                         ])
def test_ckpt_inputs2_outputs3(mask):
    module = MaskedLinearSeqDup(HIDDEN_DIM, HIDDEN_DIM)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs, mask)


class DropMaskLinear(torch.nn.Linear):
    def forward(self, x, mask):
        return super().forward(x)


def test_ckpt_arg_none():
    module = DropMaskLinear(HIDDEN_DIM, HIDDEN_DIM)
    inputs = (torch.rand(HIDDEN_DIM), None)
    inputs[0].requires_grad = True
    _test_activation_checkpoint(module, *inputs)


class LinearNonTensorInput(torch.nn.Linear):
    def forward(self, x, non_tensor_input):
        return super().forward(x)


@pytest.mark.parametrize(
    'non_tensor_input',
    [None,
     2,
     True,
     (None,
      2.5),
     (None,
      True,
      torch.randn(HIDDEN_DIM))])
def test_ckpt_non_tensor_input(non_tensor_input):
    module = LinearNonTensorInput(HIDDEN_DIM, HIDDEN_DIM)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs, non_tensor_input)


class LinearNonTensorOutput(torch.nn.Linear):
    def __init__(self, non_tensor_output):
        super().__init__(HIDDEN_DIM, HIDDEN_DIM)
        self.non_tensor_output = non_tensor_output

    def forward(self, x):
        out = super().forward(x)
        return out, self.non_tensor_output


@pytest.mark.parametrize(
    'non_tensor_output',
    [None,
     2,
     True,
     (None,
      2.5),
     (None,
      True,
      torch.randn(HIDDEN_DIM))])
def test_ckpt_non_tensor_output(non_tensor_output):
    module = LinearNonTensorOutput(non_tensor_output)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True
    _test_activation_checkpoint(module, inputs)


@pytest.mark.parametrize('non_tensor_output',
                         [
                             None,
                             (torch.randn(HIDDEN_DIM),
                              2.5),
                             (None,
                              torch.randn(HIDDEN_DIM),
                              True),
                             (None,
                              True,
                              torch.randn(HIDDEN_DIM))
                         ])
def test_ckpt_non_tensor_output_ordering(non_tensor_output):
    module = LinearNonTensorOutput(non_tensor_output)
    inputs = torch.rand(HIDDEN_DIM)
    inputs.requires_grad = True

    # First return is a tensor
    ordering = [True]
    if type(non_tensor_output) in [list, tuple]:
        ordering += [torch.is_tensor(t) for t in non_tensor_output]
    else:
        ordering += [torch.is_tensor(non_tensor_output)]
    _test_activation_checkpoint_ordering(module, ordering, inputs)
