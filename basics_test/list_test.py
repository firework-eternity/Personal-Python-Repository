#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os

Chinese_years = [{"天干": ["甲", "乙", "丙", "丁", "", "", "", "", "", ""]},
                 {"地支": ["子", ""]}]
Chinese_months = ["正月"]
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_endings = ["st", "nd", "rd"] + 17 * ["th"] + ["st", "nd", "rd"] + 7 * ["th"] + ["st"]
constant = 0

"""
year = input("Please input in sequence (year, month, day)\nYear:")
month = input("Month:")
day = input("Day:")

# 拓展：将中国阴历算法加入到日期表中，且阳历和阴历能相互对应（未完成）

# 索引
en_month = months[int(month)-1]
en_day = day + day_endings[int(day)-1]
print("English format of date :%s %s,%s" % (en_month, en_day, year))
# 拓展：对于异常数据的处理，并加入星期（未完成）

# 数据变更
past_months_list = months[0:int(month)]
past_months = ""
while constant < int(month):
    past_months = past_months + " " + past_months_list[constant]
    constant = constant + 1
print("Months in the past:%s" % past_months)
# 拓展：应用步长等列表功能，得出当前是第几季度（未完成）

sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2
print("\n" +
      " " * left_margin + "+" + "-" * (box_width - 2) + "+\n" +
      " " * left_margin + "|" + " " * (text_width + 4) + "|\n" +
      " " * left_margin + "|  " + "\033[32m%s\033[0m" % sentence + "  |\n" +
      " " * left_margin + "|" + " " * (text_width + 4) + "|\n" +
      " " * left_margin + "+" + "-" * (box_width - 2) + "+")
# 拓展：可以识别多条语句用于显示（标题、文本、注释，设定多个模板），字体颜色、大小等都可以进行设定
"""

"""
列表操作方法：
    1、append: 附加元素到列表末尾
    2、clear: 清空列表内容
    3、copy: 复制列表
    4、count: 计算列表中指定元素数目
    5、extend: 衔接另一个列表
    6、index: 查询指定元素第一次出现的索引
    7、insert: 将对象插入列表中指定索引
    8、pop: 从列表中取出指定索引的元素，并返回取出的元素
    9、remove: 删除第一次出现的指定元素
    10、reverse: 按相反的顺序排列元素
    11、sort: 对列表中元素进行排序，其参数key指的是排序参考条件，参数reverse指是顺序还是逆序排列
    12、sorted: 可对任何序列进行排序（字符串、列表、字典[识别的是key值]），返回一个列表
"""

a = ["append", "interesting", "hate", "nice"]
print(max(a))
print(len(a))
a.sort()
print(a)
a.reverse()
print(a)

# 列表操作拓展：应用以上拓展内容，实现一个可显示的日历
# 要求：1、星期与日期对应，并显示阴历；2、显示重点标注的日期以及相应的事项；3、输出一个txt格式的日志
