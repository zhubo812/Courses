## 第二章 基本概念


~~~~
计算语言学有两种基本研究方法

- 基于规则的方法
  - 理论基础：乔姆斯基文法理论
- 基于统计的方法
  - 理论基础：数理统计，信息论
~~~~
主要内容
1. 概率论基本概念
2. 信息论基本概念
~~~~

### 2.1 概率论基本概念

1. 概率
2. 条件概率
3. 乘法公式
4. 全概率公式
5. 贝叶斯公式
6. 最大似然估计
7. 二项式分布
8. 条件概率分布
9. 联合概率分布
10. 期望
11. 方差

~~~~
#### 2.1.1 概率
概率是从随机实验中的事件到实数域的函数，用以 表示事件发生的可能性。如果用`$P(A)$`作为事件`$A$`的概率，`$\Omega$`是实验的样本空间，则概率函数必须满足如下公理：
- 公理1：`$P(A)\geq0$`（非负性） 
- 公理2：`$P(\Omega)=1$`（规范性）
- 公理3：如果对任意的`$i$`和`$j(i\neq j)$`,事件`$A_i$`和`$A_j$`不相交`$(A_i\bigcap A_j=\phi)$`,则有：`$P(\bigcup_{i=0}^\infty A_i)=\sum_{i=0}^\infty P(A_i)$`（可列可加性）

~~~~

#### 2.1.2 条件概率(Conditional probability)

在事件B发生的条件下事件A发生的概率：
$$
P(A|B)=\frac {P(A,B)}{P(B)}=\frac {\frac {n_{AB}}{N}}{\frac {n_B}{N}}=\frac{n_{AB}}{n_B}
$$
其中，`$n_B$`代表事件`$B$`出现的次数,`$n_{AB}$`代表事件`$A$`和`$B$`同时出现的次数。
`$N$`是试验总次数

~~~~
![avatar](../ComputationalLinguistics/img/condiprob.jpg)

~~~~
#### 2.1.3 乘法公式

- 设`$A$`、`$B\in S, P(A)>0$`,由`$P(B|A)=\frac {P(A,B)}{P(A)}$`可得`$P(A,B)=P(A)P(B|A)$`，称为事件`$A$`、`$B$`的概率乘法公式。
- 若`$P(B)>0$`,则还有`$P(AB)=P(B)P(A|B)$`
- 上式还可推广到三个事件的情况：`$P(ABC)=P(A)P(B|A)P(C|AB)$`
- 一般情况下，有下列公式：
- `$P(A_1A_2...A_n)$` 
  `$=P(A_1)P(A_2|A_1)...P(A_n|A_1...A_{n-1})$`
- 注：乘法法则一般用于计算`$n$`个事件同时发生的概率
~~~~

词性标注问题

- "a red apple"的词性序列为"det,adj,n",计算这三个词性出现的概率如下：
- `$P(det,adj,n)  
=P(det)\times P(adj|det)\times P(n|det,adj)$`
~~~~
计算一个句子的概率如下：

`$P(w_1,w_2,...w_n)$`  
`$=P(w_1)\times P(w_2|w_1)\times ... P(w_n|w_1..w_{n-1})$`

其中，`$w_1$`,`$w_2$`,...`$w_n$`可以看做是组成句子的<font color=black>词</font>，也可以看成是组成句子的<font color=black>字</font>。
~~~~
#### 2.1.4 全概率公式

事件组`$A_1,A_2,...A_n$`(`$n$`可为`$\infty$`)称为样本空间`$S$`的一个划分，若以下条件满足：
1. `$\bigcup_{i=1}^nA_i=S$`
2. `$A_iA_j=\phi,(i\neq j)(i,j=1,2,...n)$`
![avatar](../ComputationalLinguistics/img/allprob.jpg)
~~~~
定理

设`$A_1,A_2,...A_n$`是`$S$`的一个划分,且`$P(A_i)>0,(i=1,2,...,n)$`则对任何事件`$B\in S$`有:

`$P(B)=\sum_{i=1}^nP(A_i)P(B|A_i)$`
称为全概率公式。
~~~~
全概率公式的使用

把事件`$B$`看作某一过程的结果,把`$A_1$`,`$A_2$`,...`$A_n$`看作该过程的若干个原因。根据历史资料,每一原因发生的概率已知,即`$P(A_n)$`已知,而且每一原因对结果的影响程度已知,即$P(B|A_n)$`已知,则我们可用全概率公式计算结果发生的概率,即求`$P(B)$
把事件`$B$`看作某一过程的结果,把`$A_1$`,`$A_2$`,...`$A_n$`看作该过程的若干个原因。根据历史资料,每一原因发生的概率已知,即`$P(A_n)$`已知,而且每一原因对结果的影响程度已知,即$P(B|A_n)$`已知,则我们可用全概率公式计算结果发生的概率,即求`$P(B)$`
~~~~
市场上有甲、乙、丙三家工厂生产的同一品牌产品,已知三家工厂的市场占有率分别为`$\frac{1}{4},\frac{1}{4},\frac{1}{2}$`,且三家工厂的次品率分别为 2%、1%、3%,试求市场上该品牌产品的次品率。设:
- `$B$`为买到一件次品的事件
- `$A_1$`:买到一件甲厂的产品
- `$A_2$`:买到一件乙厂的产品
- `$A_3$`:买到一件丙厂的产品  

~~~~

`$P(B)=P(BA_1)P(BA_2)P(BA_3)$`
`$=P(B|A_1)P(A_1)P(B|A_2)P(A_2)P(B|A_3)P(A_3)$`
$$=0.02\times\frac{1}{4}+0.01\times\frac{1}{4}+0.03\times\frac{1}{2} \approx 0.0225$$  

~~~~

#### 2.1.5 贝叶斯公式

贝叶斯公式（Bayesian formula）在统计自然语言处理中占据着重要的地位。 
当直接计算条件概率`$P(B|A)$`比较困难，而`$P(A|B)$`已知或是容易计算时，可以使用贝叶斯公式通过`$P(A|B)$`来计算`$P(B|A)$`。

~~~~

$$
P(B|A)= \frac{P(AB)}{P(A)}=\frac{P(A|B)P(B)}{P(A)}
$$
- `$P(B)$`为先验概率，是指根据以往经验和分析得到的概率；
- `$P(B|A)$`为后验概率，是指事情已经发生，求事件发生的原因由某因素引起的可能性的大小
- `$P(AB)$`为联合概率
~~~~
从机器学习的角度，可以视`$A$`为<font color=black>特征</font>、`$B$`为<font color=black>标签或类别</font>，那么贝叶斯公式可以表示为：

$$P(类别|特征)=\frac{P(特征|类别)P(类别)}{P(特征)}$$

~~~~
其中，

- `$P(类别|特征)$`为已知样本具有特定特征的条件下，该样本属于指定类别的概率
- `$P(特征|类别)$`为已知样本属于指定类别的条件下，该样本具有特定特征的概率
- `$P(类别)$`为未知样本具有特定特征的条件下，该样本属于指定类别的概率
- `$P(特征)$`为未知样本属于指定类别的条件下，该样本具有特定特征的概率
~~~~
贝叶斯用于文本分类问题

句子<font color=black>“我司代开正规发票”</font>,其类别为<font color=black>垃圾邮件</font>

$$
P(垃圾邮件|我司代开正规发票)
$$
$$=\frac{P(我,司,代开,正规,发票)P(垃圾邮件)}{P(我,司,代开,正规,发票)}
$$
~~~~
设标签“垃圾邮件”为`$S$`
$$
P(我,司,代开,正规,发票|S)
$$

$$
\approx P(我|S)P(司|S)P(代开|S)P(正规|S)P(发票|S)
$$
- 这就是<font color=black>条件独立假设</font>
- Bayes方法加上条件独立假设就是<font color=black>朴素贝叶斯方法(Naive Bayes)</font>
~~~~
朴素贝叶斯失去了词语之间的顺序信息。这就相当于把所有的词汇扔进到一个袋子里随便搅和，贝叶斯都认为它们一样。因此这种情况也称作词袋子模型(bag of words)。

![bw](../ComputationalLinguistics/img/bw.jpg)
~~~~
#### 2.1.5 最大似然估计(Maximum Likehood Estimation MLE)
作业
~~~~

### 2.2 信息论基本概念

| 名称 | 名称 | 名称 |
| :-----:| :----: | :----: |
| 信息量 | 熵 | 交叉熵 |
| 自信息 | 条件熵 | 互信息 |
| 联合自信息 | 联合熵 | 困惑度 |
| 条件自信息 | 相对熵 | ---- |

~~~~
人们普遍认为，Claude Elwood Shannon 在1948年发表的“通信的数学理论”（A Mathmatical Theory of Communication, BSTJ,1948）这篇里程碑性的文章标志着信息论的产生，而Shannon本人也成为信息论的奠基人。
~~~~
Shannon理论基本任务是设计有效而可靠的通信系统。

~~~~
信息论研究的内容

- 狭义信息论
- 广义信息论
~~~~
狭义信息论（经典信息论、香农信息论）

研究信息测度，信道容量以及信源和信道编码理论
一般信息论

研究信息传输和处理问题，除经典信息论外还包括噪声理论，信号滤波和预测，统计检测和估值理论，调制理论，信息处理理论和保密理论。
~~~~
广义信息论

除狭义信息论的研究内容外，还包括自然和社会领域有关信息的内容，如模式识别，计算机翻译，心理学，遗传学，神经生理学。
~~~~
#### 2.2.1 <font color=black>信息量</font>

事件发生的不确定性与事件发生的概率有关。事件发生的概率越小，事件发生所包含的不确定性和信息量就越大。而事件发生的概率越大，人们猜测这件事发生的可能性就越大，不确定性就越小。

~~~~
对于发生概率等于1的必然事件，就不存在不确定性。

因此，某事件发生所含有的信息量，应该是该事件发生的先验概率的函数，即$I(x_i)=f[P(x_i)]$

式中$P(x_i)$是事件$x_i$发生的先验概率，$I(x_i)$表示事件$x_i$发生所含有的信息量。
~~~~
函数$I(x_i)$应满足以下条件：
1. $P(x_i)$越大,$I(x_i)$越小；
2. 当$P(x_i)=1$时，$I(x_i)=0$，必然事件信息量为零
3. 当$P(x_i)=0$时，$I(x_i)=\infty$，不可能发生的事件发生了，其信息量为无穷大;
4. 两个独立事件的联合信息量，应等于它们各自信息量之和$I(x_ix_j)=f[P(x_i)]+f[P(x_j)]$
~~~~
可以看出，$I$与$P(x)$间若满足以上三点，则它们有如下关系式： 
$$
I=\log a\frac{1}{P(x)}=-\log aP(x)
$$
$I(x_i)$描述了事件$x_i$发生时的信息量，故称为自信息。

~~~~
#### 2.2.2 <font color=black>自信息</font>

事件集合$X$中的事件$x=a_i$的自信息定义为：<br>
$I_X(a_i)=-\log P_X(a_i)$<br>
简记为:$I(x)=-\log p(x)$

~~~~
$\log$底数 | 单位
:-:|:-:
2 | bit(比特)
e(ln) | nat(奈特)
10(lg) | hart(哈特)

- 注：
	- 1nat=1.44bit 
	- 1hart=3.32bit
~~~~
#### 2.2.3 联合自信息

联合事件集合$XY$中的事件$x=a_i,y=b_j$的联合自信息定义为：

$I_{XY}(a_i,b_j)=-\log P_{XY}(a_i,b_j)$

简记为：$I(xy)=-\log p(xy)$。其中,$p(xy)$要满足非负和归一化的条件。
~~~~

实际上,如果把联合事件$xy$ 视为一个单一事件,

那么联合自信息的含义与自信息的含义相同。
~~~~
例题：

箱中有90个红球，10个白球,箱中球不变，现从箱中先拿出一球，再拿出一球。
1. 求“两个球中有红、白各一球的”的不确定性
2. 求“两个球都是白球”所提供的信息量
3. 求“两个球都是白球”与“两个球都是红球”的发生,哪个更难预测
~~~~
解：三种情况都是求联合自信息，设$x$为红球数,$y$为白球数

1. $P_{XY}(1,1)=\frac {C_{90}^1C_{10}^1}{C_{100}^2}=\frac {90 \times 10}{100\times 99 \div 2}=\frac {2}{11} $

$I(1,1)=-\log \frac{2}{11}=2.46bit$
~~~~
2.$P_{XY}(0,2)=\frac {C_{10}^2}{C_{100}^2}=\frac {10 \times 9\div 2}{100\times 99 \div 2}=\frac {1}{110} $

$I(0,2)=-\log \frac{1}{110}=6.783bit$
~~~~
3.$P_{XY}(2,0)=\frac {C_{90}^2}{C_{100}^2}=\frac {90 \times 89 \div 2}{100\times 99 \div 2}=\frac {89}{110} $

$I(2,0)=-\log \frac{89}{110}=0.306bit$

因$I(0,2)>I(2,0)$, 所以事件“两个球都是白球”的发生更难预测。
~~~~
#### 2.2.4 <font color=black>条件自信息</font>

事件$x=a_i$在事件$y=b_j$给定条件下的条件自信息定义为:
$I_{X|Y}(a_i|b_j)=-\log P_{X|Y}(a_i|b_j)$
简记为：
$I(x|y)=-\log p(x|y)$

其中,条件概率$p(x|y)$也要满足非负和归一化的条件。
~~~~
条件自信息含义与自信息类似,只不过是概率空间有变化。条件自信息的含义两个方面：
1. 在事件$y=b_j$给定条件下,在$x=a_i$发生前的不确定性。
2. 在事件$y=b_j$给定条件下,在$x=a_i$发生后所得到的信息量。

证明:$I(xy)=I(x)+I(y|x)=I(y)I(x|y)$
~~~~
例题：

箱中有90个红球，10个白球,     箱中球不变，现从箱中先拿出一球，再拿出一球。
1. 在第一个球是红球的条件下、第二个球是白球的不确定性
2. 求在第一个球是红球的条件下、第二个球是红球所提供的信息量
~~~~
解：这两种情况都是求条件自信息，设$r$为红球数,$w$为白球数
~~~~
1. $p(y=w|x=r)=\frac{10}{99}$

$I(y=w|x=r)=-\log \frac{10}{99}=3.308bit$
~~~~
2. $p(y=r|x=r)=\frac{89}{99}$

$I(y=r|x=r)=-\log \frac{89}{99}=0.154bit$
~~~~
#### 2.2.5 <font color=black>熵(entropy)</font>

离散随机变量$X$的熵定义为自信息的统计平均值，记为$H(X)$

~~~~
$$
H(X)=E[I(x_i)]=-\sum_{i=1}^np(x_i)\log p(x_i)
$$
简记为：$H(X)=H(p(x_1),p(x_2),...,p(x_n))$

注：$p(x_1),p(x_2),...,p(x_n)$就是随机变量$X$的概率分布。

其中，约定$0\log0=0,H(X)$也可以写成$H(p)$。通常熵的单位为$bit$

~~~~
熵是信息论中重要的基本概念，又称为平均自信息（self-information），表示信源$X$每发一个符号（不论发什么符号）所提供的平均信息量。

熵也可以被视为描述一个随机变量的不确定性的数量。一个随机变量的熵越大，它的不确定性越大。那么，正确估计其值的可能性就越小。越不确定的随机变量越需要大的信息量用以确定其值。

~~~~

例题：
A,B两城市天气情况概率分布如下表所示,问哪个城市的天气具有更大的不确定性。

 \\| 晴| 阴| 雨
---|---|---|---
A城市 | 0.8| 0.15| 0.05
B城市 | 0.4| 0.3| 0.3
~~~~
解:
$$H(A)=H(0.8,0.15,0.05)$$
$$=-0.8\times \log0.8-0.15\times \log0.15-0.05$$
$$\times \log0.05=0.884bit$$

$$H(B)=H(0.4,0.3,0.3)$$
$$=-0.4\times \log0.4-0.3\times \log0.3-0.3$$
$$\times \log0.3=1.571bit$$

~~~~


#### 2.2.6 <font color=black>条件熵(conditional entropy) </font>

给定随机变量$X$的情况下，随机变量$Y$的条件熵定义为：
$$
H(Y|X)=\sum_ip(x_i)H(Y|X=x_i)
$$

$$
=\sum_ip(x_i)[-\sum_j^ip(y_j|x_i)\log p(y_j|x_i)]
$$

~~~~

$$
=\sum_i\sum_jp(x_i)p(y_j|x_i)\log p(y_j|x_i)
$$

$$
=-\sum_i\sum_jp(x_i,y_j)\log p(y_j|x_i)
$$

~~~~

上面条件熵定义所表示的是在已知`$X$`的情况下，传输`$Y$`额外所需的平均信息量。

~~~~

#### 2.2.7 <font color=black>联合熵(joint entropy)</font>

联合自信息量定义为：$I(x_i,y_j)=-\log p(x_i,y_j)$

$(X,Y)$被视为一个联合事件。

~~~~

联合熵$H(X,Y)$是二维随机变量$XY$的不确定性的度量:
$$
H(X,Y)=\sum_{i=1}^n\sum_{j=1}^mp(x_i,y_j)I(x_i,y_j)$$
$$=-\sum_{i=1}^n\sum_{j=1}^mp(x_i,y_j)\log_2p(x_i,y_j)
$$

~~~~

在给定$X=x_i$的条件下，随机变量$Y$的不确定性为：
$$
H(Y|x_i)=-\sum_jP(y_j|x_i)\log p(y_j|x_i)
$$
由于不同的$x_i$，$H(Y|x_i)$是变化的，对$H(Y|x_i)$的所有可能值进行平均，就得出给定$X$时，$Y$的条件熵$H(Y|X)$

~~~~

信息熵、联合熵和条件熵的关系
1. 联合熵与信息熵、条件熵的关系:
$H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)$
2. 条件熵与信息熵的关系:
$H(X|Y)\geq H(X)$
$H(Y|X)\leq H(Y)$
3. 联合熵与信息熵的关系:
$H(X,Y)=H(X)+H(Y)$
~~~~
#### 2.2.8 <font color=black>相对熵(Kullback-Leibler Divergence, KL距离)</font>

相对熵(relative entropy)又称Kullback-Leibler距离(Kullback-Leibler divergence)，或简称KL距离，是衡量相同事件空间里两个概率分布相对差距的一个量度。

~~~~
两个概率分布$p(x)$和$q(x)$的相对熵定义为：
$$
D(q||p)=\sum_{x\in\Omega}q(x)\log_2\frac{q(x)}{p(x)}=E_p(\log_2\frac{q(x)}{p(x)})
$$
该定义中约定：
$$
0\log(\frac{0}{q})=0
$$

$$
p\log(\frac{p}{0})=\infty
$$

~~~~
相对熵常被用以衡量两个随机分布的差距。
1. 当两个随机分布相同时，其相对熵为0.
2. 当两个随机分布的差别增加时，其相对熵也增大。
~~~~

#### 2.2.9 <font color=black>交叉熵(cross entropy)</font>

对于n-gram，其概率为，$P(w_i|w_{i-n+1}^{i-1})$
可以计算句子的概率为：
$$
P(S)=\prod_{i=1}^{n+1}P(w_i|w_{i-n+1}^{i-1})
$$
~~~~
假设测试语料$T$由$N$个句子构成$(n_1,n_2,...n_N)$则整个测试集的概率为:
$$
P(N)=\prod_{i=1}^N(n_i)
$$

~~~~

#### 2.2.10 <font color=black>互信息(mutual information)</font> 

互信息$I(x,y)$表示某一事件y所给出的关于另一个事件x的信息。

离散随机事件$x=a_i$和$y=b_j$之间的互信息定义为：

~~~~

$$
I_{X;Y}(a_i;b_j)=\log \frac{P_{X|Y}(a_i|b_j)}{P_X(a_i)}
$$
简记为：
$$
I(x;y)=\log \frac{p(x|y)}{p(x)}
$$

~~~~

通过简单计算，可以得到：$I(x;y)=I(x)-I(x|y),I(x;y)$也经常写成$I(x,y)$,因此,互信息有如下特点：

1. 互信息的单位与自信息单位相同
~~~~
2. $x$与$y$的互信息等于x的自信息减去在$y$条件下$x$的自信息。$I(x)$表示x的不确定性。

$I(x|y)$表示在$y$发生下$x$的不确定性。

$I(x;y)$表示当y发生后$x$不确定性的变化。

两个不确定性之差，是不确定度消除的部分，代表已经确定的东西。实际上就是由$y$发生所得到的关于$x$的信息量。

~~~~
3. 互信息反映了两个随机事件$x$和$y$之间的统计关联程度。在通信系统中，互信息的物理含义是，信道输出端接收到某消息(或消息序列)$y$后，获得的关于输入端某消息(或消息序列)x的信息量。互信息的引出，使信息传输问题进入例如定量分析的范畴，是信息论发展的一个重要的里程碑。
~~~~
#### 2.2.11 <font color=black>困惑度(perplexity)</font>
在设计语言模型时，我们常用困惑度代替交叉熵衡量语言模型的好坏。给定语言`$L$`的样本 如下：
$$
L_1^n=l_1l_2...l_n
$$
`$L$`的困惑度为:
$$
PP_q=2^{H(L,q)}\approx 2^{{\frac {1}{2}}\log(l_1^n)}=[q(l_1^n)]^{\frac {1}{n}}
$$