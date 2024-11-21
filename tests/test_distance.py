from __future__ import annotations

import unittest

from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import Distance, TorusDistance
from particle_attraction_lib.particle import Position
from particle_attraction_lib.vector import Vector


class TestDistance(unittest.TestCase):
    def test_distance_when_particles_on_same_position(self):
        p1 = Position(0, 0)
        p2 = Position(0, 0)

        distance = Distance()
        sut = distance.between(p1, p2)

        self.assertEqual(0, sut)

    def test_distance_when_particles_are_spaced(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        distance = Distance()
        sut = distance.between(p1, p2)

        self.assertEqual(5., sut)

    def test_vector_distance_between_particles(self):
        p1 = Position(1, 1)
        p2 = Position(3, 4)

        distance = Distance()
        sut = distance.vector_between(p1, p2)

        self.assertEqual(Vector(dx=2, dy=3), sut)


class TestTorusDistance(unittest.TestCase):
    def test_distance_between_positions_when_shorter_on_grid(self):
        p1 = Position(0, 0)
        p2 = Position(100, 50)

        distance = TorusDistance(board=Board(500, 500))
        sut = distance.vector_between(p1, p2)

        self.assertEqual(Vector(dx=100, dy=50), sut)

    def test_distance_between_positions_when_shorter_on_right(self):
        p1 = Position(450, 0)
        p2 = Position(50, 50)

        distance = TorusDistance(board=Board(500, 500))
        sut = distance.vector_between(p1, p2)

        self.assertEqual(Vector(dx=100, dy=50), sut)

    def test_vector_distance_between_positions_when_shorter_on_left(self):
        p1 = Position(100, 0)
        p2 = Position(400, 50)

        distance = TorusDistance(board=Board(500, 500))
        sut = distance.vector_between(p1, p2)

        self.assertEqual(Vector(dx=-200, dy=50), sut)

    def test_distance_between_positions(self):
        p1 = Position(400, 0)
        p2 = Position(200, 500)

        distance = TorusDistance(board=Board(500, 500))
        sut = distance.between(p1, p2)

        self.assertEqual(200., sut)
