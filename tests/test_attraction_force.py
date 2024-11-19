import unittest

from particle_attraction_lib.attraction_force import AttractionParameters, AttractionForce
from particle_attraction_lib.attraction_law import AttractionLawInterface
from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import Particle, Position


class FakeAttractionLaw(AttractionLawInterface):
    def __init__(self, global_attraction: float):
        self.global_attraction = global_attraction

    def between(self, a_species: int, another_species: int):
        return self.global_attraction


class TestForce(unittest.TestCase):
    def test_when_two_particles_are_too_far_away_force_is_zero(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100),
                            distance=Distance(),
                            attraction_law=FakeAttractionLaw(global_attraction=1))

        p1 = Particle(position=Position(0, 0), species=0)
        p2 = Particle(position=Position(200, 0), species=1)

        sut = f.attraction_between(a_particle=p1, another_particle=p2)

        self.assertEqual(0, sut)  # add assertion here

    def test_when_two_particles_are_too_close_there_is_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25),
                            distance=Distance(),
                            attraction_law=FakeAttractionLaw(global_attraction=1))

        p1 = Particle(position=Position(0, 0), species=0)
        p2 = Particle(position=Position(5, 0), species=1)

        sut = f.attraction_between(a_particle=p1, another_particle=p2)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -0.8)

    def test_when_two_particles_are_on_same_position_there_is_maximal_repulsion(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=25),
                            distance=Distance(),
                            attraction_law=FakeAttractionLaw(global_attraction=1))

        p1 = Particle(position=Position(0, 0), species=0)
        p2 = Particle(position=Position(0, 0), species=1)

        sut = f.attraction_between(a_particle=p1, another_particle=p2)

        self.assertLess(sut, 0)
        self.assertEqual(sut, -1)


    def test_when_two_particles_are_on_medium_range_there_is_attraction(self):
        f = AttractionForce(attraction_parameters=AttractionParameters(size_of_attraction=100,
                                                                       absolute_repulsion=20),
                            distance=Distance(),
                            attraction_law=FakeAttractionLaw(global_attraction=1))

        p1 = Particle(position=Position(0, 0), species=0)
        p2 = Particle(position=Position(60, 0), species=1)

        sut = f.attraction_between(a_particle=p1, another_particle=p2)

        self.assertGreater(sut, 0)
        self.assertAlmostEqual(sut, 1, 3)