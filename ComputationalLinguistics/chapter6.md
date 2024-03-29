## 第六章 句法分析

~~~~
### 主要内容
1. 概述
2. 基本方法
3. 概率上下文无关文法
4. 依存句法理论
~~~~
#### 6.1.1 基本概念  
1. <font color = black>句法结构分析</font>，是指对输入的单词序列（一般为句子）判断其构成是否合乎给定的语法，分析出合乎语法的句子的句法结构。
2. 
句法结构一般用树状数据结构表示，通常称为<font color = black>句法分析树</font>（syntactic parsing tree），简称分析树（parsing tree）。
3. 完成句法分析过程的程序模块称为<font color = black>句法结构分析器</font>（syntactic parser），通常简称为分析器（parser）。


~~~~

#### 6.1.2 句法分析的主要任务
一般而言，句法结构分析的任务有三个：

1. 判断输入的字符串是否属于某种语言；
2. 消除输入句子中词法和结构等方面的歧义；
3. 分析输入句子的内部结构，如成分构成、上下文关系等。如果一个句子有多种结构表示，句法分析器应该分析出该句子最有可能的结构。  
~~~~
由于在实际应用过程中，通常系统都已经知道或者默认了被分析的句子属于哪一种语言。  因此，一般不考虑任务1，而着重考虑消歧任务和最佳句法结构识别的处理问题。

~~~~

#### 6.1.3 主要难点

自然语言中，词汇歧义和结构歧义等各种类型的歧义普遍存在，而<font color = black>句法结构歧义</font>的识别和消解是句法分析面临的主要困难。



~~~~
#### 6.1.4 语法形式化
语法形式化（grammar formalism）属于句法理论研究的范畴。目前在自然语言处理中广泛使用的是上下文无关文法（CFG）和基于约束的文法（constraint-based grammar）的简单形式，后者又称为合一语法（unification grammar）。

~~~~
常用的基于约束的语法有： 
1. 功能合一语法（functional unification grammar，FUG）；
2. 树链接语法（tree-adjoining grammar，TAG）；
3. 词汇功能语法（lexical-functional grammar，LFG）；
4. 广义的短语结构语法（generalized phrase structure grammar，GPSG）；
5. 中心语驱动的短语结构语法（head-driven phrase structure grammar，HPSG）。

~~~~
### 6.2 基本方法


~~~~
1. 基于规则的分析方法
2. 基于统计的分析方法
~~~~
基于规则的句法结构分析方法的基本思路是，由人工组织语法规则，建立语法知识库，通过条件约束和检查来实现消除句法结构的歧义。
~~~~
句法分析算法有：
1. CYK分析算法（Cocke-Younger-Kasami parsing）
1. 厄尔利算法（Earley parsing）
1. 线图分析算法（chart parsing）
1. 移进-规约算法（shift-reduction parsing）
1. GLR分析算法（generalized LR parsing）
1. 左角分析算法（left-corner parsing） 

~~~~
#### 6.2.2 线图分析法
1. 自顶向下（top-down）
2. 自底向上（bottom-up）
3. 从上到下和从下到上结合

~~~~
#### 基于规则方法的主要优点
 
对于特定的领域和目的，利用手工编写的有针对性的规则能够较好地处理输入句子中的部分歧义现象。
~~~~
#### 基于规则方法的主要缺点
1. 对于一个中等长度的输入句子来说，要利用大覆盖度的语法规则分析出所有可能的句子结构是非常困难的，分析过程的复杂性往往使程序无法实现；
2. 即使能够分析出句子所有可能的结构，也难以在巨大的句法分析结果集合中实现有效的消歧，并选择出最有可能的分析结果；
3. 手工编写的规则一般带有一定的主观性，对于实际应用系统来说，往往难以覆盖大领域的所有复杂语言；
4. 手工编写规则本身是一件大工作量的复杂劳动，而且编写的规则对特定的领域有密切的相关性，不利于句法分析系统向其他领域移植。

~~~~
鉴于基于规则的句法分析方法存在诸多局限性，目前研究较多的统计句法分析方法是语法驱动的（grammar-driven），其基本思想是由生成语法（generative grammar）定义被分析的语言及其分析出的类别。  
在训练数据中观察到的各种语言现象的分布以统计数据的方式与语法规则一起编码。在句法分析的过程中，当遇到歧义情况时，统计数据用于对多种分析结果的排序或选择。
~~~~
### 6.3 概率上下文无关文法（probabilistic context-free grammar, PCFG）

基于概率上下文无关文法的句法分析方法自20世纪80年代提出以来，受到了众多学者的关注。由于这种方法既有规则方法的特点，又运用了概率信息，因此，可以认为是规则方法与统计方法的紧密结合。
~~~~
PCFG是CFG的扩展，PCFG的规则表示形式为：`$P=A \rightarrow \alpha$`其中A为非终结符，`$p$`为`$A$`推导出`$\alpha$`的概率，即`$p=P(A \rightarrow \alpha)$`，该概率分布必须满足如下条件：
$$
\sum P(A \rightarrow \alpha)=1
$$

~~~~
`$S \rightarrow NP VP(1.00) , NP \rightarrow NP PP(0.4)$`
`$PP \rightarrow P NP(1.00) , P \rightarrow with(1.00)$`
`$VP \rightarrow V NP(0.70) , VP \rightarrow VP PP(0.30)$`
`$NP \rightarrow astronomers(0.10) , NP \rightarrow ears(0.18)$`
`$NP \rightarrow saw(0.04) , NP \rightarrow stars(0.18)$`
`$NP \rightarrow telescopes(0.10) , V \rightarrow saw(1.00)$`

给定句子S：Astronomers saw stars with ears.
~~~~
![601](../ComputationalLinguistics/img/601.png)
~~~~
![602](../ComputationalLinguistics/img/602.png)
~~~~
#### PCFG需满足的基本假设：

1. 位置不变性（place invariance）:子树的概率不依赖于该子树所管辖的单词在句子中的位置；
2. 上下文无关性（context-free）:子树的概率不依赖于子树控制范围以外的单词；
3. 祖先无关性（ancestor-free）:子树的概率不依赖于推导出子树的祖先结点。
~~~~
`$P(tree_{NP})=P(NP \rightarrow astronomers)=1.0$`
~~~~
`$P(tree_{PP})=P(P \rightarrow with) \times$`
`$P(NP \rightarrow ears)\times$`
`$P(PP \rightarrow P NP)$`
`$= 1.00\times 0.18 \times 1.00= 0.18$`
~~~~
`$P(t_1)=1.00 \times 0.10 \times 0.70 \times$`
`$1.00 \times 0.40 \times 0.18 \times 1.00 $`
`$\times 1.00 \times 0.18 = 0.0009072$`
~~~~
`$P(t_1)=1.00 \times 0.10 \times 0.30 \times$`
`$0.70 \times 1.00 \times 0.18 \times 1.00 $`
`$\times 1.00 \times 0.18 = 0.0006804$`
~~~~
给定的句子`$S:P(t_1)\gt P(t_2)$`
~~~~
#### 运用PCFG的三个基本问题
1. 给定句子`$W=w_1w_2 ... w_n$`和句法`$G$`,如何快速计算`$P(W|G)$`?
2. 给定句子`$W=w_1w_2 ... w_n$`和句法`$G$`,如何快速选择最佳句法结构树？
3. 给定句子`$W=w_1w_2 ... w_n$`和句法`$G$`,如何调节`$G$`的参数，使得`$P(W|G)$`最大?
~~~~
如何解决上述三个问题？  
假设文法`$G(S)$`的规则只有两种形式：

`$A \rightarrow a, a \in V_T$`

`$A \rightarrow BC, B,C \in V_N$`
~~~~
#### 向内算法解决问题1-计算句子的概率
- 基本思想：通过动态规划计算由非终结符`$A$`推导出的字串`$W=w_iw_{i+1} ... w_j$`的概率`$\alpha_{ij}(A)$`。句子`$W=w_1w_2 ... w_n$`的概率即为文法`$G(S)$`中`$S$`推导出的字串的概率。
~~~~
- 定义  
向内变量`$\alpha_{ij}(A)$`是由非终结符`$A$`推导出的语句`$W$`中子串`$w_iw_{i+1} ... w_j$`的概率为：
$$
\alpha_{ij}(A)=P(A \rightarrow w_iw_{i+1} ... w_j)
$$
~~~~
- 计算`$\alpha_{ij}(A)$`的递推公式为：
$$
\alpha_{ij}(A)=P(A \rightarrow w_i)
$$
$$
\alpha_{ij}(A)=\sum_{B,C\in V_N}\sum_{i \leq k \leq j}P(A\rightarrow BC)\alpha_{ik}(B)\alpha_{(k+1)j}(C)
$$
~~~~
$$A \rightarrow BC$$
$$B \rightarrow w_iw_{i+1} ... w_k$$
$$C \rightarrow w_{k+1} ... w_j$$

![603](../ComputationalLinguistics/img/603.png)
~~~~

![604](../ComputationalLinguistics/img/604.png)  
向内归纳的过程
~~~~
#### 维特比算法解决问题2-最佳分析结果
- 定义： Viterbi变量`$\gamma_{ij}(A)$`是由非终结符`$A$`推导出的语句`$W$`中子串`$w_iw_{i+1} ... w_j$`的最大概率。

变量`$\psi_{i,j}$`用于记忆字串`$W=w_1w_2 ... w_n$`的Viterbi语法分析结果。
~~~~
- Viterbi搜索算法描述
	- 输入:文法`$G(S)$`,语句`$W=w_1w_2 ... w_n$`
	- 输出:`$\gamma_{1n}(S)$`
1. 初始化:`$\gmma_{ij}(A)=P(A\rightarrow w_i),A\in V_n,1\leq i \leq j \leq n$`
2. 归纳计算:`$j=1...n, i=1...n-j$`,重复下列计算:
$
\gamma_{i(i+j)}(A)= \max\limits_{B,C\in V_N; i\leq k\leq i+j}P(A\rightarrow BC)\gamma_{ik}(B)\gamma_{(k+1)(i+j)}(C)
$
$
\psi_{i(i+j)}(A)= \max\limits_{B,C\in V_N; i\leq k\leq i+j}P(A\rightarrow BC)\gamma_{ik}(B)\gamma_{(k+1)(i+j)}(C)
$`
3. 终结:`$P(S\rightarrow w_1w_2 ... w_n)= \gamma_{1n}(S)$
~~~~
#### 向内向外算法解决问题3-参数估计
- 基本思想：已知训练语料中语法结构，记录每个语法规则的使用次数，用最大似然估计计算PCFG的参数。

- 利用大量标注语料, 使用EM (Expectation Maximization) 方法估计参数。
~~~~
#### PCFG的评价

- 优点：
	- 可利用概率减少分析过程的搜索空间；
	- 可利用概率对概率较小的子树剪枝，加快分析效率；
	- 可以定量地比较两个语法的性能。
- 缺点：
	- 无法统计词与词、词类与词类、短语与短语的同现信息。

~~~~
4. 依存句法理论
~~~~
一般认为,法国语言学家Lucien Tesnière（1893—1954）是现代依存语法理论的创立者。关于依存语法理论的代表作为《结构句法基础》（Eléments de syntaxe structurale,1959）。
~~~~
Tesnière认为，一切结构句法现象可以概括为关联（connexion）、组合（jonction）和转位（tanslation）这三大核心。句法关联建立起词与词之间的从属关系，这种从属关系是由支配词和从属词联结而成；动词是句子的中心并支配别的成分，它本身不受其他任何成分支配。
~~~~
Tesnière还将化学中“价”的概念引入依存语法，一个动词所能支配的行动元（名词词组）的个数即为该动词的价数。
~~~~
在依存语法理论中，“依存”就是指词与词之间支配与被支配的关系，这种关系不是对等的，而是有方向的。处于支配地位的成分称为支配者（governor，regent，head），而处于被支配地位的成分称为从属者（modifier，subordinate，dependency）。
~~~~
![605](../ComputationalLinguistics/img/605.png)
~~~~
![606](../ComputationalLinguistics/img/606.png)
~~~~
#### 4.1 定义
用词与词之间的依存关系来描述语言结构的框架称为依存语法（dependence grammar），又称从属关系语法。
~~~~
论文*依存结构和转换规则*（J.Robinson，1970）中提出了依存语法的四条公理：
1. 一个句子只有一个独立的成分；
2. 句子的其他成分都从属于某一成分；
3. 任何一个成分都不能依存于两个或两个以上的成分；
4. 如果成分A直接从属于成分B，而成分C在句子中位于A和B之间，那么，成分C或者从属于A，或者从属于B，或者从属于A和B之间的某一成分。
~~~~

上述四条公理就是对依存图和依存树的形式约束  
1. 单一父结点（single headed）
2. 连通（connective）
3. 无环（acyclic）
4. 可投射（projective）

该约束条件能够确保句子的依存分析结果是一棵有“根”（root）的树结构，为依存语法的形式化描述及在计算机语言学中的应用奠定了基础。
~~~~
冯志伟首先将Tesnière的从属句法理论引入我国的自然语言处理研究，他把动词和形容词的行动元分为主体者、对象者和受益者3个，把状态元分为时刻、时段、时间起点、时间终点、空间点、空间段、空间起点、空间终点、初态、末态、原因、结果、目的、工具、方式、范围、条件、作用、内容、论题、比较、伴随、程度、判断、陈述、附加、修饰27个，以此来建立多语言的自动句法分析系统。
~~~~
冯志伟(1998)提出了依存结构树应满足的5个条件
1. 单纯结点条件：只有终结点，没有非终结点；
2. 单一父结点条件：除根结点没有父结点外所有的结点都只有一个父结点；
3. 独根结点条件：一个依存树只能有一个根结点，它支配其他结点；
4. 非交条件：依存树的树枝不能彼此相交；
5. 互斥条件：从上到下的支配关系和从左到右的前于关系之间是互相排斥的，如果两个结点之间存在着支配关系，它们之间就不能存在前于关系。
~~~~
<font color=black>依存语法</font>与<font color=black>短语结构语法</font>相比最大的优势是它直接按照词语之间的依存关系工作，依存语法几乎不使用词性和短语类等句法语义范畴，没有Chomsky的形式化重写规则，几乎所有的语言知识都体现在词典中，是基于词语法理论的。
~~~~
#### 依存句法标记

|  标记   | 含义  |
|  ----  | ----  |
| ROOT  | 要处理文本的语句 |
| NP  | 名词短语 |
| VP  | 动词短语 |
| LCP  | 方位词短语 |
| JJ  | 形容词或序数词 |

[依存句法标记](../ComputationalLinguistics/dependencyTag.txt)
~~~~
#### 4.2 依存句法分析
1. 生成式依存分析方法
2. 判别式依存分析方法
3. 确定性依存分析方法
~~~~
##### 4.2.1生成式依存分析方法
生成式依存分析方法采用联合概率模型生成一系列依存句法树并赋予其概率分值，然后采用相关算法找到概率打分最高的分析结果作为最后输出。
~~~~
假设句子x的依存分析结果`$y$`，模型参数为`$\theta$`，其联合概率模型为`$Score(x,y|\theta)$`，以使目标函数`$\Pi^{N}_{i=1}Score(x_i,y_i;\theta)$`最大的`$\theta$`作为模型的参数，其中`$(x_i,y_i)$`为训练实例，`$N$`为实例个数。
~~~~
J. Eisner（1996a, 1996b）对于生成式依存分析方法提出了三个模型
1. 二元亲和词汇模型（bigram lexical affinites）
2. 选择偏好模型（selectional preferences）
3. 递归生成模型（recursive generation）
~~~~
##### 4.2.2判别式依存分析方法
判别式依存分析方法采用条件概率模型`$Score(x|y,\theta)$`，避开了联合概率模型所要求的独立性假设，训练过程即寻找使目标函数 `$\Pi^{N}_{i=1}Score(x_i|y_i,\theta)$`最大的`$\theta$`。
~~~~
##### 4.2.3确定性依存分析方法
确定性依存分析方法以特定的方向逐次取一个待分析的词，为每次输入的词产生一个单一的分析结果，直至序列的最后一个词。这类算法在每一步的分析中都要根据当前分析状态做出决策（如判断其是否与前一个词发生依存关系），因此，这种方法又称决策式分析方法。
~~~~
基本思想是通过一个确定的分析动作（parsing action）序列来得到一个唯一的句法表达，即依存图（有时可能会有回溯和修补）
~~~~
#### 4.3 依存分析器性能评价
~~~~
- 评价指标
1. 无标记依存正确率（unlabeled attachment score, UAS）：测试集中找到其正确支配词的词（包括没有标注支配词的根结点）所占总词数的百分比。
~~~~
- 评价指标
2. 带标记依存正确率（labeled attachment score, LAS）：测试集中找到其正确支配词的词，并且依存关系类型也标注正确的词（包括没有标注支配词的根结点）占总词数的百分比。
~~~~
- 评价指标
3. 依存正确率（dependency accuracy, DA）：测试集中找到正确支配词非根结点词占所有非根结点词总数的百分比。
~~~~
- 评价指标
4. 根正确率（root accuracy, RA）,有两种定义方式:
	1. 测试集中正确根结点的个数与句子个数的百分比
	2. 指测试集中找到正确根结点的句子数所占句子总数的百分比。


对单根结点的语言或句子来说，二者是等价的。
~~~~
- 评价指标
5. 完全匹配率（complete match, CM）：测试集中无标记依存结构完全正确的句子占句子总数的百分比
~~~~
![607](../ComputationalLinguistics/img/607.png)
~~~~
(a)结果包括:外资（3, nmod）、企业（ 3, sbj ） 、成为（ 0, root ） 、外贸（ 6, nmod ） 、重要（6, sbj ）、增长点（ 3, obj ） 、（ 3, p ） ，共7项。  
(b)结果包括:外资（2, nmod）、企业（3, sbj）、成为（0, root）、外贸（6, nmod）、重要（6, nmod）、增长点（3, obj）、（3, p），共7项。
~~~~
$$
UAS=\frac{6}{7}\times 100\%=86.71\%
$$
$$
LAS=\frac{5}{7}\times 100\%=71.43\%
$$


