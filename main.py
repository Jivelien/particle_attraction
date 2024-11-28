from __future__ import annotations

import time

from particle_attraction_lib.attraction_force import AttractionParameters
from particle_attraction_lib.board import Board
from main_utils import init_game
from particle_attraction_lib.gui import PygameGui


def run_with_monitoring(game, gui):
    times = []
    i = 0
    running = True
    while running:
        running = gui.draw(game)

        time_before = time.time() * 1000
        game.tick()
        time_after = time.time() * 1000

        delta_time = time_after - time_before
        times.append(delta_time)
        if i % 10 == 0:
            print(
                f"iteration : {i} - time : {round(delta_time, 3)} ms -  maximum frequency : {round(1000 / delta_time, 3)} Hz")
        i += 1
    print("")
    mean_time = sum(times) / len(times)
    print(f"Average time : {round(mean_time, 3)} ms - maximum frequency : {1000 / mean_time} Hz")


def run(game, gui):
    running = True
    while running:
        running = gui.draw(game)
        game.tick()


def main():
    board = Board(600, 450)

    attraction_parameters = AttractionParameters(
        size_of_attraction=70,
        absolute_repulsion=5,
        force_factor=200)

    game = init_game(board=board,
                     attraction_parameters=attraction_parameters,
                     number_of_particles=250,
                     number_of_species=6)

    screen_size = (1500, 1500)
    gui = PygameGui(screen_size)

    # run_with_monitoring(game, gui)
    run(game, gui)


if __name__ == '__main__':
    main()
