import pytest

from src.unit.unit import Unit

UNIT_HEALTH_DEFAULT = 100
UNIT_ATTACK_DEFAULT = 5
UNIT_NAME_DEFAULT = 'Vasya'

UNIT_NEW_HEALTH = 120
UNIT_NEW_ATTACK = 10
UNIT_NEW_NAME = 'Max'


@pytest.mark.parametrize('params', [
    (), ('Max', 120, 10)
])
def test_constructor(params):
    unit = Unit(*params)

    assert unit.name == params[0] if params != () else UNIT_NAME_DEFAULT
    assert unit.hp == params[1] if params != () else UNIT_HEALTH_DEFAULT
    assert unit.damage == params[2] if params != () else UNIT_ATTACK_DEFAULT


@pytest.mark.parametrize('name, health, damage, exception_type', [
    (123, 'asd', 'asd', ValueError), (Unit, Unit, Unit, TypeError)
])
def test_constructor_exceptions(name, health, damage, exception_type):
    with pytest.raises(exception_type):
        Unit(name, health, damage)


def test_setters():
    unit = Unit()

    assert unit.name == UNIT_NAME_DEFAULT
    assert unit.damage == UNIT_ATTACK_DEFAULT
    assert unit.hp == UNIT_HEALTH_DEFAULT

    unit.name = UNIT_NEW_NAME
    unit.damage = UNIT_NEW_ATTACK
    unit.hp = UNIT_NEW_HEALTH

    assert unit.name == UNIT_NEW_NAME
    assert unit.damage == UNIT_NEW_ATTACK
    assert unit.hp == UNIT_NEW_HEALTH


@pytest.mark.parametrize('value, exception_type', [
    ('asd', ValueError), (Unit, TypeError)
])
def test_setter_exceptions(value, exception_type):
    unit = Unit()

    with pytest.raises(exception_type):
        unit.hp = value


@pytest.mark.parametrize('params, string_repr', [
    ((), 'Vasya 100/100hp, damage: 5'), (('Max', 120, 10), 'Max 120/120hp, damage: 10')
])
def test_string_repr(params, string_repr):
    unit = Unit(*params)

    assert str(unit) == string_repr


@pytest.mark.parametrize('value', [
    10, 110
])
def test_take_damage(value):
    unit = Unit()

    unit.take_damage(value)
    assert unit.hp == (unit.hp_limit - value if unit.hp_limit >= value else 0)


def test_attack():
    u1 = Unit()
    u2 = Unit()

    u1.attack(u2)
    assert u2.hp == u2.hp_limit - u1.damage


def test_counter_attack():
    u1 = Unit()
    u2 = Unit()

    u1.attack(u2)
    assert u1.hp == u1.hp_limit - int(u2.damage / 2)


def test_add_hit_points():
    u1 = Unit()
    u2 = Unit()

    u1.attack(u2)
    u2.add_hit_points(u1.damage)

    assert u2.hp == u2.hp_limit
