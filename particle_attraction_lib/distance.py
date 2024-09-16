from __future__ import annotations

from particle_attraction_lib.particle import Particle, Vector


class Distance:
    def between(self, p1: Particle, p2: Particle) -> float:
        return p1.position.distance_from(p2.position)

    def between_x(self, p1: Particle, p2: Particle) -> float:
        return p2.position.x - p1.position.x

    def between_y(self, p1: Particle, p2: Particle) -> float:
        return p2.position.y - p1.position.y

    def vector_between(self, p1, p2) -> Vector:
        return Vector(dx = self.between_x(p1, p2),
                      dy = self.between_y(p1, p2))

