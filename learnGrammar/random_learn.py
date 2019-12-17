# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .

import random

"""random"""

list = [1, 2, 4, 5, 3, 0]

print(random.random())

# 按照步长在范围内随机取值
print(random.randrange(100, 300, 5))

# list 随机排序
random.shuffle(list)
print(list)

# 随机生成下一个实数，范围内
print(random.uniform(10, 20))

print(random.choice(['3e', 'ere', 13]))
