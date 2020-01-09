import pygame
import numpy as np


class Player():
    """ """

    def __init__(self, settings, screen):
        self.screen = screen
        self.speed = settings.player_speed
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.speed = settings.player_speed
        self.moving = False
        self.move_down = False
        self.move_right = False
        self.move_left = False
        self.settings = settings
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])
        self.scaling = 0.1

    def update(self):
        """ move player """
        if self.moving:
            self.direction_vector = self.direction_vector + self.steering_vector * 1
            self.normalize_direction_vector()
            self.center -= self.direction_vector[0]
            self.bottom -= self.direction_vector[1]
            if self.bottom <= 30 or self.bottom >= 650:
                self.moving = False
                self.reset_to_initial_pos()
            if self.center >= 930 or self.center <= 30:
                self.moving = False
                self.reset_to_initial_pos()
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def reset_to_initial_pos(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])

    def get_orto_vector(self, dir):
        if dir == 'r':
            return np.array([-self.direction_vector[1], self.direction_vector[0]])
        elif dir == 'l':
            return np.array([self.direction_vector[1], -self.direction_vector[0]])

    def normalize_direction_vector(self):
        self.direction_vector = self.direction_vector / (self.direction_vector[0] ** 2 + self.direction_vector[1] ** 2) ** 1/2

    def blitme(self):
        """ draw player """
        self.screen.blit(self.image, self.rect)