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


# 高阶函数
# 以函数作为参数，
# 以函数作为返回值


def fun2(fun):
    fun()


def fun3():
    print "函数作为参数"


fun2(fun3)


def fun4(fun):
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return fun(list1)


# lambda  匿名函数
print fun4(lambda l: l[::-1])


# 以函数作为返回值

def fun5():
    def fun6():
        print "函数作为返回值"

    return fun6


fun7 = fun5()
fun7()

# 括号是执行函数的意思
fun5()()


# 函数默认值，有默认值的参数要放后面
def fun8(name, age=10):
    print age, name


fun8("张三", 23)
