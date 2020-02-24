import pygame
import numpy as np


class Player():
    """ """

    def __init__(self, settings, screen):
        self.screen = screen
        self.speed = settings.player_speed
        self.steering_sensitivity = settings.player_steering_sensitivity
        self.moving = False
        self.turning_right = False
        self.turning_left = False
        #self.settings = settings
        self.color = settings.player_color
        self.radius = settings.player_radius
        self.start_pos_center = 10000
        self.center = self.start_pos_center
        self.start_pos_bottom = 10000
        self.bottom = self.start_pos_bottom
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])
        self.rect = pygame.Rect(self.center - self.radius, self.bottom - self.radius, 2*self.radius, 2*self.radius)
        # movement boundaries #
        self.bound_left = settings.grid_block_size + self.radius
        self.bound_up = settings.grid_block_size + self.radius
        self.bound_right = settings.game_field_width - settings.grid_block_size - self.radius
        self.bound_bottom = settings.screen_height - settings.grid_block_size - self.radius

    def update(self):
        """ move player """
        if self.moving:
            if self.turning_right:
                self.steering_vector = self.get_orto_vector('r')
                self.direction_vector = self.direction_vector + self.steering_vector * self.steering_sensitivity
                self.normalize_direction_vector()
            if self.turning_left:
                self.steering_vector = self.get_orto_vector('l')
                self.direction_vector = self.direction_vector + self.steering_vector * self.steering_sensitivity
                self.normalize_direction_vector()
            self.center -= self.direction_vector[0] * self.speed
            self.bottom -= self.direction_vector[1] * self.speed
            if self.bottom <= self.bound_up or self.bottom >= self.bound_bottom:
                self.moving = False
                self.reset_to_initial_pos()
            if self.center >= self.bound_right or self.center <= self.bound_left:
                self.moving = False
                self.reset_to_initial_pos()
            self.rect.x = self.center - self.radius
            self.rect.y = self.bottom - self.radius


    def reset_to_initial_pos(self):
        self.center = self.start_pos_center
        self.bottom = self.start_pos_bottom
        self.direction_vector = np.array([0, 1])
        self.steering_vector = np.array([0, 0])

    def get_orto_vector(self, dir):
        if dir == 'r':
            return np.array([-self.direction_vector[1], self.direction_vector[0]])
        elif dir == 'l':
            return np.array([self.direction_vector[1], -self.direction_vector[0]])

    def normalize_direction_vector(self):
        norm = np.linalg.norm(self.direction_vector)
        self.direction_vector = self.direction_vector / norm

    def blitme(self):
        """ draw player """
        pygame.draw.circle(self.screen, self.color, (int(self.center), int(self.bottom)), self.radius)
        pygame.draw.line(self.screen, self.color, (self.center, self.bottom),
                         (self.center - self.direction_vector[0] * 20,
                          self.bottom - self.direction_vector[1] * 20),
                         5)