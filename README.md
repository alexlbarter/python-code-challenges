# Python Code Challenges

A collection of code challenges that I have completed in Python.

## Sum digits of number
###### [/challenges/sum-digits-of-number](challenges/sum-digits-of-number)

> Given a positive integer `n`, sum all of its digits. Repeat this until the result is one digit long, then return it.

*Source: [edabit.com](https://edabit.com/challenge/veCWQHJNgeZQCNbdY)*

## Rearrange the number
###### [/challenges/rearrange-the-number](challenges/rearrange-the-number)

> Given a number `n`, return the **difference** between the *maximum* and *minimum* numbers that can be formed when the digits are rearranged.

*Source: [edabit.com](https://edabit.com/challenge/jwzAdBnJnBxCe4AXP)*

## Shiritori
###### [/challenges/shiritori](challenges/shiritori)

> Implement an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:
> 
> 1. **First character** of *next* word must match **last character** of *previous* word.
> 2. The word must not have been said already.
>
> Example:
> ```
> ["word", "dowry", "yodel", "leader", "righteous", "serpent"]  # valid
> ["motive", "beach"]  # invalid - beach should start with an "e"
> ["hive", "eh", "hive"]  # invalid - "hive" has already been said
> ```
> 
> Write a Shiritori class with two instance attributes: `words`, a list of words that have already been used and `game_over`, and two instance methods: `play` and `restart`. 
> 
> * The `play` method should take a word as an argument, check if it follows the rules, and if so, add it to the `words` list.
> If it breaks either rule, it should set `game_over` to `True`, and return `"game over"`.
> 
> * The `restart` method should reset the `words` list, and set `game_over` to `False`.

*Source: [edabit.com](https://edabit.com/challenge/dLnZLi8FjaK6qKcvv)*

## Simplified fractions
###### [/challenges/simplified-fractions](challenges/simplified-fractions)

> Create a function that returns the simplified version of a fraction
>
> Examples:
> ```
> simplify("4/6") → "2/3"
> simplify("10/11") → "10/11"
> simplify("100/400") → "1/4"
> simplify("8/4") → "2"
> ```
>
> If an improper fraction can be simplified into an integer, the function should do so.

*Source: [edabit.com](https://edabit.com/challenge/vQgmyjcjMoMu9YGGW)*

## Primitive Pythagorean triples
###### [/challenges/primitive-pythagorean-triples](challenges/primitive-pythagorean-triples)

> Given an unordered list of three numbers, first check if they are a Pythagorean triple, i.e.
> ```
> a^2 + b^2 = c^2, c > a, b
> ```
> Return `True` if all of the numbers are pairwise coprime, i.e. each pair of numbers share no factors, `False` otherwise.
>
> Examples:
> ```
> is_primitive([4, 5, 3]) → True
> is_primitive([7, 12, 13]) → False
> is_primitive([39, 15, 36]) → False
> is_primitive([77, 36, 85]) → True
> ```

*Source: [edabit.com](https://edabit.com/challenge/vLLXeQH5tgyvbzYZS)*

## The dice game
###### [/challenges/dice-game](challenges/dice-game)

> Four friends are playing a simple dice game (players are denoted `p1`, `p2`, `p3` and `p4`).
> In each round, all players roll a pair of six-sided dice. The player with the lowest total score is removed.
> If the lowest score is shared by two or more players, the player in that group with the lowest score from their *first* die is removed.
> If the lowest score is still shared (i.e. two or more players have the same rolls in the same order), then *all* players roll again.
> This process continues until one player remains.
> Given a list of scores only (given in player order for each round), return the winning player.
>
> Example game:
> ```
> dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) > ➞ "p1"
>
>              p1      p2      p3      p4
> Round 1 -> (6, 2), (4, 3), (3, 4), (5, 4)  Player 3 removed.
> Round 2 -> (3, 5), (1, 5),         (4, 3)  Player 2 removed.
> Round 3 -> (1, 5),                 (1, 5)  No lowest score, players roll again.
> Round 4 -> (5, 6),                 (2, 2)  Player 1 wins!
> ```

*Source: [edabit.com](https://edabit.com/challenge/YjwJ6BfujKtmuTMqW)*
