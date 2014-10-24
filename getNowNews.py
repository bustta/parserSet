#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kenny.tsai
# @Date:   2014-10-22 16:29:48
# @Last Modified by:   kenny.tsai
# @Last Modified time: 2014-10-24 15:00:40
import requests
import re
from bs4 import BeautifulSoup


request_url = "http://www.nownews.com/n/2014/10/22/1469749"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent": user_agent}
itemGetHtml = requests.get(request_url, headers=headers).text
plainHtml = itemGetHtml.encode('utf-8')
# print plainHtml

soup = BeautifulSoup(plainHtml)
title = soup.title.string.encode('utf-8')

story_content = soup.find_all("div", "story_content")
writer = story_content[0].a.text.encode('utf-8')

content_list = story_content[0].find_all("p")

real_story_content = ""
for index in range(len(content_list)):
    if index == 0:
        continue
    # print content_list[index]
    item = content_list[index].encode('utf-8')
    match = re.search("bzkeyword", item)
    if not match:
        real_story_content += content_list[index].text.encode('utf-8') + "\r\n"


print "Title: {0}\n".format(title)
print "Author: {0}\n".format(writer)
print "Content: {0}\n".format(real_story_content)
