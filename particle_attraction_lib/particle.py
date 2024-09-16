from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from particle_attraction_lib.color import Color
from particle_attraction_lib.vector import Vector


@dataclass
class Position:
    x: float
    y: float

    def distance_from(self, other: Position) -> float:
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)


class Particle:
    def __init__(self, position: Position) -> None:
        self.position = position
        self.velocity = Vector(dx=0, dy=0)
        self.color = None


    def accelerate(self, velocity: Vector) -> None:
        self.velocity += velocity

    def move(self) -> None:
        self.position = Position(self.position.x + self.velocity.dx,
                                 self.position.y + self.velocity.dy)

    def apply_friction(self, factor: float) -> None:
        self.velocity *= factor

class BlueParticle(Particle):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.color = Color.BLUE

class RedParticle(Particle):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.color = Color.RED

class GreenParticle(Particle):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.color = Color.GREEN