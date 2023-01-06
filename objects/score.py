from objects.texts import RecalculableText


class ScoreDrawer(RecalculableText):
    def __init__(self, x, y, text, size, color, start_score=0):
        super().__init__(x, y, text + "{}", size, color)
        self.score = start_score

    def draw(self, screen):
        super().recreate_text(self.score)
        super().draw(screen)

    def add_score(self, value):
        self.score += value
