
# -*- coding: utf-8 -*-
# @Author: kenny.tsai
# @Date:   2014-10-06 10:08:34
# @Last Modified by:   bustta
# @Last Modified time: 2014-10-23 22:28:27
import feedparser
import time
import logging
import os

logging.basicConfig(
    filename=os.path.join(os.getcwd(), "log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    filemode="w")

d = feedparser.parse("http://world.yam.com/rss.php")
all_items = d['items']
# print e['title_detail']['value']
for item in range(len(all_items)):
    # Mon, 06 Oct 2014 16:45:39 +0800
    time_obj = time.strptime(
        all_items[item]['published'],
        "%a, %d %b %Y %H:%M:%S +0800")
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
    summary = all_items[item]['summary'].replace(u"&nbsp;", "").rstrip()
    index_and_time = "[{0}] @ {1}\n".format(item, time_string)
    title_line = "\t -- [Title]: {0}\n".format(
        all_items[item]['title'].encode('utf-8'))
    summary_line = "\t -- [Summary]: {0}".format(summary.encode('utf-8'))
    output_string = index_and_time + title_line + summary_line
    logging.info(output_string)
    print output_string
