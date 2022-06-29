# -*- coding:utf-8 -*-
'''
Created on Jan 29, 2019

@author: Jackie
'''
import jieba
import jieba.posseg as pseg
import FMM
from Counter import *

jieba.load_userdict('usr.dic')#载入用户词典
counter = {}
fmmdic = FMM.load_Dictionary()
print(fmmdic)
# words = jieba.cut("我来到渤海大学",cut_all=False)

# def printer(word):
# 	print(word)
# 	print(word)
# for word in words:
# 	print(word)
	# printer(word)

# words = pseg.cut("我来到渤海大学")
# for word, nature in words:
# 	print('%s %s' % (word, nature))

def segment(sline):
	words = pseg.cut(sline)
	return words
def segmentWithFMM(sline):
	words = FMM.FMM(fmmdic,sline)
	return words

def add(word):
	if word in counter:
		freq = counter[word]
		freq = freq +1
		counter[word]= freq
	else:
		counter[word]= 1

def checkWordCounter():
	res = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}

	for k, v in res.items():
		print(k,v)




def ngram(wordlist,n):
	ngramlist =[]
	for i in range(len(wordlist)-(n-1)):
		ngramlist.append(''.join(wordlist[i:i+n]))
	return ngramlist


if __name__ == '__main__':
	# file = open('ahmw.txt','r',encoding='utf-8')
	# lines = file.readlines()

	# counter = Counter()#实例化对象

	# for line in lines:
	# 	text = line.strip().split('\t')[5]
	# 	words = segmentWithFMM(text)
	# 	for word in words:
	# 	# words = segment(text)
	# 	# for word,nature in words:
	# 		# add(word)
	# 		counter.add(word)
	# # checkWordCounter()
	# counter.sort()

	wordlist = ['1','2','3','4','5','6']
	# print(wordlist[0:2])
	n= 4# means n in ngram
	# for i in range(len(wordlist)-(n-1)):
	# 	print(wordlist[i:i+n])
	print(ngram(wordlist, n))