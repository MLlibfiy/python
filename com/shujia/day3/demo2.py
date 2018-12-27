# coding=utf-8
class student():
    # 对象初始化方法，在创建对象的时候调用
    def __init__(self, name, age, gender="男"):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print self.name, self.age, self.gender


s = student("张三", 23)
s.print_info()
s.age = 24  # 修改属性值
s.print_info()
s.clazz = "一班"  # 动态增加属性
print s.clazz


def fun():
    print "动态增加方法"


s.fun = fun
s.fun()

s1 = student("小丽", 23, "女")
s1.print_info()


class person():
    def __init__(self, name, age):
        # 在属性前面增加两个_ 实现属性的私有化
        self.__name = name
        self.__age = age

    # 多外提供编程接口
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age


    #私有方法
    def __fun(self):
        print "私有方法"

p = person("张三", 23)
print p.get_name()
p.__name = "李四"
print p.get_name()


class student(person):

    def get_name(self):
        print "子类方法"
        print self.__name


student1 = student("王五",22)
print student1.get_name()


