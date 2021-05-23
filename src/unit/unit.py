from __future__ import annotations

from typing import Any


class Unit:
    def __init__(self, name: str = 'Vasya', hp: int = '100', damage: int = '5') -> None:
        self._name = self._validate_str(name)
        self._hp = self._validate_int(hp)
        self._hp_limit = self._hp
        self._damage = self._validate_int(damage)

    def _validate_int(self, value: Any) -> int:
        return int(value)

    def _validate_str(self, value: Any) -> str:
        return str(value)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead.'
            )

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def hp_limit(self) -> int:
        return self._hp_limit

    @property
    def damage(self) -> int:
        return self._damage

    @name.setter
    def name(self, value: Any) -> None:
        self._name = self._validate_str(value)

    @hp.setter
    def hp(self, value: Any) -> None:
        self._hp = self._validate_int(value)

    @hp_limit.setter
    def hp_limit(self, value: Any) -> None:
        self._hp_limit = self._validate_int(value)

    @damage.setter
    def damage(self, value: Any) -> None:
        self._damage = self._validate_int(value)

    def __str__(self) -> str:
        return f'{self.name} {self.hp}/{self.hp_limit}hp, damage: {self.damage}'

    def ensure_is_alive(self) -> None:
        if self._hp == 0:
            raise PermissionError('Unit is dead')

    def add_hit_points(self, hp: int) -> None:
        self.ensure_is_alive()

        if hp > 0:
            potential_hp = self.hp + hp

            if potential_hp > self.hp_limit:
                potential_hp = self.hp_limit
            self._hp = potential_hp

    def take_damage(self, dmg: int) -> None:
        self.ensure_is_alive()

        if dmg > 0:
            potential_hp = self._hp - dmg
            if potential_hp < 0:
                potential_hp = 0
            self._hp = potential_hp

    def attack(self, enemy: Unit):
        self._check_type(enemy)
        enemy.take_damage(self._damage)

        if enemy.hp != 0:
            enemy.counter_attack(self)

    def counter_attack(self, enemy: Unit):
        enemy.take_damage(int(self._damage / 2))
