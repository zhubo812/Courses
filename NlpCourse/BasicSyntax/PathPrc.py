# -*- coding:utf-8 -*-
'''
Created on Jan 29, 2019

@author: Jackie
'''
import os


print("===========1 获取当前文件所在目录.===========")
path = os.path.abspath('.')
print(path)


print("===========1 获取当前文件上级目录.===========")
path = os.path.abspath('..')
print(path)