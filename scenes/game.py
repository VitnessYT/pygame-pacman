import datetime

import pygame

from logic.sound import Sound
from objects.cherry import Cherry
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.clyde import ClydeGhost
from objects.ghosts.inky import InkyGhost
from objects.ghosts.pinky import PinkyGhost
from objects.images.drawer import Drawer
from objects.images.pacman import Pacman
from objects.life import LifeDrawer
from objects.score import ScoreDrawer
from objects.topscoredrawer import TopScoreDrawer
from scenes.base import BaseScene
from settings import Settings


class GameScene(BaseScene):
    from_prev_collision = 0

    def __init__(self):
        super().__init__()
        self.open_time = None
        self.cherry_spawn_time = None
        self.pacman_death_time = None
        self.start_sound = Sound("data/sounds/gamestart_sound.wav")
        self.cherry_sound = Sound("data/sounds/eat_cherry_sound.wav")
        self.pacman_death_sound = Sound("data/sounds/dead_of_packman_sound.wav")

    def set_up_objects(self):
        self.objects.clear()
        self.ghosts = [
            BlinkyGhost(Settings.LEFT_SHIFT + Settings.CELL_SIZE * 6, Settings.TOP_SHIFT + Settings.CELL_SIZE * 7),
            PinkyGhost(Settings.LEFT_SHIFT + Settings.CELL_SIZE * 7, Settings.TOP_SHIFT + Settings.CELL_SIZE * 7),
            InkyGhost(Settings.LEFT_SHIFT + Settings.CELL_SIZE * 8, Settings.TOP_SHIFT + Settings.CELL_SIZE * 7),
            ClydeGhost(Settings.LEFT_SHIFT + Settings.CELL_SIZE * 9, Settings.TOP_SHIFT + Settings.CELL_SIZE * 7),
        ]
        self.drawer = Drawer(
            x=Settings.LEFT_SHIFT, y=Settings.TOP_SHIFT
        )
        self.score_drawer = ScoreDrawer(
            x=Settings.WINDOW_WIDTH // 2 + 140,
            y=Settings.WINDOW_HEIGHT // 2 - 280,
            text='SCORE: ',
            size=28,
            color=pygame.Color('white')
        )
        self.highscore_drawer = TopScoreDrawer(
            x=Settings.WINDOW_WIDTH // 2 + 140,
            y=Settings.WINDOW_HEIGHT // 2,
            text='Top: ',
            size=28,
            color=pygame.Color('white')
        )
        self.pacman = Pacman(*Settings.field.get_coords(8, 14))
        self.life_drawer = LifeDrawer(550, 500)
        self.cherry = Cherry(*Settings.field.get_coords(8, 10))
        self.objects.append(self.life_drawer)
        self.objects.append(self.drawer)  # добавление в список объектов
        self.objects.append(self.score_drawer)
        self.objects.append(self.highscore_drawer)
        self.objects.append(self.cherry)
        self.objects.append(self.pacman)
        self.objects += self.ghosts

    def additional_process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            Settings.set_scene(Settings.SCENES.PAUSE)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if Settings.life_count.life > 0:
                Settings.life_count.remove()

    def back_event(self):
        self.stop_sounds()
    def process_additional_logic(self):
        for ghost in self.ghosts:
            ghost.direction_chooser.logic(self.pacman)
        self.drawer.collide(self.pacman, self.score_drawer)
        self.check_ghost_collision()
        self.process_cherry_spawn()
        self.process_cherry_despawn()
        self.process_cherry_eating()
        self.process_pacman_death()

    def check_ghost_collision(self):
        for ghost in self.ghosts:
            if self.pacman.rect.colliderect(ghost.rect):
                if Settings.fear_mode:
                    self.drawer.eaten_ghosts += 1
                    self.score_drawer.add_score((2 ** self.drawer.eaten_ghosts) * 100)
                    ghost.rect.x, ghost.rect.y = Settings.field.get_coords(6, 7)
                    ghost.direction_chooser.logic(self.pacman)    # manually change direction to fix
                                                                  # collision with wall after teleport
                else:
                    if not self.pacman_death_time or (datetime.datetime.now() - self.pacman_death_time).seconds > 3:
                        self.pacman_death_time = datetime.datetime.now()
                    self.pacman.shift_x = self.pacman.shift_y = 0

    def process_cherry_eating(self):
        if self.pacman.rect.colliderect(self.cherry.rect) and self.cherry.showing:
            self.cherry_sound.play()
            self.cherry.hide()
            self.score_drawer.add_score(100)

    def process_cherry_despawn(self):
        if self.cherry_spawn_time is not None:
            if (datetime.datetime.now() - self.cherry_spawn_time).seconds > 10:
                self.cherry.hide()

    def process_cherry_spawn(self):
        if self.open_time is not None:
            if (datetime.datetime.now() - self.open_time).seconds > 3 and self.cherry_spawn_time is None:
                self.cherry_spawn_time = datetime.datetime.now()
                self.cherry.show()

    def process_pacman_death(self):
        if self.pacman_death_time is not None:
            self.pacman_death_sound.play()
            if (datetime.datetime.now() - self.pacman_death_time).seconds < 1:
                self.pacman.shift_x = self.pacman.shift_y = 0
            else:
                Settings.life_count.remove()
                self.pacman.activate()
                for i in range(4):
                    self.ghosts[i].rect.x = (Settings.LEFT_SHIFT + Settings.CELL_SIZE * (6 + i))
                    self.ghosts[i].rect.y = (Settings.TOP_SHIFT + Settings.CELL_SIZE * 7)
                Settings.wait_pacman = True
                self.pacman_death_time = None
                if Settings.life_count.life == 0:
                    self.stop_sounds()
                    Settings.set_scene(Settings.SCENES.GAMEOVER)
                    Settings.highscores.add_score(Settings.nickname, self.score_drawer.score)
                    Settings.wait_pacman = True
    def stop_sounds(self):
        self.pacman_death_sound.stop()
        self.start_sound.stop()
        self.cherry_sound.stop()

    def additional_activate(self):
        Settings.update_settings()
        self.open_time = datetime.datetime.now()
        self.set_up_objects()
        self.start_sound.play()
