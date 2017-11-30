# -*- coding:utf-8 -*-
from collections import OrderedDict
def mulitPar(*mulit):
    for m in mulit:
        print(m)


mulitPar("hdsf")
mulitPar("hdsf", "123", "fds", "fd", "54", 45)


def dictPar(**dict):
    print(dict)


dictPar(lj="kh", hfe="fdsfd", fds="fd")


class Dog():
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def test1(self):
        print(str(self.name).upper())

    def test2(self):
        print(self.age)

    def update_age(self, age):
        self.age = age


class Cat(Dog):
    def __init__(self):
        super().__init__("hao")

    def update_age(self, age):
        self.age = 190
        print(self.age)


dog = Dog("ha", 23)
dog.test1()
dog.test2()
dog = Dog("hadsf", 2343)
dog.test1()
dog.test2()
dog = Dog("hadggewgfege")
dog.test1()
dog.test2()
dog.update_age(90)
dog.test2()

cat = Cat()
cat.test1()
cat.update_age(10)


# 类似linkedMap
ord = OrderedDict()
ord["1"] = "one"
ord["2"] = "two"
ord["3"] = "three"
ord["4"] = "four"
print(ord)
