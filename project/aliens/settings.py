# -*- coding:utf-8 -*-

# 设置模块
class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 40
        self.ship_image_path = "images/ship.bmp"
        # 子弹设置
        self.bullet_speed_factor = self.ship_speed_factor
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # 外星人
        self.alien_image_path = 'images/alien.bmp'
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
