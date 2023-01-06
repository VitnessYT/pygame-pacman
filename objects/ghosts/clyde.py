from settings import Settings
from .base import GhostBase
from logic.ghosts.clyde import ClydeTargetPoint

class ClydeGhost(GhostBase):
    def __init__(self, x, y):
        self.directory = "Clyde"
        super().__init__(x, y, ClydeTargetPoint)