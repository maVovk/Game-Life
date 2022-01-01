from Field import *


CELL_COLOR = (240, 240, 240)  # цвет живой клетки


class Cell:
    def __init__(self, status: str, pos: tuple):
        """
        :param status: начальное состояние клетки(живая или нет)
        :param pos: координата клетки по осям (X;Y)
        """
        self.position = pos
        self.current_status = status
        self.future_status = self.current_status

    def get_status(self) -> int:
        """
        :return: 1 - если в клетки есть организм, иначе - 0
        """
        if self.current_status == 'alive':
            return 1
        return 0

    def set_status(self, new_status: str):
        """
        :param new_status: новое состояние клетки

        Устанавливает будущее состояние у клетки
        """
        self.future_status = new_status

    def draw(self, screen: pygame.display, cell_size: int):
        """
        :param screen: объект дисплея, на котором идёт отрисовка
        :param cell_size: размер клетки

        Отрисовывает клетку на экране
        """
        if self.current_status == 'empty':
            return

        pygame.draw.rect(screen, CELL_COLOR, (self.position[0] * cell_size, self.position[1] * cell_size,
                                              cell_size, cell_size))

    def apply(self):
        """
        Применение изменений клетки между поколениями
        """
        self.current_status = self.future_status
        self.future_status = 'empty'
