import time

from objects.base import BaseObject
from objects.images.seeds import Energizer
from objects.images.seeds import Seed
from objects.images.wall import Wall
from objects.images.cell import Cell
from logic.sound import Sound
from settings import Settings
from objects.score import ScoreDrawer


class Drawer(BaseObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.eat_sound = Sound("data/sounds/eat_point_sound.wav")
        self.eat_energizer_sound = Sound("data/sounds/eat_energizer_sound.wav")
        self.fear_mode_begin = 0
        self.eaten_ghosts = 0
        self.objects_eaten = 0

    def draw(self, screen):
        if Settings.fear_mode and time.time() - self.fear_mode_begin > Settings.FEAR_MODE_SECONDS:
            Settings.fear_mode = False
        for i in range(Settings.field.width()):
            for j in range(Settings.field.height()):
                Settings.field[i, j].draw(screen)

    def collide(self, pacman, score):
        for (i, j), obj in Settings.field.get_nearest_objects(pacman.rect.x, pacman.rect.y).items():
            if pacman.rect.collidepoint(obj.rect.center):
                if isinstance(obj, Energizer):
                    score.add_score(50)
                    self.objects_eaten += 1
                    self.eat_energizer_sound.play()
                    Settings.field.set_empty(i, j)
                    Settings.fear_mode = True
                    self.eaten_ghosts = 0
                    self.fear_mode_begin = time.time()
                elif isinstance(obj, Seed):
                    self.objects_eaten += 1
                    score.add_score(10)
                    self.eat_sound.play()
                    Settings.field.set_empty(i, j)
                if self.objects_eaten >= 144:
                    Settings.set_scene(Settings.SCENES.GAMEEND)