import math
import random

import pygame


# TODO: идентичное хранение фигур - цетром является настоящая центральная точка, а не какая попало.
class Figure:
    def __init__(self, points, x, y, angle, speed=1, width=0):
        self.points = [pygame.Vector2(point) for point in points]
        self.points_remember = points.copy()
        self.points_count = len(points)
        self.x = x
        self.y = y
        self.angle = angle
        self.move = pygame.Vector2(math.cos(self.angle) * speed, math.sin(self.angle) * speed)
        self.cycles = 0
        self.alive = True
        self.width = width

    def is_alive(self):
        return self.alive

    def update(self, rotate_angle, life_cycle, percent_complete):
        self.cycles += 1
        for i in range(len(self.points)):
            self.points[i] = (
                        self.points[i] + self.move * 0.01 * max(125 - percent_complete, 1))  # .rotate(rotate_angle)
        if self.cycles > life_cycle:
            self.alive = False

    def draw(self, screen, color):
        if self.points:
            pygame.draw.polygon(screen, color, self.points, width=self.width)


class Circle(Figure):
    def __init__(self, x, y, size=10, speed=1, width=0):
        super().__init__([(x, y)], x, y, math.radians(random.randint(0, 360)), speed=speed, width=width)
        self.size = size

    def draw(self, screen, color):
        if self.points:
            pygame.draw.circle(screen, color, *self.points, self.size, width=self.width)


class Square(Figure):
    def __init__(self, x, y, size=10, speed=1, width=0):
        super().__init__([(x, y), (x + size, y), (x + size, y + size), (x, y + size)], x, y,
                         math.radians(random.randint(0, 360)), speed=speed, width=width)


class Triangle(Figure):
    def __init__(self, x, y, size=10, speed=1, width=0):
        super().__init__([(x, y - size), (x + size, y + size), (x - size, y + size)], x, y,
                         math.radians(random.randint(0, 360)), speed=speed, width=width)


class Line(Figure):
    def __init__(self, x, y, size=10, width=10, speed=1):
        self.width = width
        angle = math.radians(random.randint(0, 360))
        super().__init__([(x, y), (x + size * math.cos(angle), y + size * math.sin(angle))], x, y, angle, speed=speed,
                         width=width)

    def draw(self, screen, color):
        if self.points:
            pygame.draw.line(screen, color, *self.points, self.width)
