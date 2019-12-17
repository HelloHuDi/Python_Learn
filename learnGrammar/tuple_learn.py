# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .

"""
元组

元组元素不能二次赋值，相当于只读列表 ,不能修改删除 ,但是内部list 可以
"""

aa = ("1", 2, "3", "4", 5, 6.3, True, [2, 3, 4, False])

print(aa)

print(aa.__len__())

print(aa[2])

print(aa[4])

print(aa[aa.__len__() - 1][0])

aa[aa.__len__() - 1][1] = 19

for a in aa:
    print("遍历元组：", a)
    if type(a) is list:
        for b in a:
            print("遍历集合：", b)

print(aa)

print(aa * 2)

# 错误的拼接
bb = (aa, 3, 5, 111, 55, "sdjfsjgsd;skd")

print(bb)

print()

# 元组中只包含一个元素时，需要在元素后面添加逗号
# 不加逗号就不是元组
cc = (1,)
dd = (1)
print(type(cc), type(dd))

# 拼接
tupl = cc + aa
print(tupl)

# 大小
w = tuple(v for v in range(10, 100, 5) if v % 2 == 0)
print("大小", w, min(w), max(w))

print("===测试===")

t = 12345, 54321, 'hello!'

print(type(t))

u = t, (1, 2, 3, 4, 5)
print(type(u), u)
