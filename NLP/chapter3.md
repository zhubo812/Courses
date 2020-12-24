## 第三章 自动分词标注

### 主要内容
1. 汉语自动分词方法
2. 词性标注方法
3. 命名实体识别
4. 新词识别

### 汉语自动分词方法
1. 最大匹配
2. N-最短路径方法
3. 基于词的n元语法模型的分词方法
4. 由字构词的汉语分词方法
5. 基于词感知机算法的汉语分词方法
6. 其他分词方法


### 最大匹配

```
# -*- coding:utf-8 -*-
#!/usr/bin/python3


def load_Dictionary():
    dic={}
    path = "/Users/Jackie/Desktop/usr.dic"
    file = open(path,"r",encoding="UTF-8")
    for line in file:
        array = line.strip().split(" ")
        print(array)
        attr ={}
        attr["natrue"]=array[2]
        attr["freq"]= array[1]
        word = array[0]
        dic[word]=attr
    print(dic)
    return dic

#sline是要切分的字符串
def FMM(wordDict, sline):
    maxLen=3
    wordList = []#用作存储已切分的词
    slineLen = len(sline)#待切分字符串的长度
    while slineLen > 0:#待切分字符串长度大于0
        if (slineLen > maxLen):
            wordLen = maxLen
        else:
            wordLen = slineLen
        subStr = sline[0:wordLen]
        while wordLen > 1:#截取的字符串长度大于1
            if (subStr in wordDict):
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[0:wordLen]
        wordList.append(subStr)
        print(subStr)
        sline = sline[wordLen:]
        slineLen = slineLen - wordLen

    print(wordList)
    return wordList


def RMM(wordDict, sline):
    maxLen=3
    wordList = []#用作存储已切分的词
    slineLen = len(sline)#待切分字符串的长度
    while slineLen > 0:#待切分字符串长度大于0
        if (slineLen > maxLen):
            wordLen = maxLen
        else:
            wordLen = slineLen
        subStr = sline[slineLen-wordLen:]
        while wordLen > 1:#截取的字符串长度大于1
            if (subStr in wordDict):
                break
            else:
                wordLen = wordLen - 1
                subStr = subStr[1:]
        wordList.append(subStr)
        print(subStr)
        sline = sline[0:slineLen-wordLen]
        slineLen = slineLen - wordLen
    wordList.reverse()
    # print(wordList)
    return wordList

def tag(wordDict, wordList):
    wlist =[]
    for word in wordList:
        if( word in wordDict):
            value = wordDict[word]
            natrue = value["natrue"]
            wlist.append("%s/%s"%(word,natrue))
        else:
            natrue= "x"
            wlist.append("%s/%s"%(word,natrue))
    return wlist

#入口函数
if __name__ == '__main__':
    #HelloWorld()
    usrdic= load_Dictionary()
    # print(usrdic)
    line = "今天天气不错"
    # FMM(usrdic,line)
    wordList =RMM(usrdic,line)

    wordList = tag(usrdic,wordList)
    resultLine = " ".join(wordList)
    print(resultLine)
```

### jieba分词系统

### pynlpir分词系统

### 其他中文分词系统
SnowNLP
THULAC
pkuseg
pyhanlp
FoolNLTK
pyltp
Stanford CoreNLP
### 其他语言分词系统

1. MeCab
2. paoding

### 2. 词性标注方法



### 3. 命名实体识别

### 4. 新词识别