# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .

""" 条件语句"""

a = 0

while a < 100:
    if a > 50:
        break
    print("未达到条件：" + str(a))
    a += 1
print("达到条件：" + str(a))


def passTest(v):
    print('pass :', v)
    pass

var = 20

while var > 0:
    var -= 1
    if var == 5 or var == 8:
        continue
    if var == 10:
        passTest(var)
    print('当前值 :', var)
print("Good bye!")

