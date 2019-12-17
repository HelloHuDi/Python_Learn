# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
from past.builtins import raw_input

import sys

x = 'runoob'
sys.stdout.write(x + '\n')

raw_input("按下 enter 键退出，其他任意键显示...\n")

# eval 把引号去掉 ，中间内容当作代码执行
# 可以把控制台输入的代码直接执行
# 不要随意使用 ，危险，
# print(eval(input("输入：")))
