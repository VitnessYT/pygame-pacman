class Pathfinding:
    DIRECTION_MATRIXES_XY = {
        "up": [0, -1],
        "down": [0, 1],
        "left": [-1, 0],
        "right": [1, 0],
        "none": [0, 0]
    }

    @staticmethod
    def get_rotation(direction):
        return Pathfinding.DIRECTION_MATRIXES_XY[direction]

    @staticmethod
    def apply_rotation(x, y, delta, matrix):
        return x + delta * matrix[0], y + delta * matrix[1]

