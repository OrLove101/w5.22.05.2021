import pytest

from src.complex.complex import Complex

COMPLEX_DEFAULT = 1.0
COMPLEX_NEW_VALUE = 2.0


@pytest.mark.parametrize('params', [
    (), (10.0, 5.0)
])
def test_constructor(params):
    comp = Complex(*params)

    assert comp.real == params[0] if params != () else COMPLEX_DEFAULT
    assert comp.imaginary == params[1] if params != () else COMPLEX_DEFAULT


@pytest.mark.parametrize('real, imaginary, exception_type', [
    ('asd', 'asd', ValueError), (Complex, Complex, TypeError)
])
def test_constructor_exceptions(real, imaginary, exception_type):
    with pytest.raises(exception_type):
        Complex(real, imaginary)


def test_setters():
    comp = Complex()

    assert comp.real == COMPLEX_DEFAULT
    assert comp.imaginary == COMPLEX_DEFAULT

    comp.real = COMPLEX_NEW_VALUE
    comp.imaginary = COMPLEX_NEW_VALUE

    assert comp.real == COMPLEX_NEW_VALUE
    assert comp.imaginary == COMPLEX_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Complex, TypeError)
])
def test_setter_exceptions(value, exception_type):
    comp = Complex()

    with pytest.raises(exception_type):
        comp.real = value


@pytest.mark.parametrize('params, string_repr', [
    ((), '1.0+1.0i'), ((10.0, 5.0), '10.0+5.0i')
])
def test_string_repr(params, string_repr):
    comp = Complex(*params)

    assert str(comp) == string_repr


def test_comparison_operators():
    c1 = Complex()
    c2 = Complex()
    c3 = Complex(2.0, 4.0)

    assert c1 == c2
    assert not c1 == c3
    assert c1 != c3
    assert not c1 != c2


def test_comparison_operators_exception():
    c1 = Complex()

    with pytest.raises(TypeError):
        c1 == 123
