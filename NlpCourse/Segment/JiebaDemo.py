# -*- coding:utf-8 -*-
'''
Created on Jan 29, 2019

@author: Jackie
'''

import jieba
import jieba.posseg as pseg

words = jieba.cut("我来到北京清华大学",cut_all=True)

for word in words:
	print(word)

words = pseg.cut("我爱北京天安门")
for word, flag in words:
	print('%s %s' % (word, flag))



	