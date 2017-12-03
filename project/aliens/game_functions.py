# -*- coding:utf-8 -*-
import pygame
import sys
from project.aliens.bullet import Bullet
from project.aliens.alien import Alien


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        sys.exit()


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, bullets, screen, ship)


def fire_bullet(ai_setting, bullets, screen, ship):
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_events(ai_setting, screen, ship, bullets):
    # 监听鼠标 键盘事件
    for event in pygame.event.get():
        # 点击退出则关闭界面
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship, aliens, bullets):
    # 设置背景色
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 显示界面
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def creat_fleet(ai_setting, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height,
                                  alien.rect.height)
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number,
                         row_number)


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
