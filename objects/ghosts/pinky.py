from .base import GhostBase
from logic.ghosts.pinky import PinkyTargetPoint

class PinkyGhost(GhostBase):
    def __init__(self, x, y):
        self.directory = "Pinky"
        super().__init__(x, y, PinkyTargetPoint)
