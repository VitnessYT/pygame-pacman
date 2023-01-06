import logging
import sys

import pygame

from application import Application
from settings import Settings


def main():
    if '--debug' in sys.argv:
        logging.basicConfig(level=logging.DEBUG)
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT], pygame.RESIZABLE)
    pygame.display.set_caption('Pacman')
    pygame.display.set_icon(pygame.image.load("data/images/icon.png"))
    splash_image = pygame.image.load("data/images/splash.png")
    screen.blit(pygame.transform.scale(splash_image, screen.get_size()), (0, 0))
    pygame.display.flip()

    app = Application(screen)
    app.run()


if __name__ == '__main__':
    main()
