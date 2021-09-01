#!usr/bin/python
# -*- coding:UTF-8 -*-

import requests
from lxml import etree
from bs4 import BeautifulSoup


# class SpiderExercise:
#
#     def __init__(self):

# 获取网址
url = "https://www.biqooge.com/8_8539/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/86.0.4240.198 Safari/537.36", "Host": "www.biqooge.com"}

# 发送请求
response = requests.get(url, headers=headers)

# 获取网站编码格式
code = response.apparent_encoding
print(code)

# 设置网页格式
response.encoding = "gbk"

# 将页面信息转化为dom格式
content_text = response.text
dom = etree.HTML(content_text)

# 根据xpath信息定位
list_dom = dom.xpath("//*[@id=\"list\"]/dl/dd[10]/a/text()")

# 打印定位的元素信息
print(list_dom)

# 获取并进入第一章的链接
first_href = dom.xpath("//*[@id=\"list\"]/dl/dd[10]/a/@href")
new_url = "https://www.biqooge.com/" + str(first_href[0])
response = requests.get(new_url, headers=headers)
code = response.apparent_encoding
print(code)
response.encoding = "gbk"
content_text = response.text
# print(content_text)
dom = etree.HTML(content_text)
list_dom_0 = dom.xpath("//*[@id=\"content\"]/text()[1]")
# soup = BeautifulSoup(content_text, "lxml")
# list_dom_0 = soup.find_all("div", id_="content")
print(len(list_dom_0))
print(list_dom_0)

# 将抓取的内容写入文件
with open("novel_spider.txt", "w") as file:
    for i in list_dom_0:
        list_line = "".join(i.split())
        file.write(list_line)
    # file.writelines(list_dom_0)

