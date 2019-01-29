# -*- coding:utf-8 -*-
'''
Created on Jan 29, 2019

@author: Jackie
'''
from FileUtil import FileUtil
from NlpTookit.NlpTookit import NlpTookit
import jieba
import jieba.posseg as pseg

dir ="data/sports"
fu = FileUtil()
nt = NlpTookit()
wordcounter={}#统计词频的词典
poscounter={}#统计词性的词典
lengthCounter ={}#统计词长、句长分布字典
#step one: get all files' absolute paths
filelist = fu.getFiles(dir)

#step two: read every file
for filepath in filelist:
    print(filepath)
    lines = fu.readlines(filepath, "UTF-8")
    for line in lines:
        if(len(line.strip())==0):
            continue
        #step three:split sentences
#         print(line.strip())
        sentences = nt.toSentenceList(line.strip())
        for sentence in sentences:
            print(sentence)
            length = len(sentence)
            words = pseg.cut(sentence.strip())
#             print(" ".join(words))
            for word, flag in words:
                if(word in wordcounter):
                    wordcounter[word]= wordcounter[word]+1
                else:
                    wordcounter[word]=1
                if(flag in poscounter):
                    poscounter[flag] = poscounter[flag]+1
                else:
                    poscounter[flag]=1

print(wordcounter)
print(poscounter)

lengthCounter ={}
for key in wordcounter:
    length = len(key)
    if(length in lengthCounter):
        lengthCounter[length]= lengthCounter[length]+1
    else:
        lengthCounter[length]=1
print(lengthCounter)



