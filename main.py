from __future__ import annotations

import random

import pygame

from particle_attraction_lib.color import Color
from particle_attraction_lib.distance import Distance, TorusDistance
from particle_attraction_lib.particle import BlueParticle, Position, RedParticle, GreenParticle, Particle
from particle_attraction_lib.vector import Vector

law_of_attraction = {
    (Color.BLUE, Color.BLUE): -0.1,
    (Color.BLUE, Color.GREEN): -0.5,
    (Color.BLUE, Color.RED): 0.8,
    (Color.GREEN, Color.BLUE): 0.5,
    (Color.GREEN, Color.GREEN): -0.1,
    (Color.GREEN, Color.RED): 0.5,
    (Color.RED, Color.BLUE): 1,
    (Color.RED, Color.GREEN): 1,
    (Color.RED, Color.RED): -0.1

}

def update(a_particule: Particle, another_particle: Particle):
    attraction = law_of_attraction.get((a_particule.color, another_particle.color))

    # distance = Distance()
    distance = TorusDistance((500,500))
    vector = distance.vector_between(a_particule.position, another_particle.position)
    d = distance.between(a_particule.position, another_particle.position)

    F = 0
    d_rel = d / 200
    dist = 0.3
    if d_rel == 0:
        F = -1
    elif d_rel <= dist:
        F = (d_rel / dist - 1)
    elif d_rel <= 1:
        F = attraction * (1 - (abs(2 * d_rel - 1 - dist)) / (1 - dist))

    force_vector = vector * F * 0.01
    a_particule.accelerate(force_vector)


particles = []
particles += [BlueParticle(Position(x=random.randint(-400, 400),
                                    y=random.randint(-400, 400)))
              for _ in range(40)]
particles += [GreenParticle(Position(x=random.randint(-400, 400),
                                     y=random.randint(-400, 400)))
              for _ in range(40)]
particles += [RedParticle(Position(x=random.randint(-400, 400),
                                   y=random.randint(-400, 400)))
              for _ in range(40)]

screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Particles")

screen.fill((0, 0, 0))
surface_transparente = pygame.Surface(screen_size, pygame.SRCALPHA)
surface_transparente.fill((0, 0, 0, 25))

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(surface_transparente, (0, 0))

    for particle in particles:
        for other_particle in particles:
            update(particle, other_particle)

    for particle in particles:
        particle.position.x = particle.position.x % 500
        particle.position.y = particle.position.y % 500

        particle.move()
        particle.apply_friction(0.25)

        pygame.draw.circle(screen, color=particle.color.value,
                           center=(particle.position.x, particle.position.y ),
                           radius=5)

    pygame.display.flip()
    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
