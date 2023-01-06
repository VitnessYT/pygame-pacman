import pygame
import pygame.mixer
import random
from third_party.particles import Particle, Circle
from settings import Settings


class BaseScene:
    PROCESS_ESCAPE = True
    application = None

    def __init__(self):
        self.objects = []
        self.set_up_objects()

    def set_up_objects(self):
        pass

    def activate(self):
        for item in self.objects:
            item.activate()
        self.additional_activate()

    def additional_activate(self):
        pass

    def process_escape_event(self, event):
        if not self.PROCESS_ESCAPE:
            return
        if event.type != pygame.KEYDOWN or event.key != pygame.K_ESCAPE:
            return
        self.back_event()
        Settings.set_scene(Settings.SCENES.MENU)

    def back_event(self):
        pass

    def process_event(self, event):
        for item in self.objects:
            item.event(event)
        self.additional_process_event(event)
        self.process_escape_event(event)

    def additional_process_event(self, event):
        pass

    def process_logic(self):
        for item in self.objects:
            item.logic()
        self.process_additional_logic()

    def process_additional_logic(self):
        pass

    def process_draw(self, screen):
        for item in self.objects:
            item.draw(screen)
        self.process_additional_draw(screen)
        Settings.PARTICLES.draw(screen)

    def process_additional_draw(self, screen):
        pass

    def mouse_particle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            rescaled_pos = BaseScene.application.shrink_scaled_pos(event.pos)
            Settings.PARTICLES.append(Particle(
                #center_x=event.pos[0],
                #center_y=event.pos[1],
                center_x=rescaled_pos[0],
                center_y=rescaled_pos[1],
                life_seconds=0.3,
                speed=0.6,
                figure=Circle,
                size_range=(1, 3),
                width=2,
                objects_count=10,
                color=lambda x, y, percent: random.choice(
                    [(0, 234, 255), (0, 231, 248), (0, 227, 240), (0, 224, 232), (0, 221, 224), (0, 217, 216),
                     (0, 214, 207), (0, 210, 198), (0, 206, 189), (0, 203, 180), (0, 199, 171), (0, 195, 162),
                     (0, 191, 152), (0, 187, 143), (0, 183, 133), (0, 179, 123), (0, 175, 114), (0, 171, 104),
                     (0, 167, 94),
                     (0, 163, 84)])
            ))