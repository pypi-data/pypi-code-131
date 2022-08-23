"""
Do NOT manually edit this file.
Instead, run ./bin/ask_update.py.
"""

from sympy.assumptions.ask import Q
from sympy.assumptions.cnf import Literal
from sympy.core.cache import cacheit

@cacheit
def get_all_known_facts():
    """
    Known facts between unary predicates as CNF clauses.
    """
    return {
        frozenset((Literal(Q.algebraic, False), Literal(Q.imaginary, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.negative, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.positive, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.rational, True))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.transcendental, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.algebraic, True), Literal(Q.finite, False))),
        frozenset((Literal(Q.algebraic, True), Literal(Q.transcendental, True))),
        frozenset((Literal(Q.antihermitian, False), Literal(Q.hermitian, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.antihermitian, False), Literal(Q.imaginary, True))),
        frozenset((Literal(Q.commutative, False), Literal(Q.finite, True))),
        frozenset((Literal(Q.commutative, False), Literal(Q.infinite, True))),
        frozenset((Literal(Q.complex_elements, False), Literal(Q.real_elements, True))),
        frozenset((Literal(Q.composite, False), Literal(Q.even, True), Literal(Q.positive, True), Literal(Q.prime, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.even, False), Literal(Q.odd, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.positive, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.prime, True))),
        frozenset((Literal(Q.diagonal, False), Literal(Q.lower_triangular, True), Literal(Q.upper_triangular, True))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.lower_triangular, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.normal, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.symmetric, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.upper_triangular, False))),
        frozenset((Literal(Q.even, False), Literal(Q.odd, False), Literal(Q.prime, True))),
        frozenset((Literal(Q.even, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.even, True), Literal(Q.odd, True))),
        frozenset((Literal(Q.even, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.finite, False), Literal(Q.transcendental, True))),
        frozenset((Literal(Q.finite, True), Literal(Q.infinite, True))),
        frozenset((Literal(Q.fullrank, False), Literal(Q.invertible, True))),
        frozenset((Literal(Q.fullrank, True), Literal(Q.invertible, False), Literal(Q.square, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.negative, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.positive, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.negative, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.positive, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.infinite, False), Literal(Q.negative_infinite, True))),
        frozenset((Literal(Q.infinite, False), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.integer_elements, True), Literal(Q.real_elements, False))),
        frozenset((Literal(Q.invertible, False), Literal(Q.positive_definite, True))),
        frozenset((Literal(Q.invertible, False), Literal(Q.singular, False))),
        frozenset((Literal(Q.invertible, False), Literal(Q.unitary, True))),
        frozenset((Literal(Q.invertible, True), Literal(Q.singular, True))),
        frozenset((Literal(Q.invertible, True), Literal(Q.square, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.negative, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.positive, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.rational, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.irrational, True), Literal(Q.negative, False), Literal(Q.positive, False), Literal(Q.zero, False))),
        frozenset((Literal(Q.irrational, True), Literal(Q.rational, True))),
        frozenset((Literal(Q.lower_triangular, False), Literal(Q.triangular, True), Literal(Q.upper_triangular, False))),
        frozenset((Literal(Q.lower_triangular, True), Literal(Q.triangular, False))),
        frozenset((Literal(Q.negative, False), Literal(Q.positive, False), Literal(Q.rational, True), Literal(Q.zero, False))),
        frozenset((Literal(Q.negative, True), Literal(Q.negative_infinite, True))),
        frozenset((Literal(Q.negative, True), Literal(Q.positive, True))),
        frozenset((Literal(Q.negative, True), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.negative, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.negative_infinite, True), Literal(Q.positive, True))),
        frozenset((Literal(Q.negative_infinite, True), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.negative_infinite, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.normal, False), Literal(Q.unitary, True))),
        frozenset((Literal(Q.normal, True), Literal(Q.square, False))),
        frozenset((Literal(Q.odd, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.orthogonal, False), Literal(Q.real_elements, True), Literal(Q.unitary, True))),
        frozenset((Literal(Q.orthogonal, True), Literal(Q.positive_definite, False))),
        frozenset((Literal(Q.orthogonal, True), Literal(Q.unitary, False))),
        frozenset((Literal(Q.positive, False), Literal(Q.prime, True))),
        frozenset((Literal(Q.positive, True), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.positive, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.positive_infinite, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.square, False), Literal(Q.symmetric, True))),
        frozenset((Literal(Q.triangular, False), Literal(Q.unit_triangular, True))),
        frozenset((Literal(Q.triangular, False), Literal(Q.upper_triangular, True)))
    }

@cacheit
def get_known_facts_dict():
    """
    Logical relations between unary predicates as dictionary.

    Each key is a predicate, and item is two groups of predicates.
    First group contains the predicates which are implied by the key, and
    second group contains the predicates which are rejected by the key.

    """
    return {
        Q.algebraic: (set([Q.algebraic, Q.commutative, Q.complex, Q.finite]),
        set([Q.infinite, Q.negative_infinite, Q.positive_infinite,
        Q.transcendental])),
        Q.antihermitian: (set([Q.antihermitian]), set([])),
        Q.commutative: (set([Q.commutative]), set([])),
        Q.complex: (set([Q.commutative, Q.complex, Q.finite]),
        set([Q.infinite, Q.negative_infinite, Q.positive_infinite])),
        Q.complex_elements: (set([Q.complex_elements]), set([])),
        Q.composite: (set([Q.algebraic, Q.commutative, Q.complex, Q.composite,
        Q.extended_nonnegative, Q.extended_nonzero,
        Q.extended_positive, Q.extended_real, Q.finite, Q.hermitian,
        Q.integer, Q.nonnegative, Q.nonzero, Q.positive, Q.rational,
        Q.real]), set([Q.extended_negative, Q.extended_nonpositive,
        Q.imaginary, Q.infinite, Q.irrational, Q.negative,
        Q.negative_infinite, Q.nonpositive, Q.positive_infinite,
        Q.prime, Q.transcendental, Q.zero])),
        Q.diagonal: (set([Q.diagonal, Q.lower_triangular, Q.normal, Q.square,
        Q.symmetric, Q.triangular, Q.upper_triangular]), set([])),
        Q.even: (set([Q.algebraic, Q.commutative, Q.complex, Q.even,
        Q.extended_real, Q.finite, Q.hermitian, Q.integer, Q.rational,
        Q.real]), set([Q.imaginary, Q.infinite, Q.irrational,
        Q.negative_infinite, Q.odd, Q.positive_infinite,
        Q.transcendental])),
        Q.extended_negative: (set([Q.commutative, Q.extended_negative,
        Q.extended_nonpositive, Q.extended_nonzero, Q.extended_real]),
        set([Q.composite, Q.extended_nonnegative, Q.extended_positive,
        Q.imaginary, Q.nonnegative, Q.positive, Q.positive_infinite,
        Q.prime, Q.zero])),
        Q.extended_nonnegative: (set([Q.commutative, Q.extended_nonnegative,
        Q.extended_real]), set([Q.extended_negative, Q.imaginary,
        Q.negative, Q.negative_infinite])),
        Q.extended_nonpositive: (set([Q.commutative, Q.extended_nonpositive,
        Q.extended_real]), set([Q.composite, Q.extended_positive,
        Q.imaginary, Q.positive, Q.positive_infinite, Q.prime])),
        Q.extended_nonzero: (set([Q.commutative, Q.extended_nonzero,
        Q.extended_real]), set([Q.imaginary, Q.zero])),
        Q.extended_positive: (set([Q.commutative, Q.extended_nonnegative,
        Q.extended_nonzero, Q.extended_positive, Q.extended_real]),
        set([Q.extended_negative, Q.extended_nonpositive, Q.imaginary,
        Q.negative, Q.negative_infinite, Q.nonpositive, Q.zero])),
        Q.extended_real: (set([Q.commutative, Q.extended_real]),
        set([Q.imaginary])),
        Q.finite: (set([Q.commutative, Q.finite]), set([Q.infinite,
        Q.negative_infinite, Q.positive_infinite])),
        Q.fullrank: (set([Q.fullrank]), set([])),
        Q.hermitian: (set([Q.hermitian]), set([])),
        Q.imaginary: (set([Q.antihermitian, Q.commutative, Q.complex,
        Q.finite, Q.imaginary]), set([Q.composite, Q.even,
        Q.extended_negative, Q.extended_nonnegative,
        Q.extended_nonpositive, Q.extended_nonzero,
        Q.extended_positive, Q.extended_real, Q.infinite, Q.integer,
        Q.irrational, Q.negative, Q.negative_infinite, Q.nonnegative,
        Q.nonpositive, Q.nonzero, Q.odd, Q.positive,
        Q.positive_infinite, Q.prime, Q.rational, Q.real, Q.zero])),
        Q.infinite: (set([Q.commutative, Q.infinite]), set([Q.algebraic,
        Q.complex, Q.composite, Q.even, Q.finite, Q.imaginary,
        Q.integer, Q.irrational, Q.negative, Q.nonnegative,
        Q.nonpositive, Q.nonzero, Q.odd, Q.positive, Q.prime,
        Q.rational, Q.real, Q.transcendental, Q.zero])),
        Q.integer: (set([Q.algebraic, Q.commutative, Q.complex,
        Q.extended_real, Q.finite, Q.hermitian, Q.integer, Q.rational,
        Q.real]), set([Q.imaginary, Q.infinite, Q.irrational,
        Q.negative_infinite, Q.positive_infinite, Q.transcendental])),
        Q.integer_elements: (set([Q.complex_elements, Q.integer_elements,
        Q.real_elements]), set([])),
        Q.invertible: (set([Q.fullrank, Q.invertible, Q.square]),
        set([Q.singular])),
        Q.irrational: (set([Q.commutative, Q.complex, Q.extended_nonzero,
        Q.extended_real, Q.finite, Q.hermitian, Q.irrational,
        Q.nonzero, Q.real]), set([Q.composite, Q.even, Q.imaginary,
        Q.infinite, Q.integer, Q.negative_infinite, Q.odd,
        Q.positive_infinite, Q.prime, Q.rational, Q.zero])),
        Q.is_true: (set([Q.is_true]), set([])),
        Q.lower_triangular: (set([Q.lower_triangular, Q.triangular]), set([])),
        Q.negative: (set([Q.commutative, Q.complex, Q.extended_negative,
        Q.extended_nonpositive, Q.extended_nonzero, Q.extended_real,
        Q.finite, Q.hermitian, Q.negative, Q.nonpositive, Q.nonzero,
        Q.real]), set([Q.composite, Q.extended_nonnegative,
        Q.extended_positive, Q.imaginary, Q.infinite,
        Q.negative_infinite, Q.nonnegative, Q.positive,
        Q.positive_infinite, Q.prime, Q.zero])),
        Q.negative_infinite: (set([Q.commutative, Q.extended_negative,
        Q.extended_nonpositive, Q.extended_nonzero, Q.extended_real,
        Q.infinite, Q.negative_infinite]), set([Q.algebraic,
        Q.complex, Q.composite, Q.even, Q.extended_nonnegative,
        Q.extended_positive, Q.finite, Q.imaginary, Q.integer,
        Q.irrational, Q.negative, Q.nonnegative, Q.nonpositive,
        Q.nonzero, Q.odd, Q.positive, Q.positive_infinite, Q.prime,
        Q.rational, Q.real, Q.transcendental, Q.zero])),
        Q.nonnegative: (set([Q.commutative, Q.complex, Q.extended_nonnegative,
        Q.extended_real, Q.finite, Q.hermitian, Q.nonnegative,
        Q.real]), set([Q.extended_negative, Q.imaginary, Q.infinite,
        Q.negative, Q.negative_infinite, Q.positive_infinite])),
        Q.nonpositive: (set([Q.commutative, Q.complex, Q.extended_nonpositive,
        Q.extended_real, Q.finite, Q.hermitian, Q.nonpositive,
        Q.real]), set([Q.composite, Q.extended_positive, Q.imaginary,
        Q.infinite, Q.negative_infinite, Q.positive,
        Q.positive_infinite, Q.prime])),
        Q.nonzero: (set([Q.commutative, Q.complex, Q.extended_nonzero,
        Q.extended_real, Q.finite, Q.hermitian, Q.nonzero, Q.real]),
        set([Q.imaginary, Q.infinite, Q.negative_infinite,
        Q.positive_infinite, Q.zero])),
        Q.normal: (set([Q.normal, Q.square]), set([])),
        Q.odd: (set([Q.algebraic, Q.commutative, Q.complex,
        Q.extended_nonzero, Q.extended_real, Q.finite, Q.hermitian,
        Q.integer, Q.nonzero, Q.odd, Q.rational, Q.real]),
        set([Q.even, Q.imaginary, Q.infinite, Q.irrational,
        Q.negative_infinite, Q.positive_infinite, Q.transcendental,
        Q.zero])),
        Q.orthogonal: (set([Q.fullrank, Q.invertible, Q.normal, Q.orthogonal,
        Q.positive_definite, Q.square, Q.unitary]), set([Q.singular])),
        Q.positive: (set([Q.commutative, Q.complex, Q.extended_nonnegative,
        Q.extended_nonzero, Q.extended_positive, Q.extended_real,
        Q.finite, Q.hermitian, Q.nonnegative, Q.nonzero, Q.positive,
        Q.real]), set([Q.extended_negative, Q.extended_nonpositive,
        Q.imaginary, Q.infinite, Q.negative, Q.negative_infinite,
        Q.nonpositive, Q.positive_infinite, Q.zero])),
        Q.positive_definite: (set([Q.fullrank, Q.invertible,
        Q.positive_definite, Q.square]), set([Q.singular])),
        Q.positive_infinite: (set([Q.commutative, Q.extended_nonnegative,
        Q.extended_nonzero, Q.extended_positive, Q.extended_real,
        Q.infinite, Q.positive_infinite]), set([Q.algebraic,
        Q.complex, Q.composite, Q.even, Q.extended_negative,
        Q.extended_nonpositive, Q.finite, Q.imaginary, Q.integer,
        Q.irrational, Q.negative, Q.negative_infinite, Q.nonnegative,
        Q.nonpositive, Q.nonzero, Q.odd, Q.positive, Q.prime,
        Q.rational, Q.real, Q.transcendental, Q.zero])),
        Q.prime: (set([Q.algebraic, Q.commutative, Q.complex,
        Q.extended_nonnegative, Q.extended_nonzero,
        Q.extended_positive, Q.extended_real, Q.finite, Q.hermitian,
        Q.integer, Q.nonnegative, Q.nonzero, Q.positive, Q.prime,
        Q.rational, Q.real]), set([Q.composite, Q.extended_negative,
        Q.extended_nonpositive, Q.imaginary, Q.infinite, Q.irrational,
        Q.negative, Q.negative_infinite, Q.nonpositive,
        Q.positive_infinite, Q.transcendental, Q.zero])),
        Q.rational: (set([Q.algebraic, Q.commutative, Q.complex,
        Q.extended_real, Q.finite, Q.hermitian, Q.rational, Q.real]),
        set([Q.imaginary, Q.infinite, Q.irrational,
        Q.negative_infinite, Q.positive_infinite, Q.transcendental])),
        Q.real: (set([Q.commutative, Q.complex, Q.extended_real, Q.finite,
        Q.hermitian, Q.real]), set([Q.imaginary, Q.infinite,
        Q.negative_infinite, Q.positive_infinite])),
        Q.real_elements: (set([Q.complex_elements, Q.real_elements]), set([])),
        Q.singular: (set([Q.singular]), set([Q.invertible, Q.orthogonal,
        Q.positive_definite, Q.unitary])),
        Q.square: (set([Q.square]), set([])),
        Q.symmetric: (set([Q.square, Q.symmetric]), set([])),
        Q.transcendental: (set([Q.commutative, Q.complex, Q.finite,
        Q.transcendental]), set([Q.algebraic, Q.composite, Q.even,
        Q.infinite, Q.integer, Q.negative_infinite, Q.odd,
        Q.positive_infinite, Q.prime, Q.rational, Q.zero])),
        Q.triangular: (set([Q.triangular]), set([])),
        Q.unit_triangular: (set([Q.triangular, Q.unit_triangular]), set([])),
        Q.unitary: (set([Q.fullrank, Q.invertible, Q.normal, Q.square,
        Q.unitary]), set([Q.singular])),
        Q.upper_triangular: (set([Q.triangular, Q.upper_triangular]), set([])),
        Q.zero: (set([Q.algebraic, Q.commutative, Q.complex, Q.even,
        Q.extended_nonnegative, Q.extended_nonpositive,
        Q.extended_real, Q.finite, Q.hermitian, Q.integer,
        Q.nonnegative, Q.nonpositive, Q.rational, Q.real, Q.zero]),
        set([Q.composite, Q.extended_negative, Q.extended_nonzero,
        Q.extended_positive, Q.imaginary, Q.infinite, Q.irrational,
        Q.negative, Q.negative_infinite, Q.nonzero, Q.odd, Q.positive,
        Q.positive_infinite, Q.prime, Q.transcendental])),
    }
