from logic.ghost_direction_chooser import GhostDirectionChooser
from logic.teleport import Teleport
from objects.images.animated_base import AnimatedImage
from objects.images.base_image_path import BaseImagePath
from settings import Settings


class GhostBase(AnimatedImage, BaseImagePath):
    def __init__(self, x, y, target_class):  # todo: add initial and activate() to GhostBase class

        self.extra_path = "ghosts/"
        self.multiple_directories = True
        self.additional_directories = ["eaten"]
        super().__init__(x, y, automatic_load=True,
                         resize_params={'width': Settings.CELL_SIZE, 'height': Settings.CELL_SIZE})
        self.direction_chooser = GhostDirectionChooser(self, target_class)
        self.shift_x = 0
        self.shift_y = -1
        self.teleport = True
        self.tp = Teleport(self.rect)
        self.eat = False

    def move(self):
        if not Settings.wait_pacman:
            self.rect.y += self.shift_y
            self.rect.x += self.shift_x

            self.rect.x = self.tp.check_teleport()
            self.tp.teleport_access()

    def logic(self):
        self.move()

    def get_direction(self):
        if Settings.wait_pacman:
            return "down"
        if Settings.fear_mode:
            return "eaten"
        return super().get_direction()
