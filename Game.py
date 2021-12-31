import pygame
from Field import Field


class Game:
    def __init__(self, map_size=300, seed=1234, possibility=0.3):
        pygame.init()
        self.screen_size = (1200, 1200)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.field = Field(self.screen, self.screen_size, map_size, seed, possibility)
        self.gameover = False

    def start(self, delay=500) -> None:
        while not self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True

            self.screen.fill((0, 0, 0))

            self.field.draw()

            pygame.time.wait(delay)
            pygame.display.flip()

        return
