# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''

# 1.断句
# 2.记录频次 

class TextUtil(object):
    def __init__(self):
        '''
        Constructor
        '''
    
    
    def toSentenceList(self,line):
        sline=""
        sentences = []
        for i in range(0,len(line)):
            if (len(sline) == 0 and (line[i].isspace() or line[i] == ' ')):
                continue
            sline = sline+line[i]
            if(line[i] =="."):
                if (i < len(line) - 1 and line[i + 1].isdigit() is False) :
                    sentences.append(sline)
                    sline=""
            elif(line[i] == "…"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "\t"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "。"):
                sentences.append(sline)
                sline=""
            elif(line[i] == ";"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "；"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "!"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "！"):
                sentences.append(sline)
                sline=""
            elif(line[i] ==  "?"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "？"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "、"):
                sentences.append(sline)
                sline=""
            elif(line[i] == " "):
                sentences.append(sline)
                sline=""
            elif(line[i] == "\n"):
                sentences.append(sline)
                sline=""
            elif(line[i] == "\r"):
                sentences.append(sline)
                sline=""
                
        if(len(sline)>0):
            sentences.append(sline)
            sline=""
        return sentences
        
    def counter(counterDic, item):
        if(item in counterDic):
            freq = counterDic[item]
            freq = freq +1
            counterDic[item]= freq
        else:
            counterDic[item]=1 
         
         
    def isPunctuation(word):
        punctuations=["。","？","?","！","!","……",",","，","、","（","）"]
        if(word in punctuations):
            return True
        return False

    def isNum(numlist,word):
        if(word.isdigit()):
            return True
        if(isAlChnNum(numlist, word)):
            return True
        return False

    def isAlChnNum(numlist,word):
        for char in word:
            if(char not in numlist):
                return False
        return True

    def isStopWord(stoplist,word):
        if(word in stoplist):
            return True
        return False
         
         
         
         
            