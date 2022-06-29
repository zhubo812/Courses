# coding:utf-8  
 
import jieba  
import jieba.posseg as pseg  
import os  
import sys  
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  


# def getFiles2(dir):
#     pathList =[]
#     path = os.path.abspath('..')+"/"+dir+"/"
# #         print(path)
#     for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
# #             for dirname in  dirnames:                       #输出文件夹信息
# #                 print(  "dirname is" + dirname)
# #             print(filenames)
#         for filename in filenames:
#             pathList.append(path+filename)

def getFiles(dir):
    filelist=[]
    filenames = os.listdir(dir)
    for filename in filenames:
        filepath = dir+'/'+filename
        filelist.append(filepath)
    return filelist

def readlines(path,encoding):
    lines = []
    file = open(path, 'r',encoding=encoding)
    for line in file:
        lines.append(line)
    file.close()
    return lines

def segment(sline):
    words = jieba.cut(sline,cut_all=False)
    return ' '.join(words)


if __name__ == "__main__":  
    filelist = getFiles('E:/Courses/NlpCourse/crawler/data')
    # print(filelist)
    corpus = []
    for path in filelist:
        lines = readlines(path,'utf-8')
        # print(lines)
        doc =''
        for line in lines:
            if len(line.strip())==0:
                continue
            # print(line.replace('\xa0',''[:100]).strip())
            segline = segment(line.strip().replace('\xa0',''))
            # print(segline)
            doc = doc+ segline+' '
        corpus.append(doc)
        # print(docs)
        # break
    stoplist = ['了','与','他', '我']
    vectorizer=CountVectorizer( token_pattern='[\u4e00-\u9fa5]+',stop_words=stoplist,ngram_range=(1, 1),min_df=10)#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
    # print(corpus)

    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
    print('--------tfidf---------')
    # print(tfidf)
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
    print('--------word---------')
    print(word)
    print(len(word))
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    # for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
    #     print ('-------这里输出第',i,'篇文本的词语tf-idf权重------')  
    #     for j in range(len(word)):  
    #         print(word[j],weight[i][j])



def demo():
    corpus=["我 来到 北京 清华大学",#第一类文本切词后的结果，词之间以空格隔开  
        "他 来到 了 网易 杭研 大厦",#第二类文本的切词结果  
        "小明 硕士 毕业 与 中国 科学院",#第三类文本的切词结果  
        "我 爱 北京 天安门"]#第四类文本的切词结果  
    stoplist = ['了','与','他', '我']
    vectorizer=CountVectorizer( token_pattern=r'(?u)\b\w+\b',stop_words=stoplist,ngram_range=(1, 1))#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
    print(corpus)

    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
    print('--------tfidf---------')
    print(tfidf)
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
    print('--------word---------')
    print(word)
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
        print ('-------这里输出第',i,'篇文本的词语tf-idf权重------')  
        for j in range(len(word)):  
            print(word[j],weight[i][j])