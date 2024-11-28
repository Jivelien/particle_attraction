from __future__ import annotations

import random

from particle_attraction_lib.attraction_force import AttractionForce
from particle_attraction_lib.attraction_law import AttractionLaw
from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import TorusDistance
from particle_attraction_lib.mover import TorusMover
from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.particle_repository import ParticleRepository
from particle_attraction_lib.game import Game


def configure_attraction_law(number_of_species):
    attraction_law = AttractionLaw()
    for specie in range(number_of_species):
        for other in range(number_of_species):
            attraction_law.add(specie, other, round(random.random() *2 -1, 1))
    return attraction_law


def init_game(board: Board, attraction_parameters, number_of_particles: int, number_of_species: int):
    distance = TorusDistance(board)
    mover = TorusMover(board)
    particles = create_particles(board, number_of_particles, number_of_species)

    attraction_law = configure_attraction_law(number_of_species)
    attraction_force = AttractionForce(attraction_parameters=attraction_parameters, attraction_law=attraction_law)

    game = Game(distance=distance,
                attraction_force=attraction_force,
                board=board,
                mover=mover,
                particle_repository=particles)
    return game


def create_particles(board, number_of_particles, number_of_species: int):
    particles = ParticleRepository()
    all_particles_to_add = [Particle(position=Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                                       y=random.randint(-int(board.height / 2), int(board.height / 2))),
                                     species=random.randint(0, number_of_species-1)) for _ in
                            range(number_of_particles)]
    for particle in all_particles_to_add:
        particles.add(particle)
    return particles
