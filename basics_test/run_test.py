#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import re

# A = sys.path.append(sys.argv[2])

test_present_project_path = "present_project"
PRESENT_PROJECT_PATH = os.getcwd().replace("basics_test", test_present_project_path)  # 返回txt文本存放目录

txt_list = os.listdir(PRESENT_PROJECT_PATH)  # 读取txt文本存放目录下文件列表
test_txt_project = txt_list.pop()  # 随机选择读取列表下的一个文件
print("当前文件为：%s" % test_txt_project)
try:
    if ".txt" in test_txt_project:
        file = open(PRESENT_PROJECT_PATH + "\\" + test_txt_project, "r")  # 打开txt文件
        need_number_start = input("请输入您需要开始查看的章节号：")
        need_number_end = input("请输入您需要结束查看的章节号：")
        i, c, d = None, 0, 0  # i 用于循环，c 用于计算行数，d 用于表示输出状态：0-不输出，1-开始，2-结束
        if need_number_start < need_number_end:
            print("当前查看章节数为：第%s章到第%s章，共计%s章" % (need_number_start, need_number_end,
                                                int(need_number_end)-int(need_number_start) + 1))
        elif need_number_start == need_number_end:
            print("当前查看章节数为1章")
        else:
            d = 2
            print("您输入的始末章节号存在问题")
        while i is None:
            line = file.readline()
            if "====" in line:  # 对文章中的异常文字进行处理
                pass
            elif line == "\n":
                pass
            elif "http:" in line:
                pass
            else:
                re_result = re.search("第(\d+)章", line)  # 截取“第几章”数据
                re_need_number = re.split("\D", line)[1]  # 截取章节数目
                if re_result is not None and int(re_need_number) < int(need_number_start):  # 判断本行是否是需要的章节
                    pass
                elif re_result is not None and int(re_need_number) == int(need_number_start):
                    d = 1
                elif re_result is not None and int(re_need_number) > int(need_number_end):
                    d = 2
                else:
                    pass
                if d == 1:
                    line = line.replace("\n", "")  # 输出本行内容
                    long_line = len(line)
                    print("第" + str(c + 1) + "行", long_line, line)
                    c = c + 1
                elif d == 2:
                    break
                else:
                    continue
        file.close()
        print("共计读取%s行" % c)
    elif ".doc" in test_txt_project:
        print("文件格式为word，并非txt")
    else:
        print("\033[31m文件格式不正确，读取出现异常\033[0m")
except IOError:
    raise Exception("\033[31m文件读取过程中出现异常情况，未能正确读取文件\033[0m")
else:
    print("\033[34m读取文件执行完成，执行过程未出现异常情况\033[0m")

TEXT_TYPE = ["line", "paragraph", "chapter", "reel", "book"]
ADDRESS_STRING = ["==", "http:"]


def clean_advertise(text_content=str(), txt_type=str()):
    """
    清除广告内容
    :param text_content: 需要清除的文本
    :param txt_type: 文本的类型是什么，例如：行，段，章......
    :return: 清除后返回的结果
    """
    try:
        txt_type in TEXT_TYPE
    except TypeError:
        raise Exception("指定的文本类型错误")
    else:
        txt_the_state = True
        if txt_type == "line":
            while txt_the_state is True:
                if "==" in text_content:
                    text_content = text_content.replace("==", "")  # 使用正则表达式匹配到==，然后删除
                elif"http:" in text_content:
                    text_content = re.split("http:", text_content)  # 使用正则表达式匹配到网址，然后删除
                elif text_content == "\n":
                    pass
    return True


def judge_correct(check_condition=bool, correct_result=str()):
    """
    检查条件是否成立
    :param check_condition: 需要检查的条件
    :param correct_result: 如果条件成立，则会输出的结果
    :return: 返回输出的结果
    """
    try:
        check_condition is True
    except StopAsyncIteration:
        raise Exception("Condition is not true,please check that the input is correct")
    else:
        return correct_result


def judge_error(check_condition=bool, error_result=str()):
    """
    检查条件是否不成立
    :param check_condition: 需要检查的条件
    :param error_result: 如果条件不成立，则会输出的结果
    :return: 返回输出的结果
    """
    try:
        check_condition is False
    except StopAsyncIteration:
        raise Exception("Condition is not false,please check that the input is error")
    else:
        if error_result is None:
            return False
        else:
            return error_result


#
# def matching_string()
#
# def matching_web_address(text=str()):

# os.system()
# novel = open()

