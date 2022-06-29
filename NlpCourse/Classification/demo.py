from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
            '我 是 一条 天狗 呀 ！', 
            '我 把 月 来 吞 了 ，', 
            '我 把 日来 吞 了 ，', 
            '我 把 一切 的 星球 来 吞 了 ，', 
            '我 把 全宇宙 来 吞 了 。', 
            '我 便是 我 了 ！'
      ]

tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_model = tfidf.fit(documents)
print(tfidf_model.vocabulary_)
print(tfidf_model.transform(documents).todense())


text_clf=Pipeline([('tfidf',TfidfVectorizer(max_features=10000)),
                   ('clf',MultinomialNB())])
text_clf=text_clf.fit(train_texts,train_labels)
predicted=text_clf.predict(test_texts)
print("MultinomialNB准确率为：",np.mean(predicted==test_labels))