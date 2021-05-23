import pytest

from src.vector.vector import Vector

VECTOR_DEFAULT = 1.0
VECTOR_NEW_VALUE = 10.0


@pytest.mark.parametrize('params', [
    (), (10.0, 5.0)
])
def test_constructor(params):
    vector = Vector(*params)

    assert vector.x == params[0] if params != () else VECTOR_DEFAULT
    assert vector.y == params[1] if params != () else VECTOR_DEFAULT


@pytest.mark.parametrize('x, y, exception_type', [
    ('asd', 'asd', ValueError), (Vector, Vector, TypeError)
])
def test_constructor_exceptions(x, y, exception_type):
    with pytest.raises(exception_type):
        Vector(x, y)


def test_setters():
    vector = Vector()

    assert vector.x == VECTOR_DEFAULT
    assert vector.y == VECTOR_DEFAULT

    vector.x = VECTOR_NEW_VALUE
    vector.y = VECTOR_NEW_VALUE

    assert vector.x == VECTOR_NEW_VALUE
    assert vector.y == VECTOR_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Vector, TypeError)
])
def test_setter_exceptions(value, exception_type):
    vector = Vector()

    with pytest.raises(exception_type):
        vector.x = value


@pytest.mark.parametrize('params, string_repr', [
    ((), '(1.0, 1.0)'), ((10.0, 5.0), '(10.0, 5.0)')
])
def test_string_repr(params, string_repr):
    vector = Vector(*params)

    assert str(vector) == string_repr


def test_comparison_operators():
    v1 = Vector()
    v2 = Vector()
    v3 = Vector(2.0, 4.0)

    assert v1 == v2
    assert not v1 == v3
    assert v1 != v3
    assert not v1 != v2


def test_comparison_operators_exception():
    v1 = Vector()

    with pytest.raises(TypeError):
        v1 == 123


def test_len():
    v1 = Vector()
    v2 = Vector(2.0, 4.0)

    assert v1.len(v2) == 3.1622776601683795


def test_len_exception():
    with pytest.raises(TypeError):
        Vector().len('Some string')
