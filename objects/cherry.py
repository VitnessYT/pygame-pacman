import pygame

from objects.images.base import Image


class Cherry(Image):

    def __init__(self, x, y):
        self.directory = "cherry.png"
        super().__init__(x, y)
        self.showing = False

    def draw(self, screen):
        if self.showing:
            screen.blit(self.image, self.rect)

    def show(self):
        self.showing = True

    def hide(self):
        self.showing = False
