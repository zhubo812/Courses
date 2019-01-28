# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie

main usage in nlp: counting word frequency;

'''

#1. define a dictionay ,
dct = {"星期一":1,"星期二":2,"星期三":3}
print(dct)

#2. append element into a dictionary
#for instance, to put a dictionary element {"星期四":4}
dct["星期四"]=0
print(dct)

#3. query some key's value in a dictionary
key = "星期四"
value =dct[key]
print("key's value = %s"%(value))

#4. modify some element of a dictionay
key = "星期四"
dct[key] = 4
value =dct[key]
print("key's value = %s"%(value))

#5. append some elements into dictionay
list=["星期五","星期六","星期日"]
for item in list:
    dct[item] = 0
print(dct)
    


