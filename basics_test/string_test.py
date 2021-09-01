#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

"""
字符串应用：
    1、字符串内容转换，如小数（f、F）、二进制（b）、八进制（o）、十六进制（x、X）等
    2、字符串宽度（:10）、精度（.2f）、千位分隔符（，），例 name:10,.2f
    3、符号（在宽度之前）、对齐（在符号与宽度之间）
"""
print("The {mod.__name__} defines the value {mod.pi:.4f} for Π".format(mod=math))
print("{home_work:.1%} of my work is done".format(home_work=0.9146))
print("The hexadecimal number of decimal number {past_number:d} is {new_number:X}"
      .format(past_number=15, new_number=15))
print("The landlady has ${money:0>14,.2f} in assets.".format(money=10000))
# print("{:^11}\n{:^11}\n{:^11}\n{:^11}\n{:^11}".format("0", "0 0", "0   0", "0     0", "0" * 9))

# 拓展：应用字符串的符号、填充、对齐等方法，建立一个表格（未完成）
# 进阶：识别输入的列表、字典，对其内容进行归纳整理，使之成为显示成为一个表格（未完成）

"""
字符串方法：
      1、center: 将字符串居中，默认以空格填充
      2、find: 查找对应的子字符串，如果有返回第一个的索引，如果没有则返回-1
      3、join: 将序列合并成一个字符串，其中所有的元素必须是字符串
      4、split: 将字符串拆分成一个列表，可以指定拆分的分割符和拆分最大次数
      5、lower: 字符串中字母全部转换成小写
      6、title: 将字符串中每个词首大写
      7、replace: 替换字符串中的内容
      8、strip: 只将字符串开头和末尾的空白或指定内容删除
      9、translate: 将字符串中内容替换，不同的是可以同时替换多个字符，并且需要提前建立一个str.maketrans()的转换表
      10、str.maketrans: 接受两个参数，两个长度相同的字符串或者字典（替换内容空白的用None表示）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
"""
# 拓展：识别txt英文文本内容，对不规范的内容进行调整（未完成）
