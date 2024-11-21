import unittest

from particle_attraction_lib.attraction_force import AttractionParameters, AttractionForce
from particle_attraction_lib.attraction_law import AttractionLawInterface
from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.vector import Vector


class TestForce(unittest.TestCase):
    def test_when_two_particles_are_too_far_away_force_is_zero(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100))

        vector = Vector(dx=200, dy=0)
        attraction = 1

        sut = f.attraction_between(vector=vector, attraction=attraction)

        self.assertEqual(0, sut)  # add assertion here

    def test_when_two_particles_are_too_close_there_is_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25))

        vector = Vector(dx=5, dy=0)
        attraction = 1

        sut = f.attraction_between(vector=vector, attraction=attraction)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -0.8)

    def test_when_two_particles_are_on_same_position_there_is_maximal_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25))

        vector = Vector(dx=0, dy=0)
        attraction = 1

        sut = f.attraction_between(vector=vector, attraction=attraction)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -1)

    @unittest.skip("")
    def test_when_two_particles_are_on_medium_range_there_is_attraction(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=20))

        vector = Vector(dx=60, dy=0)
        attraction = 1

        sut = f.attraction_between(vector=vector, attraction=attraction)

        self.assertGreater(sut, 0)
        self.assertAlmostEqual(sut, 1, 3)
