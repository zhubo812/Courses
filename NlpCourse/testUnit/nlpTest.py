# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''
from NlpTookit.NlpTookit import NlpTookit


line="自。然.语？言！处理?"

tookit = NlpTookit()
sentences = tookit.toSentenceList(line)
print(sentences)