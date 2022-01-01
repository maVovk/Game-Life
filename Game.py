import pygame
from Field import Field


class Game:
    def __init__(self, map_size: int = 300, seed: int = 1234, possibility: float = 0.3):
        """
        :param map_size: размер игрового поля
        :param seed: зерно для рандомайзера
        :param possibility: вероятность появления живого организма в отдельно взятой клетке(до тысячных)
        """
        pygame.init()
        self.screen_size = (1200, 1200)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.field = Field(self.screen, self.screen_size, map_size, seed, possibility)
        self.gameover = False

    def start(self, delay=500) -> None:
        """
            :param delay: задержка в мс между поколениями

            Запускается бесконечный цикл, который каждый кадр отрисовывает поле
        """
        while not self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True

            self.screen.fill((0, 0, 0))

            self.field.draw()

            pygame.time.wait(delay)
            pygame.display.flip()

        return
