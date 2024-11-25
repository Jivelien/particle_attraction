from __future__ import annotations

from dataclasses import dataclass

from particle_attraction_lib.vector import Vector


@dataclass
class Position:
    x: float
    y: float


class Particle:
    def __init__(self, position: Position, species: int = None) -> None:
        self.position = position
        self.velocity = Vector(dx=0, dy=0)
        self.species = species

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
        self.species = 0


class RedParticle(Particle):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.species = 1


class GreenParticle(Particle):
    def __init__(self, position: Position) -> None:
        super().__init__(position)
        self.species = 2
