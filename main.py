from __future__ import annotations

import random

import pygame

from particle_attraction_lib.color import Color
from particle_attraction_lib.distance import Distance
from particle_attraction_lib.particle import BlueParticle, Position, RedParticle, GreenParticle, Particle

law_of_attraction = {
    (Color.BLUE, Color.BLUE): 1,
    (Color.BLUE, Color.GREEN): 2,
    (Color.BLUE, Color.RED): 0.1,
    (Color.GREEN, Color.GREEN): -0.1,
    (Color.GREEN, Color.BLUE): 1.5,
    (Color.GREEN, Color.RED): 0.5,
    (Color.RED, Color.GREEN): 0.5,
    (Color.RED, Color.BLUE): -0.1,
    (Color.RED, Color.RED): 0

}

def update(a_particule: Particle, another_particle: Particle):
    attraction = law_of_attraction.get((a_particule.color, another_particle.color))

    distance = Distance()
    vector = distance.vector_between(a_particule.position, another_particle.position)
    d = distance.between(a_particule.position, another_particle.position)

    F = 0
    d_rel = d / 200
    dist = 0.1
    if d_rel == 0:
        F = -1
    elif d_rel <= dist:
        F = (d_rel / dist - 1)
    elif d_rel <= 1:
        F = attraction * (1 - (abs(2 * d_rel - 1 - dist)) / (1 - dist)) / 50
    a_particule.accelerate(vector * F)


particles = []
particles += [BlueParticle(Position(x=random.randint(-400, 400),
                                    y=random.randint(-400, 400)))
              for _ in range(25)]
particles += [GreenParticle(Position(x=random.randint(-400, 400),
                                     y=random.randint(-400, 400)))
              for _ in range(25)]
particles += [RedParticle(Position(x=random.randint(-400, 400),
                                   y=random.randint(-400, 400)))
              for _ in range(25)]

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
        if particle.position.x + screen_size[0] / 2 < 0:
            particle.velocity.dx = -particle.velocity.dx
            particle.position.x = -screen_size[0] / 2 + 1
        if particle.position.x + screen_size[0] / 2 > screen_size[0]:
            particle.velocity.dx = -particle.velocity.dx
            particle.position.x = screen_size[0] / 2 - 1
        if particle.position.y + screen_size[1] / 2 < 0:
            particle.velocity.dy = -particle.velocity.dy
            particle.position.y = -screen_size[1] / 2 + 1
        if particle.position.y + screen_size[1] / 2 > screen_size[1]:
            particle.velocity.dy = -particle.velocity.dy
            particle.position.y = screen_size[1] / 2 - 1

        particle.move()
        particle.apply_friction(0.75)

        pygame.draw.circle(screen, color=particle.color.value,
                           center=(particle.position.x + screen_size[0] / 2, particle.position.y + screen_size[1] / 2),
                           radius=5)

    pygame.display.flip()
    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
