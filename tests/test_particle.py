from __future__ import annotations

import unittest

from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import Position, Vector, Particle


class TestParticle(unittest.TestCase):
    def test_particle_move_according_to_their_velocity(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Vector(dx=8, dy=6))
        p1.move()

        distance = Distance()
        sut2 = distance.between(p1, Particle(position=Position(0, 0)))

        self.assertEqual(10., sut2)

    def test_velocity_can_be_added_for_one_move(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Vector(dx=8, dy=6))
        p1.accelerate(Vector(dx=4, dy=3))
        p1.move()

        distance = Distance()
        sut2 = distance.between(p1, Particle(position=Position(0, 0)))

        self.assertEqual(15., sut2)

    def test_particle_will_decelerate_with_a_factor(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Vector(dx=12, dy=16))
        p1.apply_friction(factor=0.5)
        p1.move()

        distance = Distance()
        sut2 = distance.between(p1, Particle(position=Position(0, 0)))

        self.assertEqual(10., sut2)
