# encoding=utf-8
# 函数
def function1():
    print "这是一个函数"


# 带括号执行函数，不带括号引用变量
function1()
function2 = function1
function2()


def square(x, n):
    return x ** n


print square(2, 3)


def function3(flag):
    if (flag):
        return "数加"
    else:
        return 1


r = function3(True)
print type(r)

# 函数简写
lambda1 = lambda x, n: x ** n
print lambda1(2, 3)
