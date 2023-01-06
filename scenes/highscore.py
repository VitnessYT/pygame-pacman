from logic.sound import Sound
from scenes.base import BaseScene
from objects.highscore import HighscoreTableDrawer
from objects.buttons import Button
from objects.texts import Text
from settings import Settings
import pygame

class HighscoreScene(BaseScene):
    def __init__(self):
        self.select_sound = Sound("data/sounds/select_sound.wav")
        self.highscore_table = HighscoreTableDrawer(
            10, 80,
            Settings.highscores.get_data(),
            max_display_lines=9, text_size=36,
            column_size=300
        )
        self.highscore_table.move_to(
            Settings.WINDOW_WIDTH // 2 - self.highscore_table.rect.width // 2,
            80
        )
        self.scene_title = Text(0, 0, "Highscores Table", 42, pygame.Color('yellow'))
        self.scene_title.rect.x = Settings.WINDOW_WIDTH // 2 - self.scene_title.rect.width // 2
        self.scene_title.rect.y = 10
        self.back_button = Button(325, 532, 150, 58, "<- Back",
                                  lambda: Settings.set_scene(Settings.SCENES.MENU),
                                  hover_sound=self.select_sound, font=pygame.font.Font(None, 30))
        super().__init__()

    def additional_activate(self):
        Settings.highscores.update_drawer_data()
        if self.objects:
            highscore_table = HighscoreTableDrawer(
                10, 80,
                Settings.highscores.get_data(),
                max_display_lines=9, text_size=36,
                column_size=300
            )
            highscore_table.move_to(
                Settings.WINDOW_WIDTH // 2 - highscore_table.rect.width // 2,
                80
            )
            self.objects[2] = highscore_table

    def additional_process_event(self, event):
        self.mouse_particle_event(event)

    def set_up_objects(self):
        self.objects.append(self.back_button)
        self.objects.append(self.scene_title)
        self.objects.append(self.highscore_table)
