# -*- coding:utf-8 -*-
# Created by hd on 2019/12/7.

# 全局 局部变量

# global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了

Alobals = 12
def Addm(add):
    # 不添加如下语句会报 UnboundLocalError 异常
    global Alobals
    Alobals += add


print(Alobals)
Addm(2)
print(Alobals)




