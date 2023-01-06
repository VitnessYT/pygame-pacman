import os

import pygame.image

from logic.resources import *
from objects.images.base_image_path import BaseImagePath
from .base import Image


class AnimatedImage(Image, BaseImagePath):
    def __init__(
            self,
            x,
            y,
            *,
            automatic_load: bool = False,
            resize_params: dict[str, int] = None,
            update_value: int = 10,

    ):
        """
        Args:
            image_paths: Список путей ко всем картинкам
            automatic_load: Если True, то картинки загружаются из указанной директории в соответствии с их именами.
            resize_params: Словарь, содержащий ширину и высоту, до которой нужно уменьшить картинку.
            update_value: Раз в сколько кадров меняется состояние.
        """

        BaseImagePath.__init__(self)

        if automatic_load is True:
            self.images = {}
            for image_directory in self.paths:
                for file in os.listdir(image_directory):
                    if file.endswith(".png"):
                        data = file[:-4].split("_")
                        self.images.setdefault(data[1], []).append(
                            ResourceLoader.load_image(os.path.join(image_directory, file)).resource)
        else:
            self.images = self.path
            for key in self.images:
                self.images[key] = tuple(ResourceLoader.load_image(x).resource for x in self.images[key])
        if resize_params is not None:
            for key in self.images:
                self.images[key] = tuple(
                    pygame.transform.scale(x, (resize_params['width'], resize_params['height'])) for x in
                    self.images[key])
        self.rect = list(self.images.values())[0][0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.update_value = update_value
        self.shift_x = 0
        self.shift_y = 0
        self.state = 0

    def get_direction(self):
        if self.shift_x:
            return ["left", "right"][self.shift_x > 0]
        return ["up", "down"][self.shift_y > 0]

    def draw(self, screen: pygame.Surface):
        if self.shift_x or self.shift_y:
            self.state = (self.state + 1) % (self.update_value * len(self.images[self.get_direction()]))
        screen.blit(self.images[self.get_direction()][self.state // self.update_value], self.rect)
