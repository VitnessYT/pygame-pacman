import pygame

from objects.base import BaseObject

from third_party.button import Button as InternalButton


class Button(BaseObject):
    BUTTON_STYLE = {
        "hover_color": pygame.Color('darkgray'),
        "clicked_color": pygame.Color('black'),
        "clicked_font_color": pygame.Color('white'),
        "hover_font_color": pygame.Color('white'),
    }

    def __init__(self, x, y, width, height, title, action, hover_sound, **kwargs):
        super(Button, self).__init__(x, y, width, height)
        self.internal_button = InternalButton(self.rect, pygame.Color('gray'), action, text=title, hover_sound=hover_sound, **kwargs, **self.BUTTON_STYLE)

    def event(self, event: pygame.event.Event) -> None:
        self.internal_button.check_event(event)

    def draw(self, screen: pygame.Surface) -> None:
        self.internal_button.update(screen)
