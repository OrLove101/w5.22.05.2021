import pytest

from src.point.point import Point

POINT_DEFAULT = 1.0
POINT_NEW_VALUE = 10.0


@pytest.mark.parametrize('params', [
    (), (10.0, 5.0)
])
def test_constructor(params):
    point = Point(*params)

    assert point.x == params[0] if params != () else POINT_DEFAULT
    assert point.y == params[1] if params != () else POINT_DEFAULT


@pytest.mark.parametrize('x, y, exception_type', [
    ('asd', 'asd', ValueError), (Point, Point, TypeError)
])
def test_constructor_exceptions(x, y, exception_type):
    with pytest.raises(exception_type):
        Point(x, y)


def test_setters():
    point = Point()

    assert point.x == POINT_DEFAULT
    assert point.y == POINT_DEFAULT

    point.x = POINT_NEW_VALUE
    point.y = POINT_NEW_VALUE

    assert point.x == POINT_NEW_VALUE
    assert point.y == POINT_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Point, TypeError)
])
def test_setter_exceptions(value, exception_type):
    point = Point()

    with pytest.raises(exception_type):
        point.x = value


@pytest.mark.parametrize('params, string_repr', [
    ((), '(1.0, 1.0)'), ((10.0, 5.0), '(10.0, 5.0)')
])
def test_string_repr(params, string_repr):
    point = Point(*params)

    assert str(point) == string_repr


def test_comparison_operators():
    p1 = Point()
    p2 = Point()
    p3 = Point(2.0, 4.0)

    assert p1 == p2
    assert not p1 == p3
    assert p1 != p3
    assert not p1 != p2


def test_comparison_operators_exception():
    p1 = Point()

    with pytest.raises(TypeError):
        p1 == 123


def test_distance():
    p1 = Point()
    p2 = Point(2.0, 4.0)

    assert p1.distance(p2) == 3.1622776601683795


def test_distance_exception():
    with pytest.raises(TypeError):
        Point().distance('Some string')
