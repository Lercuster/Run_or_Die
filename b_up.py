'''def update(self):
    """ move player """
    if self.move_right:
        self.center += self.settings.player_speed
        if self.center >= 930:
            self.move_right = False
    if self.move_left:
        self.center -= self.settings.player_speed
        if self.center <= 10:
            self.move_left = False
    self.rect.centerx = self.center
    if self.moving:
        self.bottom -= self.settings.player_speed
        if self.bottom <= 30:
            self.moving = False
    self.rect.bottom = self.bottom
'''