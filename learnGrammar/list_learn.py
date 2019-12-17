# -*- coding: UTF-8 -*-
"""list 列表"""
import sys

testList = ["aaa", "aaaa", "aaaaa", "bbb", "aaa", "bbb", "ccc", "ddd", "eee", "fff", [1, 2, 3]]
print(testList)
del testList[2:4]
print(testList)
popValue = testList.pop(2)

# 扩展
testList.extend(["dsfsdf", "最后"])
print(testList)
print(testList.count("aaa"))

# 迭代器
it = iter(testList)
print("迭代器", it.__next__())

print("====1====")
print(popValue)
testList.append("agb")
testList.append([1, "dsfds"])
print(testList)

ga = testList.remove("eee")
print(testList)
# remove 没有返回值，pop有
print(ga)
print("====2====")
testList.__delitem__(1)
print()
testList.insert(1, "test")
print(testList)

print("\n====sort 永久排序====\n")
sortList = ["gag", "sfd", "ad", "sd", "wf", "hr", "ld"]
sortList.sort()
print(sortList)
sortList.sort(reverse=True)
print(sortList)

print("\n====sorted 临时排序====\n")
sortedList = ["afd", "hdf", "ar", "sh", "jk", "we", "yr"]
print(sorted(sortedList, reverse=True))
print(sorted(sortedList, reverse=True)[1])
print(sortedList)
print("\n====reverse排序====\n")
reverseList = ["测试1", "测试2", "测试3", "测试4", "测试5", "测试6", "sflsd"]
reverseList.reverse()
print(reverseList)
reverseList.reverse()
print(reverseList)
print(reverseList.__len__())
print(len(reverseList))
print(reverseList[-1])
print(reverseList[len(reverseList) - 1])

print("\n====遍历====\n")
for value in reverseList:
    print("item :" + str(value).title())

print("\n====遍历下标====\n")
for i, v in enumerate(reverseList):
    print(i, v)

print("\n====遍历排序====\n")
for value in sorted(set(reverseList)):
    print("item :" + str(value).title())

print("\n====遍历iter====\n")
for value in iter(reverseList):
    print("item :" + str(value).title())

aList = ["a", "b", "c"]
bList = ["d", "w", "f", 1]

print("\n====遍历组合==以最小的列表数作为截止下标==\n")
for a, b in zip(aList, bList):
    print(a, b)

#
# print("\n====遍历 try except====\n")
# it = iter(reverseList)
# while True:
#     try:
#         print("item :" + str(next(it)))
#     except StopIteration:
#         sys.exit()
#     finally:
#         print("遍历完成")


print("\n====区间====\n")
numberList1 = list(x ** 2 for x in range(2, 1000, 2) if x % 2 == 0)
print(min(numberList1))
print(max(numberList1))
print(sum(numberList1))

print("========range===========")
numberList2 = list(range(0, 20, 2))
print(numberList2)
numberList3 = list(x ** 2 for x in range(0, 20, 2) if x % 2 == 0)
print(numberList3)
numberList = list(x * y for x in numberList1 for y in numberList3)
print(numberList)

print("========range=23==========")
strList = list(x + y for x in "hu" for y in "di")
print(strList)
print("hd" in strList)
print("hd" not in strList)
print("hsfdfd" not in strList)

print("\n====切片====\n")
print(strList)
print(strList.copy().pop(2))
print(strList[2:5])
print(strList[:10])
print(strList[2:])
print(strList[-3:])  # 倒数第三位开始
print('==')
print(strList[:])
print(strList == strList[:])

if __name__ == '__main__':
    print("主程序")
