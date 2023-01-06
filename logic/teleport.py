from settings import Settings


class Teleport:
    def __init__(self, rect):
        self.teleport = True
        self.rect = rect

    def check_teleport(self):
        if self.teleport:
            if self.rect.center[1] in range(int(Settings.CELL_SIZE * 11.5), int(Settings.CELL_SIZE * 12.5)):
                if self.rect.center[0] in range(0, Settings.CELL_SIZE):
                    self.rect.x = Settings.CELL_SIZE * 16
                    self.teleport = False

                elif self.rect.center[0] in range(int(Settings.CELL_SIZE * 16.5), int(Settings.CELL_SIZE * 17.5)):
                    self.rect.x = 0
                    self.teleport = False
        return self.rect.x

    def teleport_access(self):
        if self.rect.center[0] in range(Settings.CELL_SIZE, Settings.CELL_SIZE * 2) or \
                self.rect.center[0] in range(int(Settings.CELL_SIZE * 15.5), int(Settings.CELL_SIZE * 16.5)):
            self.teleport = True
        return self.teleport
