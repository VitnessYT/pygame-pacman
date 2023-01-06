import pygame

from logic.sound import Sound
from objects.texts import Text
from scenes.base import BaseScene
from objects.buttons import Button
from settings import Settings



class PauseScene(BaseScene):
    def __init__(self):
        self.header_text = Text((Settings.WINDOW_WIDTH - 340) / 2, (Settings.WINDOW_HEIGHT / 2) - 70, 'This is pause!', 42, pygame.Color('red'))
        self.pause_sound = Sound("data/sounds/pause_sound.wav")
        self.select_sound = Sound("data/sounds/select_sound.wav")
        super().__init__()
    def back_event(self):
        self.pause_sound.stop()
    def set_up_objects(self):
        self.objects.append(self.header_text)
        self.back_to_menu = Button((Settings.WINDOW_WIDTH - 200) / 2, (Settings.WINDOW_HEIGHT / 2) + 60, 200, 50, "BACK TO MENU",
                                   lambda: Settings.set_scene(Settings.SCENES.MENU), hover_sound=self.select_sound,
                                   font=pygame.font.Font(None, 30))
        self.back_to_game = Button((Settings.WINDOW_WIDTH - 200) / 2, (Settings.WINDOW_HEIGHT / 2), 200, 50, "CONTINUE",
                                   lambda: Settings.set_scene_no_activate(Settings.SCENES.GAME), hover_sound=self.select_sound,
                                   font=pygame.font.Font(None, 30))
        self.objects.append(self.back_to_menu)
        self.objects.append(self.back_to_game)

    def additional_activate(self):
        self.pause_sound.play()

    def additional_process_event(self, event):
        self.mouse_particle_event(event)
