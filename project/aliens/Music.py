# -*- coding:utf-8 -*-

import pygame


def start_music():
    filename = "music/background.mp3".encode('utf-8')
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

'''重新播放'''


def rewind_music():
    pygame.mixer.music.rewind()


def stop_music():
    pygame.mixer.music.stop()
