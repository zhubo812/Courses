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
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline



df = pd.read_csv('data/online_shopping_10_cats.csv')
df=df[['cat','review']] # 删除无用列信息
print("数据总量: %d " % len(df))


d = {'cat':df['cat'].value_counts().index, 'count': df['cat'].value_counts()}
df_cat = pd.DataFrame(data=d).reset_index(drop=True)

print(d)
# print(df_cat)

df['cat_id'] = df['cat'].factorize()[0]
cat_id_df = df[['cat', 'cat_id']].drop_duplicates().sort_values('cat_id').reset_index(drop=True)
cat_to_id = dict(cat_id_df.values)
id_to_cat = dict(cat_id_df[['cat_id', 'cat']].values)
# df = df.sample(10)

# print(df.sample(10))


#停用词列表
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  

#加载停用词
stopwords = stopwordslist("data/stopwords.txt")
# df = df.sample(10000)
#分词，并过滤停用词
df['segment'] = df['review'].apply(lambda x: " ".join([w for w in list(jb.cut(str(x))) if w not in stopwords]))
df.head()
# print(df.sample(10))


# count_vect = CountVectorizer()
# text_counter = count_vect.fit_transform(df.segment)

# tfidf = TfidfTransformer()
# texts_tfidf = tfidf.fit_transform(text_counter)

# print(texts_tfidf)
# tfidf = TfidfVectorizer(norm='l2', ngram_range=(1, 2))
tfidf = TfidfVectorizer(norm='l2')
vectorizer = tfidf.fit_transform(df.segment)
# terms = text_counter.get_feature_names()


# km = KMeans(n_clusters=10, init='k-means++', n_init=10, max_iter=1000, tol=0.0001, verbose=0, random_state=None, copy_x=True)
# pipe = Pipeline([('vect', vectorizer), ('kmeans', km)])

# pipe.fit(df.sample(10)['segment'])
true_k = 8
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
# model.fit(vectorizer)
result = model.fit_predict(vectorizer)
# def myPredict(sec):
#     format_sec=" ".join([w for w in list(jb.cut(sec)) if w not in stopwords])
#     pred_cat_id=pipe.transform([format_sec])
#     print(pred_cat_id)
# myPredict('感谢京东自营产地直采。你们把握质量关。第三次购买')\


print( "Top terms per cluster:")
order_centroids =model.cluster_centers_.argsort()[:, ::-1]
for i in range(true_k):
    print ("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]) 
    print()

print(result)