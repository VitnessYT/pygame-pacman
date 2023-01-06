import random

from settings import Settings
from objects.images.wall import Wall

def get_random_target():
    A = []
    for i in range(Settings.field.width()):
        for j in range(Settings.field.height()):
            if not isinstance(Settings.field[i, j], Wall):
                A.append((i, j))
    return Settings.field.get_coords(*random.choice(A))