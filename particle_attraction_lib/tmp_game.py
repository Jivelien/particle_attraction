from __future__ import annotations

import random
from typing import List

from particle_attraction_lib.attraction_force import AttractionForce, AttractionParameters
from particle_attraction_lib.attraction_law import AttractionLaw
from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import DistanceInterface, TorusDistance
from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.particle_repository import ParticleRepository


class TemporaryGame:
    def __init__(self, distance: DistanceInterface, attraction_force: AttractionForce, board: Board, particle_repository: ParticleRepository):
        self.distance = distance
        self.attraction_force = attraction_force
        self.board = board
        self.particle_repository = particle_repository

    def update(self, a_particle: Particle,
               another_particle: Particle):
        vector = self.distance.vector_between(a_particle.position, another_particle.position)
        F = self.attraction_force.attraction_between(vector=vector, a_species=a_particle.species,
                                                     another_species=another_particle.species)
        a_particle.accelerate(vector * F)

    def particles_tick(self):
        for particle in self.particle_repository.all():
            for other_particle in self.particle_repository.neighbors_of(particle):
                if particle != other_particle:
                    self.update(particle, other_particle)
        for particle in self.particle_repository.all():
            particle.move()
            particle.apply_friction(0.80)
            particle.position.x = particle.position.x % self.board.height
            particle.position.y = particle.position.y % self.board.width

    def all_particles(self):
        return self.particle_repository.all()


def init_game(board: Board):
    attraction_law = AttractionLaw()
    attraction_law.add(0, 0, 0)
    attraction_law.add(0, 1, -0.6)
    attraction_law.add(0, 2, 0.9)
    attraction_law.add(1, 0, 0.6)
    attraction_law.add(1, 1, 0)
    attraction_law.add(1, 2, 1)
    attraction_law.add(2, 0, 0.4)
    attraction_law.add(2, 1, 0.2)
    attraction_law.add(2, 2, 0)
    attraction_parameters = AttractionParameters(
        size_of_attraction=75,
        absolute_repulsion=5,
        force_factor=200)
    distance = TorusDistance(board)
    attraction_force = AttractionForce(attraction_parameters=attraction_parameters, attraction_law=attraction_law)
    particles = ParticleRepository()
    particles.add_multiple([Particle(position=Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                                       y=random.randint(-int(board.height / 2), int(board.height / 2))),
                                     species=random.randint(0, 2)) for _ in
                            range(180)])

    game = TemporaryGame(distance=distance, attraction_force=attraction_force, board=board, particle_repository=particles)
    return game
