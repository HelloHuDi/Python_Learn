# -*- coding:utf-8 -*-
import pygame
from project.aliens.settings import Settings
from project.aliens.Ship import Ship
import project.aliens.game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    ship = Ship(ai_setting,screen)
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


run_game()
