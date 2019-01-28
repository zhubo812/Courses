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
