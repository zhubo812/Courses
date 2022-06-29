import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import jieba as jb
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC,LinearSVC,LinearSVR
from sklearn.neural_network._multilayer_perceptron import MLPClassifier


df = pd.read_csv('data/online_shopping_10_cats.csv')
df=df[['cat','review']] # 删除无用列信息
print("数据总量: %d " % len(df))
# print(df.sample(10))

# print("在 cat 列中总共有 %d 个空值." % df['cat'].isnull().sum())
# print("在 review 列中总共有 %d 个空值." % df['review'].isnull().sum())
# df[df.isnull().values==True]
# df = df[pd.notnull(df['review'])]

d = {'cat':df['cat'].value_counts().index, 'count': df['cat'].value_counts()}
df_cat = pd.DataFrame(data=d).reset_index(drop=True)

print(d)
# print(df_cat)

df['cat_id'] = df['cat'].factorize()[0]
cat_id_df = df[['cat', 'cat_id']].drop_duplicates().sort_values('cat_id').reset_index(drop=True)
cat_to_id = dict(cat_id_df.values)
id_to_cat = dict(cat_id_df[['cat_id', 'cat']].values)
df.sample(10)
print(df['cat_id'])

print(cat_id_df)

print(cat_to_id)
print(id_to_cat)

# print(df.sample(10))


#停用词列表
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  

#加载停用词
stopwords = stopwordslist("data/stopwords.txt")
df = df.sample(10000)
#分词，并过滤停用词
df['segment'] = df['review'].apply(lambda x: " ".join([w for w in list(jb.cut(str(x))) if w not in stopwords]))
df.head()
print(df.sample(10))

# tfidf = TfidfVectorizer(norm='l2', ngram_range=(1, 2))
# features = tfidf.fit_transform(df.segment)
# labels = df.cat_id
# print(features.shape)
# print('-----------------------------')
# print(features)

# def data_split_by_cat(df,cats,test_size=.2):
#     train = pd.DataFrame()
#     test =  pd.DataFrame()
#     for cat in cats:
#         cat_df = df[df.cat==cat][['segment','cat_id']]
#         cat_train = cat_df.sample(int(len(cat_df)*(1-test_size)))
#         cat_test = cat_df[~cat_df.index.isin(cat_train.index)]
#         train = train.append(cat_train)
#         test = test.append(cat_test)
#     train = shuffle(train) 
#     test = shuffle(test)
#     return train['segment'],test['segment'],train['cat_id'],test['cat_id']

train_texts, test_texts, train_labels, test_labels = train_test_split(df['segment'], df['cat_id'], random_state = 0,stratify=df['cat_id'])
# print(type(test_texts))
# count_vect = CountVectorizer()
# train_texts_counts = count_vect.fit_transform(train_texts)

# tfidf_transformer = TfidfTransformer()
# train_texts_tfidf = tfidf_transformer.fit_transform(train_texts_counts)

# clf = MultinomialNB().fit(train_texts_tfidf, train_labels)



# myPredict('感谢京东自营产地直采。你们把握质量关。第三次购买')

# text_clf=Pipeline([('tfidf',TfidfVectorizer(max_features=10000)),
#                    ('clf',MultinomialNB())])
# text_clf=text_clf.fit(train_texts,train_labels)
# predicted=text_clf.predict(test_texts)
# print("MultinomialNB准确率为：",np.mean(predicted==test_labels))

# # SVM
# text_clf=Pipeline([('tfidf',TfidfVectorizer(max_features=10000)),
#                    ('clf',SVC())])
# text_clf=text_clf.fit(train_texts,train_labels)
# predicted=text_clf.predict(test_texts)
# print("SVC准确率为：",np.mean(predicted==test_labels))

# MLPClassifier
text_clf=Pipeline([('tfidf',TfidfVectorizer(max_features=10000)),
                   ('clf',MLPClassifier())])
text_clf=text_clf.fit(train_texts,train_labels)
predicted=text_clf.predict(test_texts)
print("MLPClassifier准确率为：",np.mean(predicted==test_labels))

def myPredict(sec):
    format_sec=" ".join([w for w in list(jb.cut(sec)) if w not in stopwords])
    pred_cat_id=text_clf.predict([format_sec])
    print(id_to_cat[pred_cat_id[0]])

myPredict('感谢京东自营产地直采。你们把握质量关。第三次购买')


