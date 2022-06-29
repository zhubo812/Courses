
import jieba
import jieba.posseg as pseg
from Counter import *

jieba.load_userdict('usr.dic')#载入用户词典

# 1. 读取数据（*.txt,需要提取有效数据）
# 2. 循环每一行数据，进行分词
# 3. 构建NGram
# 4. 统计NGram的频次

# debug 流程
# 1. 查验错误信息, **ERROR:,Line Number
# 2. 设置断点，可以在错误行前一行设置
# 3. 检查变量值及类型
# 4. 单步调试，F7/F8,检查每一行代码涉及的变量值是否正确

# IDE的使用
# 1. 常用按钮的功能
# 2. 常用快捷键
# 3. input keywords into search en (pycharm 单步调试)


def getContent(path):
	file = open(path, 'r', encoding='utf-8')
	lines = []
	for line in file.readlines():
		
		text = line.strip().split('\t')[5]
		# print(text)
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
		words = line.strip().split()
		nlist = getNGrams(words,n)
		for ng in nlist:
			ngramlist.append('\\'.join(ng))
	return ngramlist

def NGramCounter(ngramlist):
	counter = Counter()#实例化对象
	for item in ngramlist:
		# print(item)
		counter.add(item)
	return counter.sort()


if __name__ == '__main__':
	# path = 'ahmw.txt'
	# lines = getContent(path)# 获取每一行数据
	# lines = doSegmentation(lines)#对每一行数据进行切分
	# ngramlist = doGetNG(lines, 2)
	# result = NGramCounter(ngramlist)
	# print(type(result))
	# for k, v in result.items():
	# 	print(k,v)
	items = ['a', 'b', 'c', 'a']

	counter = Counter()
	rs = counter.addwordlist(items)
	for k, v in rs.items():
		print(k,v)

