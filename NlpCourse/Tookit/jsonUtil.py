#!/usr/bin/python3
 
import json


with open('jsonfile.txt', 'r') as f:
	line = f.readline()#读取文本的一行数据
	print(line)
	data = json.loads(line)#转换成Pyhotn字典
	a = data['a']#按照字典获取某个Key的Value
	print(a)