# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import matplotlib.pyplot as plt

squares = [x ** 2 for x in range(5, 20)]
x_values = list(range(5, 20))
plt.plot(x_values, squares, linewidth=2)
plt.title("woody table")
# 设置轴名
plt.ylabel("Y AXIAL", fontsize=14)
plt.xlabel("X AXIAL", fontsize=14)
# 设置轴刻度大小
plt.tick_params(axis="both", labelsize=10)
plt.show()
