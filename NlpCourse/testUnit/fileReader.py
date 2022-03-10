import os
import requests
import bs4
import datetime
import time
#文件内容为分好词且无词性标记
# wordlist = open('text.txt', 'r',encoding='utf-8').read().split()

# print(wordlist)

#文件内容为分好词且无词性标记
# wordlist=[]
# file = open('text.txt', 'r',encoding='utf-8')
# for line in file:
# 	# print(line)
# 	for word in line.split():
# 		wordlist.append(word)
# print(wordlist)

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


def getFiles(direc):#首先要获取到指定文件夹(dir)内所有文本的路径
	filelist=[]
	filenames = os.listdir(direc)#相对路径
	for filename in filenames:
		filepath = direc+'/' + filename
		filelist.append(filepath)
	return filelist


def getAllFiles(file_path):#
    os.chdir(file_path)
    # print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(getAllFiles(file_path+'\\'+f))
            os.chdir(file_path)
        else:
            files.append(file_path+'\\'+f)
    return files

wordlist=[]
worddic = {}
filelist = getAllFiles('E:/temp/2/sogoulex/自然科学')
# print(filelist)
counter = 0
for path in filelist:
	print(path)
	file = open(path, encoding='utf-8')
	# print(file.)
	
	
	lines = file.readlines()
	for line in lines:
		# print(line)
		if(len(line.strip())==3):
			print(line)
	if counter == 5:
			break
	counter= counter+1


html= fetchUrl('https://baike.baidu.com/item/乙胺嗪')
bsobj = bs4.BeautifulSoup(html,'html.parser')
pageList = bsobj.find('div', attrs = {'class': 'para'})
print(pageList)
# for filePath in filelist:
# 	singlewordlist = open(filePath, 'r',encoding='utf-8').read().split()
# 	for word in singlewordlist:
# 		wordlist.append(word)
# for filePath in filelist:
# 	file = open(filePath,'r',encoding='utf-8')
# 	for line in file:
# 		for word in line.split():
# 			# wordlist.append(word)
# 			if word in worddic:
# 				worddic[word]= worddic[word]+1
# 			else:
# 				worddic[word]=1

# print(worddic)

# print(len(worddic))