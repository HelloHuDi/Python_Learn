# -*- coding: UTF-8 -*-
# !/usr/bin/python3
"""
字典

键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
"""

import operator

dict = {"hd": "12", "ds": "12w", "sd": "12we"}
print(dict)
for item in dict.items():
    print(item)
print("=1=")
for key in dict.keys():
    print(key)
print("=2=")
for value in dict.values():
    print(value)
print()
print("=3=")
print(dict["hd"])
# 用get不会报错 直接取报错
# print(dict["sdf"])
print(dict.get("sdf"))

print(dict.__contains__("hh"))
print(dict.__contains__("12we"))
print(dict.__contains__("ds"))
print("=4=")
del dict["hd"]
print(dict)
print()
print("=5=")
dict["dsjlfd"] = "dsfdsfsdfd"
print(dict)

print("====6===")
sd = dict.pop("sd")
print(dict)
print(sd)

print()
print("====7===")
dict["fsafe99"] = '123'
dict["bsafe99"] = '35'
dict["asafe99"] = '123'
# 排序
for key, value in sorted(dict.items()):
    print("key :" + str(key) + ",value :" + str(value) + "==type : " + str(type(value)))

# 添加如下两个元素，排序会报错，类型不一致
dict["asafe109"] = 123
dict["asafe9919"] = True
# for value in sorted(set(dict.values())):
#     print("value :" + str(value))

dict2 = {"2": "dsfs"}
print("打印比较 1 ：", operator.eq(dict, dict2))
print("打印比较 2 ：", operator.eq(dict, dict.copy()))

print("打印某模块方法：", dir(operator))

# 删除字典
del dict
