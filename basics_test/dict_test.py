#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
from copy import deepcopy

"""
字典方法：
    1、clear: 删除所有的字典项（包括任何指向此字典的变量）
    2、copy: 返回一个新字典，其包含的键值对与原字典相同（浅复制，修改副本中的值时，原字典也会受到影响，可使用深复制-deepcopy）
    3、fromkeys: 创建一个新字典，其中包含指定的键，默认对应的键为None，可提供特定的值
    4、get: 查找字典中是否存在指定的键，如果没有则返回None或者指定值
    5、items: 返回一个包含所有字典项的列表（字典视图，可用于迭代）
    6、pop: 删除与指定键对应的项
    7、keys：返回一个包含所有键的列表
    8、popitem: 随机删除一个项
    9、setdefault: 获取指定键相关的值，如果没有此键则添加键值对（值默认None），有则返回（不改变值）
    10、update: 使用b字典的项，添加或替换a字典中的项
    11、values: 返回一个包含所有值的列表
"""

dict_test = {1: "look", 2: "see", 3: "catch"}
print(dict_test.items())
print(dict_test.keys())

# 拓展：建立一个小说书数据库，能够准确的查找到需要的书籍（未完成）
