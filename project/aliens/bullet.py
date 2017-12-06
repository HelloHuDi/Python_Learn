# -*- coding:utf-8 -*-
from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load_extended(ai_setting.bullet_image_path)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
