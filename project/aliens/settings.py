# -*- coding:utf-8 -*-

class Settings():
    def __init__(self):
        # 设置屏幕
        self.black_color = (0, 0, 0)
        self.white_color = (255, 255, 255)
        self.text_size=48
        self.text_color = self.white_color
        self.screen_width = 500
        self.screen_height = 800
        self.bg_color = self.black_color
        self.ship_image_path = "images/ship.png"
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        # 设置子弹是否具有穿透属性
        self.bullet_strike = False
        # self.bullet_color = (60, 60, 60)
        self.bullet_image_path = "images/bullet_general.png"
        # 当前屏幕内允许存在的子弹数量
        self.bullets_allowed = 10
        # 外星人
        self.alien_image_path = 'images/alien.png'
        # 空白
        self.fleet_drop_speed = 10
        # button
        self.button_width = self.screen_width / 5
        self.button_height = 50

        # 外星人被击中爆炸效果
        self.alien_explode_image_path = ('images/pop1.png',
                                         'images/pop2.png',
                                         'images/pop3.png',
                                         'images/pop4.png',
                                         'images/pop5.png')
        # 设置玩家本轮游戏次数（n条命）
        self.ship_limit = 3
        # How quickly the game speeds up.
        self.speedup_scale = 0.1
        # How quickly the alien point values increase.
        self.score_scale =1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = self.ship_speed_factor * 2
        self.alien_speed_factor = self.ship_speed_factor / 1.5
        # Scoring.
        self.alien_points = 50
        # 移动方向 ，fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """游戏加速"""
        self.ship_speed_factor += self.speedup_scale
        self.bullet_speed_factor += self.speedup_scale
        self.alien_speed_factor += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        pass

    def update_bullet_destructiveness(self, level):
        """修改子弹等级"""
        if level == 0:
            self.bullet_image_path = "images/bullet_general.png"
        elif level == 1:
            self.bullet_image_path = "images/bullet_flame.png"
        elif level == 2:
            self.bullet_image_path = "images/bullet_missile.png"
