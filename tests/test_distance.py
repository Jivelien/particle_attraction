from __future__ import annotations

import unittest

from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import Particle, Position, Vector


class TestDistance(unittest.TestCase):
    def test_distance_when_particles_on_same_position(self):
        p1 = Position(0, 0)
        p2 = Position(0, 0)

        distance = Distance()
        sut2 = distance.between(p1, p2)

        self.assertEqual(0, sut2)

    def test_distance_when_particles_are_spaced(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        distance = Distance()
        sut2 = distance.between(p1, p2)

        self.assertEqual(5., sut2)

    def test_distance_on_horizontal_axis(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        distance = Distance()
        sut2 = distance.between_x(p1, p2)

        self.assertEqual(3, sut2)

    def test_distance_on_vertical_axis(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        distance = Distance()
        sut2 = distance.between_y(p1, p2)

        self.assertEqual(4, sut2)

    def test_vector_distance_between_particles(self):
        p1 = Position(1, 1)
        p2 = Position(3, 4)

        distance = Distance()
        sut2 = distance.vector_between(p1, p2)

        self.assertEqual(Vector(dx=2, dy=3), sut2)
