import time

from .figures import *


# TODO: Поворот партиклов, гравитация партиклов
class Particle:
    def __init__(self, center_x: int, center_y: int, *, speed: int = 1, life_cycle: int = 90, objects_count: int = 150,
                 figure: type = Square, color: pygame.Color = pygame.Color("white"), rotate_angle: int = 0,
                 life_seconds: int = 3, size_range: int = (10, 10), width: int = 0):
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed
        self.life_cycle = life_cycle
        self.objects_count = objects_count
        self.figure = figure
        if callable(color):
            self.color = color
        else:
            self.color = lambda x, y, percent: color
        self.rotate_angle = rotate_angle
        self.wait = random.randint(3, 10)
        self.life_seconds = life_seconds
        self.end = time.time() + life_seconds
        self.objects = []
        self.size_range = size_range
        self.state = 0  # 0 = alive, 1 = destroying, 2 = dead
        self.width = width

        self.restore_data = {
            "center_x": center_x,
            "center_y": center_y,
            "speed": speed,
            "life_cycle": life_cycle,
            "objects_count": objects_count,
            "figure": figure,
            "color": color,
            "rotate_angle": rotate_angle,
            "life_seconds": life_seconds,
            "size_range": size_range,
            "width": width
        }

    def get_percent_complete(self):
        return min((time.time() - self.end + self.life_seconds) / self.life_seconds * 100, 100)

    def process(self):
        if len(self.objects) != self.objects_count:
            self.wait -= 1
            if self.wait == 0:
                self.objects.extend(
                    [self.figure(self.center_x, self.center_y, random.randint(*self.size_range), speed=self.speed,
                                 width=self.width) for _
                     in
                     range(min(random.randint(1, self.objects_count // 10), self.objects_count - len(self.objects)))])
                self.wait = random.randint(3, 10)
        for obj in self.objects:
            obj.update(self.rotate_angle, self.life_cycle,
                       (100 - self.get_percent_complete()) // 1.2 if self.state == 1 else self.get_percent_complete())
        self.objects = [obj for obj in self.objects if obj.is_alive()]

    def draw(self, screen):
        if self.state == 2:
            return
        if self.state == 0:
            if time.time() > self.end:
                self.state = 1
                self.end = time.time() + self.life_seconds
                user_func = self.color

                def disappeared_color(x, y, percent):
                    return pygame.Color(pygame.Vector3(*user_func(x, y, 100)) * (100 - percent) / 100)

                self.color = disappeared_color

        elif self.state == 1:
            if time.time() > self.end:
                self.state = 2
        self.process()
        for obj in self.objects:
            obj.draw(screen, self.color(*(obj.points[0] - pygame.Vector2(self.center_x, self.center_y)),
                                        self.get_percent_complete()))

    def is_alive(self):
        return self.state < 2

    def copy(self):
        return Particle(**self.restore_data)
