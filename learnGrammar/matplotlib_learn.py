# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import matplotlib as mpl
import matplotlib.pyplot as plt

squares = [x ** 2 for x in range(5, 20)]
x_values = list(range(5, 20))
# 曲线
# plt.plot(x_values, squares, linewidth=2)
# 散点
plt.scatter(x_values, squares, c=squares, cmap=plt.cm.Reds, edgecolors='none', s=20)
plt.title("woody table")
# 设置轴名
plt.ylabel("Y AXIAL", fontsize=14)
plt.xlabel("X AXIAL", fontsize=14)
# 设置轴刻度大小
plt.tick_params(axis="both", labelsize=10)
# 设置xy轴范围
plt.axis([1, 20, 0, 400])
# 将图片保存 并去除空白区域
plt.savefig("image/plt.png", bbox_inches='tight')
plt.show()
