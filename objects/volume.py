from objects.texts import RecalculableText


class VolumeDrawer(RecalculableText):
    def __init__(self, x, y, text, size, color, start_vol=0):
        self.volume = start_vol
        super().__init__(x, y, text + "{}", size, color)

    def draw(self, screen):
        super().recreate_text(self.volume)
        super().draw(screen)