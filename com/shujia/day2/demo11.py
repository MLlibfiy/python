# coding=utf-8
import numpy as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print array
print type(array)

a2 = np.array(["1", "2", "3", "4"])
print a2
print a2.astype("int")

# 查看数组几行几列
print array.shape

a3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# 切片之后还是一个ndarray
print a3
print a3[1, 2]  # 去某一个位置的数据
print a3[1:, 2:]
print a3[::-1, ::-1]
print a3[::-1, ::]
a4 = a3[(0, 1, 2), (0, 1, 2)]
print type(a4)
# 布尔值索引，取出所有大于5的数据
print a3[a3 > 5]

print a3 + 1
print a3 * 10

print a3.reshape(2, 6)

print a3.T  # 转置

print np.fliplr(a3)  # 左右翻转
print np.flipud(a3)  # 上下翻转

print a3

# 对位运算

a6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print a6 + a7  # 对应位置相加
print a6 - a7  # 对应位置相减
print a6 * a7  # 对应位置相相乘
print a6 / a7  # 对应位置相相乘

lines = []

with open(r"E:\bigdata\python\data\Cource.txt", "r") as file:
    lines = file.readlines()

cources = [tuple(line.strip().split(",")) for line in lines]
print cources

dtype = [("id", int), ("name", object), ('score', int)]

np_cources = np.array(cources, dtype=dtype)

print np_cources
print np_cources['id']

print np_cources['score'] == 150
print np_cources[np_cources['score'] == 150]  # 获取分数大于150的数据

print np_cources['id'][::-1]

a7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print np.log(a7)
print np.sin(a7)
print np.cos(a7)

print a7
print np.diff(a7,axis=1)
print np.diff(a7,axis=0)


print  np.std(a7)
print  np.var(a7,axis=0)

r1 = np.random.rand(3, 4)
r2 = np.random.rand(4, 3)
print r1
print r2

print np.random.randint(0,10)
