from __future__ import annotations

import enum
import random
from math import sqrt

import pygame


class Color(enum.Enum):
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

law_of_attraction = {
            (Color.BLUE, Color.BLUE): 3,
            (Color.BLUE, Color.GREEN): 5,
            (Color.BLUE, Color.RED): 0.1,
            (Color.GREEN, Color.GREEN): -3,
            (Color.GREEN, Color.BLUE): 3,
            (Color.GREEN, Color.RED): 0.3,
            (Color.RED, Color.GREEN): 2,
            (Color.RED, Color.BLUE): -1 ,
            (Color.RED, Color.RED): 0

        }

class Particle:
    def __init__(self, x: float, y: float, color: Color, mass=1):

        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.mass = mass
        self.color = color

    def update(self, particle: Particle):
        attraction = law_of_attraction.get((self.color, particle.color))

        dx = particle.x - self.x
        dy = particle.y - self.y

        d = sqrt(dx ** 2 + dy ** 2)
        F=0
        if 1 < d :
            F = attraction * (self.mass * particle.mass) / (pow(d, 1)  * pow(self.mass, 2))
        self.x_velocity += (F * dx)/2
        self.y_velocity += (F * dy)/2



    def reverse_x_velocity(self):
        self.x_velocity /= -2


    def reverse_y_velocity(self):
        self.y_velocity /= -2

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.x_velocity *= 0.8
        self.y_velocity *= 0.8

    def __repr__(self):
        return f'Particle(x={self.x}, y={self.y}, m={self.mass})'

particles = []
particles += [Particle(x=random.randint(-400, 400),
                      y=random.randint(-400, 400),
                      mass=1,
                      color=Color.BLUE) for _ in range(50)]
particles += [Particle(x=random.randint(-400, 400),
                      y=random.randint(-400, 400),
                      mass=1,
                      color=Color.GREEN) for _ in range(50)]
particles += [Particle(x=random.randint(-400, 400),
                      y=random.randint(-400, 400),
                       mass=1,
                      color=Color.RED) for _ in range(50)]

secreen_size = (1200, 1200)
screen = pygame.display.set_mode(secreen_size)
pygame.display.set_caption("Particles")

screen.fill((0, 0, 0))
surface_transparente = pygame.Surface(secreen_size, pygame.SRCALPHA)
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
            particle.update(other_particle)

    for particle in particles:
        if particle.dx + secreen_size[0] / 2 < 0:
            particle.reverse_x_velocity()
            particle.dx = -secreen_size[0] / 2 + 1
        if particle.dx + secreen_size[0] / 2 > secreen_size[0]:
            particle.reverse_x_velocity()
            particle.dx = secreen_size[0] / 2 - 1
        if particle.dy + secreen_size[1] / 2 < 0:
            particle.reverse_y_velocity()
            particle.dy = -secreen_size[1] / 2 + 1
        if particle.dy + secreen_size[1] / 2 > secreen_size[1]:
            particle.reverse_y_velocity()
            particle.dy = secreen_size[1] / 2 - 1

        particle.move()

        pygame.draw.circle(screen, color=particle.color.value,
                           center=(particle.dx + secreen_size[0] / 2, particle.dy + secreen_size[1] / 2),
                           radius=particle.mass*5)

    pygame.display.flip()
    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
