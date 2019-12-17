# -*- coding:utf-8 -*-
# string
from filecmp import cmp

from learnGrammar.utils.line import printDivisionLine

favorite_language = 'learn python the more'
print(str(favorite_language))
# rjust 靠右 不足补空格
print(repr(favorite_language).rjust(50))
print(favorite_language.__len__())
print(favorite_language.isspace())
print(favorite_language.title())
print(favorite_language.lower())
print(favorite_language.upper())
print(favorite_language.format())
# 补0
print(favorite_language.zfill(60))
# 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print(favorite_language.isalnum())
print("favorite2language".isalnum())
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(favorite_language.count("t"))
# 把字符串的第一个字符大写
print(favorite_language.capitalize())
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(favorite_language.center(40,'*'))
print("========2dd=========")
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language.find("th"))
print(favorite_language.find("th", 12))
print(favorite_language[favorite_language.find("th"):14])
print(len(favorite_language[favorite_language.find("th"):14]))
print("=======")
favorite_language = favorite_language.strip()
print(favorite_language)
print("===``````````====")
aa = "djslfjsdljf"
bb = 3.4
cc = 3
print("我是%s" % aa)
print("我是%.2f%%" % bb)
print("我是%d" % cc)

print("===``````````====")
bc = 'ceshi'
bd = 'jh'
bw = 'ceshi'

print(bc[0:])
print(bc[:4])

print("favorite_language.casefold() \n fdsf")

str = 'print(\'Hello World\')'
exec(str)  # 执行语句

total = bc + \
        bd + \
        bw

print(total)

a = c = b = "多个附子"

print(a, c, b)

w, y, l = "1", 2, True

print(type(w), type(y), type(l))

# r 原始字符
print(r"\n")

uu = u'Hello\u0020World !'

print("打印 Unicode 字符串: "+uu)


# raise ZeroDivisionError("抛出错误")



printDivisionLine()

ss = "颠倒https://mp.weixin.qq.com/s/BiAyz1cwpY9Vdxxz3nBFiA"

print(reversed(ss))

print(ss[::-1])
print(ss[:-1])


print(ss[0:10])
# 0 -10 切片，2为步进
print(ss[0:10:2])




# 方法名前加 下划线 可变私有
def get_formatted_name(first, last, middle=''):
    print(str("\njie ") + middle)
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
