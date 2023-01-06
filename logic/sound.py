import logging

from logic.resources import *
from settings import Settings


class Sound:
    def __init__(self, sound_path):
        self.sound = ResourceLoader.load_sound(sound_path).resource
        self.set_volume(Settings.VOLUME)
        logging.debug('%f %d', self.sound.get_volume(), Settings.VOLUME)

    def play(self):
        self.set_volume(Settings.VOLUME)
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def pause(self):
        self.sound.pause()

    def get_volume(self):
        return int(self.sound.get_volume() * 10)

    def set_volume(self, volume):
        self.sound.set_volume(float(volume) / 10.0)
