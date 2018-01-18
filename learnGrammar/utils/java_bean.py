# -*- coding:utf-8 -*-
# Created by hd on 2017/12/5 .
import os
import codecs

"""

将后台mysql数据库导出的表内容转换成java实体,需要根据实际情况来调整

实际使用场景：

一张表内容过多，后台定义了表字段，前端拿到表字段后，需要复制字段生成bean,以方便使用json转换
"""


def createJavaBean(filePath, createPath):
    print("file path: " + filePath + "+" + createPath)
    with codecs.open(filePath, "r", "GBK") as file:
        with open(createPath, "w") as file_object:
            allCount = 0
            printCount = 0
            for line in file:
                allCount += 1
                try:
                    if line.index("`") == 2:
                        printCount += 1
                        name = line[line.index("`") + 1:line.index("`", 4)]
                        if line.__contains__("'"):
                            title = line[line.index("'") + 1:line.__len__() - 3]
                        else:
                            title = ""
                        if line.__contains__("tinyint") or line.__contains__("int"):
                            if len(title) > 0:
                                file_object.write("/**" + title + "*/\n")
                                file_object.write("private int " + name + ";\n")
                            else:
                                file_object.write("private int " + name + ";\n")
                        else:
                            if len(title) > 0:
                                file_object.write("/**" + title + "*/\n")
                                file_object.write("private String " + name + ";\n")
                            else:
                                file_object.write("private String " + name + ";\n")
                    else:
                        print("不需要写入：" + line + "==" + str(allCount))
                except:
                    print("错误：" + line)
        print("总数量：" + str(allCount) + "=" + str(printCount))


# createJavaBean("file/health.txt", "file/bean.txt")

mainPath = "/Users/hd/Downloads/health"
listFile = os.listdir(mainPath)
for fileName in listFile:
    try:
        createJavaBean(mainPath + "/" + fileName, "file/" + fileName)
    except:
        print("error")
        pass
