from __future__ import annotations

from typing import Any
from math import hypot


class Vector:
    def __init__(self, x: float = 1.0, y: float = 1.0) -> None:
        self._x = self._validate(x)
        self._y = self._validate(y)

    def _validate(self, value: Any) -> float:
        return float(value)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead'
            )

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: Any) -> None:
        self._x = self._validate(value)

    @y.setter
    def y(self, value: Any) -> None:
        self._y = self._validate(value)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: Vector) -> bool:
        self._check_type(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Vector) -> bool:
        return not self == other

    def len(self, other: Vector) -> float:
        self._check_type(other)
        return hypot(self.x - other.x, self.y - other.y)
