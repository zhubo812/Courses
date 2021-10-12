## 第二章 语料库与知识图谱

@@@
主要内容  
1. 语料库技术
2. 知识图谱

@@@
### 1 语料库语言学概述

#### 1.1 语料库语言学的定义

- “根据篇章材料对语言的研究称为语料库语言学。”（K.Aijmer & B.Aitenberg, 1991）
- “以语料为语言描写的起点或以语料为验证有关语言的假说的方法称为语料库语言学。”（D. Crystal, 1991）
- “基于现实生活中语言运用的实例进行的语言研究称为语料库语言学”（T.McEnery & A. Wilson, 1996）
~~~~
语料库是存放语言材料的数据库。而语料库语言学则是以语料库为基础的语言研究方法，其包含两层含义：

- 利用语料库对语言的某个方面进行研究，也就是说“语料库语言学”不是一个学科名称，而是一种研究手段。
- 依据语料库所反映出的语言事实对当前的语言学理论进行批判，提出新的观点或理论。

~~~~


#### 1.2 语料库的类型
- 用途：通用语料库、专用语料库；
- 介质：文字语料库、语音语料库；
- 语体：书面语语料库、口语语料库；
- 时间：共时语料库、历时语料库；
- 程度：生语料库、熟语料库；
- 语种：单语语料库、双语语料库（多语语料库）；

- 注：平行语料库（篇章，段落，语句进行对齐处理后的语言库）

~~~~
注：平行语料库（篇章，段落，语句进行对齐处理后的语言库）
~~~~
#### 1.3 语料库语言学的发展

语料库语言学的发展历史，大致可以分为两个阶段：

计算机应用以前，可称为传统语料库时期
计算机应用以后，可称为现代语料库时期
~~~~
##### 传统语料库
- 为词典编纂、语法研究而收集的语料库

例如，牛津英语词典（Oxford English Dictionary），1928年 引证400万条，卡片1100万张；韦伯斯特新国际词典（Webster's New International Dictionary），1961年第三版 新旧引证1000多万条
~~~~
- 为教学目的而编制的书面语料库和词表

例如，陈鹤琴《语体文应用字汇》 商务印书馆 1928年
	两次统计，第一次统计6种教材，包括554,478个汉字的语料，得出不同汉字4261个；第二次使用包含34,818个汉字的语料得出与4261个汉字相异的汉字458个
~~~~
- 为语言调查而收集的方言语料库

19、20世纪，英、美等国都做过大型的方言调查，调查结果形成几个大规模的方言语料库

在我国，运用语料的研究方法可以追溯到周秦，如我国汉语方言学的第一部著作《輶轩使者绝代语释别国方言》简称《方言》是扬雄历经27年完成的。
~~~~
1957年，乔姆斯基的《句法理论》(Syntactic Structures)及其以后的一系列论著的发表，语料库研究的发展被完全否定、受到剧烈震荡。
~~~~
乔姆斯基(Chomsky)认为，语言研究的主要目标是建立一种能够反映说话人心理现实的语言认知模式。……语料从本质上只是外在化的话语的汇集, 基于语料的研究所建立的经验模式充其量只能对语言能力作出部分解释, 因而语料不是语言学家从事语言研究的得力工具。

- 基于语料库的研究方法有误
~~~~
短语结构语法具有递归性：自然语言的句子是无限的，任何有限的语料都不能穷尽语言。
- 语料是不完整、不充分的
~~~~
- 英国伦敦大学学院(University College London )的语言学家夸克（Quirk）开创了新一代的语料库。他在1959年建立英国英语口语和书面语的“英语用法调查”（the Survey of English Usage，简称SEU）语料库的计划，目的是要对英语进行全面的描写。
- 1961年，弗朗西斯（N. Francis）和库塞拉（H. Kucera）为首的一批语言学家和计算机专家汇集在美国的布朗大学合作建成了世界上最早的机读语料库，即布朗语料库（Brown Corpus）。
- 1975年，斯沃特威克（Svartvik）与他在隆德大学的同事把SEU语料库中的口语部分转变为计算机可读的形式，最后建立了“伦敦—隆德英语口语语料库”（LLC）现代语料库
~~~~
现代语料库-第一代语料库（未加分析与标注）
1. 布朗语料库（Brown Corpus）
2. LOB语料库（The Lancaster-Oslo/Bergen Corpus）
3. LLC语料库（London-Lund Corpus of Spoken English）
4. 兰开斯特/IBM英语口语语料库（Lancaster /IBM spoken English corpus)
~~~~
现代语料库-第二代语料库（标注语料库）
1. COBUILD语料库（Collins Birmingham University International Language Database）
2. 英国国家语料库
3. 国际英语语料库
4. 朗文语料库(Longman Corpus Network)
~~~~
第三代语料库——特大型语料库

美国Lexis-Nexis 公司的机储文件已经达到15亿件，有1.5		万亿字符，并且以每周950万件的速度递增
~~~~

- 语料：从单语种到多语种。
- 数量：从百万级到千万级再到亿级和万亿级。
- 加工：从词法级到句法级再到语义和语用级。
- 文本：从抽样到全文。
~~~~
第三代语料库——动态监控语料库

互联网上，英国COBUILD语料库每周向电子邮件用户发送Word Watch（词语监察）的邮件，报告社会用语的动态变化情况
~~~~
第三代语料库——ACL-DCI

- 美国计算语言学学会(The Association for Computational Linguistics, 即ACL)倡议的数据采集计划(Data Collection Initiative, 即DCI)，其宗旨是向非赢利的学术团体提供语料，用标准通用置标语言SGML统一置标，以便于数据交换(Liberman, M.Y. 1990)
~~~~
第三代语料库-[语言资源联盟(Linguistic Data Consortium)](http://www.ldc.upenn.edu)
- 1992年在美国宾夕法尼亚大学(University of Pennsylvania)建立，它的目的是构建、收集和发布用于研发的语音和文本数据库、词典以及其他资源
- 该联盟提供了一种可供大规模发展和普遍的共享用于语言工程技术研究的资源的新机制，目前已经拥有超过100个公司、大学和政府机构会员单位。为197个会员机构和458个非会员机构提供了数据
~~~~
第三代语料库-UPenn树库（宾州树库）
- 由宾夕法尼亚（Pennsylvania）大学计算机系的M. Marcus主持，到1993年完成了近300万词的英语句子的句法结构标注。
- 2000年由LDC（语言数据协会）发行了UPenn的中文树库（规模较小，仅包含10万词，4185句）
~~~~
第三代语料库-ELRA——[欧洲语言资源学会(European Language Resources Association)](http://www.elra.info)
- 1995年在卢森堡成立，开展以语言技术为主的语言资源收集、监测、评估、鉴定、宣传、开发与利用工作，定期召开语言资源与评估国际学术会议(LREC, Language Resources and Evaluation Conference)，出版会刊《语言资源与评估》，力求语言资源建设和评估的科学化
~~~~
第三代语料库——TELRI——[跨欧洲语言资源基础建设学会(Trans-European Language Resources Infrastructure)](http://telri.nytud.hu) 

- 目的是为商业机构、研究团体和大学提供研发平台，为自然语言处理提供单语种和多语种的语言资源
- 主要任务是协调欧洲的多语言信息处理和多语言语料库的建设
- 已建成柏拉图（Plato）的《理想国》（Politeia）多语语料库、计算工具和资源的研究文档TRACTOR（Research Archive of Computational Tools and Resources）、以及欧洲语言词库EUROVOCA
~~~~
第三代语料库（国内）

- 北京语言文化大学还在1992年建成“当代北京口语语料库”，收录80年代北京口语录音（378人）转写语料170万字，其中40万字进行了分词和词性标记；
- 北京语言文化大学1995年完成“现代汉语语法研究语料库”，生语料2000万字，分词和词性标注语料200万字，其中还有部分句法标记；
~~~~
- 北京语言文化大学1995年完成“汉语中介语语料库系统”，从来自96个国家和地区的1635位留学生的5774篇语料中抽取740人的1731篇语料，共44218句，1041274字，语料进行了分词和词性标注及一些特殊的语言学标注；

- 中文语言资源联盟（ChineseLinguistic Data Consortium，缩写为ChineseLDC）——http://www.chineseldc.org/

- 国际中文语言资源联盟（Chinese Corpus Consortium, 缩写为CCC）——http://www.d-ear.com/ccc/index.htm
~~~~
北京语言大学语言BBC
- BCC汉语语料库，总字数约 150 亿字，包括：报刊（20 亿）、文学（30 亿）、微博（30 亿）、科技（30 亿）、综合（10 亿）和古汉语（20 亿）等多领域语料。


@@@

### 2 汉语语料库的数据加工
~~~~
#### 2.1 文本采集与加工
- 文本采集
- 文本加工
~~~~
##### 文本采集
1. 报纸电子版
2. 网络新闻
3. 微博
4. 知乎
5. 豆瓣
6. 电子书

~~~
引入所需模块
```Python
import requests
import bs4
import os
import datetime
import time
import json
import pandas as pd
```
~~~~
获取网页内容
```Python
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
```
~~~~
获取当天报纸的各版面的链接列表
```Python
def getPageList(year, month, day):
	'''
	功能：获取当天报纸的各版面的链接列表
	参数：年，月，日
	'''  
	url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000renmrb_01.htm'
	html = fetchUrl(url)
	bsobj = bs4.BeautifulSoup(html,'html.parser')


	pageList = bsobj.findAll(id="pageLink")
	linkList = []
	
	for page in pageList:
		link = page.get('href')
		url = 'http://paper.people.com.cn/rmrb/html/'  + year + '-' + month + '/' + day + '/' + link
		linkList.append(url)
	
	return linkList
```
~~~~
获取报纸某一版面的文章链接列表
```Python
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
```
~~~~
```Python
解析 HTML 网页，获取新闻的文章内容
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
```
~~~~
抓取指定日期的新闻内容，并存储到指定路径
```Python
def download_rmrb(path,year, month, day):
	pageList = getPageList(year, month, day)
	print(pageList)
	for page in pageList:
		titleList = getTitleList(year, month, day, page)
		for url in titleList:
			html = fetchUrl(url)
			content = getContent(html)
			#print(content)
			temp = url.split('_')[2].split('.')[0].split('-')
			pageNo = temp[1]
			titleNo = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
			newsid = year + month + day + '-' + pageNo + '-' + titleNo
			date = year +'-'+ month+'-' + day
			newsid= newsid

			filePath= path+str(newsid)
			print(content)
			writer = open(filePath,"w",encoding="utf-8")
			writer.write(content)
			writer.close()
```
~~~~
入口函数
```Python
if __name__ == '__main__':
	path = "data/"
	datelist=['2020-12-12','2020-12-13']
	for datestr in datelist:
		dateArray= datestr.split("-")
		year=dateArray[0]
		month=dateArray[1]
		day=dateArray[2]
		download_rmrb(path,year,month,day)
```
~~~~
#### 2.2 元信息标注
#### 2.3 数据存储
@@@
### 3 语料库基本功能及实现
#### 3.1 语料库检索
#### 3.2 词表及其生成
#### 3.3 主题词表及其生成
#### 3.4 语料库常用统计方法
@@@


### 4 基于语料库的研究：案例分析

#### 4.1　词汇分析
4.1.1　基于语料库的词块分析
#### 4.2　句法结构及类联接研究
4.2.1　基于语料库的句法结构分析
4.2.2　类联接扩展及研究
#### 4.3　话语研究

4.3.1　话语与话语特征
4.3.2　语料库在话语研究中的应用
@@@
### 5 知识图谱简介

#### WordNet
#### HowNet
#### FrameNet
