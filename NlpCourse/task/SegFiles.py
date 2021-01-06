import os
import jieba
import jieba.posseg as pseg

def getSentences(line):
	sentences =[]
	sentenceSpliter=["。","？","?","！","!","……"]
	# print(line)
	start=0

	for index in range(len(line)):
		char = line[index]
		if(char in sentenceSpliter):
			sen = line[start:index+1]
			sentences.append(sen)
			start = index+1
		if(index == len(line)-1 and start < index):
			sen = line[start:]
			sentences.append(sen)
	return sentences

def counter(counterDic, item):

	if(item in counterDic):
		freq = counterDic[item]
		freq = freq +1
		counterDic[item]= freq
	else:
		counterDic[item]=1

wordDict={}
natureDict={}
sentenceDict={}

path ="/Users/Jackie/Downloads/2019新闻联播/"
filenames= os.listdir(path)#获取path下所有文件名
# fielpaths = []
for filename in filenames:
	# fielpaths.append(path+file)
	filepath = path + filename#获取每个文本的路径
	print(filepath)
	file = open(filepath, 'r',encoding="utf-8")#读取每个文本
	lines = file.readlines()#读取每个文本的所有行返回列表，统计篇章级
	# text = file.read()
	# textLen= len(text)

	for line in lines:#循环所有行
		line= line.strip()#删除每一行首位空格
		if(len(line)==0):
			continue # 如果line长度为零（空行）直接跳过
		sentences = getSentences(line)# 对每一行文本进行断句
		for sen in sentences:# 循环每一句内容，统计句子级
			#句子长度统计
			senLen = len(sen)
			counter(sentenceDict, senLen)
			seg_list = pseg.cut(sen)
			for word, nature in seg_list:#循环每一个切分好的词,统计词
				counter(wordDict,word)
				counter(natureDict,nature)

	# 		break	
		# break
	# break
# print(sentenceDict)
# print(natureDict)

# for x in natureDict:
# 	print(str(x)+"\t"+str(natureDict[x]))
# 	