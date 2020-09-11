# 自然语言处理基础

<br>
渤海大学文学院

朱波

----

我们能够很容易地得到数百万数量级的文本。假设我们会写一些简单的程序，那可以用它来做些什么？本章将解决以下几个问题。

（1）通过将技术性较简单的程序与大规模文本结合起来，我们能实现什么？

（2）如何自动地提取出关键字和词组，用来总结文本的风格和内容？

（3）Python编程语言为上述工作提供了哪些工具和技术？

（4）自然语言处理中有哪些有趣的挑战呢？

[<](#/)

----

1. [Python入门](#/2)
2. [NLTK](#/3)
3. [结构化NLP程序](#/4)
4. [中文自动分词](#/5)
5. [词性标注](#/6)
6. [NLP中的概率图模型](#/7)
7. [句法理论与自动分析](#/8)
8. [NLP中的深度学习](#/9)

---

## Python入门

Python安装配置及基本语法

[<](#/)

----
## Python安装配置

* Anaconda介绍
* Anaconda安装配置
* Anaconda常用操作命令
* Sublime安装配置

----

### Anaconda介绍
Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。 

----
### Anaconda安装

1. Anaconda下载链接：https://www.anaconda.com/download/
2. 添加环境变量,勾选 <font color=yellow>Add Anaconda to the system PATH environment variable</font>
3. 测试是否安装成功, 在控制台输入命令<font color=yellow> conda --version</font>

----
### Anaconda配置
1. 创建虚拟环境，<font color=yellow> conda  create -n py36  python=3.6</font>
2. 切换虚拟环境，<font color=yellow> activate py36 </font>

----
### Anaconda常用操作命令
命令     | 功能
-------- | ---
<font color=yellow>conda env list</font> | 查询已创建虚拟环境
<font color=yellow>conda install name</font> | 安装第三方包
<font color=yellow>pip install name</font> | 安装第三方包
<font color=yellow>pip uninstall  name</font> | 卸载第三方包
<font color=yellow>conda list</font> | 查看环境包信息
<font color=yellow>conda remove -n name --all</font>    | 删除指定虚拟环境下所有包
<font color=yellow>conda remove --name --all</font>    | 删除已创建虚拟环境

----
### Sublime介绍


----
### Sublime安装
1. Sublime下载链接：https://www.sublimetext.com/3
2. 安装Package Control,安装方法链接：https://packagecontrol.io/installation
3. 按ctrl+shift+p，在打开的文本框中输入Anaconda,并点击安装

----
### Sublime配置
选择<font color=yellow>Preferences-package Setting-Anaconda-Settings-Users</font>选项，键入以下json数据。

```json
{
	"python_interpreter": 
	"C:/Users/Administrator/.conda/envs/kpy3.6/python.exe",
	"suppress_word_completions":true,
	"suppress_explicit_completions":true,
	"completions_parameters":true,
	"anaconda_linting": false,
}
```

----
### Python介绍

----
### Python基本语法


----
第一个Python程序

对于大多数程序语言，第一个入门编程代码便是"Hello World！"，以下代码为使用Python输出"Hello World！"：
```python
#!/usr/bin/python3
 
print("Hello, World!")
```

----

 Python保留字
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 
'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from',
'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
```

----
字符串(String)

字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。  
创建字符串很简单，只要为变量分配一个值即可。


----
单行注释
```python
#!/usr/bin/python3
 
# 第一个注释
print ("Hello, Python!") # 第二个注释
```
----



多行注释

可以用多个 <font color=yellow>#</font> 号，还有 <font color=yellow>''' </font>和 <font color=yellow>"""</font>：
```python
#!/usr/bin/python3
 
# 第一个注释
# 第二个注释
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""
print ("Hello, Python!")
```

----
字符串运算符

字符串可以用运算符"<font color=yellow>+</font>"连接在一起，用运算符"<font color=yellow>*</font>"重复。
----
```python
#!/usr/bin/python3
 
str='Trump'
print(str + '你好')        # 连接字符串

print(str*3)

```
----
字符串连接结果
```python
Trump你好
```
字符串重复结果
```python
TrumpTrumpTrump
```
----
字符串索引
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
----
Python访问字符串中的值
```python
#!/usr/bin/python3
 
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
```
----
访问结果
```python
var1[0]:  H
var2[1:5]:  unoo
```
----
练习
```python
#!/usr/bin/python3
 
str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
```
----
输出结果

```python
str: Runoo
str[0:-1]: R
str[2:5]: noo
str[2:]: noob
str * 2: RunoobRunoob
str + '你好': Runoob你好
```
----
Python字符串运算符

下表实例变量a值为字符串 "Hello"，b变量值为字符串 "Python"：

操作符 | 描述 | 实例 | 输出结果
---|---|--- | --- 
+| 字符串链接 | a + b | HelloPython
\* | 重复输出字符串 | a\*2 | HelloHello
[] | 通过索引获取字符串中字符 | a[1] | e
[:] | 截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。 | a[1:4] | ell
in | 成员运算符 - 如果字符串中包含给定的字符返回 True | 'H' in a | True
not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True | 'M' not in a | True

----
Python转义字符

转义字符 | 描述
---|---
\\ | 反斜杠符号
\' | 单引号
\" | 双引号
\t | 横向制表符
\n | 换行
\r | 回车
----
转义字符在Python中的使用
```python
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print('hello\trunoob')      # 使用反斜杠(\)+t转义特殊字符
```

----
输出结果
```python
"hello\nrunoob":
hello
runoob
"hello\trunoob":hello	runoob
```

----
Python字符串格式化
```python
#!/usr/bin/python3
 
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```
----
输出结果
```python
我叫 小明 今年 10 岁!
```
----
python字符串格式化常用符号:

符号 | 描述
---|---
%s |  格式化字符串
%d | 格式化整数



---

## NLTK

Live happily ever after.

[<](#/)

---

## 结构化NLP程序

Live happily ever after.

[<](#/)

---

## 中文自动分词

Live happily ever after.

[<](#/)

---

## 词性标注

Live happily ever after.

[<](#/)

---

## 句法理论与自动分析

Live happily ever after.

[<](#/)

---

## NLP中的深度学习

Live happily ever after.

[<](#/)