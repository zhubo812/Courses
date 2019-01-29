# -*- coding:utf-8 -*-
'''
Created on 2019年1月28日

@author: Jackie
'''

#1声明字符串变量并赋值
var1 = 'Hello World!'
var2 = "Runoob"

#2访问字符串中的值
print("===========2访问字符串中的值============")
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:2])

#3 字符串拼接
print("===========3 字符串连接============")
var3= var1+var2
print(var3)
var3=var1*2
print(var3)



#4 转义符的使用
print("===========4 转义符的使用============")
var4="\'\\\t\""
print(var4)

#5 字符串截取
print("===========5 字符串截取============")
var5= var1[0:2]#0为待截取字符串的开始位置；2为截取字符个数
print(var5)

#6 字符串格式化
print("===========6 字符串格式化============")
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

#7 字符串常用内置函数
#7.1检查字符串是否以 指定字符 结束
print("===========7.1检查字符串是否以 指定字符 结束===========")
flag = var1.endswith("!")
print(flag)

print("===========7.2检查字符串是否以 指定字符 开始===========")
#7.2检查字符串是否以 指定字符 开始
bool = var1.startswith("!")
print(flag)

print("===========7.3检测 指定字符串 是否包含在待检字符串中===========")
#7.3检测 指定字符串 是否包含在待检字符串中
flag= var1.find("l")
print(flag)

print("===========7.4如果字符串只包含数字则返回 True 否则返回 False.===========")
flag = var1.isdigit()
print(flag)

print("===========7.5如果字符串中只包含空白，则返回 True，否则返回 False.===========")
flag = var1.isspace()
print(flag)

print("===========7.6返回字符串长度.===========")
length = len(var1)
print(length)


print("===========7.7以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串.===========")
items=["a","b","c"]
line = ";".join(items)
print(line)

print("===========7.8把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。.===========")
str1 = "Hi"
str2 = var1.replace("Hello", str1)
print(str2)

print("===========7.9以 指定分隔符分割字符串.===========")
splitor=" "
words = var1.split(splitor)
print(words)

print("===========7.10删除字符串左右两端空格.===========")
str3= "  "+ var1+"   "
print(str3)
str3= str3.strip()
print(str3)

print("===========8.1 用for 循环字符串中的每个字符.===========")
for c in var1:
    print(c)


print("===========8.2 用range 循环字符串中的每个字符.===========")
for i in range(0,len(var1)):
    print(("第%d个字符是%s")%(i,var1[i]))



