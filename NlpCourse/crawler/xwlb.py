# Copy input to output
import requests
import bs4
import os
import datetime
import time
import json
import pandas as pd


newsidList=[]
datesList=[]
contentList=[]  

def fetchUrl(url):
	'''
	功能：访问 url 的网页，获取网页内容并返回
	参数：目标网页的 url
	返回：目标网页的 html 内容
	'''
	
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}
	
	r = requests.get(url,headers=headers)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	return r.text


def getPageLink(num):
	iniUrl = "http://xwlbo.com/"
	pageend= "txt.html"
	#http://xwlbo.com/txt_12.html
	links = []
	inilink = iniUrl+pageend
	links.append(inilink)

	for i in range(2,num):
		link = iniUrl+"txt_"+str(i)+".html"
		links.append(link)
	return links

def getLinks(pageUrl):
	html = fetchUrl(pageUrl)
	print(html)
	bsobj = bs4.BeautifulSoup(html,'html.parser')
	links = bsobj.find('ol', attrs = {'class': 'xwlist'}).ul.find_all('a')
	linkList = []
	print(links)

getLinks("http://xwlbo.com/txt_6.html")



