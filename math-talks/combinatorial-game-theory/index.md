---
layout: default
title: Combinatorial Game Theory
permalink: /math-talks/combinatorial-game-theory/
toc: true
---

# Combinatorial Game Theory

## 1 Introduction

Let's play a game.

- take a bunch of fruit from the dining hall – say 1 apple, 2 bananas, 3 oranges, 4 pears, and 5
	mangoes – and sort them by the kind of fruit they are
- take turns eating the fruit
	- select one type of fruit, and eat as many of it as you want
	- but you need to eat at least one
- the person who eats the last piece of fruit wins

This is an example of a game of **Nim**.

Okay, now stop imagining and actually play the game with someone!

**Combinatorial game**

- no luck involved
	- this separates it from blackjack and poker and go fish
- both players have complete information about the situation of the game: nothing is hidden
- the players take turns making moves
- examples: chess, tic-tac-toe, Connect 4, and go
- since these games have no chance, there do exist strategies for "perfect play"
	- tic-tac-toe: when both players play optimally, neither player will win – a **solved** game
	- Connect 4 has been solved as well, but with significant help from computers
	- chess and go are so complex that we still do not know what the best strategies are
		- this might be a good thing, because it is what makes them fun!

**Impartial game**

- both players are allowed the exact same set of moves
	- compare this to chess: you are not allowed to move your opponent's pieces around the board!
- Nim is impartial; the others above are not

## 2 The Subtraction Game

An example simpler than Nim.

- we have all the fruit again, but we do not distinguish between the different kinds
- on each turn, you can choose to eat one or two pieces of fruit
- the person who eats the last piece wins
- the available moves are elements of the set $$S = \{1, 2\}$$

**Directed graph**

- the possible positions are the vertices
- the possible moves between positions are the directed edges

![Directed graph of the subtraction game: each position n points to n−1 and n−2](images/subtraction-game-graph.svg){: width="100%"}

Working backwards:

- to win the game, you have to be the one that moves to the 0 vertex
- move to 1? the opponent can move to 0, so not a good idea
- move to 2? no, for the same reason
- move to 3? your opponent must move to 1 or 2, and you can win right afterwards
- 4 and 5 are unsafe to move to, while 6 is safe
- in general, the safe positions to move to are those which are divisible by 3

## 3 P-positions and N-positions

### 3.1 Definitions

"Safe" really meant "safe to move *to*", as opposed to "safe to move *from*". To avoid this
ambiguity:

**P-position**

- a position that is good to move to
- the **p**revious player can win by playing optimally

**N-position**

- a position that is bad to move to
- the **n**ext person to play can win by playing optimally

In the subtraction game:

- P-positions: all the positions which are divisible by 3
- N-positions: the rest

### 3.2 Criteria {#criteria}

To solve an impartial game, we have to identify the P-positions and the N-positions. The following
properties need to be satisfied:

1. Every possible position is either a P-position or an N-position (but not both).
2. From every N-position, it is possible to move to a P-position.
3. From any P-position, it is not possible to move to another P-position.
4. The ending position is a P-position.

The strategy:

- on our turn, we move to a P-position
- the opponent has no choice but to move to an N-position
- but then we can move to another P-position, and so on
- this only works if we start by moving from an N-position
	- if we start from a P-position, then the opponent can use that strategy
	- offer to let your opponent make the first move!

## 4 Back to Nim

A position in Nim is an unordered $$n$$-tuple.

- (1 apple, 2 bananas, 3 oranges, 4 pears, 5 mangoes) $$= (1, 2, 3, 4, 5)$$
- all piles are nonempty, so all variables are positive integers

### 4.1 The simplest cases

- the ending position is $$()$$, when there are no piles left
	- this has to be a P-position
- anything that moves to $$()$$ must be an N-position
	- these are precisely the positions with 1 nonempty pile
	- the next player can just remove everything from that pile
- $$(1, 1)$$: the moves are forced, $$(1, 1) \longrightarrow (1) \longrightarrow ()$$
	- the second player wins, so $$(1, 1)$$ is a P-position
	- from $$(1, 1)$$, we cannot find a move to another P-position
- $$(1, a)$$ with $$a \geq 2$$ is an N-position
	- the next player can move to $$(1, 1)$$ and win
- with two piles, the P-positions are the ones for which the two piles have equal size
	- if the other player removes $$k$$ from one pile, you remove $$k$$ from the other
	- the two piles always have the same size after your move

So now, we have:

- P-positions: $$()$$; $$(a, a)$$
- N-positions: $$(a)$$; $$(a, b)$$ with $$a \neq b$$

### 4.2 Positions with 3 piles

Now it is not so easy. Using our current list of P and N positions, where the smallest pile has
number $$s$$:

| $$s$$ | P-positions |
| :---: | --- |
| 1 | (1, 2, 3); (1, 4, 5); (1, 6, 7); (1, 8, 9); (1, 10, 11); (1, 12, 13); ... |
| 2 | (2, 4, 6); (2, 5, 7); (2, 8, 10); (2, 9, 11); (2, 12, 14); (2, 13, 15); ... |
| 3 | (3, 4, 7); (3, 5, 6); (3, 8, 11); (3, 9, 10); (3, 12, 15); (3, 13, 14); ... |
| 4 | (4, 8, 12); (4, 9, 13); (4, 10, 14); (4, 11, 15); ... |
| 5 | (5, 8, 13); (5, 9, 12); (5, 10, 15); (5, 11, 14); ... |

Don't just take my word for it – try to build these lists for yourself!

### 4.3 Looking for a pattern

There is a pattern, but it is very hard to spot. What happens if you write the positions of Nim in
**binary**?

| Decimal | (1, 4, 5) | (2, 4, 6) | (3, 12, 15) | (4, 8, 12) | (5, 9, 12) |
| --- | --- | --- | --- | --- | --- |
| Binary | (1, 100, 101) | (10, 100, 110) | (11, 1100, 1111) | (100, 1000, 1100) | (101, 1001, 1100) |

Do you notice anything? **Don't open the solution below until you've identified the pattern!**

### 4.4 The solution

<details markdown="1">
<summary>I've found the pattern – click to show the solution</summary>

In all P-positions:

- for each digit written in base 2, an even number of the numbers in the $$n$$-tuple have a 1 for
	that digit
- put another way: convert each number to binary and add them together
	- add normally, except we forget to carry over to the next digit
	- for a P-position, we end up with a "sum" of zero

**Nim sum**

- "binary addition without carrying"
- the symbol $$\oplus$$ denotes the operation

$$
\begin{array}{r}
101 \\
1001 \\
\oplus\ 1100 \\
\hline
0000
\end{array}
\qquad\qquad
\begin{array}{r}
11 \\
1011 \\
\oplus\ 1110 \\
\hline
0110
\end{array}
$$

- $$(5, 9, 12) = (101, 1001, 1100)$$ is a P-position, and $$5 \oplus 9 \oplus 12 = 0$$
- $$(3, 11, 14) = (11, 1011, 1110)$$ is an N-position, and $$3 \oplus 11 \oplus 14 = 6 \neq 0$$
- this works in general, not just for 3 piles

**Theorem 1.** If $$(a_1, a_2, \ldots, a_n)$$ is a position in Nim, then it is a P-position if and
only if

$$a_1 \oplus a_2 \oplus \cdots \oplus a_n = 0$$

*Proof.* Exercise!

Remember, you have to prove this for yourself! What counts as a proof? Show that the conditions in
[Section 3.2](#criteria) are satisfied:

- properties 1 and 4 are easy
- see if you can prove 2 and 3 are true!

</details>

## 5 Some other impartial games

In all the ones listed below, the game will eventually end, and one of the players must win – no
draws.

### 5.1 The Subtraction Game

- we can find a lot of interesting results when we change the set of possible moves
- there is a clear generalization of our winning strategy to $$S = \{1, 2, \ldots, n\}$$ for all
	$$n \in \mathbb{N}$$
- what about $$S = \{1, 3\}$$, $$S = \{2, 3, 5, 7\}$$, $$S = \{10, 11, 12\}$$,
	$$S = \{\text{powers of } 2\}$$?
- from some nonzero positions, it might not be possible to make a valid move
	- new rule: if you cannot make a valid move on your turn, then you lose

### 5.2 Chomp

- take turns eating a rectangular chocolate bar, broken up into $$m$$ rows and $$n$$ columns
- you start eating from the bottom-right
- whenever you eat a piece of the bar, you have to eat everything that is below it or to its right
- whoever eats the top-left piece loses!

A $$3 \times 5$$ game (from Wikipedia!). The black dot is the top-left piece, and dashed circles
are the pieces eaten on that turn:

![Example 3×5 game of Chomp](images/chomp-3x5-example.svg){: width="100%"}

Player A loses because he/she has to eat the last piece on the next turn.

### 5.3 The Rook Game

- the board has one corner at the bottom-left, but extends infinitely both right and upwards
- we place some rooks (from chess) on some of the squares
- on each turn, choose one rook, and move it to the left or downwards, with a valid rook move
- the person who cannot make a valid move loses
	- the game ends when all the rooks are at the bottom-left square
- we can replace the rook with other chess pieces
- we can make the chessboard a "board" in 3 dimensions or higher if we wanted to!

### 5.4 Misère Nim

- identical to Nim, except: the person who makes the last move **loses**
- this changes the game quite a bit, since $$(1)$$ is now a P-position
- you can take any "normal" impartial game and make a Misère version of it
	- "normal": the player who makes the last move wins
	- to keep the convention of "person who cannot make a legal move loses", alter the game to not
		allow removing the last piece

## 6 Sums of games

Take any two impartial games. Then their *sum* is also an impartial game!

- play the two games side by side
- on each turn, you choose one (and only one) of the two games, and make a move in it
- the winner is the last player who can make a legal move

This allows us to create many new impartial games by combining old ones:

- the sum of a game of Nim with a game of Chomp
- add on a game of the Rook Game
- add on a second game of Chomp!

## 7 Analyzing all these games

- we can identify P-positions and N-positions with the method we used in the Subtraction Game and
	in Nim
- but there's actually an even easier way:

**Theorem 2.** (Sprague–Grundy) Every impartial game is equivalent to Nim.

Your task:

- understand what this theorem is saying exactly
- prove it
- apply it to beat people in impartial games from now on!

Good luck!
