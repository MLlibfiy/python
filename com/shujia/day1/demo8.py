# coding=utf-8
# 文件读写
file = open(r"E:\bigdata\python\data\students.txt")
# 读取文件中所有数据
# print file.read()
# file.close()

# 读取一行数  strip 去除前后空格
print file.readline().strip()
# 指定读取多少了字符
print file.read(10)

# 写文件
file1 = open(r"E:\bigdata\python\data\a.txt", "w")
file1.write("数加科技")
file1.close()

# 读文件
file2 = open(r"E:\bigdata\python\data\students.txt", "r")
lines = file.readlines()
print lines[-1]
print lines[::-1]

lists = []

for line in lines:
    tmp = line.strip()  # 去掉前后换行符
    split = tmp.split(",")
    lists.append(split)

for line in lists:
    print line

# str 的 join 方法 和 split 方法功能相反
list4 = ["张三", "23", "男", "文科一班"]
str1 = ','.join(list4)
print str1
