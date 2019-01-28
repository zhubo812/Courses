# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''
from FileUtil import FileUtil
import os

fu = FileUtil()

fu.getFiles("data")

path = "E:/github/nlpcourse/NlpCourse/data/test.txt"

content = fu.readFile(path, "UTF-8")
print(content)
lines = fu.readlines(path, "UTF-8")
print(lines)
