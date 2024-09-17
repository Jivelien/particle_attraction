from __future__ import annotations

import functools
from abc import ABC, abstractmethod
from math import sqrt, copysign
from typing import Tuple

from particle_attraction_lib.board import Board
from particle_attraction_lib.particle import Position
from particle_attraction_lib.vector import Vector


class DistanceInterface(ABC):
    @abstractmethod
    def between(self, p1: Position, p2: Position) -> float:
        raise NotImplementedError

    @abstractmethod
    def vector_between(self, p1: Position, p2: Position) -> Vector:
        raise NotImplementedError


class Distance(DistanceInterface):
    def between(self, p1: Position, p2: Position) -> float:
        return p1.distance_from(p2)

    def vector_between(self, p1: Position, p2: Position) -> Vector:
        return Vector(dx=self._between_x(p1, p2),
                      dy=self._between_y(p1, p2))

    def _between_x(self, p1: Position, p2: Position) -> float:
        return p2.x - p1.x

    def _between_y(self, p1: Position, p2: Position) -> float:
        return p2.y - p1.y


class TorusDistance(DistanceInterface):
    def __init__(self, board: Board):
        self._width, self._height = board

    def between(self, p1: Position, p2: Position) -> float:
        dx = self._between_x(p1, p2)
        dy = self._between_y(p1, p2)

        return sqrt(dx ** 2 + dy ** 2)

    def vector_between(self, p1: Position, p2: Position) -> Vector:
        return Vector(dx=self._between_x(p1,p2),
                      dy=self._between_y(p1,p2))

    def _between_x(self, p1: Position, p2: Position) -> float:
        return self._between_value(p1.x, p2.x, length=self._width)

    def _between_y(self, p1: Position, p2: Position) -> float:
        return self._between_value(p1.y, p2.y, length=self._height)

    def _between_value(self, p1: float, p2: float, length: float) -> float:
        d = p2 - p1
        if abs(d) > length / 2:
            d -= length * copysign(1, d)
        return d

