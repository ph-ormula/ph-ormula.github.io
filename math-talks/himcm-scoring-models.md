---
layout: default
title: "HiMCM: 方案评分的三种建模"
permalink: /math-talks/himcm-scoring-models/
toc: true
---

# HiMCM: 方案评分的三种建模

## 层次分析法（AHP）

层次分析法的目的是把一个选择考虑的不同维度分解成各个指标，并且依托他们的相对重要性得到权重向量，由判定向量与权重向量的内积确定最终得分。比较得分大小，可判定出最优选择

### 初始矩阵

我们可以通过一个选择考虑的不同维度（指标类型），以及不同候选选项在这些指标上的得分构建初始评分矩阵。例如，我们购买手机时考虑相机像素，电池续航，芯片强度；候选选项有苹果，华为，小米。那么可以根据数据，得到矩阵
$$X =
\begin{pmatrix}
48 & 3274 & 3.78 \\
50 & 5000 & 3.13 \\
50 & 4880 & 3.30
\end{pmatrix}$$

::: definition
**定义 1** (量纲).
量纲和单位差不多，只不过是个更广泛的概念，告诉你的是"你在测量什么"。例如，千米与米是不同的单位，然而是相同量纲，由于都在测量长度。
:::

::: remark
*Remark 1*.
两个物理量的量纲不同，就无法进行比较；例如我们无法比较电池的续航与芯片的强度。
:::

### 归一化$\rightarrow$标准化

标准化的核心目的是在保留指标的数值比之下，消除量纲，使得指标之间可以比较并且运算。\
对于 $n$ 行矩阵的标准化公式：
$$x_{ij}' = \frac{x_{ij}}{\sum_{i=1}^{n} x_{ij}}$$
最终我们得到的归一化向量，每个维度的分量和为
1（即归一化）。注意：分子分母均包含量纲，相除后量纲被约除。所以归一化处理使得指标之间可以相互比较、运算，并且保留了原先的相对比值。对于矩阵中每一列向量进行归一化操作，我们就完成了矩阵的标准化。\
回看原先的矩阵
$X$，显然量纲未被消除。我们可以通过将每一列向量归一化，得到标准化矩阵，令其为
$X'$。

### 判定矩阵

由题意，我们可以得到不同的指标相对于另几个的重要性比值，得出一个判定矩阵。可参考
Saaty 1--9 比例表：

| Scale | Definition | Interpretation |
| --- | --- | --- |
| 1 | Equal importance | Two criteria contribute equally to the objective. |
| 3 | Moderate importance | One criterion is slightly more important than the other. |
| 5 | Strong importance | One criterion is strongly more important. |
| 7 | Very strong importance | One criterion is very strongly more important. |
| 9 | Extreme importance | One criterion is absolutely more important. |
| 2, 4, 6, 8 | Intermediate values | Used for compromise between adjacent judgments. |
| $\tfrac{1}{3}, \tfrac{1}{5}, \dots$ | Reciprocal values | If criterion $i$ is less important than $j$. |

  : Saaty 1--9 Fundamental Scale for AHP

若题目未暗示不同指标的重要性（更经常的情况），我们需要进行主观揣测。若查表后，我们得到了重要性的比例关系，那么可汇总成表格，假设为

|  | $C_1$ | $C_2$ | $C_3$ |
| --- | --- | --- | --- |
| $C_1$ | 1 | 1/3 | 1/5 |
| $C_2$ | 3 | 1 | 1/2 |
| $C_3$ | 5 | 2 | 1 |

  : Pairwise Comparison Matrix for Three Criteria

 等价写成矩阵， $$A =
\begin{pmatrix}
1 & \tfrac{1}{3} & \tfrac{1}{5} \\
3 & 1 & \tfrac{1}{2} \\
5 & 2 & 1
\end{pmatrix}$$ 这就是判定矩阵。

::: remark
*Remark 2*.
表格中$C_1, C_2, C_3$均表示指标。判定矩阵中任意元素$a_{ij}$表示第i行指标与第j列的指标的重要性之比。
:::

### 一致性矩阵与检验

假设我们有指标A,B,C,令a,b,c为他们分别的重要性。得到$\frac{a}{b}$与$\frac{b}{c}$后，我们可以简单推得$\frac{a}{c}$,
然而A对C的重要性比值是我们主观估算出来的------这就引出了误差。\
完美世界里，我们的判定矩阵应是一致的，看定义：

::: definition
**定义 2** (一致性矩阵).
我们称n阶方阵X为一致性矩阵，当且仅当它满足以下条件

1.  $a_{ii} = 1, \quad \forall i \in \{1,2,\cdots, n\}$

2.  $a_{ij} = \frac{1}{a_{ji}}, \quad \forall i,j \in \{1,2,\cdots, n\}$

3.  $a_{ij} = a_{ik} \cdot a_{kj}, \quad \forall i,j,k \in \{1,2,\cdots, n\}$
:::

显然：前两条会被任意的判定矩阵满足，我们的注意力应该在第三条：i与k，k与j的重要性比值给定后，我们可以通过他们的乘积自然推广i与j的比值。这三条都满足时（即矩阵一致）判定矩阵是完美的。然而大多情况都会有误差，我们先引入一些便于量化的概念与结论。

::: definition
**定义 3** (特征向量与特征根). 设 $A$ 是一个 $n \times n$ 的方阵。
若存在非零向量 $\mathbf{x} \in \mathbb{R}^n$ 和标量
$\lambda \in \mathbb{R}$，使得 $A\mathbf{x} = \lambda \mathbf{x},$ 则称
$\lambda$ 为矩阵 $A$ 的**特征值**（eigenvalue）， $\mathbf{x}$ 为对应于
$\lambda$ 的**特征向量**（eigenvector）。
:::

::: remark
*Remark 3*.
当一个矩阵为一致性矩阵，其最大特征根为其阶数。并且越不一致，特征根比阶数越大。
:::

这些定义不需要完全掌握理解，当作结论记住即可。
现在我们可以引入一致性检验
$$CR=\frac{CI}{RI}, CI=\frac{\max_{\lambda}-n}{n-1}, RI=\frac{\max_{\lambda‘}-n}{n-1}$$
注意这里的RI是定值，可以查表得到；不同阶数的方阵有各自对应的数值。一个矩阵越不一致，由CR的计算公式，CR数值越大。由此，我们引入判定标准

| $CR$ 取值范围 | 含义 |
| --- | --- |
| $CR < 0.10$ | 一致性良好，判断矩阵可接受。 |
| $0.10 \leq CR < 0.20$ | 一致性一般，可根据需要进行微调。 |
| $CR \geq 0.20$ | 一致性较差，需重新调整判断矩阵。 |

  : 一致性比率 $CR$ 的判定标准

### 构造权重向量

假设矩阵通过检验，此时我们可以构造权重向量。三种方法为：算术平均法，几何平均法，特征值法，第三种更经常用。

##### (1) 算术平均法（Arithmetic Mean Method）

先将判断矩阵按列归一化，得到归一化矩阵
$b_{ij} = \frac{a_{ij}}{\sum_{i=1}^n a_{ij}}, \quad i,j=1,2,\dots,n.$
然后对每一行取算术平均，得到权重：
$w_i = \frac{1}{n}\sum_{j=1}^n b_{ij}, \quad i=1,2,\dots,n.$

##### (2) 几何平均法（Geometric Mean Method）

直接对判断矩阵的每一行取几何平均：
$w_i = \left(\prod_{j=1}^n a_{ij}\right)^{1/n}, \quad i=1,2,\dots,n.$
然后将所得结果归一化：
$w_i' = \frac{w_i}{\sum_{k=1}^n w_k}, \quad i=1,2,\dots,n.$

##### (3) 特征值法

特征值法最简单，当一个矩阵满足一致性检验时，取最大特征根对应的特征向量并且归一化，即可给出权重向量。

::: remark
*Remark 4*. 建议三种方法都跑一次，取分量平均值。
:::

### 计算得分

将归一化后的评分矩阵左乘权重向量，得到评分向量------每一个分量对应一个方案的得分。过程如下：给定评分矩阵A与权重向量w，计算
$$\begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
\begin{pmatrix}
w_1 \\ w_2 \\ \vdots \\ w_n
\end{pmatrix}
=
\begin{pmatrix}
a_{11}w_1 + a_{12}w_2 + \dots + a_{1n}w_n \\
a_{21}w_1 + a_{22}w_2 + \dots + a_{2n}w_n \\
\vdots \\
a_{m1}w_1 + a_{m2}w_2 + \dots + a_{mn}w_n
\end{pmatrix}.$$ 经过比较，即可选择最优。

## Topsis

该方法的本质是把方案当作向量，分量为不同指标的数据。由给定的方案与其对应的指标分量，得到一个理想最优和最劣的方案。将所有方案与这两个点做欧氏距离，离最优点最近，最劣点最远的方案就是目标方案。

### 矩阵正向化

Topsis的核心在于区分指标类型，回答的问题是：理想指标应该最大化，最小化，趋近某个具体值，还是属于某个最佳区间？因此我们总结出四种指标：极大型，极小型，中间型，区间型。给定3行3列初始矩阵
$$A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix},$$ 令行表示方案，列表示指标，i.e.,
$a_{ij}$表示方案i在j指标的数值。正向化的目的是将所有的指标转化为最大型，具体操作如下

|类型|方法|
|-|-|
|极大
|极小型|$\tilde{x}=\max-x_i$|
|中间型|$M=\max(\vert x_i-x_\mathrm{best}\vert)$, $\tilde{x}=1-\frac{\vert x_i-x_\mathrm{best}\vert}{M}$|

显然，原先问题的优化被简化为了求解正向化指标的最大值。令正向化后的初始矩阵为
$$A' = 
\begin{pmatrix}
a_{11}' & a_{12}' & a_{13}' \\
a_{21}' & a_{22}' & a_{23}' \\
a_{31}' & a_{32}' & a_{33}'
\end{pmatrix}.$$

### 另一种标准化

在AHP（层次分析）中，我们使用了按列归一化的方法对于整个矩阵标准化。考虑到标准化的唯一目的是保留比例的同时消除量纲，我们可以对于这个操作更创造性一点，不妨考虑对于每一列进行如下操作
$$z_{ij} = \dfrac{x_{ij}}{\sqrt{\sum_{i=1}^{n} x_{ij}^2}}.$$
这种方法显然是可行的，因为比例被保存，同时分子分母中的量纲都可被约掉。

::: remark
*Remark 5*.
有趣的是：这是一个$\frac{x}{||x||}$的形式，即向量除以自身范数------给出单位向量。如果对矩阵的每一列向量进行这种操作，我们实际上把所有的方案限制在了一个单位闭球上。（无意义的观察，不需要理解）
:::

令标准化后的矩阵为 $$A'‘ = 
\begin{pmatrix}
a_{11}'‘ & a_{12}'’& a_{13}‘' \\
a_{21}‘' & a_{22}'‘ & a_{23}‘' \\
a_{31}‘' & a_{32}‘' & a_{33}‘'
\end{pmatrix},$$
此时，三个方案可以由正向化矩阵的三行向量$a_1, a_2, a_3$进行表示。

### 最优判定

对于原始指标的优化简化为了对于正向化指标的最大化，我们可以由此推导理想最优与最劣方案（指标向量），定义
$$x^{+}=(\max\{a_{11}, a_{21}, a_{31}\}, \cdots, \max\{a_{13}, a_{23}, a_{33}\}), x^{-}=(\min\{a_{11}, a_{21}, a_{31}\}, \cdots, \min\{a_{13}, a_{23}, a_{33}\}).$$
为了方便，我们假设权重向量w已经给定，且维数（分量个数）为3。 定义
$$D_i^{+} = \sqrt{ \sum_{j=1}^{3} w_j (x_j^{+} - a_{ij})^2 }$$
$$D_i^{-} = \sqrt{ \sum_{j=1}^{3} w_j (x_j^{-} - a_{ij})^2 }.$$
观察可得，这个形式与三维两点距离公式几乎一致，只是在每个维度的计算加了权重向量的分量。我们希望找到方案使得其与最优方案x最近，最劣方案x'最远。此时目标可以由
$$\arg\max_{a_i} \frac{D_i^-}{D_i^-+D_i^+}$$
表示。通过代入三个方案，简单比较得到的数值，并取那个代入得到最大数值的方案即可。

## 熵权法

大家应该敏锐注意到，权重向量在"最优方案"类的建模问题中是绝对重要的------它决定了一个指标被重视的程度，以及你评估最终得分。AHP诚然是经典方法，然而主观性往往导致一致性检验不过关，做矩阵微调也较麻烦。熵权法是HiMCM中最常用的权重向量计算方法之一：建立在信息论之上，它避免了一切可能的主观性。\
熵权法的基本思想是：一个指标的信息效用值越大，在评分中就越重要，获得的权重越大。

### 信息量，信息熵

信息论认为一个事件发生的概率越高，信息量越低，反之亦然。考虑最极限的概率为一的情况，我们知道它必然发生，故信息量是最低的。同时注意到，离散信息论中不考虑概率为零的事件：既然它不可能发生，谈何带来的信息量？所以为了方便理解，我们可以把信息量粗暴简化为"如果一件事发生了，我会有多惊讶"。由此我们引入信息量公式
$$I(x)=-ln P(x).$$
几何意义上这个公式是很直觉性的。自变量，即事件x的概率，被定义在$(0,1]$区间。在概率为1时，信息量取最小值零；并且信息量随着概率的减小而单调上升。由此我们可以从信息量诱导信息熵的概念：假设一个随机变量有n种可能事件，我们有
$$H(x)=-\sum_{i=1}^{n} P(x_i) ln P(x_i).$$
张紫铭副社之后可能会在概率论的系列中讲，这是一个期望（expectancy）的形式：即我们把一个随机变量（这里是某个事件的信息量）所有的可能的结果乘以其概率再进行求和。所以信息熵衡量的就是随机变量的期望信息量。然而更常见的形式，我们会将信息熵归一化，得到以下式子
$$e_j=-\frac{1}{lnn}\sum_{i=1}^{n} P(x_{ij}) ln P(x_{ij}) \in [0,1]$$
当随机变量的概率分布对于n个事件完全平均，i.e.,
每个事件的概率为$\frac{1}{n} e_j$取到最大值，为1（可以用拉格朗日乘数法证明，附录会包括我自己的证明）。同时不难发现该式子在概率被限制在$(0,1]$时，取值恒非负，故最小值为0。我们成功将信息熵定义在了\[0,1\]之间。

::: remark
*Remark 6*.
简单注意到当信息熵取零时，某事件的概率取1。结合之前我们发现的"概率平均，熵取最大"，我们得以更直觉性的理解信息熵：当每件事一样有概率发生时，我们无法判断更有可能发生什么------此时系统具有高不确定性，熵也取到最大。然而当系统确定了绝对会发生一件事情，系统是稳定可预测的，熵取最小。所以亦可说信息熵衡量了系统的混乱度。
:::

### 信息效用值与赋权

信息效用值，或有效信息，直接决定了权重，公式为 $$d_j=1-e_j.$$
读完了remark，我相信你可以更好的理解这个公式。一个变量或系统越不确定，越混乱，能帮到我们的信息------即有效信息------就越少；系统越稳定，有效信息自然越多。

### 信息论与决策模型

现在我们直接把以上内容套用到模型中。依然假设我们有三个方案与三个指标，初始矩阵在正向化，归一化，标准化（这三个基本操作我希望大家可以熟悉）后为
$$A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix},$$
此时的随机变量有三个，分别是：只考虑三个中的一个指标，我们选哪个方案。对于某个随机变量的可能事件是：考虑这个指标，我们选择了某个具体方案。假设我们只考虑指标1：不难看出，选择方案1这一事件的概率就是方案1在指标1上的得分，即$a_{11}$。由此可以直接代入信息效用值公式，得到三个指标分别的$d_j$。略作总结：评分（在正向化标准化归一化后）就是概率。\
思考：为什么我们要归一化？

### 赋权与最终选择
现在可以引入赋权公式了， $$w_j=\frac{d_j}{\sum_{j=1}^{3} d_j}.$$

略作解释，信息效用值越大，信息熵越小，事件概率/评分的分布越不均匀，越离散。我们认为分布的离散度代表了某个指标对于方案评分的区分度。一个指标越能区分方案的优劣性，在评分中就越有权重------这是一个相当直观的结论。
用矩阵A左乘这个向量，即可得到评分向量，比较分量大小取最大即可判定出最优方案。当然结合Topsis亦可。

## Topsis+熵权法例题

## HiMCM 2020 Problem B: Funding Biodiversity Conservation-简化版本

### Background

Many plant species in Florida are endangered, yet conservation funds are
limited. The Florida Rare Plant Conservation Endowment (FRPCE) aims to
determine how to allocate resources to protect 48 imperiled species.
Each project includes data on *Benefit*, *Taxonomic Uniqueness*,
*Feasibility of Success*, and annual costs over 25 years.

### Tasks

1.  Develop a model to determine the minimum fundraising needed to
    support all projects over a 25-year period.

2.  Create a model to rank the 48 projects by priority based on their
    conservation importance and cost.

## HiMCM 2018 Problem A: Roller Coaster-依旧简化

### Scope

Consider only roller coasters *currently in operation*. The provided
dataset includes coasters whose height, speed, and/or drop exceed
worldwide averages. Family/kiddie, bobsled, and mountain-type coasters
are excluded.

### Available Data (examples)

Numerical and descriptive specs such as speed, height, drop, ride
duration, inversions, length, material (steel/wood), and launch type.

### Tasks

1.  Develop an **objective** quantitative algorithm (or set of
    algorithms) to produce a *descriptive* rating/ranking of coasters
    using only specification data (no subjective scores).

2.  Apply the algorithm(s) to create a **Top 10 in the World** list.
    Compare and discuss your results with at least two online
    rating/ranking systems.

## HiMCM Problem B: City Crime and Safety-依旧依旧简化

### Background

Major cities collect vast amounts of crime data, yet simple counts do
not accurately reflect how safe a city is. **My City** is an
international hub with a population of 2.8 million and an additional 6
million in the surrounding metropolitan area. The dataset
`My_City_Crime_Data.xlsx` provides two weeks of police reports,
including case number, date, primary and secondary crime type, location,
arrest record, domestic indicator, and police beat.

### Task

Using mathematical modeling, analyze the data and develop a **safety
rating** for My City. Use this rating to provide a quantitative measure
of how safe the city is.
