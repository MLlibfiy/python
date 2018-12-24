# coding=utf-8
# if

age = 24
if 18 < age < 24:  # age> 18 and age < 24
    print "已经成年了"
elif age >= 24:
    print "中年危机"
else:
    print "还是个小孩"

# for循环
list1 = [1, 2, 3, 4, 5, 6, 7]

for i in list1:
    print i

dict1 = {1: 1, 2: 2, 3: 3}

for k, v in dict1.items():
    print k, v

# while 循环
i = 1
sum1 = 0
while i <= 100:
    sum1 += i
    i += 1
print sum1
