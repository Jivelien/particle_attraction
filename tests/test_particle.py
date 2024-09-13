from __future__ import annotations

import unittest

from particle_attraction_lib.particle import Position, Velocity, Particle


class TestPosition(unittest.TestCase):
    def test_distance_when_position_are_spaced(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        sut = p1.distance_from(p2)
        self.assertAlmostEqual(5., sut)


class TestVelocity(unittest.TestCase):
    def test_aaa(self):
        v1 = Velocity(dx=1, dy=0)
        v2 = Velocity(dx=0, dy=1)

        sut = v1 + v2
        self.assertEqual(Velocity(1, 1), sut)

    def test_bbb(self):
        v1 = Velocity(dx=1, dy=1)
        sut = v1 * 2

        self.assertEqual(Velocity(2, 2), sut)

class TestParticle(unittest.TestCase):
    def test_distance_when_particles_on_same_position(self):
        p1 = Particle(position=Position(0, 0))
        p2 = Particle(position=Position(0, 0))

        sut = p1.distance_from(p2)
        self.assertEqual(0, sut)  # add

    def test_distance_when_particles_are_spaced(self):
        p1 = Particle(position=Position(0, 0))
        p2 = Particle(position=Position(3, 4))

        sut = p1.distance_from(p2)
        self.assertAlmostEqual(5., sut)


    def test_particle_move_according_to_their_velocity(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Velocity(dx=8, dy=6))
        p1.move()

        sut = p1.distance_from(Particle(position=Position(0, 0)))
        self.assertAlmostEqual(10., sut)

    def test_velocity_can_be_added_for_one_move(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Velocity(dx=8, dy=6))
        p1.accelerate(Velocity(dx=4, dy=3))
        p1.move()

        sut = p1.distance_from(Particle(position=Position(0, 0)))
        self.assertAlmostEqual(15., sut)

    def test_particle_will_decelerate_with_a_factor(self):
        p1 = Particle(position=Position(0, 0))
        p1.accelerate(Velocity(dx=12, dy=16))
        p1.apply_friction(factor=0.5)
        p1.move()

        sut = p1.distance_from(Particle(position=Position(0, 0)))
        self.assertAlmostEqual(10., sut)