from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass
class Position:
    x: float
    y: float

    def distance_from(self, other: Position) -> float:
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)


@dataclass
class Velocity:
    dx: float
    dy: float

    def __add__(self, other: Velocity) -> Velocity:
        return Velocity(self.dx + other.dx,
                        self.dy + other.dy)

    def __mul__(self, factor: float) -> Velocity:
        return Velocity(self.dx * factor,
                        self.dy * factor)


class Particle:
    def __init__(self, position: Position) -> None:
        self.position = position
        self.velocity = Velocity(dx=0, dy=0)

    def distance_from(self, other_particle: Particle) -> float:
        other_position = other_particle.position
        return self.position.distance_from(other_position)

    def accelerate(self, velocity: Velocity) -> None:
        self.velocity += velocity

    def move(self) -> None:
        self.position = Position(self.position.x + self.velocity.dx,
                                 self.position.y + self.velocity.dy)

    def apply_friction(self, factor: float) -> None:
        self.velocity *= factor
