import pygame
from Field import *


CELL_COLOR = (240, 240, 240)


class Cell:
    def __init__(self, status: str, pos: tuple):
        self.position = pos
        self.current_status = status
        self.future_status = self.current_status

    def get_status(self) -> int:
        if self.current_status == 'alive':
            return 1
        return 0

    def draw(self, screen, cell_size):
        if self.current_status == 'empty':
            return

        pygame.draw.rect(screen, CELL_COLOR, (self.position[0] * cell_size, self.position[1] * cell_size,
                                              cell_size, cell_size))

    def set_status(self, new_status):
        self.future_status = new_status

    def apply(self):
        if self.future_status is not None:
            self.current_status = self.future_status
            self.future_status = None
        else:
            raise ValueError
