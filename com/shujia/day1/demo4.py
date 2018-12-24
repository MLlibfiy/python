# coding=utf-8
if __name__ == '__main__':
    # 字典dict
    dict1 = {1: "java",
             5: "scala",
             2: "scala",
             "3": "python"}
    print dict1
    # 根据key获取value
    print dict1["3"]

    keyList = [1, 2, 3, 4]
    valueList = ['1', '2', '3', '4']
    l = zip(keyList, valueList)
    print l
    print type(l)

    # 遍历列表
    for i in keyList:
        print i

    dict2 = {}
    for k, v in l:
        dict2[k] = v
    print dict2

    # 如果键不存在会报异常
    # print dict2[6]
    print dict2.get(6)  # 如果key不存在返回None

    # 判断key是否存在
    print 6 in dict2
    print dict2.has_key(5)

    if 4 in dict2:
        print dict2[4]

    # 返回一个列表
    keys = dict2.keys()
    print type(keys)
    values = dict2.values()
    print type(values)

    # 返回一个列表，k v 组成一个tuple
    print dict2.items()

    for k, v in dict2.items():
        print k, v

    dict2 = {1: "java",
             5: "scala",
             2: "scala",
             "3": "python"}

    del dict2['3']
    print dict2
    # 获取并删除
    print dict2.pop(1)

    # 清空字典
    dict2.clear()
    print dict2
