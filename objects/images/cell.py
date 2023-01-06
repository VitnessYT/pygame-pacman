from objects.images.base import Image
from settings import Settings


class Cell(Image):

    def __init__(self, x, y):
        self.directory = "cell_empty.png"
        super().__init__(x, y)


Settings.TYPES[0] = Cell
