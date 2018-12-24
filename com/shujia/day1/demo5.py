# coding=utf-8

if __name__ == '__main__':
    # 集合   无序，不唯一
    set1 = {"shu", "jia", 1, "a", "a"}
    print set1

    # 创建空的集合
    set2 = set()
    set2.add("java")
    set2.add("java")
    set2.add("java")
    set2.add("scala")

    print set2

    set4 = {1, 2, 3, 4, 5, 6}
    set5 = {4, 5, 6, 7, 8, 9}

    print set4 | set5  # 并集
    print set4 & set5  # 交集
    print set4 - set5  # 差集
    print set4 ^ set5  # 对称集
