import pygame

from objects.images.base import Image
from objects.images.animated_base import AnimatedImage
from settings import Settings


class Seed(Image):
    MARGIN = 8
    seed_weight = 10

    def __init__(self, x, y):
        if not hasattr(self, "directory"):
            self.directory = "seed.png"

        super().__init__(
            x, y,
            resize_params={
                'width': Settings.CELL_SIZE - 2 * self.MARGIN,
                'height': Settings.CELL_SIZE - 2 * self.MARGIN
            }
        )

    def draw(self, screen):
        screen.blit(self.image, [self.rect.x + self.MARGIN, self.rect.y + self.MARGIN])


class Energizer(AnimatedImage):
    MARGIN = 4
    seed_weight = 50

    def __init__(self, x, y):
        self.directory = "energizer/"
        super().__init__(x, y, resize_params={
            'width': Settings.CELL_SIZE - 2 * self.MARGIN,
            'height': Settings.CELL_SIZE - 2 * self.MARGIN
        }, automatic_load=True, update_value=100)
        self.radius = self.rect.width // 2
        self.initial = {
            'x': x,
            'y': y,
        }
        self.rect.x += self.MARGIN
        self.rect.y += self.MARGIN
        self.shift_y = self.shift_x = 1

    def get_direction(self):
        return "energizer"

    def activate(self):
        self.rect.x = self.initial['x']
        self.rect.y = self.initial['y']


Settings.TYPES[2] = Seed
Settings.TYPES[3] = Energizer