from enum import Enum

import pygame
from third_party.particles import ParticleContainer
from logic.field import Field
from logic.highscore import HighscoreTable
from logic.life import LifeCounter


class SceneIndexes(Enum):
    MENU = 0
    GAME = 1
    PAUSE = 2
    SETTINGS = 3
    HIGHSCORE = 4
    GAMEOVER = 5
    GAMEEND = 6


class Settings:

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    MAX_COLLISION_COUNT = 5
    MAX_WAIT_SECONDS = 3
    BACKGROUND_COLOR = pygame.Color('black')
    LEFT_SHIFT = 10
    TOP_SHIFT = 30
    CELL_SIZE = 27
    SCENES = SceneIndexes
    TYPES = [None, None, None, None]  # Stores classes [Cell, Wall, Seed, Energizer]
    FEAR_MODE_SECONDS = 5
    PARTICLES = ParticleContainer()
    # Changeable
    VOLUME = 10
    nickname = "hello"
    # Change with scenes
    scene_changed = True
    scene_index = 0
    # Game only
    highscores: HighscoreTable = HighscoreTable()
    life_count = LifeCounter()
    field: Field = ...
    fear_mode = False
    wait_pacman = True

    @staticmethod
    def set_scene(index):
        Settings.scene_changed = True
        Settings.scene_index = index.value

    @staticmethod
    def update_settings():
        Settings.life_count = LifeCounter()
        Settings.field.reload()
        Settings.fear_mode = False
        Settings.wait_pacman = True

    @staticmethod
    def set_scene_no_activate(index):
        Settings.scene_index = index.value


Settings.field = Field("data/levels/field.txt", Settings)
