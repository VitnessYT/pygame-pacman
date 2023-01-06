from .base import GhostBase
from logic.ghosts.inky import InkyTargetPoint

class InkyGhost(GhostBase):
    def __init__(self, x, y):
        self.directory = "Inky"
        super().__init__(x, y, InkyTargetPoint)
