import pygame
from settings import Settings


class BaseObject:
    def __init__(self, x, y, width=Settings.CELL_SIZE, height=Settings.CELL_SIZE):
        self.rect = pygame.Rect(x, y, width, height)

    def activate(self):
        pass

    def event(self, event):
        pass

    def logic(self):
        pass

    def draw(self, screen):
        pass