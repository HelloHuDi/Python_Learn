# -*- coding:utf-8 -*-
from time import sleep

import pygame
import sys
from project.aliens.bullet import Bullet
from project.aliens.alien import Alien
from project.aliens import Music


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        sys.exit()


def check_key_down_events(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, bullets, screen, ship)
    elif event.key == pygame.K_w or event.key == pygame.K_1:
        ai_setting.update_bullet_destructiveness(0)
    elif event.key == pygame.K_e or event.key == pygame.K_2:
        ai_setting.update_bullet_destructiveness(1)
    elif event.key == pygame.K_r or event.key == pygame.K_3:
        ai_setting.update_bullet_destructiveness(2)


'''装弹'''


def fire_bullet(ai_setting, bullets, screen, ship):
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_events(ai_setting, screen, stats, play_button, sb,
                 ship, aliens, bullets):
    # 监听鼠标 键盘事件
    for event in pygame.event.get():
        # 点击退出则关闭界面
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.USEREVENT:
            Music.start_music()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, play_button, sb,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, sb, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_setting, stats, screen, sb, ship, aliens, bullets, play_button):
    # 设置背景色
    screen.fill(ai_setting.bg_color)
    if not stats.game_active:
        play_button.draw_button()
    else:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        sb.show_score()
        aliens.draw(screen)
    # 显示界面
    pygame.display.flip()


def update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    # 超出屏幕顶部 则移除
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, aliens, bullets)


'''
检查子弹与外星人是否碰撞(重合)
'''


def check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, not ai_setting.bullet_strike, True)
    # 调用爆炸效果
    for values in collisions.values():
        for alien in values:
            stats.score += ai_setting.alien_points
            sb.prep_score()
            alien.explode(alien)
    check_high_score(stats, sb)
    if len(aliens) == 0:
        # Destroy existing bullets, and create new fleet.
        bullets.empty()
        # Increase level.
        stats.level += 1
        sb.prep_level()

        ai_setting.increase_speed()
        creat_fleet(ai_setting, screen, ship, aliens)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


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
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_setting, alien_width):
    # 计算可用空间
    available_space_x = ai_setting.screen_width - 2 * alien_width
    # 计算一行可容纳多少个外星人
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_setting, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    # 3 * alien_height 留给飞机操作的空间
    available_space_y = (ai_setting.screen_height - (3 * alien_height) - ship_height)
    # 计算一屏可容纳多少行外星人
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_setting, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        # 检查是否到达边缘
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    # 向下移动
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    # 调整方向
    ai_setting.fleet_direction *= -1


def update_aliens(ai_setting, stats, screen, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
      then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, sb, ship, aliens, bullets)
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_setting, stats, screen, sb, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    print("game over!")
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Update scoreboard.
        sb.prep_ships()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet, and center the ship.
    creat_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    # Pause.
    sleep(0.5)


'''检查外星人是否已经到达屏幕底部'''


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break
