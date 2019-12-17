# -*- coding:utf-8 -*-
# Created by hd on 2019/12/6.

import time

import calendar

t = time.time()
print("当前时间戳为 : ", t)
t1 = time.localtime(t)
print("当前时间 : ", t1)
t2 = time.asctime(t1)
print("当前时间 : ", t2)

# 格式化成2016-03-20 11:45:39形式
s1 = "%Y-%m-%d %H:%M:%S"

# 格式化成Sat Mar 28 22:24:24 2016形式
s2 = "%a %b %d %H:%M:%S %Y"

t3 = time.strftime(s1, t1)
t4 = time.strftime(s2, t1)
print("当前时间 : ", t3, "===", t4)

# 将格式字符串转换为时间戳
print("当前时间 : ", time.mktime(time.strptime(t2, s2)))

print("当前日期 : ", calendar.month(2019, 12))

print("当前日期 : ", calendar.calendar(2019))

print("当前日期 : ", calendar.monthrange(2019, 12))


#
# from openpyxl.styles import Alignment, PatternFill, Font
# from openpyxl.utils import get_column_letter
# from openpyxl.drawing.image import Image
# import openpyxl
# import calendar
#
# # 设置第一天为星期天
# calendar.setfirstweekday(firstweekday=6)
# # 创建一个工作䈬
# wb = openpyxl.Workbook()
# # 遍历12个月
# # 添加工作表
# for i in range(1, 13):
#     sheet = wb.create_sheet(index=0, title=str(i) + '月')
# # 获取具体日期时间
# for j in range(len(calendar.monthcalendar(2019, i))):
#     for k in range(len(calendar.monthcalendar(2019, i)[j])):
#         value = calendar.monthcalendar(2019, i)[j][k]
# # 将0值变为空值
# if value == 0:
#     value = ''
#     sheet.cell(row=j + 9, column=k + 1).value = value
# else:
#     sheet.cell(row=j + 9, column=k + 1).value = value
# # 设置字体
# sheet.cell(row=j + 9, column=k + 1).font = Font(u'微软雅黑', size=11)
# # 单元格文字设置,右对齐,垂直居中
# align = Alignment(horizontal='right', vertical='center')
# # 单元格填充色属性设置
# fill = PatternFill("solid", fgColor="B9EBF7")
# # 对单元格进行颜色填充
# for k1 in range(1, 100):
#     for k2 in range(1, 100):
#         sheet.cell(row=k1, column=k2).fill = fill
# # 添加星期几信息行
# days = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
# num = 0
# for k3 in range(1, 8):
#     sheet.cell(row=8, column=k3).value = days[num]
# sheet.cell(row=8, column=k3).alignment = align
# sheet.cell(row=8, column=k3).font = Font(u'微软雅黑', size=11)
# # 设置列宽12
# c_char = get_column_letter(k3)
# sheet.column_dimensions[get_column_letter(k3)].width = 12
# num += 1
# # 设置行高30
# for k4 in range(8, 14):
#     sheet.row_dimensions[k4].height = 30
# # 合并单元格
# sheet.merge_cells('I1:P20')
# # 添加图片
# img = Image('image/plt.png')
# sheet.add_image(img, 'I1')
# # 添加年份及月份
# sheet.cell(row=3, column=1).value = '2019年'
# sheet.cell(row=4, column=1).value = str(i) + '月'
# # 设置年份及月份文本属性
# sheet.cell(row=3, column=1).font = Font(u'微软雅黑', size=16, bold=True, color='FF7887')
# sheet.cell(row=4, column=1).font = Font(u'微软雅黑', size=16, bold=True, color='FF7887')
# sheet.cell(row=3, column=1).alignment = align
# sheet.cell(row=4, column=1).alignment = align
# # 保存文档
# wb.save('爱豆日历.xlsx')
