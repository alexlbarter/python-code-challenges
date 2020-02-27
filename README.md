# Python Code Challenges

A collection of code challenges that I have completed in Python.

## Sum digits of number
###### [/sum-digits-of-number](sum-digits-of-number)

> Given a positive integer `n`, sum all of its digits. Repeat this until the result is one digit long, then return it.

*Source: [edabit.com](https://edabit.com/challenge/veCWQHJNgeZQCNbdY)*

## Rearrange the number
###### [/rearrange-the-number](rearrange-the-number)

> Given a number `n`, return the **difference** between the *maximum* and *minimum* numbers that can be formed when the digits are rearranged.

*Source: [edabit.com](https://edabit.com/challenge/jwzAdBnJnBxCe4AXP)*

## Shiritori
###### [/shiritori](shiritori)

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
###### [/simplified-fractions](simplified-fractions)

> Create a function that returns the simplified version of a fraction
>
> Examples:
> ```
> simplify("4/6") → "2/3"
> simplify("10/11") → "10/11"
> simplify("100/400") → "1/4"
> simplify("8/4") → "2"
>
> If an improper fraction can be simplified into an integer, the function should do so.

*Source: [edabit.com](https://edabit.com/challenge/vQgmyjcjMoMu9YGGW)*
