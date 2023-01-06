from objects.images.base import Image
from settings import Settings


class Wall(Image):
    # filename = 'images/cell_wall.png'

    def __init__(self, x, y):
        self.directory = "cell_wall.png"
        super().__init__(
            x, y,
            resize_params={
                'width': Settings.CELL_SIZE,
                'height': Settings.CELL_SIZE
            }
        )

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Settings.TYPES[1] = Wall
