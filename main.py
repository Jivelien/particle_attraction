from __future__ import annotations

from particle_attraction_lib.board import Board
from particle_attraction_lib.tmp_game import init_game
from particle_attraction_lib.tmp_gui import PygameGui


def main():
    board = Board(300, 300)
    game = init_game(board)

    screen_size = (1200, 1200)
    gui = PygameGui(screen_size)

    while gui.draw(game):
        game.particles_tick()


if __name__ == '__main__':
    main()
