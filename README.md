# Game-Life
## Задание на вступительном экзамене на курс ML в Tinkoff Generation 



### Подготовка к запуску

В программе используется графическая библиотека pygame

```
pip install pygame
```

### Запуск

```python
game = Game(map_size=400, seed=115, possibility=0.25)
```

**map_size** - размер игрового поля

**seed** - зерно для random

**possibility** - вероятность появления живого организма в отдельно взятой клетке, имеет значение только до тысячных

```python
game.start(delay=300)
```

**delay** - задержка между кадрами в мс



## Класс Game

### Конструктор

**screen_size** - размер экрана

**screen** - объект экрана из библиотеки pygame

**field** - объект класса Field

**gameover** - переменная, прерывающая основной цикл игры



### start

**delay** - задержка в мс между кадрами

Функция запускает основной цикл игры,  в котором и происходит вся отрисовка игры



## Класс Field

### Конструктор

**screen** - объект экрана из библиотеки pygame

**map_size** - сторона квадрата поля в клетках

**map** - массив поля, в котором хранятся клетки

**cell_size** - сторона одной клетки в пикселях

**seed** - зерно для инициализации random

**possibility** - вероятность появления организма в клетке



### create_field

**possibility** - вероятность появления организма в клетке

Заполняет поле организмами случайным образом с заданной вероятностью



### check_cell

**x,y** - координата клетки

Функция, которая определяет, что произойдет с клеткой в следующем поколении



### draw

Отрисовывает поле и применяет изменения на поле



## Класс Cell

**CELL_COLOR** - цвет живой клетки

### Конструктор

**position** - позиция клетки

**current_status** - текущее состояние клетки('alive' - если клетка живая, 'empty' - если нет)

**future_status** - будущее состояние клетки



### get_status

Возвращает 1 - если в клетки есть организм, иначе - 0



### set_status

Устанавливает состояние клетки в следующем поколении



### draw

Отрисовывает клетку на поле



### apply

Меняет состояние клетки при переходе между поколениями
