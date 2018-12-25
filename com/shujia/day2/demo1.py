# coding=utf-8
str1 = "    shujia  \t\n"

print str1.strip()  # 去除前后空格和制表符
print str1.lstrip()  # 去除左边空格和制表符
print str1.rstrip()  # 去除右边边空格和制表符

student = "1500100005,宣谷芹,22,女,理科五班"
slist = student.split(",")
print slist
joinstr = "\t".join(slist)
print joinstr

# 导入一个模块
import csv

f = open(r"E:\bigdata\python\data\students.csv")
# 每行数据通过逗号分隔，产生一个列表
reader = csv.reader(f)  # 返回一个迭代器
print type(reader)

for line in reader:
    print line[0]
    
f.close()