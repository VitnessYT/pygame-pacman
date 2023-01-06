from objects.texts import RecalculableText
from settings import Settings


class TopScoreDrawer(RecalculableText):
    def __init__(self, x, y, text, size, color):
        super().__init__(x, y, text + "{}", size, color)

    def draw(self, screen):
        super().recreate_text(Settings.highscores[0])
        super().draw(screen)
