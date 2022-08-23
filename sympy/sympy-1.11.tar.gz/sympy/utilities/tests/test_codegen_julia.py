from io import StringIO

from sympy.core import S, symbols, Eq, pi, Catalan, EulerGamma, Function
from sympy.core.relational import Equality
from sympy.functions.elementary.piecewise import Piecewise
from sympy.matrices import Matrix, MatrixSymbol
from sympy.utilities.codegen import JuliaCodeGen, codegen, make_routine
from sympy.testing.pytest import XFAIL
import sympy


x, y, z = symbols('x,y,z')


def test_empty_jl_code():
    code_gen = JuliaCodeGen()
    output = StringIO()
    code_gen.dump_jl([], output, "file", header=False, empty=False)
    source = output.getvalue()
    assert source == ""


def test_jl_simple_code():
    name_expr = ("test", (x + y)*z)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    assert result[0] == "test.jl"
    source = result[1]
    expected = (
        "function test(x, y, z)\n"
        "    out1 = z .* (x + y)\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


def test_jl_simple_code_with_header():
    name_expr = ("test", (x + y)*z)
    result, = codegen(name_expr, "Julia", header=True, empty=False)
    assert result[0] == "test.jl"
    source = result[1]
    expected = (
        "#   Code generated with SymPy " + sympy.__version__ + "\n"
        "#\n"
        "#   See http://www.sympy.org/ for more information.\n"
        "#\n"
        "#   This file is part of 'project'\n"
        "function test(x, y, z)\n"
        "    out1 = z .* (x + y)\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


def test_jl_simple_code_nameout():
    expr = Equality(z, (x + y))
    name_expr = ("test", expr)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y)\n"
        "    z = x + y\n"
        "    return z\n"
        "end\n"
    )
    assert source == expected


def test_jl_numbersymbol():
    name_expr = ("test", pi**Catalan)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test()\n"
        "    out1 = pi ^ catalan\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


@XFAIL
def test_jl_numbersymbol_no_inline():
    # FIXME: how to pass inline=False to the JuliaCodePrinter?
    name_expr = ("test", [pi**Catalan, EulerGamma])
    result, = codegen(name_expr, "Julia", header=False,
                      empty=False, inline=False)
    source = result[1]
    expected = (
        "function test()\n"
        "    Catalan = 0.915965594177219\n"
        "    EulerGamma = 0.5772156649015329\n"
        "    out1 = pi ^ Catalan\n"
        "    out2 = EulerGamma\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_jl_code_argument_order():
    expr = x + y
    routine = make_routine("test", expr, argument_sequence=[z, x, y], language="julia")
    code_gen = JuliaCodeGen()
    output = StringIO()
    code_gen.dump_jl([routine], output, "test", header=False, empty=False)
    source = output.getvalue()
    expected = (
        "function test(z, x, y)\n"
        "    out1 = x + y\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


def test_multiple_results_m():
    # Here the output order is the input order
    expr1 = (x + y)*z
    expr2 = (x - y)*z
    name_expr = ("test", [expr1, expr2])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y, z)\n"
        "    out1 = z .* (x + y)\n"
        "    out2 = z .* (x - y)\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_results_named_unordered():
    # Here output order is based on name_expr
    A, B, C = symbols('A,B,C')
    expr1 = Equality(C, (x + y)*z)
    expr2 = Equality(A, (x - y)*z)
    expr3 = Equality(B, 2*x)
    name_expr = ("test", [expr1, expr2, expr3])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y, z)\n"
        "    C = z .* (x + y)\n"
        "    A = z .* (x - y)\n"
        "    B = 2 * x\n"
        "    return C, A, B\n"
        "end\n"
    )
    assert source == expected


def test_results_named_ordered():
    A, B, C = symbols('A,B,C')
    expr1 = Equality(C, (x + y)*z)
    expr2 = Equality(A, (x - y)*z)
    expr3 = Equality(B, 2*x)
    name_expr = ("test", [expr1, expr2, expr3])
    result = codegen(name_expr, "Julia", header=False, empty=False,
                     argument_sequence=(x, z, y))
    assert result[0][0] == "test.jl"
    source = result[0][1]
    expected = (
        "function test(x, z, y)\n"
        "    C = z .* (x + y)\n"
        "    A = z .* (x - y)\n"
        "    B = 2 * x\n"
        "    return C, A, B\n"
        "end\n"
    )
    assert source == expected


def test_complicated_jl_codegen():
    from sympy.functions.elementary.trigonometric import (cos, sin, tan)
    name_expr = ("testlong",
            [ ((sin(x) + cos(y) + tan(z))**3).expand(),
            cos(cos(cos(cos(cos(cos(cos(cos(x + y + z))))))))
    ])
    result = codegen(name_expr, "Julia", header=False, empty=False)
    assert result[0][0] == "testlong.jl"
    source = result[0][1]
    expected = (
        "function testlong(x, y, z)\n"
        "    out1 = sin(x) .^ 3 + 3 * sin(x) .^ 2 .* cos(y) + 3 * sin(x) .^ 2 .* tan(z)"
        " + 3 * sin(x) .* cos(y) .^ 2 + 6 * sin(x) .* cos(y) .* tan(z) + 3 * sin(x) .* tan(z) .^ 2"
        " + cos(y) .^ 3 + 3 * cos(y) .^ 2 .* tan(z) + 3 * cos(y) .* tan(z) .^ 2 + tan(z) .^ 3\n"
        "    out2 = cos(cos(cos(cos(cos(cos(cos(cos(x + y + z))))))))\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_jl_output_arg_mixed_unordered():
    # named outputs are alphabetical, unnamed output appear in the given order
    from sympy.functions.elementary.trigonometric import (cos, sin)
    a = symbols("a")
    name_expr = ("foo", [cos(2*x), Equality(y, sin(x)), cos(x), Equality(a, sin(2*x))])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    assert result[0] == "foo.jl"
    source = result[1];
    expected = (
        'function foo(x)\n'
        '    out1 = cos(2 * x)\n'
        '    y = sin(x)\n'
        '    out3 = cos(x)\n'
        '    a = sin(2 * x)\n'
        '    return out1, y, out3, a\n'
        'end\n'
    )
    assert source == expected


def test_jl_piecewise_():
    pw = Piecewise((0, x < -1), (x**2, x <= 1), (-x+2, x > 1), (1, True), evaluate=False)
    name_expr = ("pwtest", pw)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function pwtest(x)\n"
        "    out1 = ((x < -1) ? (0) :\n"
        "    (x <= 1) ? (x .^ 2) :\n"
        "    (x > 1) ? (2 - x) : (1))\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


@XFAIL
def test_jl_piecewise_no_inline():
    # FIXME: how to pass inline=False to the JuliaCodePrinter?
    pw = Piecewise((0, x < -1), (x**2, x <= 1), (-x+2, x > 1), (1, True))
    name_expr = ("pwtest", pw)
    result, = codegen(name_expr, "Julia", header=False, empty=False,
                      inline=False)
    source = result[1]
    expected = (
        "function pwtest(x)\n"
        "    if (x < -1)\n"
        "        out1 = 0\n"
        "    elseif (x <= 1)\n"
        "        out1 = x .^ 2\n"
        "    elseif (x > 1)\n"
        "        out1 = -x + 2\n"
        "    else\n"
        "        out1 = 1\n"
        "    end\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


def test_jl_multifcns_per_file():
    name_expr = [ ("foo", [2*x, 3*y]), ("bar", [y**2, 4*y]) ]
    result = codegen(name_expr, "Julia", header=False, empty=False)
    assert result[0][0] == "foo.jl"
    source = result[0][1];
    expected = (
        "function foo(x, y)\n"
        "    out1 = 2 * x\n"
        "    out2 = 3 * y\n"
        "    return out1, out2\n"
        "end\n"
        "function bar(y)\n"
        "    out1 = y .^ 2\n"
        "    out2 = 4 * y\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_jl_multifcns_per_file_w_header():
    name_expr = [ ("foo", [2*x, 3*y]), ("bar", [y**2, 4*y]) ]
    result = codegen(name_expr, "Julia", header=True, empty=False)
    assert result[0][0] == "foo.jl"
    source = result[0][1];
    expected = (
        "#   Code generated with SymPy " + sympy.__version__ + "\n"
        "#\n"
        "#   See http://www.sympy.org/ for more information.\n"
        "#\n"
        "#   This file is part of 'project'\n"
        "function foo(x, y)\n"
        "    out1 = 2 * x\n"
        "    out2 = 3 * y\n"
        "    return out1, out2\n"
        "end\n"
        "function bar(y)\n"
        "    out1 = y .^ 2\n"
        "    out2 = 4 * y\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_jl_filename_match_prefix():
    name_expr = [ ("foo", [2*x, 3*y]), ("bar", [y**2, 4*y]) ]
    result, = codegen(name_expr, "Julia", prefix="baz", header=False,
                     empty=False)
    assert result[0] == "baz.jl"


def test_jl_matrix_named():
    e2 = Matrix([[x, 2*y, pi*z]])
    name_expr = ("test", Equality(MatrixSymbol('myout1', 1, 3), e2))
    result = codegen(name_expr, "Julia", header=False, empty=False)
    assert result[0][0] == "test.jl"
    source = result[0][1]
    expected = (
        "function test(x, y, z)\n"
        "    myout1 = [x 2 * y pi * z]\n"
        "    return myout1\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrix_named_matsym():
    myout1 = MatrixSymbol('myout1', 1, 3)
    e2 = Matrix([[x, 2*y, pi*z]])
    name_expr = ("test", Equality(myout1, e2, evaluate=False))
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y, z)\n"
        "    myout1 = [x 2 * y pi * z]\n"
        "    return myout1\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrix_output_autoname():
    expr = Matrix([[x, x+y, 3]])
    name_expr = ("test", expr)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y)\n"
        "    out1 = [x x + y 3]\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrix_output_autoname_2():
    e1 = (x + y)
    e2 = Matrix([[2*x, 2*y, 2*z]])
    e3 = Matrix([[x], [y], [z]])
    e4 = Matrix([[x, y], [z, 16]])
    name_expr = ("test", (e1, e2, e3, e4))
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y, z)\n"
        "    out1 = x + y\n"
        "    out2 = [2 * x 2 * y 2 * z]\n"
        "    out3 = [x, y, z]\n"
        "    out4 = [x  y;\n"
        "    z 16]\n"
        "    return out1, out2, out3, out4\n"
        "end\n"
    )
    assert source == expected


def test_jl_results_matrix_named_ordered():
    B, C = symbols('B,C')
    A = MatrixSymbol('A', 1, 3)
    expr1 = Equality(C, (x + y)*z)
    expr2 = Equality(A, Matrix([[1, 2, x]]))
    expr3 = Equality(B, 2*x)
    name_expr = ("test", [expr1, expr2, expr3])
    result, = codegen(name_expr, "Julia", header=False, empty=False,
                     argument_sequence=(x, z, y))
    source = result[1]
    expected = (
        "function test(x, z, y)\n"
        "    C = z .* (x + y)\n"
        "    A = [1 2 x]\n"
        "    B = 2 * x\n"
        "    return C, A, B\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrixsymbol_slice():
    A = MatrixSymbol('A', 2, 3)
    B = MatrixSymbol('B', 1, 3)
    C = MatrixSymbol('C', 1, 3)
    D = MatrixSymbol('D', 2, 1)
    name_expr = ("test", [Equality(B, A[0, :]),
                          Equality(C, A[1, :]),
                          Equality(D, A[:, 2])])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(A)\n"
        "    B = A[1,:]\n"
        "    C = A[2,:]\n"
        "    D = A[:,3]\n"
        "    return B, C, D\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrixsymbol_slice2():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 2, 2)
    C = MatrixSymbol('C', 2, 2)
    name_expr = ("test", [Equality(B, A[0:2, 0:2]),
                          Equality(C, A[0:2, 1:3])])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(A)\n"
        "    B = A[1:2,1:2]\n"
        "    C = A[1:2,2:3]\n"
        "    return B, C\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrixsymbol_slice3():
    A = MatrixSymbol('A', 8, 7)
    B = MatrixSymbol('B', 2, 2)
    C = MatrixSymbol('C', 4, 2)
    name_expr = ("test", [Equality(B, A[6:, 1::3]),
                          Equality(C, A[::2, ::3])])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(A)\n"
        "    B = A[7:end,2:3:end]\n"
        "    C = A[1:2:end,1:3:end]\n"
        "    return B, C\n"
        "end\n"
    )
    assert source == expected


def test_jl_matrixsymbol_slice_autoname():
    A = MatrixSymbol('A', 2, 3)
    B = MatrixSymbol('B', 1, 3)
    name_expr = ("test", [Equality(B, A[0,:]), A[1,:], A[:,0], A[:,1]])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(A)\n"
        "    B = A[1,:]\n"
        "    out2 = A[2,:]\n"
        "    out3 = A[:,1]\n"
        "    out4 = A[:,2]\n"
        "    return B, out2, out3, out4\n"
        "end\n"
    )
    assert source == expected


def test_jl_loops():
    # Note: an Julia programmer would probably vectorize this across one or
    # more dimensions.  Also, size(A) would be used rather than passing in m
    # and n.  Perhaps users would expect us to vectorize automatically here?
    # Or is it possible to represent such things using IndexedBase?
    from sympy.tensor import IndexedBase, Idx
    from sympy.core.symbol import symbols
    n, m = symbols('n m', integer=True)
    A = IndexedBase('A')
    x = IndexedBase('x')
    y = IndexedBase('y')
    i = Idx('i', m)
    j = Idx('j', n)
    result, = codegen(('mat_vec_mult', Eq(y[i], A[i, j]*x[j])), "Julia",
                      header=False, empty=False)
    source = result[1]
    expected = (
        'function mat_vec_mult(y, A, m, n, x)\n'
        '    for i = 1:m\n'
        '        y[i] = 0\n'
        '    end\n'
        '    for i = 1:m\n'
        '        for j = 1:n\n'
        '            y[i] = %(rhs)s + y[i]\n'
        '        end\n'
        '    end\n'
        '    return y\n'
        'end\n'
    )
    assert (source == expected % {'rhs': 'A[%s,%s] .* x[j]' % (i, j)} or
            source == expected % {'rhs': 'x[j] .* A[%s,%s]' % (i, j)})


def test_jl_tensor_loops_multiple_contractions():
    # see comments in previous test about vectorizing
    from sympy.tensor import IndexedBase, Idx
    from sympy.core.symbol import symbols
    n, m, o, p = symbols('n m o p', integer=True)
    A = IndexedBase('A')
    B = IndexedBase('B')
    y = IndexedBase('y')
    i = Idx('i', m)
    j = Idx('j', n)
    k = Idx('k', o)
    l = Idx('l', p)
    result, = codegen(('tensorthing', Eq(y[i], B[j, k, l]*A[i, j, k, l])),
                      "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        'function tensorthing(y, A, B, m, n, o, p)\n'
        '    for i = 1:m\n'
        '        y[i] = 0\n'
        '    end\n'
        '    for i = 1:m\n'
        '        for j = 1:n\n'
        '            for k = 1:o\n'
        '                for l = 1:p\n'
        '                    y[i] = A[i,j,k,l] .* B[j,k,l] + y[i]\n'
        '                end\n'
        '            end\n'
        '        end\n'
        '    end\n'
        '    return y\n'
        'end\n'
    )
    assert source == expected


def test_jl_InOutArgument():
    expr = Equality(x, x**2)
    name_expr = ("mysqr", expr)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function mysqr(x)\n"
        "    x = x .^ 2\n"
        "    return x\n"
        "end\n"
    )
    assert source == expected


def test_jl_InOutArgument_order():
    # can specify the order as (x, y)
    expr = Equality(x, x**2 + y)
    name_expr = ("test", expr)
    result, = codegen(name_expr, "Julia", header=False,
                      empty=False, argument_sequence=(x,y))
    source = result[1]
    expected = (
        "function test(x, y)\n"
        "    x = x .^ 2 + y\n"
        "    return x\n"
        "end\n"
    )
    assert source == expected
    # make sure it gives (x, y) not (y, x)
    expr = Equality(x, x**2 + y)
    name_expr = ("test", expr)
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x, y)\n"
        "    x = x .^ 2 + y\n"
        "    return x\n"
        "end\n"
    )
    assert source == expected


def test_jl_not_supported():
    f = Function('f')
    name_expr = ("test", [f(x).diff(x), S.ComplexInfinity])
    result, = codegen(name_expr, "Julia", header=False, empty=False)
    source = result[1]
    expected = (
        "function test(x)\n"
        "    # unsupported: Derivative(f(x), x)\n"
        "    # unsupported: zoo\n"
        "    out1 = Derivative(f(x), x)\n"
        "    out2 = zoo\n"
        "    return out1, out2\n"
        "end\n"
    )
    assert source == expected


def test_global_vars_octave():
    x, y, z, t = symbols("x y z t")
    result = codegen(('f', x*y), "Julia", header=False, empty=False,
                     global_vars=(y,))
    source = result[0][1]
    expected = (
        "function f(x)\n"
        "    out1 = x .* y\n"
        "    return out1\n"
        "end\n"
        )
    assert source == expected

    result = codegen(('f', x*y+z), "Julia", header=False, empty=False,
                     argument_sequence=(x, y), global_vars=(z, t))
    source = result[0][1]
    expected = (
        "function f(x, y)\n"
        "    out1 = x .* y + z\n"
        "    return out1\n"
        "end\n"
    )
    assert source == expected
