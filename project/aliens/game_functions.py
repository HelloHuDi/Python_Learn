# -*- coding:utf-8 -*-
import pygame
import sys


def check_events(ship):
    # 监听鼠标 键盘事件
    for event in pygame.event.get():
        # 点击退出则关闭界面
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.K_RIGHT:
            ship.rect.centerx += 1
        elif event.type == pygame.K_LEFT:
            ship.rect.centerx -= 1


def update_screen(ai_setting, screen, ship):
    # 设置背景色
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # 显示界面
    pygame.display.flip()
