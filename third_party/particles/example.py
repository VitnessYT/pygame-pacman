from .base import Particle
from .figures import *
from .container import ParticleContainer
import pygame
import random

white_cubes = Particle(
    center_x=1280 / 6,
    center_y=720 / 4,
    life_seconds=1.3,
    speed=3,
    figure=Square,
    size_range=(5, 25),
    color=lambda x, y, percent: tuple([255 * (100 - percent) / 100] * 3)
)

sunflowers = Particle(
    center_x=1280 / 6 * 3,
    center_y=720 / 4,
    life_seconds=0.8,
    speed=2,
    figure=Circle,
    size_range=(1, 5),
    color=lambda x, y, percent: random.choice([(250, 250, 110), (250, 247, 106), (251, 244, 102), (251, 241, 99), (251, 238, 95), (251, 236, 91), (252, 233, 88), (252, 230, 84), (252, 227, 81), (253, 224, 77), (253, 221, 74), (253, 218, 70), (253, 215, 67), (254, 212, 64), (254, 209, 60), (254, 206, 57), (254, 203, 54), (254, 200, 50), (255, 196, 47), (255, 193, 44), (255, 190, 41), (255, 187, 38), (255, 184, 35), (255, 181, 32), (255, 177, 29), (255, 174, 26), (255, 171, 23), (255, 168, 20), (255, 164, 17), (255, 161, 14), (255, 158, 11), (255, 154, 8), (255, 151, 6), (255, 147, 4), (255, 144, 2), (255, 140, 1), (255, 137, 0), (255, 133, 0), (255, 130, 0), (255, 126, 0)])
)

smoke = Particle(
    center_x=1280 / 6 * 5,
    center_y=720 / 4,
    life_seconds=0.8,
    speed=3,
    figure=Circle,
    size_range=(20, 50),
    objects_count=40,
    color=lambda x, y, percent: random.choice([(139, 139, 139), (137, 137, 137), (135, 134, 135), (133, 132, 134), (131, 129, 132), (128, 127, 130), (126, 124, 128), (124, 122, 127), (122, 119, 125), (120, 117, 123)])
)

lasers = Particle(
    center_x=1280 / 6,
    center_y=720 / 4 * 3,
    life_seconds=0.8,
    speed=2,
    figure=Line,
    size_range=(50, 60),
    objects_count=30,
    width=7,
    color=lambda x, y, percent: random.choice([(9, 34, 182), (16, 34, 182), (21, 33, 183), (26, 33, 183), (30, 33, 184), (33, 32, 184), (36, 32, 184), (39, 32, 185), (42, 31, 185), (45, 31, 185), (47, 30, 186), (50, 30, 186), (52, 29, 186), (55, 29, 187), (57, 28, 187), (59, 28, 187), (61, 27, 188), (63, 27, 188), (65, 26, 188), (67, 25, 189), (69, 25, 189), (71, 24, 189), (73, 23, 190), (75, 23, 190), (77, 22, 190), (79, 21, 190), (80, 20, 191), (82, 19, 191), (84, 18, 191), (86, 17, 192), (87, 16, 192), (89, 15, 192), (91, 14, 192), (92, 12, 193), (94, 11, 193), (96, 9, 193), (97, 7, 193), (99, 6, 194), (100, 4, 194), (102, 2, 194)])
)

triangles = Particle(
    center_x=1280 / 6 * 3,
    center_y=720 / 4 * 3,
    life_seconds=0.8,
    speed=2,
    figure=Triangle,
    size_range=(5, 10),
    color=lambda x, y, percent: random.choice([(0, 234, 255), (0, 230, 255), (0, 226, 255), (0, 222, 255), (0, 217, 255), (0, 213, 255), (0, 209, 255), (0, 204, 255), (0, 200, 255), (0, 195, 255), (0, 190, 255), (0, 186, 255), (0, 181, 255), (0, 176, 255), (0, 171, 255), (0, 166, 255), (0, 161, 255), (0, 156, 252), (0, 150, 250), (0, 145, 247)])
)

bubbles = Particle(
    center_x=1280 / 6 * 5,
    center_y=720 / 4 * 3,
    life_seconds=0.9,
    speed=2,
    figure=Circle,
    size_range=(10, 30),
    width=2,
    objects_count=20,
    color=lambda x, y, percent: random.choice([(0, 234, 255), (0, 231, 248), (0, 227, 240), (0, 224, 232), (0, 221, 224), (0, 217, 216), (0, 214, 207), (0, 210, 198), (0, 206, 189), (0, 203, 180), (0, 199, 171), (0, 195, 162), (0, 191, 152), (0, 187, 143), (0, 183, 133), (0, 179, 123), (0, 175, 114), (0, 171, 104), (0, 167, 94), (0, 163, 84)])
)

def run():
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Vitness's particles example")
    pygame.init()
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1500)
    particles = ParticleContainer(
        white_cubes.copy(),
        sunflowers.copy(),
        smoke.copy(),
        lasers.copy(),
        triangles.copy(),
        bubbles.copy()
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                particles.append(white_cubes.copy())
                particles.append(sunflowers.copy())
                particles.append(smoke.copy())
                particles.append(lasers.copy())
                particles.append(triangles.copy())
                particles.append(bubbles.copy())
        screen.fill("black")
        particles.draw(screen)
        pygame.display.flip()
        clock.tick(60)
