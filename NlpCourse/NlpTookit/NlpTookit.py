# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''



class NlpTookit(object):
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
        
         
         
         
         
         
         
         
         
            