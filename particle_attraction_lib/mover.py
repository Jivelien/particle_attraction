from abc import ABC, abstractmethod

from particle_attraction_lib.board import Board
from particle_attraction_lib.particle import Particle, Position

class MoverInterface(ABC):
    @abstractmethod
    def apply_movement(self,particle: Particle) -> None:
        raise NotImplementedError

class Mover(MoverInterface):
    def apply_movement(self, particle: Particle) -> None:
        actual_position = particle.position
        velocity = particle.velocity
        new_position = Position(x = actual_position.x + velocity.dx,
                                y = actual_position.y + velocity.dy)
        particle.position = new_position


class TorusMover(MoverInterface):
    def __init__(self, board: Board):
        self.board = board

    def apply_movement(self,particle: Particle) -> None:
        actual_position = particle.position
        velocity = particle.velocity
        new_position = Position(x = (actual_position.x + velocity.dx) % self.board.width,
                                y = (actual_position.y + velocity.dy) % self.board.height)
        particle.position = new_position
