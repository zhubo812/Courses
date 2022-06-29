
import requests
import bs4
import os
import datetime
import time
import json
# import pandas as pd




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

def getPageList(year, month, day):
	'''
	功能：获取当天报纸的各版面的链接列表
	参数：年，月，日
	'''  
	url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000renmrb_01.htm'
	html = fetchUrl(url)
	bsobj = bs4.BeautifulSoup(html,'html.parser')# 使用bs4解析页面内容


	pageList = bsobj.findAll(id="pageLink")#查找所有的pageLink
	linkList = []
	
	#拼接版面连接
	for page in pageList:
		link = page.get('href')
		link = link.replace('./','')
		url = 'http://paper.people.com.cn/rmrb/html/'  + year + '-' + month + '/' + day + '/' + link
		linkList.append(url)
	
	return linkList

def getTitleList(year, month, day, pageUrl):
	'''
	功能：获取报纸某一版面的文章链接列表
	参数：年，月，日，该版面的链接
	'''
	html = fetchUrl(pageUrl)
	bsobj = bs4.BeautifulSoup(html,'html.parser')

	titleList = bsobj.find('div', attrs = {'class': 'news'}).ul.find_all('li')
	linkList = []
	
	for title in titleList:
		tempList = title.find_all('a')
		for temp in tempList:
			link = temp["href"]
			if 'nw.D110000renmrb' in link:
				url = 'http://paper.people.com.cn/rmrb/html/'  + year + '-' + month + '/' + day + '/' + link
				linkList.append(url)
	
	return linkList

def getContent(html):
	'''
	功能：解析 HTML 网页，获取新闻的文章内容
	参数：html 网页内容
	'''	
	bsobj = bs4.BeautifulSoup(html,'html.parser')
	
	# 获取文章 标题
	title = bsobj.h3.text + '\n' + bsobj.h1.text + '\n' + bsobj.h2.text + '\n'
	#print(title)
	
	# 获取文章 内容
	pList = bsobj.find('div', attrs = {'id': 'ozoom'}).find_all('p')
	content = ''
	for p in pList:
		content += p.text + '\n'	  
	#print(content)
	
	# 返回结果 标题+内容
	resp = title + content
	return resp

def download_rmrb(path,year, month, day):
	pageList = getPageList(year, month, day)# 抓取版面数据链接
	print(pageList)
	for page in pageList:#循环每个版面链接
		titleList = getTitleList(year, month, day, page)#获取一个版面所有文章的链接
		for url in titleList:#循环文章链接
			html = fetchUrl(url)
			content = getContent(html)#获取文章内容
			#print(content)
			temp = url.split('_')[2].split('.')[0].split('-')
			pageNo = temp[1]
			titleNo = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
			newsid = year + month + day + '-' + pageNo + '-' + titleNo
			date = year +'-'+ month+'-' + day
			newsid= newsid

			filePath= path+str(newsid)
			# print(content)
			writer = open(filePath,"w",encoding="utf-8")
			writer.write(content)
			writer.close()





if __name__ == '__main__':
	path = "data/"
	datelist=['2022-04-14','2022-04-15']
	for datestr in datelist:
		dateArray= datestr.split("-")
		year=dateArray[0]
		month=dateArray[1]
		day=dateArray[2]
		download_rmrb(path,year,month,day)


# url = 'http://paper.people.com.cn/rmrb/html/2022-04/11/nw.D110000renmrb_20220411_1-01.htm'
# htmlText = fetchUrl(url)

# pagelist = getPageList('2022','04','15')
# pagelink = 'http://paper.people.com.cn/rmrb/html/2022-04/15/nbs.D110000renmrb_20.htm'
# titlelist = getTitleList('2022','04','15',pagelink)


# artlink = 'http://paper.people.com.cn/rmrb/html/2022-04/15/nw.D110000renmrb_20220415_3-20.htm'
# html = fetchUrl(artlink)
# content = getContent(html)
# print(content)