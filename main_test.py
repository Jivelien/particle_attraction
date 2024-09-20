from __future__ import annotations

import random
from typing import List

import pygame
import pygame_gui

from particle_attraction_lib.board import Board
from particle_attraction_lib.color import Color
from particle_attraction_lib.distance import TorusDistance
from particle_attraction_lib.particle import BlueParticle, Position, RedParticle, GreenParticle, Particle

pygame.init()
# law_of_attraction = {
#     (Color.BLUE, Color.BLUE): -0.1,
#     (Color.BLUE, Color.GREEN): 0.5,
#     (Color.BLUE, Color.RED): -0.8,
#     (Color.GREEN, Color.BLUE): 0.5,
#     (Color.GREEN, Color.GREEN): -0.3,
#     (Color.GREEN, Color.RED): 0.25,
#     (Color.RED, Color.BLUE): -0.5,
#     (Color.RED, Color.GREEN): 0.6,
#     (Color.RED, Color.RED): -0.3
# }
law_of_attraction = {
    (Color.BLUE, Color.BLUE): 0,
    (Color.BLUE, Color.GREEN): -0.6,
    (Color.BLUE, Color.RED): 0.9,
    (Color.GREEN, Color.BLUE): 0.6,
    (Color.GREEN, Color.GREEN): 0,
    (Color.GREEN, Color.RED): 1,
    (Color.RED, Color.BLUE): 0.4,
    (Color.RED, Color.GREEN): 0.2,
    (Color.RED, Color.RED): 0
}

board = Board(500, 500)
screen_size = tuple(board)
distance = TorusDistance(board)

config = { "reduc" : 10,
           "zone": 60,
           "min": 0.35}
particles = []
particles += [BlueParticle(Position(x=random.randint(-400, 400), y=random.randint(-400, 400))) for _ in range(35)]
particles += [GreenParticle(Position(x=random.randint(-400, 400), y=random.randint(-400, 400))) for _ in range(35)]
particles += [RedParticle(Position(x=random.randint(-400, 400), y=random.randint(-400, 400))) for _ in range(35)]

def update(a_particule: Particle, another_particle: Particle, distance):
    attraction = law_of_attraction.get((a_particule.color, another_particle.color), 0)

    vector = distance.vector_between(a_particule.position, another_particle.position)
    d = distance.between(a_particule.position, another_particle.position)

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

def particles_tick(particles: List[Particle]):
    for particle in particles:
        for other_particle in particles:
            update(particle, other_particle, distance)

    for particle in particles:
        particle.move()
        particle.apply_friction(0.25)
        particle.position.x = particle.position.x % 500
        particle.position.y = particle.position.y % 500


# Particle initialization

screen = pygame.display.set_mode((board.width+300, board.height))
pygame.display.set_caption("Particles")
screen.fill((0, 0, 0))
surface_transparente = pygame.Surface((board.height+300, board.width), pygame.SRCALPHA)
surface_transparente.fill((0, 0, 0, 25))

manager = pygame_gui.UIManager((500,500))


blue_blue_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 10), (200, 25)),
                                                          start_value=float(law_of_attraction.get((Color.BLUE, Color.BLUE),0)),
                                                          value_range=(-2, 2),click_increment=0.1,
                                                          manager=manager)
blue_blue_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 10), (150, 25)), text=f"blue-blue: {blue_blue_slider.get_current_value()}", manager=manager)

blue_green_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 50), (200, 25)),
                                                           start_value=float(law_of_attraction.get((Color.BLUE,Color.GREEN),0)),
                                                           value_range=(-2, 2),click_increment=0.1,
                                                           manager=manager)
blue_green_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 50), (150, 25)), text=f"blue-green: {blue_green_slider.get_current_value()}", manager=manager)

blue_red_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 90), (200, 25)),
                                                         start_value=float(law_of_attraction.get((Color.BLUE,Color.RED),0)),
                                                         value_range=(-2, 2),click_increment=0.1,
                                                         manager=manager)
blue_red_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 90), (150, 25)), text=f"blue-red: {blue_red_slider.get_current_value()}", manager=manager)

green_green_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 130), (200, 25)),
                                                            start_value=float(law_of_attraction.get((Color.GREEN,Color.GREEN),0)),
                                                            value_range=(-2, 2),click_increment=0.1,
                                                            manager=manager)
green_green_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 130), (150, 25)), text=f"green-green: {green_green_slider.get_current_value()}", manager=manager)

green_red_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 170), (200, 25)),
                                                          start_value=float(law_of_attraction.get((Color.GREEN,Color.RED),0)),
                                                          value_range=(-2, 2),click_increment=0.1,
                                                          manager=manager)
green_red_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 170), (150, 25)), text=f"green-red: {green_red_slider.get_current_value()}", manager=manager)

green_blue_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 210), (200, 25)),
                                                           start_value=float(law_of_attraction.get((Color.GREEN,Color.BLUE),0)),
                                                           value_range=(-2, 2),click_increment=0.1,
                                                           manager=manager)
green_blue_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 210), (150, 25)), text=f"green-blue: {green_blue_slider.get_current_value()}", manager=manager)

red_green_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 250), (200, 25)),
                                                          start_value=float(law_of_attraction.get((Color.RED,Color.GREEN),0)),
                                                          value_range=(-2, 2),click_increment=0.1,
                                                          manager=manager)
red_green_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 250), (150, 25)), text=f"red-green: {red_green_slider.get_current_value()}", manager=manager)

red_red_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 290), (200, 25)),
                                                        start_value=float(law_of_attraction.get((Color.RED,Color.RED),0)),
                                                        value_range=(-2, 2),click_increment=0.1,
                                                        manager=manager)
red_red_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 290), (150, 25)), text=f"red-red: {red_red_slider.get_current_value()}", manager=manager)

red_blue_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 330), (200, 25)),
                                                         start_value=float(law_of_attraction.get((Color.RED,Color.BLUE),0)),
                                                         value_range=(-2, 2),click_increment=0.1,
                                                         manager=manager)
red_blue_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 330), (150, 25)), text=f"red-blue: {red_blue_slider.get_current_value()}", manager=manager)



reduc_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 390), (200, 25)),
                                                         start_value=float(config.get("reduc",0)),
                                                         value_range=(1, 100),click_increment=1,
                                                         manager=manager)
reduc_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 390), (150, 25)), text=f"reduc: {reduc_slider.get_current_value()}", manager=manager)

zone_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 430), (200, 25)),
                                                         start_value=float(config.get("zone",0)),
                                                         value_range=(1, 500),click_increment=10,
                                                         manager=manager)
zone_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 430), (150, 25)), text=f"zone: {zone_slider.get_current_value()}", manager=manager)

min_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 470), (200, 25)),
                                                         start_value=float(config.get("min",0)),
                                                         value_range=(0, 1),click_increment=0.01,
                                                         manager=manager)
min_label = pygame_gui.elements.UILabel( relative_rect=pygame.Rect((210, 470), (150, 25)), text=f"min: {min_slider.get_current_value()}", manager=manager)

running = True
clock = pygame.time.Clock()




while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    manager.update(time_delta)

    # Update the attraction values from sliders
    law_of_attraction[(Color.BLUE, Color.BLUE)]  = blue_blue_slider.get_current_value()
    law_of_attraction[(Color.BLUE, Color.GREEN)] = blue_green_slider.get_current_value()
    law_of_attraction[(Color.BLUE, Color.RED)]   = blue_red_slider.get_current_value()
    law_of_attraction[(Color.GREEN, Color.BLUE)] = green_blue_slider.get_current_value()
    law_of_attraction[(Color.GREEN, Color.GREEN)] = green_green_slider.get_current_value()
    law_of_attraction[(Color.GREEN, Color.RED)]  = green_red_slider.get_current_value()
    law_of_attraction[(Color.RED, Color.BLUE)] = red_blue_slider.get_current_value()
    law_of_attraction[(Color.RED, Color.GREEN)] = red_green_slider.get_current_value()
    law_of_attraction[(Color.RED, Color.RED)]  = red_red_slider.get_current_value()
    config["reduc"] = reduc_slider.get_current_value()
    config["zone"] = zone_slider.get_current_value()
    config["min"]  = min_slider.get_current_value()

    screen.blit(surface_transparente, (0, 0))

    particles_tick(particles)
    for particle in particles:
        pygame.draw.circle(screen, color=particle.color.value,
                           center=(particle.position.x + 300, particle.position.y),
                           radius=5)
    blue_blue_label.set_text(f"blue_blue: {round(blue_blue_slider.get_current_value(),2)}")
    blue_green_label.set_text(f"blue_green: {round(blue_green_slider.get_current_value(),2)}")
    blue_red_label.set_text(f"blue_red: {round(blue_red_slider.get_current_value(),2)}")
    green_green_label.set_text(f"green_green: {round(green_green_slider.get_current_value(),2)}")
    green_red_label.set_text(f"green_red: {round(green_red_slider.get_current_value(),2)}")
    green_blue_label.set_text(f"green_blue: {round(green_blue_slider.get_current_value(),2)}")
    red_green_label.set_text(f"red_green: {round(red_green_slider.get_current_value(),2)}")
    red_red_label.set_text(f"red_red: {round(red_red_slider.get_current_value(),2)}")
    red_blue_label.set_text(f"red_blue: {round(red_blue_slider.get_current_value(),2)}")

    zone_label.set_text(f"zone: {round(zone_slider.get_current_value(),0)}")
    min_label.set_text(f"min: {round(min_slider.get_current_value(),2)}")
    reduc_label.set_text(f"reduc: {round(reduc_slider.get_current_value(),0)}")

    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
