
import jieba
import jieba.posseg as pseg
from Segment.Counter import *

jieba.load_userdict('usr.dic')#载入用户词典

# 1. 读取数据（*.txt,需要提取有效数据）
# 2. 循环每一行数据，进行分词
# 3. 构建NGram
# 4. 统计NGram的频次


def getContent(path):
	file = open(path, 'r', encoding='utf-8')
	lines = []
	for line in file.readlines():
		text = line.strip.split('\t')[4]
		lines.append(text)
	return lines

def doSegmentation(lines):
	seglist = []
	for line in lines:
		words = jieba.cut(line,cut_all=False)
		sline = ' '.join(words)
		seglist.append(sline)
	return seglist

def getNGrams(wordlist, n):
    return [ wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

def doGetNG(seglist,n):
	ngramlist = []
	for line in seglist:
		words = line.strip.split()
		nlist = getNGrams(words,n)
		for ng in nlist:
			ngramlist.append(ng)
	return ngramlist

def NGramCounter(ngramlist):
	counter = Counter()#实例化对象
	for item in ngramlist:
		counter.add(item)
	counter.sort()
	print(counter.worddic)


if __name__ == '__main__':
	path = 'ahmw.txt'
	lines = getContent(path)
	lines = doSegmentation(lines)
	ngramlist = doGetNG(line, 2)
	NGramCounter(ngramlist)

