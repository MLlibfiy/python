# coding=utf-8
# 快速生成列表
list1 = range(10)
# 开始位置，结束位置，步长
list2 = range(2, 10, 2)
print list1
print list2

# 列表推导式
list3 = [i ** 2 for i in range(10)]
print list3

set1 = {i ** 2 for i in range(10)}
print set1
print type(set1)

list4 = ["shujia", "java", "scala", "python"]

# 在每一行前面增加一个索引
for i, v in enumerate(list4):
    print i, v
