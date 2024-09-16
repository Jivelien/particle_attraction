from __future__ import annotations

from particle_attraction_lib.particle import Vector, Position


class Distance:
    def between(self, p1: Position, p2: Position) -> float:
        return p1.distance_from(p2)

    def between_x(self, p1: Position, p2: Position) -> float:
        return p2.x - p1.x

    def between_y(self, p1: Position, p2: Position) -> float:
        return p2.y - p1.y

    def vector_between(self, p1: Position, p2: Position) -> Vector:
        return Vector(dx=self.between_x(p1, p2),
                      dy=self.between_y(p1, p2))
