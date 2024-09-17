from __future__ import annotations

from dataclasses import dataclass


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
