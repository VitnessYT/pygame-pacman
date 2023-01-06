from logic.ghosts.blinky import BlinkyTargetPoint
from .base import GhostBase


class BlinkyGhost(GhostBase):
    def __init__(self, x, y):
        self.directory = "Blinky"
        super().__init__(x, y, BlinkyTargetPoint)
