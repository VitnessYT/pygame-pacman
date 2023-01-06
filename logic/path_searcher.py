from queue import Queue

from objects.images.wall import Wall
from settings import Settings


def path_searcher(ghost, target):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    directions.remove((-ghost.shift_x, -ghost.shift_y))
    q = Queue()  # ((indexes), (first_destination))
    x, y = Settings.field.get_cell(ghost.rect.x, ghost.rect.y)
    used = [[False for _ in range(Settings.field.height())] for _ in range(Settings.field.width())]
    used[x][y] = True
    for i, j in directions:
        rect = ghost.rect.move(i, j)
        for obj in Settings.field.get_nearest_objects(rect.x, rect.y, obj_type=Wall).values():
            if rect.colliderect(obj.rect):
                break
        else:
            q.put(((x + i, y + j), (i, j)))
            used[x + i][y + j] = True
    if (x, y) == target:
        return q.get()[1]
    directions.append((-ghost.shift_x, -ghost.shift_y))
    while not q.empty():
        (x, y), first_destination = q.get()
        if (x, y) == target:
            return first_destination
        for i, j in directions:
            if 0 <= x + i < Settings.field.width() and 0 <= y + j < Settings.field.height() and\
                    not used[x + i][y + j] and not isinstance(Settings.field[x + i, y + j], Wall):
                q.put(((x + i, y + j), first_destination))
                used[x + i][y + j] = True
    print(Settings.field[Settings.field.get_cell(ghost.rect.x, ghost.rect.y)], Settings.field[target])

