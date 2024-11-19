from __future__ import annotations

import random
from typing import List

from particle_attraction_lib.board import Board
from particle_attraction_lib.distance import TorusDistance
from particle_attraction_lib.particle import BlueParticle, Position, RedParticle, GreenParticle, Particle

law_of_attraction = {
    (0, 0): 0,
    (0, 1): -0.6,
    (0, 2): 0.9,
    (1, 0): 0.6,
    (1, 1): 0,
    (1, 2): 1,
    (2, 0): 0.4,
    (2, 1): 0.2,
    (2, 2): 0
}

board = Board(1500, 1500)
screen_size = tuple(board)
distance = TorusDistance(board)

config = { "reduc" : 10,
           "zone": 60,
           "min": 0.35}
particles = []
particles += [BlueParticle(Position(x=random.randint(-int(board.width/2), int(board.width/2)), y=random.randint(-int(board.height/2), int(board.height/2)))) for _ in range(50)]
particles += [GreenParticle(Position(x=random.randint(-int(board.width/2), int(board.width/2)), y=random.randint(-int(board.height/2), int(board.height/2)))) for _ in range(50)]
particles += [RedParticle(Position(x=random.randint(-int(board.width/2), int(board.width/2)), y=random.randint(-int(board.height/2), int(board.height/2)))) for _ in range(50)]

def update(a_particule: Particle, another_particle: Particle, distance):
    attraction = law_of_attraction.get((a_particule.species, another_particle.species), 0)

    vector = distance.vector_between(a_particule.position, another_particle.position)
    d = distance.distance_of_vector(vector)

    reduc = config.get("reduc")
    d_rel = d / config.get("zone")
    dist = config.get("min")
    if d_rel > 1:
        F = 0
    elif d_rel == 0:
        F = -reduc
    elif d_rel <= dist:
        F = (d_rel / dist - 1) * reduc
    elif d_rel <= 1:
        F = attraction * (1 - (abs(2 * d_rel - 1 - dist)) / (1 - dist))

    force_vector = vector * F * (1/reduc)
    a_particule.accelerate(force_vector)

def particles_tick(particles: List[Particle], distance):
    for particle in particles:
        for other_particle in particles:
            update(particle, other_particle, distance)

    for particle in particles:
        particle.move()
        particle.apply_friction(0.25)
        particle.position.x = particle.position.x % board.height
        particle.position.y = particle.position.y % board.width

def main():
    board = Board(1500, 1500)
    screen_size = tuple(board)
    distance = TorusDistance(board)

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

    for i in range(100):
        particles_tick(particles, distance)


if __name__ == '__main__':
    main()

# Particle initialization
