import unittest

from particle_attraction_lib.board import Board
from particle_attraction_lib.mover import Mover, TorusMover
from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.vector import Vector


class TestMover(unittest.TestCase):
    def test_something(self):
        particle = Particle(position=Position(x=0,y=0))
        particle.accelerate(velocity=Vector(dx=1, dy=1))

        m = Mover()

        m.apply_movement(particle=particle)

        self.assertEqual(particle.position, Position(x=1,y=1))


class TestTorusMover(unittest.TestCase):
    def test_something(self):
        particle = Particle(position=Position(x=0,y=0))
        particle.accelerate(velocity=Vector(dx=150, dy=150))

        m = TorusMover(board=Board(100, 100))

        m.apply_movement(particle=particle)

        self.assertEqual(particle.position, Position(x=50,y=50))

