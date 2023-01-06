import datetime

import pygame

from logic.sound import Sound
from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings

class GameOverScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.nickname = None
        self.set_up_objects()
        self.wait_seconds = 0
        self.open_scene_datetime = datetime.datetime.now()
        self.gameover_sound = Sound("data/sounds/gameover_sound.wav")

    def set_up_objects(self):
        rect = Text(1, 1, 'Game over', 78, pygame.Color('red')).rect
        self.objects.append(
            Text(
                (Settings.WINDOW_WIDTH - rect.width) // 2,
                (Settings.WINDOW_HEIGHT - rect.height) // 2,
                'Game over', 78, pygame.Color('red'))
        )

    def additional_activate(self):
        self.open_scene_datetime = datetime.datetime.now()
        self.gameover_sound.play()

    def process_additional_logic(self):
        now = datetime.datetime.now()
        wait_seconds = (now - self.open_scene_datetime).seconds
        if wait_seconds == Settings.MAX_WAIT_SECONDS:
            Settings.set_scene(Settings.SCENES.MENU)
