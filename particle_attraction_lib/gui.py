import dataclasses
from typing import Tuple

import pygame
import pygame_gui

from particle_attraction_lib.game import Game

@dataclasses.dataclass
class Color:
    name: str
    hex: Tuple[int,int,int]

class PygameGui:
    def __init__(self, screen_size):
        self.screen_size = screen_size

        pygame.init()
        pygame.display.set_caption("Particle attraction")

        self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((self.screen_size[0], self.screen_size[1]))
        self.interaction_controllers = {}
        self.parameters_controllers = {}

    def _draw_interaction_controller(self, i, key, value):
        if not self.interaction_controllers.get(key):
            y_position = i * 25 + 5
            slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, y_position), (200, 25)),
                                                                      start_value=float(value),
                                                                      value_range=(-1., 1.), click_increment=0.1,
                                                                      manager=self.manager)

            label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((210, y_position), (150, 25)),
                                                text=f"{self._color(key[0]).name} -> {self._color(key[1]).name}: {float(value)}",
                                                manager=self.manager)
            self.interaction_controllers[key] = (label, slider)
        else:
            ui_item = self.interaction_controllers.get(key)
            slider_value = round(ui_item[1].get_current_value(),2)
            ui_item[0].set_text(f"{self._color(key[0]).name} -> {self._color(key[1]).name}: {slider_value}")

    def _draw_parameters_controller(self, i, key, value, min, max):
        if not self.parameters_controllers.get(key):
            y_position = i * 25 + 5
            slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, y_position), (200, 25)),
                                                                      start_value=value,
                                                                      value_range=(min, max), click_increment=1,
                                                                      manager=self.manager)

            label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((210, y_position), (200, 25)),
                                                          text=f"{key}: {value}",
                                                          manager=self.manager )
            self.parameters_controllers[key] = (label, slider)
        else:
            self.parameters_controllers.get(key)[0].set_text(f"{key}: {value}")

    def _color(self, i:int):
        match i:
            case 0:
                return Color("Red",(255,0,0))
            case 1:
                return Color("Green",(0,255,0))
            case 2:
                return Color("Blue",(0,0,255))
            case 3:
                return Color("Cyan",(0,255,255))
            case 4:
                return Color("Magenta",(255,0,255))
            case 5:
                return Color("Yellow",(255,255,0))
            case _:
                return Color("None",(0,0,0))

    def draw(self, game: Game):
        self.screen.fill((0, 0, 0))
        time_delta = self.clock.tick(60) / 1000.0

        idx=0
        for idx, (key, value) in enumerate(game.attraction_force.attraction_law.laws.items()): #TODO: IMPROVE
            self._draw_interaction_controller(idx, key, value)

        self._draw_parameters_controller(idx+1, "Size of attraction", game.attraction_force.attraction_parameters.size_of_attraction, 1, 200)
        self._draw_parameters_controller(idx+2, "Absolute repulsion", game.attraction_force.attraction_parameters.absolute_repulsion, 0, 50)
        self._draw_parameters_controller(idx+3, "Force reduction factor", game.attraction_force.attraction_parameters.force_factor, 1, 200)

        for key, ui_item in self.interaction_controllers.items(): #TODO: control should be external
            game.attraction_force.attraction_law.add(key[0], key[1],self.interaction_controllers.get(key)[1].get_current_value() )
        game.attraction_force.attraction_parameters.size_of_attraction = self.parameters_controllers["Size of attraction"][1].get_current_value()
        game.attraction_force.attraction_parameters.absolute_repulsion = self.parameters_controllers["Absolute repulsion"][1].get_current_value()
        game.attraction_force.attraction_parameters.force_factor = self.parameters_controllers["Force reduction factor"][1].get_current_value()

        for particle in game.all_particles():
            color = self._color(particle.species).hex
            pygame.draw.circle(self.screen, color,
                               (int((particle.position.x / game.board.width) * self.screen_size[0]),
                                int((particle.position.y / game.board.height) * self.screen_size[1])), 5)

        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.screen_size = (event.w, event.h)
            self.manager.process_events(event)

        return True
