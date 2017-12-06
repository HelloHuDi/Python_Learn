# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import threadpool
import pygame

''' 创建线程池'''
task_pool = threadpool.ThreadPool(5)


def explode(alien):
    requests = threadpool.makeRequests(async_explode, {alien, })
    [task_pool.putRequest(req) for req in requests]
    task_pool.wait()


def async_explode(alien):
    paths = alien.explode_image_path
    if type(paths) is tuple:
        for path in paths:
            alien.blitme(pygame.image.load_extended(path))
        pygame.display.update()
    else:
        alien.blitme(pygame.image.load_extended(paths))
