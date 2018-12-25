# coding=utf-8
lines = []

with open(r"E:\bigdata\python\data\Cource.txt") as file:
    lines = file.readlines()

list1 = []

file1 = open(r"E:\bigdata\python\data\Cource1.txt", "w")

for line in lines:
    str = line.decode("utf-8").encode("GBK")
    file1.write(str)

file1.close()
