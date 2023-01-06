from objects.images.pacman import Pacman
from objects.images.cell import Cell
from settings import Settings
from .random import get_random_target


class InkyTargetPoint:
    @staticmethod
    def get_target_point(pacman: Pacman):
        return get_random_target()