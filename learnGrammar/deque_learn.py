# -*- coding:utf-8 -*-
# Created by hd on 2019/12/7.

# deque 队列

# 如下做法效率不高

from collections import deque

de = deque([1, 2, 3, 4, 5, 6])

print(de.popleft())

print(de)

print(de.popleft())

print(de)

print(de.append(9))

print(de)

# 嵌套列表解析
# 3 * 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

print()
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)




