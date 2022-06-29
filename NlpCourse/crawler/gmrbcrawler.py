import requests
import bs4
import os
import datetime
import time
import json
import mysql.connector


def getMySQL():
	mydb = mysql.connector.connect(
  	host="192.168.1.107",
  	user="root",
  	passwd="admin",
  	database="test"
	)
	return mydb


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
	url = 'http://epaper.gmw.cn/gmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000gmrb_01.htm'
	html = fetchUrl(url)
	bsobj = bs4.BeautifulSoup(html,'html.parser')# 使用bs4解析页面内容


	pageList = bsobj.findAll(id="pageLink")#查找所有的pageLink
	linkList = []
	
	#拼接版面连接
	for page in pageList:
		link = page.get('href')
		link = link.replace('./','')
		url = 'http://epaper.gmw.cn/gmrb/html/'  + year + '-' + month + '/' + day + '/' + link
		linkList.append(url)
	
	return linkList


def getTitleList(year, month, day, pageUrl):
	'''
	功能：获取报纸某一版面的文章链接列表
	参数：年，月，日，该版面的链接
	'''
	html = fetchUrl(pageUrl)
	bsobj = bs4.BeautifulSoup(html,'html.parser')

	titleList = bsobj.find('div', attrs = {'class': 'l_c'}).ul.find_all('li')
	
	# print('titleList:',len(titleList))
	linkList = []
	
	for title in titleList:
		tempList = title.find_all('a')
		for temp in tempList:
			link = temp["href"]
			if 'nw.D110000gmrb' in link:
				url = 'http://epaper.gmw.cn/gmrb/html/'  + year + '-' + month + '/' + day + '/' + link
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
		content += p.text.strip() + '\n'	  
	#print(content)
	
	# 返回结果 标题+内容
	resp = title + content
	return resp


def download_gmrb(path,year, month, day):
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

def download_gmrb2MySQL(path,year, month, day):
	mydb = getMySQL()
	mycursor = mydb.cursor()
	pageList = getPageList(year, month, day)# 抓取版面数据链接
	print(pageList)
	for page in pageList:#循环每个版面链接
		titleList = getTitleList(year, month, day, page)#获取一个版面所有文章的链接
		for url in titleList:#循环文章链接
			html = fetchUrl(url)
			content = getContent(html).replace('\u2003',' ').replace('\xa0','').replace('\n\n','\n')#获取文章内容
			#print(content)
			temp = url.split('_')[2].split('.')[0].split('-')
			pageNo = temp[1]
			titleNo = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
			newsid = year + month + day +  pageNo  + titleNo

			date = year +'-'+ month+'-' + day
			newsid = int(newsid)
			print(type(newsid))
			print(content)
			# filePath= path+str(newsid)
			# # print(content)
			# writer = open(filePath,"w",encoding="utf-8")
			# writer.write(content)
			# writer.close()
			source = '光明日报'
			sql = "INSERT INTO paper (newsid, source, text) VALUES (%d, \"%s\", \"%s\")" % (newsid,source,content)
			# sql = 'INSERT INTO paper (newsid) VALUES（11）'
			#paper为表名，newsid为插入数据的字段
			print(sql)
			
			mycursor.execute(sql)
			 
			mydb.commit()    # 数据表内容有更新，必须使用到该语句
	mydb.close()

def download_gmrb2MySQLMany(path,year, month, day):
	mydb = getMySQL()
	mycursor = mydb.cursor(prepared=True)
	pageList = getPageList(year, month, day)# 抓取版面数据链接
	# print(pageList)
	valueList = []# 存放新闻数据的列表
	for page in pageList:#循环每个版面链接
		titleList = getTitleList(year, month, day, page)#获取一个版面所有文章的链接
		for url in titleList:#循环文章链接
			html = fetchUrl(url)
			content = getContent(html).replace('\u2003',' ').replace('\xa0','').replace('\n\n','\n')#获取文章内容
			#print(content)
			temp = url.split('_')[2].split('.')[0].split('-')
			pageNo = temp[1]
			titleNo = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
			newsid = year + month + day +  pageNo  + titleNo

			date = year +'-'+ month+'-' + day
			newsid = int(newsid)
			# print(type(newsid))
			# print(content)
			# filePath= path+str(newsid)
			# # print(content)
			# writer = open(filePath,"w",encoding="utf-8")
			# writer.write(content)
			# writer.close()
			source = '光明日报'
			value = (newsid,source, content[0:10])
			# value = (newsid,source)
			# print(value)
			# print(type(value))
			valueList.append(value)
			# break
		break
	sql = 'INSERT INTO paper (newsid, source, text) VALUES (%d, %s, %s)'
	# sql = "INSERT INTO paper (newsid, source) VALUES (%d, %s)"
	# sql = 'INSERT INTO paper (newsid) VALUES（11）'
	#paper为表名，newsid为插入数据的字段
	print(sql)
	print(valueList)
	mycursor.executemany(sql,valueList)
			 
	mydb.commit()    # 数据表内容有更新，必须使用到该语句
	mydb.close()


if __name__ == '__main__':
	path = "data/"
	datelist=['2022-03-21','2022-03-22']
	for datestr in datelist:
		dateArray= datestr.split("-")
		year=dateArray[0]
		month=dateArray[1]
		day=dateArray[2]
		download_gmrb2MySQLMany(path,year,month,day)

# year = '2022'
# month = '04'
# day = '22'

# pagelist = getPageList(year='2022',month='04',day='22')

# for item in pagelist:
# 	#获取每一个版面的文章链接
# 	articleList = getTitleList(year='2022',month='04',day='22',pageUrl= item)
# 	for artiLink in articleList:
# 		html = fetchUrl(artiLink)
# 		content = getContent(html)
# 		writer = open('data/gmrb.txt','w',encoding='utf-8')
# 		# print(content)
# 		writer.write(content)
# 		writer.close()
# 		break
# 	break

