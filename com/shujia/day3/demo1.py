# coding=utf-8
import sys

print sys.path

import site

print site.getsitepackages()

# 增加临时模块搜索路径
sys.path.append("E:\\第二期\\视频\\python")

print sys.path
