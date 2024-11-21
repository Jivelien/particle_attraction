import unittest

from particle_attraction_lib.attraction_force import AttractionParameters, AttractionForce
from particle_attraction_lib.attraction_law import AttractionLawInterface
from particle_attraction_lib.vector import Vector


class FakeAttractionLaw(AttractionLawInterface):
    def between(self, a_species: int, another_species: int):
        return 1


class TestForce(unittest.TestCase):
    def test_when_two_particles_are_too_far_away_force_is_zero(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100),
                            attraction_law=FakeAttractionLaw())

        vector = Vector(dx=200, dy=0)

        sut = f.attraction_between(vector=vector, a_species=0, another_species=1)

        self.assertEqual(0, sut)  # add assertion here

    def test_when_two_particles_are_too_close_there_is_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25),
                            attraction_law=FakeAttractionLaw())

        vector = Vector(dx=5, dy=0)
        attraction = 1

        sut = f.attraction_between(vector=vector, a_species=0, another_species=1)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -0.8)


    def test_when_two_particles_are_on_same_position_there_is_maximal_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25),
                            attraction_law=FakeAttractionLaw())

        vector = Vector(dx=0, dy=0)

        sut = f.attraction_between(vector=vector, a_species=0, another_species=1)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -1)


    def test_when_two_particles_are_on_medium_range_there_is_attraction(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=20),
                            attraction_law=FakeAttractionLaw())

        vector = Vector(dx=60, dy=0)

        sut = f.attraction_between(vector=vector, a_species=0, another_species=1)

        self.assertGreater(sut, 0)
        self.assertAlmostEqual(sut, 1, 3)
