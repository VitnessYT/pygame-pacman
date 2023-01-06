import pygame
import time

from scenes.base import BaseScene
from scenes.game import GameScene
from scenes.game_over import GameOverScene
from scenes.menu import MenuScene
from scenes.pause import PauseScene
from scenes.settings import SettingsScene
from scenes.highscore import HighscoreScene
from scenes.game_end import GameEndScene
from logic.resources import *
from settings import Settings
from objects.highscore import HighscoreTableDrawer
from objects.input import InputBox
from third_party.button.button import Button


class Application:
    def __init__(self, screen):
        self.screen = screen
        self.virtual_screen = pygame.Surface(screen.get_size())
        self.game_over = False

        Button.application = self
        HighscoreTableDrawer.application = self
        BaseScene.application = self
        InputBox.application = self

        ResourceLoader.setup(ResourceLoader.generate_raw_resource_dict("."))
        ResourceLoader.load()
        self.scenes = [
            MenuScene(),
            GameScene(),
            PauseScene(),
            SettingsScene(),
            HighscoreScene(),
            GameOverScene(),
            GameEndScene()
        ]
        print(ResourceLoader.loaded)

        time.sleep(0.5)

    def scene_activate(self):
        Settings.scene_changed = False
        self.scenes[Settings.scene_index].activate()

    def scene_event(self):
        for event in pygame.event.get():
            self.process_application_exit(event)
            self.scenes[Settings.scene_index].process_event(event)

    def process_application_exit(self, event):
        if event.type != pygame.QUIT:
            return
        self.game_over = True
        Settings.highscores.insert_to_file()

    def scene_logic(self):
        self.scenes[Settings.scene_index].process_logic()

    def scene_draw(self):
        self.virtual_screen.fill(Settings.BACKGROUND_COLOR)
        self.scenes[Settings.scene_index].process_draw(self.virtual_screen)
        scaled = pygame.transform.scale(self.virtual_screen, self.screen.get_size())
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()

    def process_frame(self):
        self.scene_event()
        if Settings.scene_changed:
            self.scene_activate()
            return
        self.scene_logic()
        self.scene_draw()
        pygame.time.wait(3)

    def run(self):
        while not self.game_over:
            self.process_frame()

    def shrink_scaled_pos(self, pos):
        adjust_ratio = [
            self.virtual_screen.get_size()[0] / self.screen.get_size()[0],
            self.virtual_screen.get_size()[1] / self.screen.get_size()[1],
        ]
        return [pos[0] * adjust_ratio[0], pos[1] * adjust_ratio[1]]