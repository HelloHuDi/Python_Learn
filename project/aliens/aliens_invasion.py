# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group

from project.aliens import Music
from project.aliens.settings import Settings
from project.aliens.Ship import Ship
from project.aliens.game_stats import GameStats
import project.aliens.game_functions as gf
from project.aliens.button import Button
from project.aliens.scoreboard import Scoreboard


def run_game():
    pygame.init()
    Music.start_music()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting, screen)
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_setting, screen, "PLAY")
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, sb,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen,sb, ship, aliens, bullets)
        gf.update_screen(ai_setting, stats, screen, sb, ship, aliens, bullets, play_button)


run_game()
