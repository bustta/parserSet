#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kenny.tsai
# @Date:   2014-10-08 11:51:15
# @Last Modified by:   tsaihung-ju
# @Last Modified time: 2014-10-23 21:58:15


# src: http://bbs.591.com.tw/sitemap.xml

from bs4 import BeautifulSoup
import logging
import os
import requests


logging.basicConfig(
    filename=os.path.join(os.getcwd(), "log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s", filemode="w")

soup = BeautifulSoup(requests.get("http://bbs.591.com.tw/sitemap.xml").text)
items = soup.find_all("url")
# for itemIndex in range(len(items)):
# 	itemUrl = "{0}: {1}".format(itemIndex, items[itemIndex].loc.string)

request_url = items[0].loc.string
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent": user_agent}


itemGetHtml = requests.get(request_url, headers=headers).text
logging.info("Page: {0}".format(request_url))

parsed_html = BeautifulSoup(itemGetHtml)
logging.info(parsed_html)
max_photo_div = parsed_html.find(id="maxphoto")
big_pics_container = max_photo_div.textarea
pics = big_pics_container.find_all("img")

# print type(pics)

print "\n".join(set(pic['src'] for pic in pics))
# for index_each_pic in range(len(pics)):
#   img = "[{0}]: {1}\n".format(index_each_pic, pics[index_each_pic])
#   print img
#   logging.info(img)
