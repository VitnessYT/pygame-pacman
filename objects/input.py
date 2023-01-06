from objects.base import BaseObject
from objects.texts import RecalculableText
import pygame


class InputBox(BaseObject):
    application = None

    def __init__(self,
                 x: int,
                 y: int,
                 text: str = "",
                 max_chars: int = 10,
                 background: tuple[int, int, int] = (0, 40, 40),
                 foreground: tuple[int, int, int] = (250, 250, 30),
                 hint_color: tuple[int, int, int] = (200, 200, 200),
                 font_size: int = 36,
                 insets: int = 5,
                 hint: str = "",
                 on_edit = lambda self: None
                 ):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.is_focused = False
        self.text = text
        self.max_chars = max_chars
        self.background = background
        self.foreground = foreground
        self.font_size = font_size
        self.rect.width = font_size * max_chars
        self.rect.height = font_size + insets * 2
        self.insets = insets
        self.hint = hint
        self.hint_color = hint_color
        self.hint_object = RecalculableText(
            self.x + self.insets,
            self.y + self.insets,
            self.hint,
            self.font_size,
            self.hint_color
        )
        self.text_object = RecalculableText(
            self.x + self.insets,
            self.y + self.insets,
            self.text,
            self.font_size,
            self.foreground
        )
        self.on_edit = on_edit

    def event(self, event):
        super().event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(InputBox.application.shrink_scaled_pos(event.pos)):
                self.is_focused = True
            else:
                self.is_focused = False

        if event.type == pygame.KEYDOWN and self.is_focused:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                print(self.text)
            elif len(self.text) < self.max_chars:
                self.text += event.unicode
                print(self.text)
            self.on_edit(self)
        self.text_object.text = self.text
        self.text_object.render()

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.rect(
            screen,
            self.background,
            self.rect
        )
        if len(self.text) < 1:
            self.hint_object.draw(screen)
        else:
            self.text_object.draw(screen)
        if self.is_focused:
            pygame.draw.rect(screen, self.foreground, self.rect, 2)

    def move_to(self, nx, ny):
        dx, dy = nx - self.x, ny - self.y
        self.x = nx
        self.y = ny
        self.rect.x = nx
        self.rect.y = ny
        self.text_object.rect.x += dx
        self.text_object.rect.y += dy
        self.hint_object.rect.x += dx
        self.hint_object.rect.y += dy