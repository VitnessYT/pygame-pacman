import pygame

from objects.images.base import Image
from settings import Settings
from logic.resources import *


class LifeDrawer(Image):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.directory = "life.png"
        super().__init__(x, y)

    def draw(self, screen):
        number_of_lives = int(Settings.life_count.life)
        for i in range(number_of_lives):
            screen.blit(self.image, (self.rect.x + (self.rect.width + 10) * i, self.rect.y))
