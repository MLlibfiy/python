# coding=utf-8
print "start"
# 手动抛出异常
assert 1 == 1, BaseException
print "=" * 20
assert 1 == 0, BaseException
assert False, BaseException
print "end"
