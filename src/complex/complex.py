from __future__ import annotations

from typing import Any


class Complex:
    def __init__(self, real: float = 1.0, imaginary: float = 1.0) -> None:
        self._real = self._validate(real)
        self._imaginary = self._validate(imaginary)

    def _validate(self, value: Any) -> float:
        return float(value)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead'
            )

    @property
    def real(self) -> float:
        return self._real

    @property
    def imaginary(self) -> float:
        return self._imaginary

    @real.setter
    def real(self, value: Any) -> None:
        self._real = self._validate(value)

    @imaginary.setter
    def imaginary(self, value: Any) -> None:
        self._imaginary = self._validate(value)

    def __str__(self) -> str:
        return f'{self.real}+{self.imaginary}i' if self.imaginary >= 0 else f'{self.real}{self.imaginary}i'

    def __eq__(self, other: Complex) -> bool:
        self._check_type(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other: Complex) -> bool:
        return not self == other
