import pygame
from Field import Field


class Game:
    def __init__(self):
        pygame.init()
        self.screen_size = (1200, 1200)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.field = Field(self.screen, self.screen_size)
        self.gameover = False

    def start(self) -> None:
        while not self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True

            self.screen.fill((0, 0, 0))

            self.field.draw()

            pygame.time.wait(100)
            pygame.display.flip()

        return
