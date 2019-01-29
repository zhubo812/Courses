# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''
from FileUtil import FileUtil
import os

fu = FileUtil()

filelist = fu.getFiles("data/sports")
print(filelist)
path = os.path.abspath('..')

path = path+"/data/test.txt"
print(path)

content = fu.readFile(path, "UTF-8")
print(content)
lines = fu.readlines(path, "UTF-8")
print(lines)
