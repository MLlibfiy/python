# encoding=UTF-8

if __name__ == '__main__':
    # 单引号和双引号的区别
    print "我爱'数加"
    print '我爱"数加'

    # 列表，插入顺序
    list1 = [1, "shujia", 3.14, "java", "java"]
    # 打印列表
    print list1
    print type(list1)
    # 在列表末尾插入一个元素
    list1.append("scala")
    print list1
    # 指定元素的值删除元素
    list1.remove("shujia")
    print list1
    # 根据下标获取值
    # 从左到右从0开始
    print list1[2]
    # 从右到左，从-1开始
    print list1[-2]
    # 指定下表删除元素
    del list1[1]
    print list1
    # 取出最后一个元素
    print list1.pop()
    print list1
    print list1.pop(1)
    print list1
    # 指定下表插入数据
    list1.insert(1, "scala")
    list1.insert(1, "scala")
    list1.insert(5, "scala")
    print list1

    print list1.count("scala")
    # 反转
    list1.reverse()
    print list1
    # 获取列表长度
    print len(list1)

    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 列表切片  返回新的列表
    print list2[2:6]
    print list2[2:-3]
    print list2[-7:-3]
    # 步长为2
    print list2[1:10:2]
    print list2

    # 逆向切片，步长得是负数
    print list2[-2:-6:-1]

    # 通过切片反转列表
    print list2[::-1]

    print list2[1:]
    print list2[:-2]

    # 嵌套列表
    list3 = [[1, 2, 3, 4], "shujia"]
    print list3
    list4 = list3[0]
    print list4
    print list3[0][1]
