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


# 压缩
import zlib

# b" "前缀表示：后面字符串是bytes 类型。
s = b'witch which has which witches wrist watch'

print(len(s))

w = zlib.compress(s)

print(len(w), w)

print(zlib.decompress(w))
