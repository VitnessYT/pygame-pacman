import pygame

from logic.sound import Sound
from objects.buttons import Button
from objects.texts import Text
from objects.volume import VolumeDrawer
from scenes.base import BaseScene
from settings import Settings
from objects.buttons import Button

class SettingsScene(BaseScene):
    back_button: Button

    def __init__(self):
        super().__init__()

    def set_up_objects(self):
        self.select_sound = Sound("data/sounds/select_sound.wav")
        self.back_button = Button(10, 10, 150, 50, "<- Back", lambda: Settings.set_scene(Settings.SCENES.MENU),
                                  hover_sound=self.select_sound, font=pygame.font.Font(None, 30))
        self.objects.append(Text(x=170, y=10, text='Settings', size=58, color=pygame.Color('yellow')))
        self.objects.append(self.back_button)
        self.cur_volume = self.select_sound.get_volume()
        self.objects.append(
            Text(x=Settings.WINDOW_WIDTH / 2 - 42, y=Settings.WINDOW_HEIGHT / 2 - 40, text='Volume', size=24,
                 color=pygame.Color('yellow')))
        self.volume_display = VolumeDrawer(x=Settings.WINDOW_WIDTH / 2 - 35, y=Settings.WINDOW_HEIGHT / 2 - 10, text='',
                                           size=58, color=pygame.Color('yellow'))
        self.volume_display.volume = self.cur_volume
        self.objects.append(self.volume_display)
        self.button_down_volume = Button((Settings.WINDOW_WIDTH - 220) / 2, Settings.WINDOW_HEIGHT / 2 - 10, 50, 50,
                                         "<",
                                         lambda: self.change_volume(-1), font=pygame.font.Font(None, 30),
                                         hover_sound=self.select_sound)
        self.objects.append(self.button_down_volume)
        self.button_up_volume = Button((Settings.WINDOW_WIDTH + 120) / 2, Settings.WINDOW_HEIGHT / 2 - 10, 50, 50, ">",
                                       lambda: self.change_volume(1), hover_sound=self.select_sound,
                                       font=pygame.font.Font(None, 30))
        self.objects.append(self.button_up_volume)

    def change_volume(self, vol):
        self.select_sound.stop()
        self.select_sound.play()
        self.cur_volume += vol
        if (self.cur_volume < 0):
            self.cur_volume = 10
        elif (self.cur_volume > 10):
            self.cur_volume = 0
        if (self.cur_volume == 10):
            self.volume_display.rect.x = Settings.WINDOW_WIDTH / 2 - 35
        else:
            self.volume_display.rect.x = Settings.WINDOW_WIDTH / 2 - 15
        self.volume_display.volume = self.cur_volume
        self.select_sound.set_volume(self.cur_volume)
        Settings.VOLUME = self.cur_volume
        self.select_sound = Sound("data/sounds/select_sound.wav")
        self.back_button = Button(10, 10, 150, 50, "<- Back", lambda: Settings.set_scene(Settings.SCENES.MENU),
                                  hover_sound=self.select_sound)
        self.objects.append(Text(x=170, y=10, text='Settings', size=58, color=pygame.Color('yellow')))
        self.objects.append(self.back_button)

    def additional_process_event(self, event):
        self.mouse_particle_event(event)
