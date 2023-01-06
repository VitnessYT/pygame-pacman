import random

import pygame

from logic.sound import Sound
from objects.buttons import Button
from objects.texts import Text
from objects.input import InputBox
from scenes.base import BaseScene
from settings import Settings
from sys import exit
from third_party.particles import Particle, Circle


class MenuScene(BaseScene):
    PROCESS_ESCAPE = False

    def set_up_objects(self):
        def on_nick_edit(input_box):
            Settings.nickname = input_box.text

        def new_game():
            if not Settings.nickname:
                return
            Settings.set_scene(Settings.SCENES.GAME)

        self.select_sound = Sound("data/sounds/select_sound.wav")
        self.objects.append(
            Text(
                x=Settings.WINDOW_WIDTH // 2 - 105, y=Settings.WINDOW_HEIGHT // 2 - 80,
                text='Pacman', size=58, color=pygame.Color('yellow')
            )
        )
        self.button_new_game = Button((Settings.WINDOW_WIDTH - 200) / 2, Settings.WINDOW_HEIGHT / 2, 200, 50,
                                      "NEW GAME",
                                      new_game, hover_sound=self.select_sound,
                                      font=pygame.font.Font(None, 30))
        self.button_settings = Button((Settings.WINDOW_WIDTH - 200) / 2, (Settings.WINDOW_HEIGHT / 2) + 50, 200, 50,
                                      "SETTINGS",
                                      lambda: Settings.set_scene(Settings.SCENES.SETTINGS),
                                      hover_sound=self.select_sound,
                                      font=pygame.font.Font(None, 30))
        self.button_highscore = Button((Settings.WINDOW_WIDTH - 200) / 2, (Settings.WINDOW_HEIGHT / 2) + 100, 200, 50,
                                       "HIGHSCORE",
                                       lambda: Settings.set_scene(Settings.SCENES.HIGHSCORE),
                                       hover_sound=self.select_sound,
                                       font=pygame.font.Font(None, 30))
        self.button_exit = Button((Settings.WINDOW_WIDTH - 200) / 2, (Settings.WINDOW_HEIGHT / 2) + 150, 200, 50,
                                  "EXIT", exit, hover_sound=self.select_sound, font=pygame.font.Font(None, 30))
        self.name_input = InputBox(0, 0, text="Player", hint="Nickname", on_edit=on_nick_edit)
        self.name_input.move_to((Settings.WINDOW_WIDTH - self.name_input.rect.width) // 2,
                                100)
        self.objects.append(self.name_input)
        self.objects.append(self.button_new_game)
        self.objects.append(self.button_settings)
        self.objects.append(self.button_highscore)
        self.objects.append(self.button_exit)

    def additional_activate(self):
        Settings.life_count.life = 3

    def additional_process_event(self, event):
        self.mouse_particle_event(event)
