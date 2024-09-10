from __future__ import annotations

import random
from math import sqrt

import pygame


class Particle:
    def __init__(self, x: float, y: float, mass = 5):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.mass = mass
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def update(self, particle: Particle):
        dx = particle.x - self.x
        dy = particle.y - self.y

        d = sqrt(dx ** 2 + dy ** 2)
        F = 0
        if d != 0:
            F = ((self.mass * particle.mass) / (d * d))/self.mass

        self.x_velocity += F * dx
        self.y_velocity += F * dy

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def __repr__(self):
        return f'Particle(x={self.x}, y={self.y}, m={self.mass})'


particles = [Particle(random.randint(-400,400), random.randint(-400,400), random.randint(1,5)) for _ in range(5)]

secreen_size = (1200, 800)
screen = pygame.display.set_mode(secreen_size)
pygame.display.set_caption("Particles")

screen.fill((0,0,0))
surface_transparente = pygame.Surface(secreen_size, pygame.SRCALPHA)
surface_transparente.fill((0, 0, 0, 1))

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(surface_transparente, (0, 0))

    for particle in particles:
        for other_particle in particles:
            particle.update(other_particle)

    for particle in particles:
        particle.move()

        pygame.draw.circle(screen, color=particle.color, center=(particle.x + secreen_size[0]/2, particle.y + secreen_size[1]/2), radius=particle.mass)

    pygame.display.flip()
    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
