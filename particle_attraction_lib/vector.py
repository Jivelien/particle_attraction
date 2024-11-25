from __future__ import annotations

import functools
from dataclasses import dataclass
from math import sqrt


@dataclass
class Vector:
    dx: float
    dy: float

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.dx + other.dx,
                      self.dy + other.dy)

    def __mul__(self, factor: float) -> Vector:
        return Vector(self.dx * factor,
                      self.dy * factor)

    @property
    def length(self):
        return sqrt(self.dx ** 2 + self.dy ** 2)
