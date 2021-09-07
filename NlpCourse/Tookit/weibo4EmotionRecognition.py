#!/usr/bin/python3

import xmltodict
import json
import pymongo

def xml2Json(xml_PAHT):
	xml_file = open(xml_PAHT,'r',encoding='utf-8')
	xml_str = xml_file.read()
	json= xmltodict.parse(xml_str)
	return json
	

filelist = ['微博情绪样例数据V5-13.xml','微博情绪标注语料.xml']

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://corpus.bhu.edu.cn:9100/")
mydb = myclient["weibo"]
mycol = mydb["EmotionRecognition"]


for filename in filelist:
	xml_PAHT=filename
	print(xml_PAHT)
	jsonobj=xml2Json(xml_PAHT)

	weibo = jsonobj["TestingData"]['weibo']
	for item in weibo:
		data= json.dumps(item)
		data = data.replace("@","")
		data = data.replace("#text","text")
		jsd = json.loads(data)
		mycol.insert_one(jsd)
	# 	print(data)
	# break

