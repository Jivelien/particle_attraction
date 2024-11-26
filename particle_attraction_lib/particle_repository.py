from typing import List

from particle_attraction_lib.particle import Particle


class ParticleRepository:
    def __init__(self):
        self._all_particles: List[Particle] = []

    def add(self, particle: Particle):
        self._all_particles.append(particle)

    def neighbors_of(self, particle: Particle):
        return [other_particle for other_particle in self._all_particles if particle != other_particle]

    def __contains__(self, item: Particle):
        return item in self._all_particles

    def __iter__(self):
        return self._all_particles.copy().__iter__()
