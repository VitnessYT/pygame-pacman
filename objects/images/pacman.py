import pygame
from settings import Settings
from logic.teleport import Teleport
from objects.images.wall import Wall
from objects.images.animated_base import AnimatedImage


class Pacman(AnimatedImage):

    def __init__(self, x, y):

        self.directory = "pacman"
        super().__init__(x, y, resize_params={'width': Settings.CELL_SIZE, 'height': Settings.CELL_SIZE}, automatic_load=True)

        self.initial = {
            "x": x,
            "y": y
        }
        self.activate()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            self.next_shift_x = {pygame.K_a: -1, pygame.K_d: 1}.get(event.key, 0)
            self.next_shift_y = {pygame.K_w: -1, pygame.K_s: 1}.get(event.key, 0)

    def activate(self):
        self.shift_x = self.shift_y = self.next_shift_x = self.next_shift_y = 0
        self.rect.x = self.initial["x"]
        self.rect.y = self.initial["y"]
        self.last_direction = None

    def logic(self):
        self.rect.x += self.shift_x
        self.rect.y += self.shift_y
        for obj in Settings.field.get_nearest_objects(self.rect.x, self.rect.y, obj_type=Wall).values():
            if self.rect.colliderect(obj.rect):
                self.rect.x -= self.shift_x
                self.rect.y -= self.shift_y
                self.last_direction = super().get_direction()
                self.shift_x = self.shift_y = 0


        if self.next_shift_x or self.next_shift_y:
            try_rotate = self.rect.move(self.next_shift_x * 5, self.next_shift_y * 5)
            for obj in Settings.field.get_nearest_objects(try_rotate.x, try_rotate.y, obj_type=Wall).values():
                if try_rotate.colliderect(obj.rect):
                    break
            else:
                self.shift_x = self.next_shift_x
                self.shift_y = self.next_shift_y
                self.last_direction = None
                Settings.wait_pacman = False
                self.next_shift_x = self.next_shift_y = 0

        if self.rect.collidepoint(Settings.field.get_coords(0, 10)):
            self.rect.x = Settings.LEFT_SHIFT + Settings.CELL_SIZE * (Settings.field.width() - 1.5)
        if self.rect.collidepoint(Settings.field.get_coords(Settings.field.width(), 10)):
            self.rect.x = Settings.LEFT_SHIFT + Settings.CELL_SIZE // 2

    def get_direction(self):
        if self.last_direction:
            return self.last_direction
        return super().get_direction()