---
layout: default
title: "更多数学"
permalink: /math-talks/more-math/
toc: true
---

# 常识

## 基本符号
后续数学学习的书写中常常用一些符号，有几个较重要：

- $$\forall$$：对于所有，念作 "for all"。
- $$\exists$$：存在，念作 "there exists"。
- $$\text{s.t.}$$：使得，念作 “such that"。
- $$d(\cdot, \cdot)$$：任意空间下两点距离函数。


## 欧几里得空间
小学讨论一维欧氏空间（实数轴），初中介绍二维（一二次，反比例函数，平面几何证明），高中扩展二维的讨论（更多的函数和平面几何），同时逐步到三维（立体几何）。然而当我们只考虑若干有穷条实数轴组成的坐标系时，便脱离了维度限制，到达了许多有趣结论诞生的地方：任意有限维欧氏空间。它的规定很少：暂且只需知道对于 $$n$$ 维欧氏空间：

- 任意一点 $$x$$ 可用坐标 $$(x_1, x_2, \cdots, x_n)$$ 进行表示（异常的重要，希望你可以记住），
- 对于任意两点 $$x,y\in \mathbb{R}^n$$，$$d(x,y)=\sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$$
- 任意两点可以比较大小，规则如下

- 
$$
x = y \;\Longleftrightarrow\; x_i = y_i \text{ 对所有 } i.
$$

- 
$$
x \ge y \;\Longleftrightarrow\; x_i \ge y_i \text{ 对所有 } i.
$$

- 
$$
x > y \;\Longleftrightarrow\; x \ge y \text{ 且存在某个 } j \text{ 使得 } x_j > y_j.
$$

- 
$$
x \gg y \;\Longleftrightarrow\; x_i > y_i \text{ 对所有 } i.
$$


所谓“比大小”也有一个严格数学名称：偏序（partial order）。


请各位在脑中的 x-y 坐标系中想象一个 $$(1,1),(0,2)$$，是否发现在我们定义的欧式偏序下，这两点不可比较（incomparable）？这便是偏序和全序（total order）的区别——在一个集合（空间只是一种特殊集合）的全序下，所有点均可比较，然而偏序不做这种要求。

# 开集
我们讨论欧氏空间中开集的概念，包括定义、推论以及证明。
[$$\epsilon$$-开球]
在有限维欧式空间 $$\mathbb{R} ^n$$ 中，以点 $$x$$ 为中心的 $$\epsilon$$ 开球记作 $$B_{\epsilon}(x) = \{y \in \mathbb{R} ^n\mid d(x,y) < \epsilon \},$$其中 $$\epsilon$$ 是给定的正实数。在部分教材里，该集合会被称为 $$x$$ 的 $$\epsilon$$-邻域。

我们可以用开球来定义一个开集。
[开集]
我们称一个有限维欧式空间的集合 $$X$$ 为一个开集，当且仅当它满足 $$\forall \; x \in X, \exists \epsilon \in \mathbb{R} ^+$$ 使得 $$B_{\epsilon}(x) \subset X$$。

简言之，对于开集中任意的元素，都可以找到一个它的开球，使得这个开球完全包含在该开集中。

任意多的开集的并集是开集。


我们用定义0.2完成证明。考虑一个开集族 $$\{X_{\beta}\}_{\beta \in I}$$，即对于任意一个 $$\beta$$，$$X_\beta$$ 都是开集。设我们定义了一个新的集合，满足 $$\cup_{\beta \in I} X_\beta$$。任取 $$x \in \cup_{\beta \in I} X_\beta$$，则存在某个 $$\beta_0$$ 使得 $$x \in X_{\beta_0}$$。由于 $$X_{\beta_0}$$ 为开集，根据定义0.2，存在 $$\epsilon>0$$ 使得 $$B_{\epsilon}(x) \subset X_{\beta_0}$$。从而有 $$B_{\epsilon}(x) \subset \cup_{\beta \in I} X_\beta$$。因此，我们定义的新集合，内任意一个元素，都可以找到一个其开球，使得其为 $$\cup_{\beta \in I} X_\beta$$ 的子集。由定义 0.2，该集合为开集。


有限个开集的交集是开集。


依旧通过定义0.2完成证明。考虑一个由有限个集合构成的开集族 $$X_i$$, $$i=1,2,\cdots n$$，任取 $$x \in \cap_{i=1}^{n} X_i \in X_i$$。因为每个 $$X_i$$ 都是开集，所以存在一个 $$\epsilon_i>0$$，满足 $$B_{\epsilon_i}(x) \subset X_i$$。取 $$\epsilon = \min\{\epsilon_1,\cdots \epsilon_n\}$$，则有 $$B_{\epsilon}(x) \subset B_{\epsilon_i}(x) \subset X_i$$。因此，对于 $$\cap_{i=1}^{n} X_i$$ 中的元素，都可以找到一个它的开球使得其为 $$\cap_{i=1}^{n} X_i$$ 的子集，证毕。


当开集无穷多时，它们的交集依然开吗？考虑反证法（prove by contradiction）：我们可以构建一族开区间（一维开集），使得其无穷交集为一个闭区间（一维闭集）。


一族开区间
$$X_i = \left(-\frac{1}{i},\,1 + \frac{1}{i}\right), \quad i = 1,2,\dots$$
的无穷交集是闭区间 $$[0,1]$$，即
$$
\bigcap_{i=1}^{\infty} X_i = [0,1].
$$


该开区间在 $$i$$ 增大时会逐渐缩小。很显然，区间 $$[0,1]$$ 是每一个 $$X_i$$ 的子集：对所有 $$i$$，都有
$$[0,1] \subset \left(-\frac{1}{i},\,1 + \frac{1}{i}\right).$$
因此 $$[0,1]$$ 是 $$\bigcap_{i=1}^{\infty} X_i$$ 的子集。接下来我们需要证明 $$[0,1]$$ 也是这个无穷交集的“全部元素”，即没有遗漏任何点，从而得到
$$[0,1] = \bigcap_{i=1}^{\infty} X_i.$$


考虑 $$x<0, \exists k \in \mathbb{N} \; s.t. \; - \frac{1} {k} > x$$。因此对于某些 $$i$$, $$x \notin X_i$$，即 $$x \notin \cap_{i=1}^{\infty} X_i$$。类似的，再考虑 $$x>1, \exists k \in \mathbb{N} \; s.t. \; 1+\frac{1} {k} < x$$。同理可得：对于某些 $$i$$, $$x \notin X_i$$，即 $$x \notin \cap_{i=1}^{\infty} X_i$$。又 $$\forall x \in [0,1], x \in X_i, \text{对于任意} i=1,2,\cdots$$，证毕.



我们证明了对于所有不属于 $$[0,1]$$ 的 $$x$$，它都不属于开区间族的无穷交集——即我们没有漏掉任何一个元素。
# 闭集
有了对于开集的认识，讨论闭集变得格外简单，其一般定义如下：
$$\text{我们称集合} X \text{为闭集，当且仅当} X^c \text{为开集}.$$
即闭集的补集是开集。
\\我们可以用推论1.1，1.2来极短地证明闭集的推论——利用他们互为补集的关系。但得先复习一下德摩根定律，它会格外有用！
[德摩根定律]
$$\cap X_\beta^c=(\cup X_\beta)^c, \quad \cup X_\beta^c=(\cap X_\beta)^c$$

看着绕，实则简单：两条完全对称，记了一条能自然推第二条。蓝色Core只教了两个集合的情况，然而任意多，无穷多的集合同样适用，画下试试便知。


任意多的闭集的交集是闭集



考虑闭集族 $$X_\beta$$, 由德摩根：$$(\cap X_\beta)^c=\cup X_\beta^c$$。我们由闭集的定义知道$$X_\beta$$的补集都是开集，又由任意多开集的并集是开集（推论2.1），$$\cup X_\beta^c$$ 是开集，故 $$\cap X_\beta$$——它的补集——是闭集，证毕。



有穷个闭集的并集是闭集。



让我们榨干德摩根的价值：考虑有穷闭集族 $$X_i$$, $$i=1,2,\cdots,n$$，我们知道 $$(\cup_{i=1}^{n} X_i)^c=\cap_{i=1}^{n} X_i^c$$，由推论2.2和闭集定义，$$(\cup_{i=1}^{n} X_i)^c$$ 是闭集，证毕。

都很短吧？依惯例，我们需要检查一下推论2.2中“有穷个”是否冗余。但这一次不再做完整的反证了。邀请你们自行思考以下证明题：


一族闭区间
$$X_i=[\frac{1}{i}, 1-\frac{i}{i}], i=2,3\cdots$$
的无穷并集是开区间 (0,1)。

一点关于证明的启发：我们在证命题2.3的时候说明了我们没有遗漏元素，是否可以借鉴这个套路？

# 界
我们对于集合的了解已经较完善，现在引入最后的一个概念：集合的界。

[上下界]
我们称 $$\bar{x}$$ 为集合 $$X$$ 的上界（或下界），当且仅当
$$
\forall x \in X,\, x \le \bar{x}\, \text{（或 }\bar{x} \le x\text{）}.
$$

可以看出一个集合往往有若干，甚至无穷个上下界。因此我们规定了一组更有用的定义：上下确界：他们被定义为最小（或最大）的上界（或下界）。


集合 $$X$$ 的上确界（或下确界）被标注为
$$
\sup X \text{ （或 } \inf X \text{） }.
$$


[有界集合]
我们称一个集合 $$X$$ 有界，当且仅当
$$
\exists \epsilon>0 \text{ s.t. } X \subset B_\epsilon (0)
$$

即对于有界集，永远可以找到一个以原点为中心的开球来包住集合。

# 序列与收敛
我们接触过了无穷数列——这是一维欧氏空间（实数轴）的序列。更一般的，序列中的元素可以是任意维度欧氏空间中的点：在二维笛卡尔系中任意画无数个点，这也是个序列。两件重要须知：

- 序列可被看作一种集合，
- 序列中的元素有无穷个。


[序列]
一个 $$\mathbb{R}^n$$ 中的序列可用 $$\left\{x_i\right\}_{i=1}^{\infty}$$ 进行标注。 若想省事，形如 $$\left\{x_i\right\}$$ 亦可；也可用上标代替下标。注：序列下标必须为自然数！

自然引出“子序列”的定义和标注：
[子序列]
设 $$\left\{x_n\right\}_{n\in\mathbb{N}}$$ 是一个序列。若存在一个递增的自然数列
$$
n_1 < n_2 < n_3 < \cdots,\, n_k\in\mathbb{N},
$$
则序列
$$
\{x_{n_k}\}_{k\in\mathbb{N}} = x_{n_1},x_{n_2},x_{n_3},\dots
$$
称为原序列 $$\left\{x_n\right\}$$ 的一个子序列。

打个比方，我们有 $$x_1,x_2,x_3, \cdots$$，子序列就可以是 $$x_1,x_3, \cdots$$。要点在于：可以跳过原序列某些元素，但绝不能乱序！与序列密切相关的概念是"收敛"：

[收敛序列]
一个欧氏空间中的 $$\left\{x_i\right\}_{i=1}^{\infty}$$ 向 $$x$$ 收敛，当且仅当
$$
\forall \epsilon>0, \, \exists N \in \mathbb{N} \text{ s.t. }  \forall i \geq N, \, d(x_i, x) < \epsilon.
$$

换句话，序列元素可与收敛极限任意近。考虑实数序列 $$\left\{\frac{1}{i}\right\}$$，它向零收敛。你随便定很小的一个 $$\epsilon$$，我都能取一个足够大的 $$N$$， 使得从元素 $$\frac{1}{N}$$ 开始，每个元素与零的距离都比 $$\epsilon$$ 小。


要介绍所有赫赫有名的序列，那我自己得先上几年大学再说。但仅在欧氏空间中，我们最关心的毋庸置疑是柯西序列：

[柯西序列]
我们称一个序列 $$\left\{x_i\right\}$$ 为柯西序列，当且仅当它满足
$$
\forall \epsilon, \exists K \in \mathbb{N} \text{ s.t. } \forall k,j \geq K, \; d(x_k, x_j) < \epsilon
$$

大家须注意到定义5.1与5.2的根本差别：柯西序列中元素之间（而非元素与收敛极限，它不一定收敛！）可以任意近。当然在欧氏空间中，柯西序列就是收敛序列，结论在前：


在欧氏空间中，柯西序列必收敛。


这条定理当作单纯记下便可（好用，好用）。但如果你实在无法抵抗证明的诱惑，那我们先略做准备再开始。


[实数完备性公理]
实数柯西序列必收敛。


进一步有了这条公理（即无法且无需证明），证明豁然开朗。


令序列 $$\left\{x^m\right\}_{m=1}^{\infty} \in \mathbb{R}^n$$ 为柯西序列，任定一个 $$\epsilon >0$$，再令 $$x^j,x^k$$ 为满足 $$d(x^k,x^j)<\epsilon$$ 的两点。回忆章节1.2的第一条，可将它们写为坐标形式，即 $$(x^j_1, x^j_2, \cdots, x^j_n), \; (x^k_1, x^k_2, \cdots, x^k_n).$$易得 
$$
\vert x^j_i-x^k_i\vert \leq \sqrt{\sum_{i=1}^{n} (x^j_i-x^k_i)^2}=d(x_j,x_k)<\epsilon,
$$
根据定义5.2，$$\left\{x^m_i\right\}_{m=1}^{\infty}$$ 为实数柯西序列（由每个原序列的元素的第 $$i$$ 个实数坐标构成）。又由公理5.3，该实数序列收敛。令 $$x^m_i \to x_i$$，我们得到 $$x=(x_1,x_2,\cdots,x_n)$$。不难看出，这就是柯西序列的收敛极限。证毕？用“不难看出”达到结论是一个极差习惯。任定一个 $$\epsilon>0$$，对于每个收敛极限 $$x_i$$，$$\exists N_i \in \mathbb{N} \text{ s.t. } \forall m \geq N_i, \, d(x^m_i,x_i)=|x^m_i-x_i|<\epsilon,$$这是由实数序列收敛得到的。令 $$N=\sup \left\{N_1, N_2., \cdots, N_n\right\}$$，则 
$$
\forall m \geq N, \, d(x, x^m)=\sqrt{\sum_{i=1}^{n}(x_i-x^m_i)^2}<\sqrt{n \times \epsilon^2}=\sqrt{n}\times \epsilon. 
$$
（这个结论较为显然，$$d(x_i^m,x_i)=|x_i^m-x_i|<\epsilon$$ 若要对所有的 $$i$$ 都成立，则需要一个足够大的 $$m$$：$$m\geq \sup\{N_1, N_2., \cdots, N_n\}$$ 就是足够大的。）既然 $$\epsilon$$ 可以任意小，$$\sqrt{n}\times \epsilon$$ 亦可，故原柯西序列向 $$x$$ 收敛，证毕。


对序列逐坐标取收敛极限，得到收敛坐标——这是个经典的思路。

已知在任意空间中，$$d(x,y)\leq d(x,z)+d(y,z)$$都成立 （任意维度的三角不等式），你能否证明欧氏空间中的收敛序列也必是柯西序列？这便是大名鼎鼎的“柯西收敛判断”：**欧氏空间的序列收敛，当且仅当（等价于）它是柯西序列**。

# 闭集与序列收敛
上次习题的答案：
[求证：欧氏空间的收敛序列是柯西序列]
考虑 $$\mathbb{R}^n$$ 中一个序列 $$\left\{x_i\right\}$$ 向 $$x$$ 收敛。由收敛序列定义，$$\forall \epsilon>0, \, \exists N \in \mathbb{N}$$ s.t. $$\forall n\geq N, \, d(x_n,x)<\epsilon$$。任取 $$j,k \geq N$$，有 $$d(x_j,x) <\epsilon, \, d(x_k,x)<\epsilon$$。由三角不等式：
$$
d(x_j,x_k)\leq d(x_j,x)+d(x_k,x)<2\epsilon.
$$
既然 $\epsilon$ 可任意小，$2\epsilon$ 也可任意小——二者等价。故 $\{x_i\}$ 满足柯西序列定义，证毕。


步入正题：我们可以用序列的收敛给欧氏空间中的闭集下一个真正有用的定义。

[闭集]
我们称 $$S \subset \mathbb{R}^n$$ 为一个闭集，当且仅当：对于所有收敛的 $$ \left\{x_i\right\} \subset S$$ 且其极限为 $$x \in \mathbb{R}^n$$，我们有 $$x \in S$$。


和以往的定义不同，6.1可以，也需要被证明——我们需要两步准备工作。
[当且仅当很麻烦！]
当我们被要求证明一个“当且仅当”的命题时，我们上的火车就不是单程的了。“当且仅当”意味着等价性——需要说明由A可得B，由B同时可得A。熟悉吗？没错，上章节柯西收敛判定的证明完全如此：柯西序列 $\to$ 收敛序列，收敛序列 $\to$ 柯西序列。


[必要的掉头]
一个命题“如果A，那么B”的等价形式是“如果不B，那么不A”，也被称为原命题的逆否。考虑这句话：“如果下雨，那么地变湿”，是不是等价于“如果地不湿，那么没下雨”？当一个方向的证明很棘手，我们可以考虑它的逆否方向（prove by contrapositive），这是一个必要的掉头。

我们开始。

假设 $$\mathbb{R}^n$$ 中的集合 $$S$$ 为闭集，我们需要证明：对于所有收敛的 $$ \left\{x_i\right\} \subset S$$ 且其极限为 $$x \in \mathbb{R}^n$$，有 $$x \in S$$。我们使用反证法。为了达到矛盾，设 $$x \notin S$$，即 $$x \in S^c$$。由闭集的一般定义，$$S^c$$ 为开集，即 $$\exists \epsilon>0$$ 使得 $$B_\epsilon (x) \subset S^c$$。由 $$ \left\{x_i\right\} \subset S$$

$$
\forall x_i \in \{x_i\}, \, d(x_i, x) > \epsilon.
$$ 
然而由定义3.1，$$\forall \epsilon>0, \, \exists N \in \mathbb{N} \, s.t. \, \forall i \geq N, \, d(x_i, x) < \epsilon,$$ 矛盾。\\
现在假设对于所有收敛的 $$ \left\{x_i\right\} \subset S$$ 且其极限为 $$x \in \mathbb{R}^n$$ 有 $$x \in S$$，我们需要证明 $$S$$ 是闭集。我们采用逆否命题法证明，即假设 $$S$$ 不闭，证明存在一个极限为 $$x \notin S$$ 的 $$ \left\{x_i\right\} \subset S$$。由 $$S$$ 不闭，$$S^c$$ 不开。取定义2.2的否命题，$$\exists x' \in S^c$$ s.t. $$\forall \epsilon>0, B_\epsilon (x') \nsubseteq S^c$$，或等价的，$$B_\epsilon \cap S \neq \emptyset$$。若能构造一个 $$S$$ 中的序列，使得其向 $$x'$$ 收敛，证明便完成。令 $$\left\{x'_i\right\}$$ 满足 $$x'_i \in B_{\frac{1}{i}} (x') \cap S.$$因为对于任意 $$i$$ 有 $$d(x'_i, x') < \frac{1}{i}$$，那么 $$\forall \mu>0, $$ 我们都能找到足够大的 $$N$$ s.t. $$\forall i \geq N, \, d(x'_i, x') < \mu $$。由定义5.2，$$x'$$ 为该序列极限。


# 一些定理
这部分强度老大了，完全可以选择性的阅读。定理的排序依托难度进行。

[有界单调实数序列必收敛]
对于有界序列 $$\left\{x_i\right\}$$，若满足 $$\forall k>j$$，$$x_k \geq x_j$$，则该序列收敛。



我们采用对称证明：先考虑单调不减的实数序列。由有界性，$$\exists M >0 \text{ s.t. } \left\{x_i\right\} \subset B_M (0)=(-M,M)$$，可得 $$\forall x_i, x_i<M$$。由定义，$$M$$ 为序列上界，再由定义，$$\sup \left\{x_i\right\} \leq M$$。令 $$x=\sup \left\{x_i\right\}$$，我们想说明 $$x$$ 为序列的极限。注意到任取一个 $$\epsilon>0$$， $$x-\epsilon$$ 不是序列的上界，因上确界最已是小上界。故存在 $$x_n \in \left\{x_i\right\} \text{ s.t. } x_n > x-\epsilon$$。由单调不减，对于所有 $$m>n$$，

$$x_m \geq x_n > x-\epsilon$$

再次由上确界定义，$$\forall m,$$ $$x \geq x_m$$。故对于所有 $$m>n$$，

$$x > x_m-\epsilon$$

联系不等式（1）与（2），我们有 $$\vert x-x_m\vert=d(x,x_m)<\epsilon$$。由定义5.1，$$x$$ 为极限。对于单调不增序列，相同的论述可证明其收敛 （by symmetric argument），证毕。


[鸟巢定理（Nested Cells Theorem）]
对于一系列无穷嵌套的闭区间 $$[a_1,b_1] \supset [a_2,b_2] \supset \cdots$$，交集 $$\bigcap_{i=1}^{\infty} [a_i,b_i]$$ 为非空区间（即形如[a,b])。



考虑序列 $$\left\{a_i\right\}, \left\{b_i\right\}$$，注意到二者分别单调不减、单调不增（由区间嵌套关系），又由于对所有 $$i$$ 有 $$a_1 \le a_i \le b_i \le b_1$$，故二者均有界。由定理6.1，两序列均收敛，令极限分别为 $$a\text{、}b$$ 。现在只需说明: $$b \geq a$$，即可完成区间非空的证明。考虑序列 $$\left\{b_i-a_i\right\} \subset [0,b_1-a_1]$$ ，闭集定义会告诉我们：若序列收敛，极限属于闭区间 $$[0,b_1-a_1]$$。若我们能证明极限正好是 $$b-a$$，则 $$b-a\geq 0, \, b \geq a$$ 就得以说明了。注意到 $$\forall \epsilon>0, \exists N \in \mathbb{N} \text{ s.t. } d(a_i,a)=\vert a_i-a\vert<\epsilon, \, d(b_i,b)=\vert b_i-b\vert<\epsilon$$。因此，

$$
\begin{aligned}
d((b-a),(b_i-a_i))
&= \vert(b-a)-(b_i-a_i)\vert \\
&= \vert(b-b_i)+(a_i-a)\vert \\
&\le \vert b_i-b\vert + \vert a_i-a\vert \\
&= 2\epsilon.
\end{aligned}
$$

既然 $$\epsilon$$ 可以任意小，$$2\epsilon$$ 亦可任意小——二者等价。那么再次由收敛序列定义，$$\left\{b_i-a_i\right\} \to b-a \geq 0,$$证毕。

无限嵌套下去，区间长度不该趋近于零，使得最终交集退化成单点？但如果让 $$[a,b]$$ 无限自我嵌套（我从没规定过是一串真子集），最终交集仍是自己。几乎trivial到令人哭笑不得——别忘了我们也可用真子集定义“嵌套”。所以我们害怕的不是自我嵌套，而是 
$$
{\boldsymbol{ \left[ a,\, b+\frac{1}{n} \right] }}.
$$
嵌套的闭区间是一串真子集，无限交集也是标准区间 $$[a,b]$$ 而非单点——没办法了？直觉误人。当然这又引出了一个新的命题：

当嵌套闭区间的长度趋近于零时，无限交集退化为单点。

反证！

我们已经证明了嵌套闭区间的收敛性，只需说明：只存在一个点属于 $$[a,b]$$ 即可。为了达到矛盾，假设存在 $$x,y \in [a,b]$$，且不失一般性的（assuming without the loss of generality）：$$y>x$$。令 $$y-x=\delta$$，由 $$b_i-a_i \to 0$$，

$$
\exists N \text{ s.t. } \forall n \geq N, \, b_n-a_n<\delta=y-x.
$$

由无限交集定义，$$\forall i \in \mathbb{N}$$，$$x,y \in [a_i,b_i]$$，或等价的，$$y-x \leq b_i-a_i$$。代入 $$i=n$$（这显然无争议，由于该不等式对所有 $$i$$ 成立）有 $$y-x \leq b_n-a_n$$，同时联系不等式（3），得到 $$y-x \leq b_n-a_n < y-x, \forall n \geq N:$$ 一个好笑的矛盾。


这个定理很重要：
[Bolzano-Weierstrass定理]
对于任意有界 $$\left\{x_i\right\} \in \mathbb{R}^n$$，它都有至少一个收敛子序列。

[柯西序列证明]
由有界性，$$\exists M>0 \text{ s.t. }B_M(0) \supset \left\{x_i\right\}$$。以原点为中心，$$2M$$ 为边长做 $$n$$ 维立方体 $$Q_0=[-M,M]^n \supset B_M(0)$$。注意到 $$Q_0$$ 的直径（即最长对角线）为 $$\sqrt{n} M$$（边长为$$2M$$的正方形的对角线为 $$2\sqrt{2} M$$，正方体的对角线为 $$2\sqrt{3} M$$，以此类推）。沿象限将立方体平分为 $$2^n$$个全等的子立方体（例如在二维，可以切成四个小正方形；三维可切成八个正方体，以此类推）。此时必有一个子立方体中包括无穷个序列元素；若不然，即所有子立方体中元素有穷，则序列元素有穷，矛盾。令包含无穷元素的子立方体为 $$Q_1$$，其直径为 $$\frac{2\sqrt{n}M}{2}$$。在其中任选一个原序列 $$\left\{x_i\right\}$$ 中的元素作为 $$x_{i_1}$$。重复该切割-选点过程 $$m$$ 次，我们发现此时的子立方体  $$Q_m$$ 的直径为 $$\frac{2\sqrt{n}M}{2^m}=\frac{\sqrt{n}M}{2^{m-1}},$$
既然后续子列元素只能在 $$Q_m$$ 中任选，所有元素之间的距离必定不超过 $$Q_m$$ 直径，故 $$\forall j,k \geq m, d(x_{i_j},x_{i_k}) < \frac{\sqrt{n}M}{2^{m-1}}.$$ 我们想说明：现在的挑选方法给我们的正是一个柯西序列——它在欧氏空间中收敛！任意定一个 $$\epsilon>0$$，假设 $$\frac{\sqrt{n}M}{2^{m-1}} \leqslant \epsilon$$。两遍各取自然对数，得 $$m \geq 1+\frac{(lnM-ln\epsilon)\sqrt{n}}{ln2}.$$很显然，对于任意 $$\epsilon$$，我们永远可以找到这样足够大的 $$m$$ 使得 $$j,k>m$$ 时，$$d(x_{i_j},x_{i_k})<\epsilon$$。由定义，我们构造的子序列为收敛的柯西序列，证毕。


# 一些有趣的延伸
鸟巢定理是否可以被拓展到 $$n$$ 维？请各位想象一个正方形，里面套了一个更小的，再套了一个更小的...无限嵌套，直觉告诉我们：正方形收敛，并且收敛向单点。这次别怀疑直觉！不妨脱离维度限制，如果嵌套的是正方体，四维正方体，$$n$$ 维正方体？？结果不改变！
[康托交集定理]
对于一系列 $$\mathbb{R}^n$$ 中嵌套的闭立方体 $$Q_1 \supset Q_2 \supset \cdots$$，若立方体直径趋近于零，它们的交集 $$\bigcap_{i=1}^{\infty}$$ 为单点集。

别意外：把区间想象成边长，你会发现立方体实则由区间构成。我们自然可以想象正方形随着区间的缩小而缩小。既然鸟巢定理告诉我们：每个实数轴（维度）上的闭区间若无限嵌套且长度趋近于零，会向单点收敛，我们会得到 $$n$$ 条轴上的 $$n$$ 个收敛极限。它们共同可以组成一个 $$n$$ 维坐标，它不就是立方体收敛的极限？这就是“逐维度击破“的思想。

对于第 $$k$$ 个立方体 $$Q_k$$，令 $$a_k^i= \inf \{x_i \mid x\in Q_k\}$$，再令 $$b_k^i=\sup \{x_i \mid x\in Q_k\}$$$, $$i$$ 表示某个维度。这相当于我们找到了立方体在第 $$i$$ 个维度（实数轴）上的上限与下限。不难发现，闭区间 $$[a_k^i,b_k^i]$$ 随着立方体的嵌套而嵌套，且长度随之趋近于零（直径作为内部最大长度若趋近于零，立方体边长，即区间长度，也一定趋近于零），由鸟巢定理：$$\bigcap_{k=1}^{\infty} [a_k^i,b_k^i]=x^i  \in [a_k^i,b_k^i], \, \forall k$$，且对于每个 $$i$$ 都如此。令 $$x=(x^1,x^2,\cdots,x^n)$$，我们说明它是唯一交集。注意到对于任意 $$k,i$$，立方体在 $$i$$ 维度上的长度为 $$b_k^i-a_k^i$$，故可以定义序列 $$\left\{x_k\right\}_{k=1}^{\infty} \subset Q_k$$，使得序列元素满足 $$\vert x_k^i-x^i\vert\leq b_k^i-a_k^i \to 0$$。所以对于每一个维度 $$i$$，$$x_k^i \to x^i$$，必然有 $$x_k \to x$$。由 $$Q_k$$ 闭，收敛极限满足 $$x \in Q_k$$，$$\forall k$$，$$x$$ 属于交集 $$\bigcap_{k=1}^{\infty} Q_k$$。我们现在说明交集内只存在 $$x$$。假设存在某个 $$y\in \bigcap_{k=1}^{\infty} Q_k$$，且 $$y\neq x$$。由立方体直径 $$\mathrm{diam}(Q_k)$$ 趋近于零，$$\exists N \in \mathbb{N}$$ s.t. $$d(x,y)>\mathrm{diam}(Q_N)$$。然而由交集定义，$$x,y\in Q_N$$，故 $$d(x,y) \leq \mathrm{diam}(Q_N)$$（二者距离必定不超过立方体内部最长距离），明显矛盾！证毕。

在思考立方体嵌套的过程中，是否有想到我们在证明Bolzano-Weierstrass定理时的切割-选元素技巧？真巧，我们同样构造了嵌套立方体。那么不就豁然开朗了？最后再看个短证吧：

继续定理7.4证明中的切割-选元素过程，注意到我们构造了一系列嵌套闭立方体 $$Q_0 \supset Q_1 \supset \cdots$$。由康托交集定理，立方体向单点 $$x$$ 收敛。因此，我们构造的子列 $$\left\{x_{i_m}\right\}$$ 必向 $$x$$ 收敛，证毕。


# $\epsilon$语言

收束。是什么把数学和哲学区分开来？除了讨论的内容真正有意义以外，语言的绝对严格也是重要一环。魏尔斯特拉斯（Karl Weierstrass）早在19世纪便提出了 $$\epsilon$$ 语言：用可以任意小的变量打穿所有定义。你们对这个形式绝对不陌生了： “对于所有 $$\epsilon$$，存在一个 $$N$$ 使得...”，这位就是一种 $$\epsilon$$ 语言家族中的 $$\epsilon-N$$ 成员。该语言的伟大不言而喻，陶哲轩（Terence Tao）本人命名自己的实分析教材为 “an Epsilon of Room”，“The title of this book is a reference to a fundamental trick in soft analysis: the epsilon regularisation argument. [...] In many situations, one can obtain control over a quantity by first regularising it slightly with an epsilon of room, and then letting epsilon go to zero at the end of the argument.”。在魏尔斯特拉斯之前，数学家若要表示序列的收敛，会有多麻烦？然而我们现在有
$$
\forall \epsilon>0, \, \exists N \in \mathbb{N} \text{ s.t. }  \forall i \geq N, \, d(x_i, x) < \epsilon.
$$
这就是语言严格性的张力。

# 完
希望读到这里的各位在阅读所有的定理，证明，讲解，我打的比喻的过程中或多或少感受到了数学的乐趣。这份文档旨在用最简单直接的语言讲通透大一实分析最重要的几个结论，如果你觉得还不错，蛮有趣——别埋没！推荐教材：陶哲轩实分析/Baby Rudin。
$$\varepsilon$$
