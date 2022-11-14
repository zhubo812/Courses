# -*- coding:utf-8 -*-
'''
Created on 2020年2月15日

@author: Jackie
'''
import requests
from lxml import etree#xpath
import os


inirul = "https://www.bilibili.com/video/av86991001?p="
pid = 141##配置视频pid

pidstr = str(pid)
link = inirul+pidstr
print(link)
## 配置视频存储路径path
os.system('you-get -o {path} {url}'.format(path="D:/NLP",url=link))#使用os操作有个you-get


