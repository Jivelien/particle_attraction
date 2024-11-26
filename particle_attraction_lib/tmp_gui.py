import pygame

from particle_attraction_lib.game import Game


class PygameGui:
    def __init__(self, screen_size):
        pygame.init()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()

    def draw(self, game: Game):
        self.screen.fill((0, 0, 0))

        for particle in game.all_particles():
            match particle.species:
                case 0:
                    color = (255, 0, 0)
                case 1:
                    color = (0, 255, 0)
                case 2:
                    color = (0, 0, 255)
                case _:
                    color = (255, 255, 255)

            pygame.draw.circle(self.screen, color,
                               (int((particle.position.x / game.board.width) * self.screen_size[0]),
                                int((particle.position.y / game.board.height) * self.screen_size[1])), 5)

        pygame.display.flip()
        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        return True
