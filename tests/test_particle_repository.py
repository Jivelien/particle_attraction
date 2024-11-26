import unittest

from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.particle_repository import ParticleRepository


class TestParticleRepository(unittest.TestCase):
    def test_particle_repository_can_save_a_particle(self):
        pr = ParticleRepository()
        a_particle = Particle(position=Position(x=0, y=0))
        pr.add(a_particle)

        self.assertTrue(a_particle in pr)

    def test_particle_repository_can_give_the_neighbors_of_a_particle(self):
        pr = ParticleRepository()
        a_particle = Particle(position=Position(x=0, y=0))
        another_particle = Particle(position=Position(x=0, y=0))
        pr.add(a_particle)
        pr.add(another_particle)

        sut = pr.neighbors_of(particle = a_particle)

        self.assertEqual(sut, [another_particle])
