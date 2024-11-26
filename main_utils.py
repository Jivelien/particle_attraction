from __future__ import annotations

import random

from particle_attraction_lib.attraction_force import AttractionForce
from particle_attraction_lib.attraction_law import AttractionLaw
from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import TorusDistance
from particle_attraction_lib.particle import Particle, Position
from particle_attraction_lib.particle_repository import ParticleRepository
from particle_attraction_lib.game import Game


def configure_attraction_law():
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
    return attraction_law


def init_game(board: Board, attraction_parameters, number_of_particles: int):
    attraction_law = configure_attraction_law()
    attraction_force = AttractionForce(attraction_parameters=attraction_parameters, attraction_law=attraction_law)

    distance = TorusDistance(board)

    particles = create_particles(board, number_of_particles)

    game = Game(distance=distance, attraction_force=attraction_force, board=board,
                particle_repository=particles)
    return game


def create_particles(board, number_of_particles):
    particles = ParticleRepository()
    particles.add_multiple([Particle(position=Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                                       y=random.randint(-int(board.height / 2), int(board.height / 2))),
                                     species=random.randint(0, 2)) for _ in
                            range(number_of_particles)])
    return particles
