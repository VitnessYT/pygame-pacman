import random
import pygame
from objects.images.wall import Wall
from settings import Settings
from logic.path_searcher import path_searcher


class GhostDirectionChooser:
    def __init__(self, ghost, target_class):
        self.ghost = ghost
        self.target_class = target_class

    def logic(self, pacman):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        directions.remove((-self.ghost.shift_x, -self.ghost.shift_y))
        for x, y in directions.copy():
            pos = self.ghost.rect.move(x, y)
            for obj in Settings.field.get_nearest_objects(pos.x, pos.y, obj_type=Wall).values():
                if pos.colliderect(obj.rect):
                    directions.remove((x, y))
                    break
        if len(directions) == 1:
            self.ghost.shift_x, self.ghost.shift_y = directions[0]
        else:
            target = self.target_class.get_target_point(pacman)
            path = path_searcher(self.ghost, Settings.field.get_cell(target[0], target[1]))
            if path is None:
                print(Settings.field[target], Settings.field[Settings.field.get_cell(self.ghost.rect.x, self.ghost.rect.y)])
            self.ghost.shift_x, self.ghost.shift_y = path
