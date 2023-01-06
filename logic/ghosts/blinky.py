from objects.images.pacman import Pacman
from .random import get_random_target
from settings import Settings

class BlinkyTargetPoint:
    @staticmethod
    def get_target_point(pacman: Pacman):
        if Settings.fear_mode:
            return get_random_target()
        return pacman.rect.x, pacman.rect.y