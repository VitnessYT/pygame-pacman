from queue import Queue


class Field:
    def __init__(self, path, settings):
        self.settings = settings
        self.path = path  # "levels/field.txt"

    def reload(self):
        """Перезагружает поле"""
        with open(self.path) as grid:
            lines = grid.readlines()
            field = [list(map(int, line.split(", "))) for line in lines]  # remove with table prints
        self.field = [list(map(int, line.split(", "))) for line in lines]
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = self.settings.TYPES[self.field[i][j]](*self.get_coords(j, i))

        colors = ["[0;30m", "[0;34m", "[0;33m", "[0;31m"]
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                print("\u001b" + colors[field[i][j]] + self.field[i][j].__class__.__name__[0], end=" ")
            print()
        print("\u001b[0m")

    def get_nearest_objects(self, x: int, y: int, distance: int = 1, obj_type=None, return_this=True) -> dict:
        result = {}
        if return_this:
            i, j = self.get_cell(x, y)
            if obj_type is None or isinstance(self.field[j][i], obj_type):
                result[(i, j)] = self.field[j][i]

        if distance == 0:
            return result
        q = Queue()
        q.put((self.get_cell(x, y), 0))
        while not q.empty():
            (i, j), dist = q.get()
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= x < self.width() and 0 <= y < self.height():
                    if obj_type is None:
                        result[(x, y)] = self.field[y][x]
                    elif isinstance(self.field[y][x], obj_type):
                        result[(x, y)] = self.field[y][x]
                    if dist < distance:
                        q.put(((x, y), dist + 1))
        return result

    def __getitem__(self, pos: tuple[int, int]):
        """
        Возвращает клетку, находящуюся на позиции pos
        --- Индексы используются в порядке x, y
        """
        return self.field[pos[1]][pos[0]]

    def __setitem__(self, pos: tuple[int, int], value) -> None:
        """
        Изменяет значение клетки, находящейся на позиции pos
        --- Индексы используются в порядке x, y
        """
        self.field[pos[1]][pos[0]] = value

    def get(self, pos: tuple[int, int]):
        """
        Возвращает клетку, находящуюся на позиции pos
        --- Индексы используются в порядке y, x
        """
        return self.field[pos[0]][pos[1]]

    def set(self, pos: tuple[int, int], value) -> None:
        """
        Изменяет значение клетки, находящейся на позиции pos
        --- Индексы используются в порядке y, x
        """
        self.field[pos[0]][pos[1]] = value

    def get_coords(self, i: int, j: int) -> tuple[int, int]:
        """
        Преобразовывает индексы в координаты
        --- Индексы используются в порядке x, y
        """
        return self.settings.LEFT_SHIFT + self.settings.CELL_SIZE * i, self.settings.TOP_SHIFT + self.settings.CELL_SIZE * j

    def get_cell(self, x: int, y: int) -> tuple[int, int]:
        """
        Преобразовывает координаты в индексы
         --- Индексы используются в порядке x, y
        """
        return (x - self.settings.LEFT_SHIFT) // self.settings.CELL_SIZE, (
                    y - self.settings.TOP_SHIFT) // self.settings.CELL_SIZE

    def set_empty(self, i: int, j: int):
        """Делает клетку пустой (Класс Cell)"""
        x, y = self.get_coords(i, j)
        self.field[j][i] = self.settings.TYPES[0](x, y)

    def width(self):
        """Ширина поля (х)"""
        return len(self.field[0])

    def height(self):
        """Высота поля (y)"""
        return len(self.field)
