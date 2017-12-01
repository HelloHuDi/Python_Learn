with open("testFile/read.txt") as file:
    # print(len(file.read().strip().split()))
    for line in file:
        print(line.strip().split(","))

# r :只读 ，w:只写，文件若存在则清空内容，不存在则创建，a:追加，不会清空内容，r+ :读写模式
with open("testFile/write.txt", "a") as file_object:
    file_object.write("write object 1\n")
    file_object.write("write object 2\n")
    file_object.write("write object 3\n")
    file_object.write("write object 4\n\n")
