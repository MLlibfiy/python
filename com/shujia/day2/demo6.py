# encoding=utf-8

try:
    a = 10
    b = int(raw_input())
    c = a / b
    print c
except (BaseException), e:
    print e
else:
    print "没有发生异常"
finally:
    print "都会执行"