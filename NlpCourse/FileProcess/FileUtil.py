# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''
import os
import os.path

class FileUtil(object):

    def __init__(self):
        '''
        Constructor
        '''
    def readFile(self,path,encoding):
        file = open(path, 'r',encoding=encoding)
        content = file.read()
        file.close()
        return content
    
    def readlines(self,path,encoding):
        lines = []
        file = open(path, 'r',encoding=encoding)
        for line in file:
            lines.append(line)
        file.close()
        return lines
    
    def getFiles(self,dir):
        pathList =[]
        path = os.path.abspath('..')+"/"+dir+"/"
#         print(path)
        for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#             for dirname in  dirnames:                       #输出文件夹信息
#                 print(  "dirname is" + dirname)
#             print(filenames)
            for filename in filenames:
                pathList.append(path+filename)
        return pathList
    
    
    
    