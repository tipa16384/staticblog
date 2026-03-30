---
date: '2022-12-21T22:08:13-05:00'
draft: false
title: "Advent of Code Day 21 -- Monkey Math"
author: "Tipa"
summary: "Hey, monkeys again! Shouting! Luckily, we have an elephant to interpret. I feel... morally uneasy about today's solution."
categories:
  - "Advent of Code"
tags:
  - "Elephant"
  - "Monkey"
  - "Python"
  - "Sympy"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-21-21.48.47-A-large-group-of-monkeys-shouting-at-a-woman-wearing-a-Christmas-stocking-cap-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-21-21.48.47-A-large-group-of-monkeys-shouting-at-a-woman-wearing-a-Christmas-stocking-cap-by-Bob-Eggleton-detailed-and-intricate.png"
---
Hey, monkeys again! Shouting! Luckily, we have an elephant to interpret. I feel... morally uneasy about today's solution.
<!--more-->

The monkeys that stole all our stuff awhile ago are back -- and [they are just standing around shouting](https://adventofcode.com/2022/day/21). Well, at least they aren't stealing stuff. A nearby elephant let me know that they saw I was lost and thought I should solve a really complicated algebra problem to get their help.

Well, sure!

The puzzle input is a symbol dictionary -- like 

`root: vtsj + tfjf
mqjw: 5
qplt: tpfl * vmpn
dpsb: 2
`

It starts at **root**, and then you substitute that with **vtsj + tfjf**, and then substitute those terms with their expansions until you have a super long expression to solve. My first instinct was to use a stack parser, which is the usual way to do these things. My *second* instinct was just to make the whole thing into an expression that Python could evaluate, and just let Python worry about it. This is exactly what I used to solve Part 1 before work this morning.

I do occasionally peek in on Reddit while at work, and though I didn't look at anyone's code, I saw people mention several times that the **sympy** Python library could handle these complicated algebra problems easily.

So this is my moral dilemma: I was going to solve Part 2 (which introduces a variable for which we should solve) by just writing that stack parser, and just preserving the variable, and then simplifying the resulting equation by hand. I could also solve Part 1 this way, first, which would make it easier to port this to, say, Java, or other languages without such a large number of useful libraries.

But then, I thought I should really learn **sympy**, as it looks incredibly useful. And since I am writing up these AoC solutions, maybe someday in the future, someone will stumble upon this post and find out about it, too. Nobody would find my stack parser helpful -- but maybe this would be good to know.

And so here we are. I rewrote Part 1 to use sympy, and then did Part 2 in it as well.

**Python 3.11**

From **sympy**, **symbols** is how you define symbols (*x* in this case), **solve** solved equations for a symbol, and **simplify** simplifies equations. Part 1 uses simplify, Part 2 uses solve.

There is a little bit of magic to set up Part 2, but this is one of the shortest, if not the shortest, solution, and I feel a little guilty that I let a library do the heavy lifting when I could have done it myself with a little more effort.

```
from sympy import symbols, solve, simplify

def expand(s):
    if s.isnumeric() or s == 'x': return s
    toks = s.split()
    return '(' + expand(symbols_dict[toks[0]]) + ' ' + toks[1] + ' ' + expand(symbols_dict[toks[2]]) + ')'

with open(r"2022\puzzle21.txt") as f:
    symbols_dict = {l[:4]: l[6:] for l in f.read().splitlines()}

print ("Part 1:", simplify(expand(symbols_dict['root'])))

symbols_dict['humn'] = 'x'
s = symbols_dict['root'].split()
symbols_dict['root'] = s[0] + ' - ' + s[2]

print ("Part 2:", solve(expand(symbols_dict['root']), symbols('x'))[0])

```
