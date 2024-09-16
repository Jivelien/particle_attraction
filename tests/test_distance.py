from __future__ import annotations

import unittest

from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import Particle, Position


class TestDistance(unittest.TestCase):
    def test_distance_when_particles_on_same_position(self):
        p1 = Particle(position=Position(0, 0))
        p2 = Particle(position=Position(0, 0))

        distance = Distance()
        sut2 = distance.between(p1, p2)

        self.assertEqual(0, sut2)

    def test_distance_when_particles_are_spaced(self):
        p1 = Particle(position=Position(0, 0))
        p2 = Particle(position=Position(3, 4))

        distance = Distance()
        sut2 = distance.between(p1, p2)

        self.assertEqual(5., sut2)
