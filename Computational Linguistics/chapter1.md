## 第一章 概述
~~~~
1. [计算语言学的性质及特点](#/2/1)
2. [计算语言学的发展及学科位置](#/2/59)


~~~~
### 计算语言学的性质及特点

~~~~
1. 计算语言学的<font color = yellow>定义</font>
2. 计算语言学的<font color = yellow>特点</font>
3. 计算语言学的<font color = yellow>研究方法</font>
4. 计算语言学对人们<font color = yellow>语言观的影响</font>

~~~~
#### 定义

计算语言学的中心任务是开发研制出一种人类能用自己的语言与之自由交谈的智能计算机。

——(德国计算语言学家 Roland Hausser,*Foundations of Computational Linguistics*）

~~~~
Question

计算机能理解、会思维吗？
~~~~
英国天才的数学家、计算机科学家图灵（Turing）提出了“图灵测试”————如果有<font color = yellow>超过30%的测试者不能确定出被测试者是人还是机器</font>，那么这台机器就通过了测试，并被认为具有人类智能。

![timg](../cl/img/timg.jpg)

~~~~
根据“图灵测试”的思想，计算机如果做到了下面四条中的一条，就可以认为它是智能的：
1. 问答（question-answering）
2. 生成文摘（summarizing）
3. 释义（paraphrase）
4. 翻译（translation）

~~~~
#### 1.1 计算语言学的定义

计算语言学是通过建立形式化的计算模型，用计算机分析处理、理解并生成自然语言的学科。
~~~~
#### 自然语言生成（Nature Language Generation,NLG）

自然语言生成从知识库或逻辑形式等等机器表述系统去生成自然语言,可以说是一种将资料转换成自然语言表述的翻译器。
~~~~
NLG一般通过多个子任务来解决问题。 一般可以分为以下六类：
1. 内容确定（Content determination）：决定在建文本中包含哪些信息；

2. 文本结构（Text structuring）：确定将在文本中显示的信息；

3. 句子聚合（Sentence aggregation）：决定在单个句子中呈现哪些信息；
~~~~

4. 词汇化（Lexicalisation）：找到正确的单词和短语来表达信息；

5. 引用表达式生成（Referring expression generation）：选择单词和短语以识别域对象；

6. 语言实现（Linguistic realisation）：将所有单词和短语组合成格式良好的句子。
~~~~
对计算语言学，也有广义和狭义两种理解。上述是狭义的理解。
~~~~
广义的计算语言学不仅包括上述内容，还包括利用计算机研究自然语言的有关问题，如风格统计、词语计量研究等等。

~~~~
| 作者   | 句平均词数 | 句平均字数 | 平均词长 |
| ------ | ---------- | ---------- | -------- |
| 巴金   | 24.75      | 40.65      | 1.642    |
| 倪海曙 | 15.79      | 24.05      | 1.523    |

~~~~
《静静的顿河》的作者是…肖洛霍夫？克留柯夫？
~~~~
我们可以用以下指标作为区别特征：
1. 平均句长
2. 句长分档，每档百分比
3. 不同词类统计
4. 不同词类在句中的顺序
5. 某些词汇特点的统计
6. 比较样品中使用一次、二次、三次……的词
~~~~
《红楼梦》的作者是一个人？还是两个人？

1. 上下文相关性（型例比/种次比）
2. 不同字符数的统计
3. 字符串的统计

~~~~

#### 统计结果：
1. 前八十回<后四十回
2. 前八十回>后四十回
3. 前八十回双音节字符串<单音节字符串，后四十回双音节字符串>单音节字符串

~~~~
##### 结论
作者应该是两个人

~~~~
#### 语言计量研究的基本概念

- 词种（type）
- 词次（token）

~~~~
句子“我明天要去上海看世博会，你去不去？” 的<font color = yellow>词种数</font>和<font color = yellow>词次数</font>分别是多少？
~~~~
- 词种：9
- 词次：11
~~~~
字符种？字符次？

~~~~
#### 语言计量研究涉及的问题

1. 计量研究的目标是什么？
目标决定对象、方法和过程。

2. 如何得到数据？
需要掌握各种统计工具、计算方法。

3. 如何对数据进行分析？
综合运用各种知识挖掘数据背后潜藏的东西。


~~~~
### 1.2 计算语言学的特点

~~~~
计算语言学的特点一

**元语言的形式化**
~~~~
对象语言与元语言：

- 对象语言，就是你所要研究的那种语言;
- 元语言，是指研究者在研究描述对象（语言）时使用的语言。

~~~~
**元语言的形式化**
1. 用自然语言作元语言的缺陷是歧义太多。
2. 数学公式、逻辑符号等都是形式化的元语言。
3. 形式化的元语言是人和计算机沟通的必要途径。
4. 计算语言学研究的是元语言应该如何设计才能更好地描述对象语言里的规律，而且计算机能够读懂。

~~~~
**规则描述语言**

1. 一|这|那/Q1/ (a)/ n* = N4 [NP>N1 N2 of N3 N4]
2. a)/ n|r* = N2 [NP > N1 N2]
3. d/ a* = N2 [a > N1 N2]



~~~~
计算语言学的特点二

**可操作性**

~~~~
<font color = yellow>可操作性</font>是计算语言学最根本、最关键的方法论原则就是要指出各种语言形式出现和变换的条件。
~~~~
所谓的<font color = yellow>条件</font>和与之想关联的<font color = yellow>动作</font>是一切计算机工作的最基本的方式，也是建立计算语言学语法的最基本、最关键的公式。
~~~~
计算语言学的研究手段是计算，计算的<font color = yellow>表现形式</font>是算法。
~~~~
算法是对解题方法的精确描述,可表示为一组有穷的操作规则。其特点如下：
1. 通用性：算法是针对一类问题的
2. 机械性：算法的每一步骤都是确定的
3. 有限性：算法必须在有限步骤内结束
4. 离散性：算法的输入及输出数据都是离散符号
~~~~
根据算法的特点如何在实现识别或生成语言？
~~~~
例如,N+N短语

- 偏正关系：学校图书馆、木头桌子
- 并列关系：工人农民、爸爸妈妈
- 复指关系：首都北京、鲁迅先生
- 主谓关系：今天星期二、鲁迅浙江人
~~~~
今天星期六、今天三八节（主谓）

今天下午，今年三八节（偏正）？
~~~~

计算语言学的特点三

**工程性**
~~~~
1. 机器翻译（Machine Translation）
2. 文本分类（Text Classification）
3. 自动文摘（Automatic Text Abstraction）
4. 信息检索（Information Retrieval）
5. 信息提取（Information Extraction）
6. 语音合成（Speech Synthesis）
7. 语音识别（Speech Recognition）
8. ……
~~~~
从本质上说，计算语言学是一门实验性、工程性的学科。
~~~~
计算语言学的特点四

**语言研究的全局性、一般性**
~~~~
歧义现象

- 咬死了猎人的狗（动宾/偏正，实例歧义）
- 咬死了猎人的鸡（动宾）
- 咬死了鸡的老虎（偏正）

VP + NP1 + 的 + NP2（格式歧义、潜在歧义）
~~~~
#### 计算语言学的特点
1. 元语言的形式化
2. 可操作性
3. 工程性
4. 语言研究的全局性、一般性

~~~~
#### 1.3 计算语言学的研究方法
~~~~
1. 规则驱动的方法
2. 数据驱动的方法
3. 二者融合的方法

~~~~
##### 规则驱动的方法
1. 研究人员（例如语言学家）对语言的规律进行总结，形成规则形式的知识库。
2. 研制语言处理算法，利用这些规则对自然语言进行处理。
3. 研究人员根据处理结果，调整规则，改进处理效果。
~~~~

根据如下6条规则，分析句子“The boy saw the girl with a telescope.”，并画出树形图。


1. `$S\rightarrow NP+VP$`
2. `$NP\rightarrow DET+N$`
3. `$NP\rightarrow NP+PP$`
4. `$VP\rightarrow VP+PP$`
5. `$VP\rightarrow V+NP$`
6. `$PP\rightarrow P+NP$`

~~~~
<font color = yellow>规则驱动的方法的问题</font>

All grammar leak(Sapir1921)认为：

对于自然语言而言，不大可能写出一部完备的规则集，语言规则有很强的伸缩性。
一般而言，很多基于规则的系统不能满足真实语言文本处理的要求，而只能处理真实语言的某个很小的子集。
~~~~
数据驱动的方法（统计方法）
~~~~

All grammar leak(Sapir1921)

1. 建立可以反映语言使用情况的语料库；
2. 研究人员对自然语言进行统计；
3. 建模利用统计技术或机器学习技术，基于语料库训练统计语言模型；
4. 利用得到的模型设计算法对语言进行处理；
5. 根据处理效果改进模型，提高处理性能。

~~~~

在数据驱动的方法中，语言模型通常体现为一组参数，这些参数通常表示某个语言形式发生的概率值。

对一个由三个词构成的字符串来说，其发生的概率可以表示为：`$P(w_3|w_1,w_2)$`

~~~~
判断“今天是周末”和“今天是课堂”哪个句子概率大?

𝑃(周末│今天是)>𝑃(课堂│今天是)

~~~~
<font color = yellow>数据驱动的方法（统计方法）的问题</font>

数据驱动的方法忽视了语言的深层结构。

~~~~
二者融合的方法

1. 融合规则驱动、数据驱动的优劣不能简单评价
2. 很多研究人员（包括知名计算语言学家）建议如此
3. 已经提出了一些策略，但如何结合尚须进一步探索

~~~~
两种方法的区别
~~~~
1. 对研究对象语言知识的认识不同。

- 规则方法：语言知识在人的大脑里，即人的语言能力；(<font color = yellow>语言</font>)
- 统计方法：语言知识在语言数据之中。(<font color = yellow>言语</font>)

~~~~
2. 获取语言知识的方法和途径不同。
- 规则方法：用内省方法，建立形式化的知识系统描述语言知识；
- 统计方法：用语料库方法，根据对语言数据的统计得到语言知识。
~~~~
3. 使用语言知识K构建语言处理系统时使用的算法不同。

- 规则方法：发展出许多比较成熟的算法技术；
- 统计方法：主要使用概率统计模型的自然语言处理算法。
~~~~
4. 对语言事实的评价不同。

- 规则方法：基于乔姆斯基的语言原则，语句是<font color = yellow>正确的/错误的</font>；
- 统计方法：基于先农(Shannon)的信息论,语句是<font color = yellow>常见的/罕见的</font>。


~~~~
#### 1.4 计算语言学对人们语言观的影响
~~~~
传统的语言观

- 语言是人类最重要的交际工具；
- 语言是一个符号系统。
~~~~
 新的语言观

- 语言是人类最重要的交际工具；
- 语言是人类和计算机共同的表达知识、传递信息、实施控制的符号系统。
~~~~
新的语言观

1. 语言是人类和计算机的共同的交际工具；
2. 语言是表达知识的最有效方法；
3. 语言是传递信息的最主要的载体；
4. 语言是实施控制的最方便的手段；
5. 语言是一个多层面的符号系统。
	- 语构层面:符号与符号之间的形式结构关系---句法学；
	- 语义层面:符号与其所指之间的意义关系---语义学；
	- 语用层面:符号与使用者之间的效用关系---语用学。
~~~~
小结

1. [计算语言学的定义](#/2/6)
2. [计算语言学的特点](#/2/37)
3. [计算语言学的研究方法](#/2/39)
4. [新的语言观](#/2/56)
5. [语言计量研究的基本概念](#2/16)
~~~~

#### 1.5 计算语言学的发展

计算语言学的历史可以大致分为萌芽期、发展期和繁荣期三个阶段。

~~~~
**1. 萌芽期**(1956年以前)

- <圣经•创世纪>巴别塔
- 20世纪30年代初，法国科学家阿尔楚尼（Artsouni）的“机械脑”（mechanicalbrain）;
- 1933年，苏联发明家特洛扬斯基（Tроянский）设计了语言翻译机.
- 1946年，美国宾夕法尼亚大学的埃克特（J.P.Eckert）和莫希来(J.W.Mauchly)设计并研制出世界上第一台电子计算机爱尼亚克(ENIAC)。

~~~~

- 同年，美国洛克菲勒基金会副总裁韦弗(W.Weaver)和英国工程师布斯(A.D.Booth)在讨论电子计算机的应用范围时，就谈到了利用计算机进行语言自动翻译的想法。
- 1949年，韦弗发表题为《翻译》的备忘录，正式提出机器翻译问题。
- 1954年，美国乔治敦大学&IBM公司，用IBM-701计算机，进行了世界第一次机器翻译试验，把几个简单的俄语句子翻译成英语。

~~~~
**机器翻译(Machine Translation,简称MT）**

机器翻译是利用计算机把一种语言的语句自动地转换为语义与之完全相同的另一种语言的语句。

~~~~
| 源文   | 正确的译文 | 机器的译文 | 
| ------ | ---------- | ---------- | 
| How are you?   | 你好吗？      | 怎么是你？      |
| How old are you? | 你多大了？     | 怎么老是你      | 

~~~~

**2. 发展期(1957-20世纪70年代初)**


早期：<font color = yellow>关键词</font>匹配为主流

- [1968年维金鲍姆（J·Weizenbaum）的ELIZA系统 （模拟心理医生、能与患者谈话的系统）](http://www.manifestation.com/neurotoys/eliza.php3)
~~~~
中后期：以<font color = yellow>句法-语义分析</font>技术为主流

- 维诺格拉德于1972年在美国麻省理工学院建成著名的SHRDLU系统（积木世界）。 
~~~~
![SHRDLU系统（积木世界）](
../cl/img/SHRDLU.jpg)

下面是 SHRDLU系统中人和计算机之间的一段对话：
- <font color = yellow>Person</font>: Pick up a big red block.
	- <font color = red>Computer</font>: Ok. (does it)
- <font color = yellow>Person</font>: Grasp the pyramid.
	- <font color = red>Computer</font>: I don't understand which pyramid you mean.
~~~~
- <font color = yellow>Person</font>: Find a block which is taller than the one you are holding and put it into the box.
	- <font color = red>Computer</font>: By "it", I assume you mean the block which is taller than the one I am holding.
~~~~
商克(Schannk)及其学生于1973年在斯坦福大学 建成MARGIE系统。 

MARGIE系统能以推理或释义两种方式运行。在推理方式下，它接受一个输入句，然后利用 推理器生成这个句子所蕴涵的事实。
~~~~

输入 <font color = yellow>John gave Mary some aspirin. </font>（约翰给玛丽一些阿司匹林。）


系统就可以作出推理： <font color = yellow>John believes Mary wants an aspirin. Mary is sick.</font> （约翰相信玛丽需要阿司匹林。玛丽病了。）

~~~~
**在释义方式下，它将以尽可能多的等价方式来复 述输入的句子。**

- 如输入<font color = yellow>John killed Mary by chokingher.</font>(约翰扼杀了玛丽。)

- 系统就会复述出如下的句子：
	- <font color = yellow>John strangled Mary.</font>(约翰勒死了玛丽。) 
	- <font color = yellow>John choked Mary and she died because she was unable to breathe. </font>(约翰扼住玛丽的脖子，她因为不能呼吸就死了。）

~~~~
李家治、陈永明等人建成的“古汉语机器理解系统——ACLUS”。

ACLUS能分析句法，能把《郑人买履》、《刻舟求剑》文言译成现代汉语，并回答故事中的语法和词义问题。
~~~~

- <font color = yellow>问</font>：‘先度其足’中的‘度’是什么意思？ 
	- <font color = red>答</font>：‘度’是动词，是测量某种东西尺寸的意思。 
- <font color = yellow>问</font>：‘吾忘持度’中的‘度’是什么意思？ 
	- <font color = red>答</font>：‘度’是名词，是尺寸的意思。

~~~~
范继淹、徐志敏等人建成的“TK——84汉语人机 对话实验系统”。这是一个铁路客运咨询系统。

- <font color = yellow>问</font>：从北京到大连有高铁吗？
	- <font color = red>答</font>：有。 
- <font color = yellow>问</font>：开往沈阳的快车都有卧铺吗？ 
	- <font color = red>答</font>：11次没有卧铺，其他都有。 
- <font color = yellow>问</font>：11次为什么没有卧铺？ 
	- <font color = red>答</font>：11次8点从北京开，18点49分到沈阳，卧铺没有必要。

~~~~
**发展期理论建设方面的成果**

- 英国数学家图灵(A·M·Turing)与美国语言学家乔姆斯基 (N·Chomsky)的贡献

~~~~
**发展期句法分析方面的成果**

- 乔姆斯基的<font color = yellow>短语结构语法</font>（phrase structure grammar，简称PSG）
- 伍兹的<font color = yellow>扩充转移网络</font>(augemented transition network,简称ATN)； 
- 卡普兰等的<font color = yellow>词汇功能语法</font>（Lexical-functional grammar，简称 LFG）； 马丁·凯依的<font color = yellow>功能合一语法</font>(functional unificational grammar，简称 FUG)；
- 盖兹达等的<font color = yellow>广义短语结构语法</font>(generalized phrase structure grammar,简称GPSG)等等。

~~~~
**发展期语义分析方面的成果**

- 菲尔摩的<font color = yellow>格语法</font>（case grammar); 
- 威尔克斯的<font color = yellow>优选语义学</font>(preference semantics)
- 商克的<font color = yellow>概念依存理论</font>(Conception Dependency Theory, 简称CD理论)  
~~~~

发展期的计算语言学逐渐融入了<font color = yellow>人工智能</font>的研究领域。研究方法上出现了<font color = yellow>基于规则</font>和<font color = yellow>基于统计(概率)</font>两种思想，并形成了两大阵营。

- 基于规则方法的<font color = yellow>符号派</font>(symbolic)
- 基于统计方法的<font color = yellow>随机派</font>(stochastic)。
~~~~
- 以Chomsky为代表的符号派学者开始了形式语言理论和生成句法的研究，20世纪60年代末又进行了形式逻辑系统的研究。

- 随机派学者采用基于贝叶斯方法的统计学研究方法。但由于在人工智能领域中，这一时期多数学者注重研究推理和逻辑问题，只有少数学者在研究基于概率的统计方法和神经网络。因此，这一时期基于规则方法的研究明显多于基于概率方法的研究。
~~~~
随着研究的深入，人们发现计算语言学的很多应用在短时间内无法解决，而的新问题新需求又不断地涌现。因此，计算语言学研究受到较大影响。从70年代开始，计算语言学的很多研究领域进入了低谷时期。
~~~~
但尽管如此，计算语言学仍然在这期间取得了一些成果。例如，
- <font color = yellow>基于隐马尔可夫模型</font>(Hidden Markov Model, HMM);
- <font color = yellow>话语分析</font>(Discourse Analysis)。

之后，由于计算语言学研究者对于过去的研究进行了总结，有限状态模型和经验主义研究方法也开始复苏。

~~~~
**3. 繁荣期**(20世纪70年代中后期-20世纪80年代末)

 繁荣期主要以<font color = yellow>机器翻译</font>的出现及发展为标志
~~~~

- 1976年，加拿大蒙特利尔大学与加拿大联邦政府翻译局联合开发的实用性英法机器翻译系统TAUM-METEO正式投入使用，提供天气预报的翻译服务。
- 美国的SYSTRAN系统
- 日本富士通公司的ATLAS系统
- 德国西门子公司与美国德克萨斯大学联合开发的METAL系统
~~~~
- 1988年由中国军事科学院开发、中国计算机软件与技术公司投入 市场的第一个机器翻译系统“译星1号”实现了商品化
- 中国社科院与北京高立公司联合开发的“高立英汉机器翻译系统”
- 中科院计算所开发的“863-IMT/EC智能型英汉机器翻译系统”
- 先是国防科技大学开发、后由深圳桑夏公司进一步开发的“桑夏译王英汉机器翻译系统”

~~~~

**4. 融合期发展期**(20世纪90年代至今）

20世纪90年代中期以后，计算机的处理速度和存储量等<font color = yellow>硬件</font>性能大幅提升，为计算语言学改善了物质基础，使得语言处理的商品化开发成为可能；

此外，1994年Internet商业化和同期<font color = yellow>网络技术</font>的发展使得基于自然语言的信息检索和信息抽取的需求变得尤为重要。

~~~~
**Milestone**
- 2003年 [神经概率语言模型](#/2/85)
- 2008年 [多任务学习](#/2/88)
- 2013年 [词嵌入](#/2/92)
- 2013年 [NLP中的神经网络](#/2/94)
- 2014年 [序列到序列模型](#/2/107)
- 2015年 [注意力机制](#/2/110)
- 2015年 [基于记忆的神经网络](#/2/114)
- 2018年 [预训练语言模型](#/2/116)
~~~~

<font color = yellow>神经概率语言模型（Neural Probabilistic language models）</font>

神经网络（Neural Network, NN）被应用于语言建模之前,主流语言模型是N-Gram模型，利用前面n个词语预测下一个单词。
神经网络语言模型引起广泛关注是在[Bengio et al. (2003)](https://jmlr.csail.mit.edu/papers/volume3/bengio03a/bengio03a.pdf)提出前向神经网络（Feed-forward Neural Network, FNN）语言模型之后.

[<](#/2/84)
~~~~
神经概率语言模型以某个词语前面的n个词语作为输入向量。这样的向量现在被称为词嵌入（word embeddings）。这些词向量入被连接并输入隐含层，然后再将隐含层结果输入softmax层。


[<](#/2/84)
~~~~
![nlm](../cl/img/nlm.jpg)
~~~~

<font color = yellow>多任务学习（Multi-task learning）</font>

多任务学习是在多个任务下训练的模型之间共享参数的方法。在神经网络中，这可以通过绑定不同层的权重来轻松完成。多任务学习的想法于年由Rich Caruana(1993)首次提出，
[Collobert,Jason(2008)](https://ronan.collobert.com/pub/matos/2008_nlp_icml.pdf)首次将多任务学习应用于NLP。在多任务学习框架下，词嵌入矩阵被两个在不同任务下训练的模型共享。

~~~~
![mtl](../cl/img/mtl.png)

~~~~
共享词嵌入使模型能够在词嵌入矩阵中协作并共享一般的低级信息，这类信息常构成模型中大部分的参数。

[Collobert,Jason(2008)](https://ronan.collobert.com/pub/matos/2008_nlp_icml.pdf)证明了共享词嵌入在多任务学习中的应用，引领了诸如预训练词嵌入和使用卷积神经网络（CNN）相关的方法，他们因此获得了2018年机器学习国际会议（ICML）的“时间测试”奖。
~~~~
多任务学习应用于多项NLP任务，实际应用中通常预先定义共享参数，然后通过参数优化学习到不同的共享模式。随着NLP各项任务对模型的泛化能力有更高的要求，使得多任务学习越来越重要。

[<](#/2/84)
~~~~
<font color = yellow>词嵌入（Word embeddings）</font>

[Bengio et al. (2003)](https://jmlr.csail.mit.edu/papers/volume3/bengio03a/bengio03a.pdf)证明使用神经网络训练的语言模型可以生成更好的词向量,并且提出了很多优化训练的方法。

[Mikolov et al. (2003)](https://arxiv.org/pdf/1310.4546.pdf)通过删除隐含层和近似目标来使这些词嵌入的训练更有效。
~~~~
<font color = yellow>word2vec--高效的词嵌入工具</font>

word2vec包含两种模式：

1. CBOW（continuous bag-of-words）
2. skip-gram

两种模式的目标不同：一个基于周围的单词预测中心词，而另一个则相反。

[<](#/2/84)
~~~~
<font color=yellow>Neural networks for NLP</font>

2013、2014期间神经网络模型逐渐在NLP任务中广泛采用。主要有以下三种类型：

- 卷积神经网络（Convolutional Neural Networks）
- 循环神经网络（Recurrent Neural Networks）
- 递归神经网络（Recursive Neural Networks）



~~~~
<font color=yellow>卷积神经网络</font>

卷积神经网络（CNN）被广泛用于计算机视觉，[Kalchbrenner,2014](https://arxiv.org/pdf/1404.2188.pdf)[Kim,2014](https://arxiv.org/pdf/1408.5882.pdf)将CNN应用于语言研究。下图显示了NLP中使用的典型CNN。

~~~~
![cnn](../cl/img/cnn.png)
~~~~
<font color=yellow>循环神经网络（Recurrent Neural Networks）</font>

循环神经网络从<font color=yellow>时间维度</font>展开，表示信息在时间维度上的传递和积累，后一个信息的概率建立在前面信息的基础上，在神经网络结构上表现为后面隐含层的输入是前面的隐含层的输出。
~~~~
<img align="left" src="../cl/img/RecurrentNN0.jpg"/>

`$x$`是一个向量，它表示输入层的值；

`$s$`是一个向量，它表示隐含层的值；

`$U$`是输入层到隐藏层的权重矩阵；

`$o$`也是一个向量，它表示输出层的值；

`$V$`是隐藏层到输出层的权重矩阵;

`$W$`就是隐含层上一次的值作为这一次的输入的权重。
~~~~
![recurrentNN](../cl/img/RecurrentNN.jpg)
~~~~
![recurrentNN1](../cl/img/RecurrentNN1.png)
~~~~
<font color=yellow>长短期记忆模型(Long-short Term Memory,LSTM)</font>
LSTM是Recurrent Neural Networks算法中的一种。LSTM很好的解决了原始RNN算法中的梯度消失弥散（Vanishing Gradient）问题。
~~~~
一个LSTM神经元（Cell）可以接收两个信息，其中一个是序列的某一位输入，另一个是上一轮的隐藏状态。

同时，一个LSTM神经元也会产生两个信息，一个是当前轮的输出，另一个是当前轮的隐藏状态。
~~~~
![LSTM](../cl/img/lstm2.jpg)
~~~~

相比RNN只有一个传递状态`$h^t$`，LSTM有两个传输状态，一个`$c^t$`（cell state），和一个`$h^t$`（hidden state）。（Tips：RNN中的`$h^t$`对于LSTM中的`$c^t$`）
~~~~
<font color=yellow>递归神经网络（Recursive Neural Networks）</font>

递归神经网络从<font color=yellow>空间维度</font>的展开，是一个树结构。
![RecursiveNN](../cl/img/RecursiveNN.png)
~~~~

递归神经网络把一个<font color=yellow>树型结构</font>信息编码为一个<font color=yellow>向量</font>,也就是把信息映射到一个语义向量空间中,语义相似的向量距离更近。两句话内容不同，但意思是相近，那么这两句话的向量的距离也相近；反之，语义差异越大，向量的距离则很远。
~~~~
![RecursiveNN1](../cl/img/RecursiveNN1.png)
~~~~

<font color=yellow>序列到序列模型（Sequence-to-sequence models）</font>

[Kyunghyun,Bengio et al. 2014](https://arxiv.org/pdf/1406.1078.pdf)提供了一种崭新的RNN Encoder-Decoder算法，并且将其应用于机器翻译中。
这种算法也是现在谷歌已经应用于线上机器翻译的算法，翻译质量基本达到、甚至超越人类水平。

~~~~
![stsm](../cl/img/stsm.jpg)
~~~~
以机器翻译为例，"How are you"翻译为"你好吗"，模型示例如下：
~~~~

![stsm1](../cl/img/stsm1.png)

~~~~


<font color=yellow>注意力机制（Attention）</font>

RNN应用于翻译时依赖将整个句子压缩成固定输入的向量，当句子包含单词过多时，不可避免地造成信息丢失，导致翻译错误。

注意力机制使得机器翻译中利用原始的句子信息，减少信息损失。在解码层，生成每个时刻的`$y$`，都会利用到`$x_1,x_2,x_3....$`，而不再仅仅利用最后时刻的隐藏状态向量。
~~~~
![stsm](../cl/img/attention1.png)


~~~~
[Bahdanau et al.2015](https://arxiv.org/pdf/1409.0473.pdf)提出了BahdanauAttention

[Luong et al.2015](https://arxiv.org/pdf/1508.04025.pdf)提出了LuongAttention
BahdanauAttention与LuongAttention的区别
1. BahdanauAttention对Encoder和Decoder的双向的RNN的state拼接起来作为输出，LuongAttention仅使用最上层的RNN输出
~~~~

2. 计算流程不同。BahdanauAttention的计算流程为`$h_{t-1} \rightarrow a_t → c_t → h_t$`，它使用前一个位置`$t-1$`的state计算`$t$`时刻的`$h_t$`。LuongAttention计算流程为`$h_t → a_t → c_t → h^t$` 使用t位置的state当前位置的`$h_t$`
3. BahdanauAttention只在concat对齐函数上进行了实验，LuongAttention在多种对齐函数进行了实验。


[<](#/2/84)
~~~~
<font color=yellow>基于记忆的神经网络</font>

记忆网络可以看做一个框架，用于QA或者分类等任务。
传统的记忆架构做关系推理时有困难，DeepMind和伦敦大学学院提出关系推理模块[RMC](https://arxiv.org/pdf/1806.01822.pdf)，能够在序列信息中执行关系推理，在WikiText-103, Project Gutenberg和GigaWord 数据集上达到了当前最佳性能。

[<](#/2/84)
~~~~
<font color=yellow>预训练的语言模型(Pre-trained Models)</font>

预训练语言模型可以在数据量十分少的情况下有效学习。由于语言模型的训练只需要无标签的数据，因此他们对于数据稀缺的低资源语言特别有利。

~~~~
<font color=yellow>预训练模型的发展</font>
1. 词嵌入（Word Embedding）
	- Word2Vec和[GloVe](#/2/118)[(Global  Vectors for Word Representation)](http://nlp.stanford.edu/projects/glove/)
2. 上下文嵌入(Context Word Embedding)
	- [CoVe](#/2/120)(Context Vectors)和[ELMo](#/2/121)
3. 预训练模型
	- [GPT](#/2/123)和BERT(Bidirectional Encoder Representation from Transformers)

~~~~
4. 改进型和领域定制型预训练模型
	- 改进型的代表为ALBERT和XLNet
	- 领域定制化代表为SciBert (Scientific Bert) 和BioBert(Biomedical Bert)
~~~~
<font color=yellow>小结</font>

为什么各类神经网络被广泛应用于NLP任务?

<font color=yellow>缓解特征工程问题</font>。非神经NLP方法通常严重依赖于离散的手工特征，而神经方法通常使用低维和稠密的向量(又称分布式表示)隐式地表示语言的语法或语义特征。这些表示是在特定的NLP任务中学习的。因此，神经方法使人们可以很容易地开发各种NLP系统。

[<](#/2/84)
~~~~
<font color=yellow>[预训练模型](#/2/116)--GloVe</font>

GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space. 
~~~~
<font color=yellow>[预训练模型](#/2/116)--GloVe</font>

GloVe与skip-gram和CBOW相比，skip-gram与CBOW每次用一个窗口中的信息更新出词向量，GloVe则是用了全局的信息（共现矩阵），即同时使用多个窗口进行更新词向量。
~~~~
<font color=yellow>[预训练模型](#/2/116)--CoVe</font>

[Bryan McCann et al.2017](https://arxiv.org/pdf/1708.00107.pdf)提出CoVe。与GloVe作为模型的输入时候的效果进行比较。实验结果表明他们提出的 Context Vectors 在不同任务中都带来了不同程度效果的提升。

CoVe更侧重于如何将现有数据上预训练得到的表征迁移到新任务场景中，而之前的句子级任务中大多数都只把迁移过程当做一个评估他们表征效果的手段，因此观念上有所不同。
~~~~
<font color=yellow>[预训练模型](#/2/116)--[ELMo(Embeddings from Language Models)](https://allennlp.org/elmo)</font>

[ELMo](https://www.aclweb.org/anthology/N18-1202/) is a deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). 
~~~~
<font color=yellow>[预训练模型](#/2/116)--ELMo(Embeddings from Language Models)</font>

双向语言模型（Bidirectionbbal language models, biLM）
![elmo](../cl/img/elmo.png)
~~~~
<font color=yellow>[预训练模型](#/2/116)-GPT</font>

[GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)的核心思想是先通过无标签的文本去训练生成语言模型，再根据具体的NLP任务利用有标签的数据对模型进行fine-tuning。
~~~~
<font color=yellow>[预训练模型](#/2/116)--BERT</font>

GloVe与skip-gram和CBOW相比，skip-gram与CBOW每次用一个窗口中的信息更新出词向量，GloVe则是用了全局的信息（共现矩阵），即同时使用多个窗口进行更新词向量。