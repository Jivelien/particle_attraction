from __future__ import annotations

from particle_attraction_lib.attraction_force import AttractionForce
from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import DistanceInterface
from particle_attraction_lib.mover import MoverInterface
from particle_attraction_lib.particle import Particle
from particle_attraction_lib.particle_repository import ParticleRepository


class Game:
    def __init__(self,
                 board: Board,
                 distance: DistanceInterface,
                 mover: MoverInterface,
                 attraction_force: AttractionForce,
                 particle_repository: ParticleRepository):
        self.distance = distance
        self.attraction_force = attraction_force
        self.board = board
        self.mover = mover
        self.particle_repository = particle_repository

    def tick(self):
        self._update_all_particles()
        self._move_all_particles()

    def all_particles(self):
        return self.particle_repository.__iter__()

    def _update_all_particles(self):
        for particle in self.particle_repository:
            particle.apply_friction(0.85)
            self._update(particle)

    def _update(self, particle):
        for other_particle in self.particle_repository.neighbors_of(particle):
            self._update_attraction_between(particle, other_particle)

    def _update_attraction_between(self, a_particle: Particle,
                                   another_particle: Particle):
        vector = self.distance.vector_between(a_particle.position, another_particle.position)
        F = self.attraction_force.attraction_between(vector=vector, a_species=a_particle.species,
                                                     another_species=another_particle.species)
        a_particle.accelerate(vector * F)

    def _move_all_particles(self):
        for particle in self.particle_repository:
            self.mover.apply_movement(particle=particle)


