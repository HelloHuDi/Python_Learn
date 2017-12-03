# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Group
from project.aliens.settings import Settings
from project.aliens.Ship import Ship
from project.aliens.alien import Alien
import project.aliens.game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(ai_setting,screen,ship,aliens)
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, aliens,bullets)


run_game()
