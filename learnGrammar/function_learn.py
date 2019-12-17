# -*- coding:utf-8 -*-

# 从模块中导入一个指定的部分到当前命名空间中，表示导入指定的内容否则就是导入所有
# from collections import * 表示导入所有
from collections import OrderedDict


def special(type, content):
    return {
        "0": str,
        "1": len
    }[type](content)


print(special("1", "有意思的方法"))
print(special("0", "有意思的方法"))


# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入
def mulitPar(*mulit):
    for m in mulit:
        if type(m) is int:
            print("int类型")
        elif type(m) is str:
            print("str类型")
        else:
            print("随便%s" % m)


mulitPar("hdsf")
mulitPar("hdsf", "123", "fds", "fd", "54", 45)


# 加了两个星号 ** 的参数会以字典的形式导入
def dictPar(**dict):
    print(dict)


dictPar(lj="kh", hfe="fdsfd", fds="fd")


# 声明函数时，参数中星号 * 可以单独出现
# 这里看不到任何意义
def more(a, b, *, c):
    return a + b + c


# 报错
# print(more(1, 2, 4, c=3))
print(more(1, 2, c=3))


class Dog():
    __aaa = "我是私有"

    def __init__(self, name="ceshi", age=18):
        self.name = name
        self.age = age
        self.__privateMethod()

    def test1(self):
        print(str(self.name).upper())

    def test2(self):
        print(self.age)

    def update_age(self, age):
        self.age = age

    def __str__(self):
        print("打印对象")
        return self.name + "==" + str(self.age)

    # 私有方法无法被外包访问
    def __privateMethod(self):
        print("我是个私有方法")

    def __cmp__(self, other):
        print("我是个比较方法")
        return False


class Cat(Dog):

    def __init__(self):
        super().__init__("hao")
        print("本对象即将被初始化：" + self.__str__())

    def update_age(self, age):
        self.age = 190
        print(self.age)

    def __del__(self):
        print("本对象即将被删除：" + self.__str__())


dog = Dog()
# 临时属性
dog.xxx = "临时属性"
dog.test1()
dog.test2()

# python 伪私有
# 私有方法无法被外包访问,但是可以通过 '_类名__方法名' 实现访问，该方法不推荐使用
dog._Dog__privateMethod()

print(dog.__cmp__("wodsf"))
print(dog.xxx)
dog = Dog("hadsf", 2343)
dog.test1()
dog.test2()
dog = Dog("hadggewgfege")
dog.test1()
dog.test2()
dog.update_age(90)
dog.test2()
# xxx是属于上一个对象的临时属性，当前对象不具备
# 此处报错
# print(dog.xxx)


cat = Cat()
cat.test1()
cat.update_age(10)

del cat

# 类似linkedMap
ord = OrderedDict()
ord["1"] = "one"
ord["2"] = "two"
ord["4"] = "four"
ord["3"] = "three"
print(ord)
