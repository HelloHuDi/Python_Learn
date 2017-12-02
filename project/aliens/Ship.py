# -*- coding:utf-8 -*-
import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load_basic("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞船置于底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
