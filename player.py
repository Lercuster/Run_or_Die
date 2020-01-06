import pygame


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
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False
        self.settings = settings
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        """ move player """
        if self.move_right:
            self.center += self.settings.player_speed
            if self.center >= self.settings.screen_width - 10:
                self.move_right = False
        if self.move_left:
            self.center -= self.settings.player_speed
            if self.center <= 10:
                self.move_left = False
        self.rect.centerx = self.center
        if self.move_up:
            self.bottom -= self.settings.player_speed
            if self.bottom <= 30:
                self.move_up = False
        if self.move_down:
            self.bottom += self.settings.player_speed
            if self.bottom >= 600:
                self.move_down = False
        self.rect.bottom = self.bottom

    def blitme(self):
        """ draw player """
        self.screen.blit(self.image, self.rect)