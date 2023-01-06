from typing import Dict, Optional

import pygame

from objects.base import BaseObject
from logic.resources import *
from objects.images.base_image_path import BaseImagePath


class Image(BaseObject, BaseImagePath):
    visible: bool
    eaten: bool

    def __init__(self, x: int, y: int, resize_params: Optional[Dict[str, int]] = None):
        BaseImagePath.__init__(self)
        self.image = ResourceLoader.load_image(self.path).resource
        if resize_params is not None:
            self.__check_resize_params(resize_params)
            self.__resize(resize_params['width'], resize_params['height'])
        r = self.image.get_rect()
        self.visible = True
        self.eaten = False
        BaseObject.__init__(self, x, y, r.width, r.height)

    def __check_resize_params(self, resize_params: Optional[Dict[str, int]]) -> None:
        if not isinstance(resize_params, dict):
            raise RuntimeError('resize_params must be dict')
        if 'width' not in resize_params:
            raise KeyError('resize_params has no key "width"')
        if 'height' not in resize_params:
            raise KeyError('resize_params has no key "height"')

    def __resize(self, width: int, height: int):
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def set_eaten(self, is_eaten):
        self.eaten = is_eaten

    def can_be_eaten(self):
        return self.visible and not self.eaten
