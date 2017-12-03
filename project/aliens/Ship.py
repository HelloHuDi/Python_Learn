# -*- coding:utf-8 -*-
import pygame


class Ship(object):
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load_basic("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞船置于底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.rect.right > self.screen_rect.right:
            self.center -= self.rect.right - self.screen_rect.right
        if self.rect.left < 0:
            self.center += abs(self.rect.left)
        self.rect.centerx = self.center
