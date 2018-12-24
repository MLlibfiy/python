# coding=utf-8
import keyword

print 'hellowrold'
print keyword.kwlist

shot_id = 10
# 打印变量类型变量类型
print shot_id, type(shot_id)
# 变量重新赋值
shot_id = '10'
print shot_id, type(shot_id)
PI = 3.1415926
print PI, type(PI)

'''
多行注释
'''
"""
多行注释
"""

# print 在2.X中可以同时使用print 和print()
# 在pytho2.x print是关键字，在3.x print 是一个方法
print "helloworld"
print("helloworld")

print "我爱\n数加"
print r"我爱\n数加"

print 2 > 3
print 2 < 3
print 2 == 2
print 2 != 2
print 'a' == 'a'
print "a" == "a"

print True and False
print True and True
print True or False
print not True

a = None
print a, type(a)

# 算术运算符
a = 10
b = 4.0
print a + b
print a - b
print a * b
print a / b
print a // b
print a ** b

# 类型转换

print type(int('10'))
print type(str(10))
print type(float("3.14"))
print bool(None)
print bool(1)
print bool(0)
print bool("0")
print bool("assad")

# 类型转换异常
#print float("asdsad")

print isinstance("a", str)
print isinstance(10, str)
