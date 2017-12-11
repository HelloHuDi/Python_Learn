# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import numpy as np

a = [x for x in range(10)]
b = np.array(a)
print(b)
print(type(b))

print(b.shape)
print(b.argmax())
print(b.argmin())
print(b.max())
print(b.mean())
print(b.min())
