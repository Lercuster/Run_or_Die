import pygame
from global_settings import Settings
from time import sleep
from random import randint


def update_screen(settings, screen):
    screen.fill(settings.background_color)
    pygame.display.flip()


if __name__ == '__main__':
    print('kvsugvd')