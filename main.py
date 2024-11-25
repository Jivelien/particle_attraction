from __future__ import annotations

from particle_attraction_lib.attraction_force import AttractionParameters
from particle_attraction_lib.board import Board
from particle_attraction_lib.tmp_game import init_game
from particle_attraction_lib.tmp_gui import PygameGui


def main():
    board = Board(500, 500)

    attraction_parameters = AttractionParameters(
        size_of_attraction=90,
        absolute_repulsion=10,
        force_factor=150)

    game = init_game(board=board,
                     attraction_parameters=attraction_parameters,
                     number_of_particles=200)

    screen_size = (1200, 1200)
    gui = PygameGui(screen_size)

    running = True
    while running:
        running = gui.draw(game)
        game.tick()


if __name__ == '__main__':
    main()
