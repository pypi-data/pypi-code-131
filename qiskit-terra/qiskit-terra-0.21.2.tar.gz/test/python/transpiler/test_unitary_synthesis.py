# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-function-docstring

"""
Tests for the default UnitarySynthesis transpiler pass.
"""

import unittest

from test import combine

from ddt import ddt, data

from qiskit import transpile
from qiskit.test import QiskitTestCase
from qiskit.providers.fake_provider import FakeVigo, FakeMumbaiFractionalCX
from qiskit.providers.fake_provider.fake_backend_v2 import FakeBackendV2, FakeBackend5QV2
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import QuantumVolume
from qiskit.converters import circuit_to_dag
from qiskit.transpiler.passes import UnitarySynthesis
from qiskit.quantum_info.operators import Operator
from qiskit.quantum_info.random import random_unitary
from qiskit.transpiler import PassManager, CouplingMap, Target, InstructionProperties
from qiskit.transpiler.exceptions import TranspilerError
from qiskit.exceptions import QiskitError
from qiskit.transpiler.passes import (
    Collect2qBlocks,
    ConsolidateBlocks,
    Optimize1qGates,
    SabreLayout,
    Depth,
    FixedPoint,
    FullAncillaAllocation,
    EnlargeWithAncilla,
    ApplyLayout,
    Unroll3qOrMore,
    CheckMap,
    BarrierBeforeFinalMeasurements,
    SabreSwap,
    TrivialLayout,
)
from qiskit.circuit.library import CXGate, ECRGate, UGate
from qiskit.circuit import Parameter


@ddt
class TestUnitarySynthesis(QiskitTestCase):
    """Test UnitarySynthesis pass."""

    def test_empty_basis_gates(self):
        """Verify when basis_gates is None, we do not synthesize unitaries."""
        qc = QuantumCircuit(1)
        qc.unitary([[0, 1], [1, 0]], [0])

        dag = circuit_to_dag(qc)

        out = UnitarySynthesis(None).run(dag)

        self.assertEqual(out.count_ops(), {"unitary": 1})

    @data(
        ["u3", "cx"],
        ["u1", "u2", "u3", "cx"],
        ["rx", "ry", "rxx"],
        ["rx", "rz", "iswap"],
        ["u3", "rx", "rz", "cz", "iswap"],
    )
    def test_two_qubit_synthesis_to_basis(self, basis_gates):
        """Verify two qubit unitaries are synthesized to match basis gates."""
        bell = QuantumCircuit(2)
        bell.h(0)
        bell.cx(0, 1)
        bell_op = Operator(bell)

        qc = QuantumCircuit(2)
        qc.unitary(bell_op, [0, 1])
        dag = circuit_to_dag(qc)

        out = UnitarySynthesis(basis_gates).run(dag)

        self.assertTrue(set(out.count_ops()).issubset(basis_gates))

    def test_two_qubit_synthesis_to_directional_cx_from_gate_errors(self):
        """Verify two qubit unitaries are synthesized to match basis gates."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap(conf.coupling_map)
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)
        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_swap_synthesis_to_directional_cx(self):
        """Verify two qubit unitaries are synthesized to match basis gates."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap(conf.coupling_map)
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.swap(qr[0], qr[1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)

        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_two_qubit_synthesis_to_directional_cx_multiple_registers(self):
        """Verify two qubit unitaries are synthesized to match basis gates
        across multiple registers."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr0 = QuantumRegister(1)
        qr1 = QuantumRegister(1)
        coupling_map = CouplingMap(conf.coupling_map)
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr0, qr1)
        qc.unitary(random_unitary(4, seed=12), [qr0[0], qr1[0]])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=None,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)
        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_two_qubit_synthesis_to_directional_cx_from_coupling_map(self):
        """Verify natural cx direction is used when specified in coupling map."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)
        # the decomposer defaults to the [1, 0] direction but the coupling
        # map specifies a [0, 1] direction. Check that this is respected.
        self.assertTrue(
            all(((qr[1], qr[0]) == instr.qubits for instr in qc_out.get_instructions("cx")))
        )
        self.assertTrue(
            all(((qr[0], qr[1]) == instr.qubits for instr in qc_out_nat.get_instructions("cx")))
        )
        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_two_qubit_synthesis_to_directional_cx_from_coupling_map_natural_none(self):
        """Verify natural cx direction is used when specified in coupling map
        when natural_direction is None."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=None,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)
        # the decomposer defaults to the [1, 0] direction but the coupling
        # map specifies a [0, 1] direction. Check that this is respected.
        self.assertTrue(
            all(((qr[1], qr[0]) == instr.qubits for instr in qc_out.get_instructions("cx")))
        )
        self.assertTrue(
            all(((qr[0], qr[1]) == instr.qubits for instr in qc_out_nat.get_instructions("cx")))
        )
        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_two_qubit_synthesis_to_directional_cx_from_coupling_map_natural_false(self):
        """Verify natural cx direction is used when specified in coupling map
        when natural_direction is None."""
        # TODO: should make check more explicit e.g. explicitly set gate
        # direction in test instead of using specific fake backend
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)

        unisynth_pass_nat = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=False,
        )

        pm_nat = PassManager([triv_layout_pass, unisynth_pass_nat])
        qc_out_nat = pm_nat.run(qc)
        # the decomposer defaults to the [1, 0] direction but the coupling
        # map specifies a [0, 1] direction. Check that this is respected.
        self.assertTrue(
            all(((qr[1], qr[0]) == instr.qubits for instr in qc_out.get_instructions("cx")))
        )
        self.assertTrue(
            all(((qr[1], qr[0]) == instr.qubits for instr in qc_out_nat.get_instructions("cx")))
        )
        self.assertEqual(Operator(qc), Operator(qc_out))
        self.assertEqual(Operator(qc), Operator(qc_out_nat))

    def test_two_qubit_synthesis_not_pulse_optimal(self):
        """Verify not attempting pulse optimal decomposition when pulse_optimize==False."""
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=False,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)
        if isinstance(qc_out, QuantumCircuit):
            num_ops = qc_out.count_ops()
        else:
            num_ops = qc_out[0].count_ops()
        self.assertIn("sx", num_ops)
        self.assertGreaterEqual(num_ops["sx"], 16)

    def test_two_qubit_pulse_optimal_true_raises(self):
        """Verify raises if pulse optimal==True but cx is not in the backend basis."""
        backend = FakeVigo()
        conf = backend.configuration()
        # this assumes iswawp pulse optimal decomposition doesn't exist
        conf.basis_gates = [gate if gate != "cx" else "iswap" for gate in conf.basis_gates]
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        with self.assertRaises(QiskitError):
            pm.run(qc)

    def test_two_qubit_natural_direction_true_duration_fallback(self):
        """Verify not attempting pulse optimal decomposition when pulse_optimize==False."""
        # this assumes iswawp pulse optimal decomposition doesn't exist
        backend = FakeVigo()
        conf = backend.configuration()
        # conf.basis_gates = [gate if gate != "cx" else "iswap" for gate in conf.basis_gates]
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 0], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)
        self.assertTrue(
            all(((qr[0], qr[1]) == instr.qubits for instr in qc_out.get_instructions("cx")))
        )

    def test_two_qubit_natural_direction_true_gate_length_raises(self):
        """Verify not attempting pulse optimal decomposition when pulse_optimize==False."""
        # this assumes iswawp pulse optimal decomposition doesn't exist
        backend = FakeVigo()
        conf = backend.configuration()
        for _, nduv in backend.properties()._gates["cx"].items():
            nduv["gate_length"] = (4e-7, nduv["gate_length"][1])
            nduv["gate_error"] = (7e-3, nduv["gate_error"][1])
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 0], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            backend_props=backend.properties(),
            pulse_optimize=True,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        with self.assertRaises(TranspilerError):
            pm.run(qc)

    def test_two_qubit_pulse_optimal_none_optimal(self):
        """Verify pulse optimal decomposition when pulse_optimize==None."""
        # this assumes iswawp pulse optimal decomposition doesn't exist
        backend = FakeVigo()
        conf = backend.configuration()
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=None,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        qc_out = pm.run(qc)
        if isinstance(qc_out, QuantumCircuit):
            num_ops = qc_out.count_ops()
        else:
            num_ops = qc_out[0].count_ops()
        self.assertIn("sx", num_ops)
        self.assertLessEqual(num_ops["sx"], 12)

    def test_two_qubit_pulse_optimal_none_no_raise(self):
        """Verify pulse optimal decomposition when pulse_optimize==None doesn't
        raise when pulse optimal decomposition unknown."""
        # this assumes iswawp pulse optimal decomposition doesn't exist
        backend = FakeVigo()
        conf = backend.configuration()
        conf.basis_gates = [gate if gate != "cx" else "iswap" for gate in conf.basis_gates]
        qr = QuantumRegister(2)
        coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3], [3, 4]])
        triv_layout_pass = TrivialLayout(coupling_map)
        qc = QuantumCircuit(qr)
        qc.unitary(random_unitary(4, seed=12), [0, 1])
        unisynth_pass = UnitarySynthesis(
            basis_gates=conf.basis_gates,
            coupling_map=coupling_map,
            backend_props=backend.properties(),
            pulse_optimize=None,
            natural_direction=True,
        )
        pm = PassManager([triv_layout_pass, unisynth_pass])
        try:
            qc_out = pm.run(qc)
        except QiskitError:
            self.fail("pulse_optimize=None raised exception unexpectedly")
        if isinstance(qc_out, QuantumCircuit):
            num_ops = qc_out.count_ops()
        else:
            num_ops = qc_out[0].count_ops()
        self.assertIn("sx", num_ops)
        self.assertLessEqual(num_ops["sx"], 14)

    def test_qv_natural(self):
        """check that quantum volume circuit compiles for natural direction"""
        qv64 = QuantumVolume(5, seed=15)

        def construct_passmanager(basis_gates, coupling_map, synthesis_fidelity, pulse_optimize):
            def _repeat_condition(property_set):
                return not property_set["depth_fixed_point"]

            seed = 2
            _map = [SabreLayout(coupling_map, max_iterations=2, seed=seed)]
            _embed = [FullAncillaAllocation(coupling_map), EnlargeWithAncilla(), ApplyLayout()]
            _unroll3q = Unroll3qOrMore()
            _swap_check = CheckMap(coupling_map)
            _swap = [
                BarrierBeforeFinalMeasurements(),
                SabreSwap(coupling_map, heuristic="lookahead", seed=seed),
            ]
            _check_depth = [Depth(), FixedPoint("depth")]
            _optimize = [
                Collect2qBlocks(),
                ConsolidateBlocks(basis_gates=basis_gates),
                UnitarySynthesis(
                    basis_gates,
                    synthesis_fidelity,
                    coupling_map,
                    pulse_optimize=pulse_optimize,
                    natural_direction=True,
                ),
                Optimize1qGates(basis_gates),
            ]

            pm = PassManager()
            pm.append(_map)  # map to hardware by inserting swaps
            pm.append(_embed)
            pm.append(_unroll3q)
            pm.append(_swap_check)
            pm.append(_swap)
            pm.append(
                _check_depth + _optimize, do_while=_repeat_condition
            )  # translate to & optimize over hardware native gates
            return pm

        coupling_map = CouplingMap([[0, 1], [1, 2], [3, 2], [3, 4], [5, 4]])
        basis_gates = ["rz", "sx", "cx"]

        pm1 = construct_passmanager(
            basis_gates=basis_gates,
            coupling_map=coupling_map,
            synthesis_fidelity=0.99,
            pulse_optimize=True,
        )
        pm2 = construct_passmanager(
            basis_gates=basis_gates,
            coupling_map=coupling_map,
            synthesis_fidelity=0.99,
            pulse_optimize=False,
        )

        qv64_1 = pm1.run(qv64.decompose())
        qv64_2 = pm2.run(qv64.decompose())
        edges = [list(edge) for edge in coupling_map.get_edges()]
        self.assertTrue(
            all(
                [qv64_1.qubits.index(qubit) for qubit in instr.qubits] in edges
                for instr in qv64_1.get_instructions("cx")
            )
        )
        self.assertEqual(Operator(qv64_1), Operator(qv64_2))

    @data(1, 2, 3)
    def test_coupling_map_transpile(self, opt):
        """test natural_direction works with transpile/execute"""
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [0, 1])
        circ_01 = transpile(
            circ, basis_gates=["rz", "sx", "cx"], optimization_level=opt, coupling_map=[[0, 1]]
        )
        circ_10 = transpile(
            circ, basis_gates=["rz", "sx", "cx"], optimization_level=opt, coupling_map=[[1, 0]]
        )
        circ_01_index = {qubit: index for index, qubit in enumerate(circ_01.qubits)}
        circ_10_index = {qubit: index for index, qubit in enumerate(circ_10.qubits)}

        self.assertTrue(
            all(
                (
                    (1, 0) == (circ_10_index[instr.qubits[0]], circ_10_index[instr.qubits[1]])
                    for instr in circ_10.get_instructions("cx")
                )
            )
        )
        self.assertTrue(
            all(
                (
                    (0, 1) == (circ_01_index[instr.qubits[0]], circ_01_index[instr.qubits[1]])
                    for instr in circ_01.get_instructions("cx")
                )
            )
        )

    @combine(
        opt_level=[0, 1, 2, 3],
        bidirectional=[True, False],
        dsc=(
            "test natural_direction works with transpile using opt_level {opt_level} on"
            " target with multiple 2q gates with bidirectional={bidirectional}"
        ),
        name="opt_level_{opt_level}_bidirectional_{bidirectional}",
    )
    def test_coupling_map_transpile_with_backendv2(self, opt_level, bidirectional):
        backend = FakeBackend5QV2(bidirectional)
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [0, 1])
        circ_01 = transpile(
            circ, backend=backend, optimization_level=opt_level, layout_method="trivial"
        )
        circ_01_index = {qubit: index for index, qubit in enumerate(circ_01.qubits)}
        self.assertGreaterEqual(len(circ_01.get_instructions("cx")), 1)
        for instr in circ_01.get_instructions("cx"):
            self.assertEqual(
                (0, 1), (circ_01_index[instr.qubits[0]], circ_01_index[instr.qubits[1]])
            )

    @data(1, 2, 3)
    def test_coupling_map_unequal_durations(self, opt):
        """Test direction with transpile/execute with backend durations."""
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [1, 0])
        backend = FakeVigo()
        tqc = transpile(
            circ,
            backend=backend,
            optimization_level=opt,
            translation_method="synthesis",
            layout_method="trivial",
        )
        tqc_index = {qubit: index for index, qubit in enumerate(tqc.qubits)}
        self.assertTrue(
            all(
                (
                    (0, 1) == (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]])
                    for instr in tqc.get_instructions("cx")
                )
            )
        )

    @combine(
        opt_level=[0, 1, 2, 3],
        bidirectional=[True, False],
        dsc=(
            "Test direction with transpile using opt_level {opt_level} on"
            " target with multiple 2q gates with bidirectional={bidirectional}"
        ),
        name="opt_level_{opt_level}_bidirectional_{bidirectional}",
    )
    def test_coupling_unequal_duration_with_backendv2(self, opt_level, bidirectional):
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [1, 0])
        backend = FakeBackend5QV2(bidirectional)
        tqc = transpile(
            circ,
            backend=backend,
            optimization_level=opt_level,
            translation_method="synthesis",
            layout_method="trivial",
        )
        tqc_index = {qubit: index for index, qubit in enumerate(tqc.qubits)}
        self.assertGreaterEqual(len(tqc.get_instructions("cx")), 1)
        if bidirectional:
            for instr in tqc.get_instructions("cx"):
                self.assertEqual((1, 0), (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]]))

        else:
            for instr in tqc.get_instructions("cx"):
                self.assertEqual((0, 1), (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]]))

    @combine(
        opt_level=[0, 1, 2, 3],
        dsc=(
            "Test direction with transpile using opt_level {opt_level} on"
            " target with multiple 2q gates"
        ),
        name="opt_level_{opt_level}",
    )
    def test_non_overlapping_kak_gates_with_backendv2(self, opt_level):
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [1, 0])
        backend = FakeBackendV2()
        tqc = transpile(
            circ,
            backend=backend,
            optimization_level=opt_level,
            translation_method="synthesis",
            layout_method="trivial",
        )
        tqc_index = {qubit: index for index, qubit in enumerate(tqc.qubits)}
        self.assertGreaterEqual(len(tqc.get_instructions("ecr")), 1)
        for instr in tqc.get_instructions("ecr"):
            self.assertEqual((1, 0), (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]]))

    def test_fractional_cx_with_backendv2(self):
        """Test fractional CX gets used if present in target."""
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [0, 1])
        backend = FakeMumbaiFractionalCX()
        synth_pass = UnitarySynthesis(target=backend.target)
        tqc = synth_pass(circ)
        tqc_index = {qubit: index for index, qubit in enumerate(tqc.qubits)}
        self.assertGreaterEqual(len(tqc.get_instructions("rzx")), 1)
        for instr in tqc.get_instructions("rzx"):
            self.assertEqual((0, 1), (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]]))

    @combine(
        opt_level=[0, 1, 2, 3],
        dsc=(
            "Test direction with transpile using opt_level {opt_level} on"
            "target with multiple 2q gates available in reverse direction"
        ),
        name="opt_level_{opt_level}",
    )
    def test_reverse_direction(self, opt_level):
        target = Target(2)
        target.add_instruction(CXGate(), {(0, 1): InstructionProperties(error=1.2e-6)})
        target.add_instruction(ECRGate(), {(0, 1): InstructionProperties(error=1.2e-7)})
        target.add_instruction(
            UGate(Parameter("theta"), Parameter("phi"), Parameter("lam")), {(0,): None, (1,): None}
        )
        qr = QuantumRegister(2)
        circ = QuantumCircuit(qr)
        circ.append(random_unitary(4, seed=1), [1, 0])
        tqc = transpile(
            circ,
            target=target,
            optimization_level=opt_level,
            translation_method="synthesis",
            layout_method="trivial",
        )
        tqc_index = {qubit: index for index, qubit in enumerate(tqc.qubits)}
        self.assertGreaterEqual(len(tqc.get_instructions("ecr")), 1)
        for instr in tqc.get_instructions("ecr"):
            self.assertEqual((0, 1), (tqc_index[instr.qubits[0]], tqc_index[instr.qubits[1]]))


if __name__ == "__main__":
    unittest.main()
