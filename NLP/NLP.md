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
- python中单引号和双引号使用完全相同。
- 使用三引号('''或""")可以指定一个多行字符串。
- 转义符 '\'
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。

----
字符串运算(String)
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
```python
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
```

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
字符串操作
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
print('------------------------------')
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
```
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