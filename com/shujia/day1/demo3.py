# coding=utf-8
if __name__ == '__main__':
    list1 = ["java", 1, 3.14, '1']
    list1[1] = "scala"
    print list1
    # 元组，tuple   不可变列表
    tuple1 = ("java", 1, 3.14, '1')
    # tuple1[1] = "scala"
    print tuple1
    print tuple1[1]

    # tuple 切片，实际上是返回一个新的tuple
    tuple2 = tuple1[1:-1]
    print type(tuple2)
    print tuple1[::-1]


