#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

print(sys.argv[0])
print(sys.argv[1])
PRESENT_PROJECT_PATH = os.getcwd()  # 返回当前工作目录

# a = os.path.abspath(PRESENT_PROJECT_PATH)  #返回绝对路径
# b = os.path.basename(PRESENT_PROJECT_PATH)  #返回文件名
c = os.path.abspath(os.curdir())
# print('\033[31m%s\033[0m'%a)
# print('\033[31m%s\033[0m'%b)
# print('\033[31m%s\033[0m'%c)
