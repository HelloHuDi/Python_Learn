# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped1 = zip(a, b)
print(*zipped1)
zipped2 = zip(a, c)
print(*zipped2)
zipped3, zipped4 = zip(*zip(a, b))
print(*zipped3)
print(*zipped4)
