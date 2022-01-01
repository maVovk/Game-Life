import random
import pygame
import Cell


class Field:
    def __init__(self, screen: pygame.display, screen_size: tuple, map_size: int = 300, seed: int = 1234,
                 possibility: float = 0.3):
        """
        :param screen: pygame объект для отрисовки
        :param screen_size: размер экрана в пискелях(ширина, высота)
        :param map_size: размер игрового поля
        :param seed: зерно для рандомайзера
        :param possibility: вероятность появления живого организма в отдельно взятой клетке(до тысячных)
        """

        self.map_size = map_size  # размер поля
        self.cell_size = screen_size[0] // self.map_size  # размер одной клетки
        self.map = []
        self.screen = screen

        # инициализация рандомайзера, чтобы была возможность управлять генерацией
        random.seed(seed, version=2)

        self.create_field(possibility)

    def generate_random_status(self, possibility: float) -> str:
        """
         :param possibility: вероятность появления живого организма в отдельно взятой клетке(до сотых)

         :return: 'alive' если в данной клетке должна быть жизнь, иначе 'empty'
        """
        result = random.randint(1, 1000)

        if result <= int(possibility * 1000):
            return 'alive'
        return 'empty'

    def create_field(self, possibility: float) -> None:
        """
        :param possibility: вероятность появления живого организма в отдельно взятой клетке(до сотых)

        Генерирует поле, в соответствии с заданной вероятностью
        """
        for i in range(self.map_size):
            self.map.append([])

            for j in range(self.map_size):
                if i != 0 and j != 0:
                    self.map[i].append(Cell.Cell(self.generate_random_status(possibility), (i, j)))
                else:
                    self.map[i].append(Cell.Cell('empty', (i, j)))

    def check_cell(self, x: int, y: int) -> None:
        """
        :param x: позиция клетки по оси X(первое измерение массива)
        :param y: позиция клетки по оси Y(второе измерение массива)

        Устанавливает новый статус клетки, в соответствии с правилами игры
        """

        summ = self.map[x - 1][y - 1].get_status() + self.map[x - 1][y].get_status() + \
            self.map[x - 1][y + 1].get_status() + self.map[x][y - 1].get_status() + \
            self.map[x][y + 1].get_status() + self.map[x + 1][y - 1].get_status() + \
            self.map[x + 1][y].get_status() + self.map[x + 1][y + 1].get_status()

        if 2 <= summ <= 3 and self.map[x][y].get_status() == 1:
            self.map[x][y].set_status('alive')
        elif summ == 3 and self.map[x][y].get_status() == 0:
            self.map[x][y].set_status('alive')
        elif summ < 2 or summ >= 4:
            self.map[x][y].set_status('empty')

    def draw(self) -> None:
        """
        Отрисовывает поле и применяет изменения, произошедшие в данном поколении
        """
        for i in range(1, self.map_size - 1):
            for j in range(1, self.map_size - 1):
                self.check_cell(i, j)
                self.map[i][j].draw(self.screen, self.cell_size)

        for i in range(1, self.map_size - 1):
            for j in range(1, self.map_size - 1):
                self.map[i][j].apply()
