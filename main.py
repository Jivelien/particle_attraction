from __future__ import annotations

import random
import time
from typing import List

from particle_attraction_lib.attraction_force import AttractionParameters, AttractionForce
from particle_attraction_lib.attraction_law import AttractionLaw
from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import TorusDistance, DistanceInterface
from particle_attraction_lib.particle import BlueParticle, Position, RedParticle, GreenParticle, Particle

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
    size_of_attraction=60,
    absolute_repulsion=20,
    force_factor=10)


def update(a_particle: Particle,
           another_particle: Particle,
           attraction_force: AttractionForce,
           distance: DistanceInterface):
    vector = distance.vector_between(a_particle.position, another_particle.position)

    F = attraction_force.attraction_between(vector=vector, a_species=a_particle.species,
                                            another_species=another_particle.species)

    force_vector = vector * F * (1 / attraction_parameters.force_factor)
    a_particle.accelerate(force_vector)


def particles_tick(particles: List[Particle], board, attraction_force, distance):
    for particle in particles:
        for other_particle in particles:
            update(particle, other_particle, attraction_force, distance)

    for particle in particles:
        particle.move()
        particle.apply_friction(0.25)
        particle.position.x = particle.position.x % board.height
        particle.position.y = particle.position.y % board.width


def main():
    board = Board(1500, 1500)
    screen_size = tuple(board)
    distance = TorusDistance(board)

    attraction_force = AttractionForce(attraction_parameters=attraction_parameters, attraction_law=attraction_law)

    particles = []
    particles += [BlueParticle(Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                        y=random.randint(-int(board.height / 2), int(board.height / 2)))) for _ in
                  range(50)]
    particles += [GreenParticle(Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                         y=random.randint(-int(board.height / 2), int(board.height / 2)))) for _ in
                  range(50)]
    particles += [RedParticle(Position(x=random.randint(-int(board.width / 2), int(board.width / 2)),
                                       y=random.randint(-int(board.height / 2), int(board.height / 2)))) for _ in
                  range(50)]

    running = True

    iter = 500
    times = []
    for i in range(iter):
        time_before = time.time() * 1000
        particles_tick(particles, board, attraction_force, distance)
        time_after = time.time() * 1000

        delta_time = time_after - time_before
        times.append(delta_time)
        mean_time = sum(times)/len(times)
        print(f"iteration : {i} - time : {round(delta_time,3)} ms - average : {round(mean_time,3)} ms - maximum frequency : {1000/mean_time} Hz", end="\r")


if __name__ == '__main__':
    main()
