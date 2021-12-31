import random
import pygame
import Cell


class Field:
    def __init__(self, screen: pygame.display, screen_size: tuple, seed=1234, possibility=0.3):
        self.map_size = 300
        self.cell_size = screen_size[0] // self.map_size
        self.map = []
        self.screen = screen

        random.seed(seed, version=2)

        self.create_field(possibility)

    def generate_random_status(self, possibility: float) -> str:
        result = random.randint(1, 100)

        if result <= int(possibility * 100):
            return 'alive'
        return 'empty'

    def create_field(self, possibility: float) -> None:
        for i in range(self.map_size):
            self.map.append([])

            for j in range(self.map_size):
                if i != 0 and j != 0:
                    self.map[i].append(Cell.Cell( self.generate_random_status(possibility), (i, j)))
                else:
                    self.map[i].append(Cell.Cell('empty', (i, j)))

    def check_cell(self, x: int, y: int) -> None:
        summ = self.map[x-1][y-1].get_status() + self.map[x-1][y].get_status() + self.map[x-1][y+1].get_status() +\
                self.map[x][y - 1].get_status() + self.map[x][y+1].get_status() +\
                self.map[x+1][y-1].get_status() + self.map[x+1][y].get_status() + self.map[x+1][y+1].get_status()

        if 2 <= summ <= 3 and self.map[x][y].get_status():
            self.map[x][y].set_status('alive')
        if summ == 3 and not self.map[x][y].get_status():
            self.map[x][y].set_status('alive')
        if summ < 2 or summ > 4:
            self.map[x][y].set_status('dead')

    def draw(self) -> None:
        for i in range(1, self.map_size-1):
            for j in range(1, self.map_size-1):
                self.check_cell(i, j)
                self.map[i][j].draw(self.screen, self.cell_size)
