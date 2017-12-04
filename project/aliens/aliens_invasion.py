# -*- coding:utf-8 -*-
from time import sleep

import pygame
from pygame.sprite import Group

from project.aliens import Music
from project.aliens.settings import Settings
from project.aliens.Ship import Ship
from project.aliens.game_stats import GameStats
import project.aliens.game_functions as gf


def run_game():
    pygame.init()
    Music.start_music()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting, screen)
    stats = GameStats(ai_setting)
    bullets = Group()
    aliens = Group()
    gf.creat_fleet(ai_setting, screen, ship, aliens)
    pygame.display.set_caption("Alien Invasion")
    while stats.game_active:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
        gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)


run_game()
