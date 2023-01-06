from objects.images.cell import Cell
from objects.images.pacman import Pacman
from objects.images.seeds import Seed, Energizer
from settings import Settings
from .random import get_random_target


class PinkyTargetPoint:
    """
    Вернуть после теста.
    @staticmethod
        def get_target_point(pacman: Pacman):
        return Pathfinding.apply_rotation(
            pacman.x,
            pacman.y,
            4,
            Pathfinding.get_rotation(pacman.direction)
        )
    """

    @staticmethod
    def get_target_point(pacman: Pacman):
        if Settings.fear_mode:
            return get_random_target()
        max_x, max_y = Settings.field.get_coords(Settings.field.width() - 1, Settings.field.height() - 1)
        x = max(0, min(max_x, pacman.rect.x + pacman.shift_x * 4 * Settings.CELL_SIZE))
        y = max(0, min(max_y, pacman.rect.y + pacman.shift_y * 4 * Settings.CELL_SIZE))
        obj = list(Settings.field.get_nearest_objects(x, y,
                                                      distance=1,
                                                      obj_type=(Cell, Seed, Energizer)).values())[0]

        return obj.rect.x, obj.rect.y
