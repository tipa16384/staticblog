---
date: '2021-12-27T14:59:48-05:00'
draft: false
title: "Advent of Code 2021 -- Completed."
author: "Tipa"
summary: "It was an obsession, it was a challenge, it was a lesson. The Advent of Code is an annual coding event that runs from the..."
categories:
  - "Advent of Code"
tags:
  - "Algorithms"
  - "Clojure"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2021/12/AoC_banner.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/12/AoC_banner.png"
---
It was an obsession, it was a challenge, it was a lesson. The Advent of Code is an annual coding event that runs from the...
<!--more-->

It was an obsession, it was a challenge, it was a lesson. The [Advent of Code](https://adventofcode.com/) is an annual coding event that runs from the first to the twenty-fifth of December, but instead of chocolate treats, this advent calendar delivers delicious daily coding puzzles... although you don't necessarily need to code to solve them.

(The header image is from the [Python Discord](https://blog.pythondiscord.com/advent-of-code-2020/).)

My family thinks I was insane for doing this. And toward the end, I pretty much agreed with them. The last weekend was grueling, and I spent most of the last weekend before Christmas trying to solve particularly twisty puzzles. A lot of people dropped off at that point.

Advent of Code starts off as a pleasant walk. The first puzzle was to simply count the number of times a value was greater than the previous value in a list. Here's a solution I wrote in BASIC:

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/12/image.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/12/image.png)

I first heard about Advent of Code a couple months ago at one of our team learning sessions at work. The place where I work asks every developer to document the training they are taking in order to keep their skills up to date.

One of the developers mentions a few different places to keep skills sharp by solving puzzles. There was [LeetCode](https://leetcode.com/), which focuses on the kinds of basic knowledge puzzles that often come up in job interviews. I mentioned [code.golf](https://code.golf/), where programmers compete to solve problems in the fewest number of characters.

I'd never heard of Advent of Code, but I looked up the previous years puzzles and it looked pretty cool, so I added it to my development plan.

The people who join AoC come from all backgrounds. Some have only just started programming; some do competitive programming all the time. Some are working in languages they have never used, some are experts in a language hoping to improve their skills. Some just want to have some fun.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/12/image-1.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/12/image-1.png)Day 1, Part 1 in Rockstar, by [CCC_037](https://old.reddit.com/r/adventofcode/comments/r66vow/2021_day_1_solutions/hmy9wj9/).

I use Java at work, and Python at home (and at work when I can find a good excuse), so I thought the problems would be... no problem for me, and I started looking into old languages that I learned way back when that I could do the problems in -- just to make it a little bit of a challenge.

I looked into getting Prolog running -- not much luck there. I couldn't get Pascal working -- the first language I got paid to use. I had no desire to go back to FORTRAN, even though I wrote a lot of games in it back in the mainframe era. COBOL, no, never. BASIC was my first language, but there aren't really any decent implementations available.

I considered Forth and Clojure, but it turned out to be a bad idea to try to learn a new language while AoC was going.

According to [Reddit](https://old.reddit.com/r/adventofcode/), people used all those languages to solve the problems. Me, after the puzzles started getting more challenging, I just opted to stick with Python, a language I thought I knew -- but, I really didn't know much at all.

To be brutally honest with myself, I was kind of hoping I wouldn't have to solve these puzzles by myself. I'd installed [GitHub Copilot](https://copilot.github.com/) in my VS Code IDE and had been trying it out on a few easier coding puzzles. GitHub Copilot looks at your code and comments as you write it, and automatically completes your code with what it thinks you're trying to do. My test was to see if I could just describe the problem and the functions needed, in English, and have it write the code.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/12/image-2.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/12/image-2.png)via GitHub Copilot

As an example, I just now wrote two comments in a new window and GitHub Copilot wrote Clojure code to satisfy it. Unlike that example I wrote in BASIC, this one uses map/reduce to do the work. That's not how I solved the puzzle in Python, but it's *better* than I could have come up with.

Redoing my Python solution using the knowledge from that Clojure fragment, I come up with:

`with open('puzzle1a.dat') as f: data = list(map(int, f.read().split('\n')))
print("Part 1:",sum(1 for i, x in enumerate(data) if i > 0 and x > data[i-1]))
`

I just typed this into VS Code, and Copilot helpfully suggested this second line after I wrote the first one:

`print(sum(x for i, x in enumerate(data) if x > data[i-1]))`

It somehow knew what I wanted to do, but it was also *wrong*. I wanted the total count, not the total sum, and this code will give the wrong answer due to a quirk with Python. The previous value in the first comparison will come from the end of the list of values -- it shouldn't wrap around like that at all.

That's the issue I had with Copilot all along, and it got worse with time. It was handy for the small stuff, but anything larger just trended toward the weird. It works by looking in its huge public code repositories for something similar to what you seem to be doing, and handing what it finds to you. This actually works reasonably well with older AoC puzzles, as past programmers have posted their solutions. I have even had Copilot give me my own code back to me, which was a little creepy.

Back before AoC, I would never have written Python code that concisely. Every single day, I learned new tricks from looking at other people's freely shared solutions. [My actual solution](https://github.com/tipa16384/adventofcode/blob/main/2021/puzzle1.py) to [the Day 1 problem](https://adventofcode.com/2021/day/1) is... a little different. Quite a bit naïve. 

**The Lanternfish Incident**

By Day 6, I'd long abandoned any hope that Github Copilot would be much use, although its code completion was often handy as a starting point, and almost always wrong in some subtle way if I thought I could trust it.

The [Lanternfish puzzle](https://adventofcode.com/2021/day/6) was the first one where the answer wasn't clearly straightforward. Solved the most obvious way, Part 1 finishes relatively quickly, but due to its exponential nature, Part 2 will probably never finish if solved that same way. It requires not modeling each fish, but modeling collections of identical fish. Then, it's just a matter of addition. My solution got a couple comments for using a floating pointer into the array of fish buckets to save even a few more microseconds.

To continue from this point, I was going to have to accept that the obvious solution for the first part of the puzzle almost always was going to be the wrong solution.

`def solve(days):
    buckets = [fishes.count(i) for i in range(9)]
    for i in range(days): buckets[(i+7) % 9] += buckets[i % 9]
    print(sum(buckets))

with open('puzzle6.dat') as f:
    fishes = list(map(int, f.read().strip().split(',')))

`

This was probably the high point of AoC, for me.

Day 7 was knowing about **mean** and **median**. Day 8 was a logic puzzle that took me longer than I expected, and was shown just how far ahead of me a lot of other programmers were at these things. Day 9 was implementing a floodfill algorithm, though people found even cooler ways of doing it. Some people solved it by just displaying the input and looking at it. Day 10 I solved with a stack and thought I was clever, but people solved it better with pattern matching. 

Day 11 demonstrated [spontaneous synchronization](https://arxiv.org/abs/1805.06647#:~:text=Spontaneous%20synchronization%20is%20a%20remarkable,oscillations%20at%20a%20common%20frequency.), and it was here I understood I was going to be learning stuff if I continued. Day 12 was a graphing problem that I solved with brute force, and then, reading other solutions, I learned why Python is so strong in data analysis -- since it is the most popular computer language, a lot of high powered libraries have been written for it. This puzzle could have been solved in minutes with "[networkx](https://networkx.org/documentation/stable/index.html)", instead of the hours it took me. I'll know it for next time.

Day 13 was quick enough that I started looking into doing visualizations -- I'd done one for the day 11 puzzle, and did one for this as well, using the [curses](https://en.wikipedia.org/wiki/Curses_(programming_library)) library. Day 14 was a restatement of the Lanternfish problem, and it took me awhile before I realized that. I was still, at this point, brute forcing Part 1 and hoping Part 2 would just be the same thing.

Day 15 was the [Dijkstra's pathfinding algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) puzzle. I'd actually implemented the related A* algorithm for a game not long ago, so this was straightforward and fun.

Day 16 was a packet processing puzzle which would be instantly familiar to anyone dealing with low level TC/P and UD/P network protocols. It's been a few years for me, but I got through it.

Day 17 implemented ballistic trajectories with gravity and drag taken into account. Many people saw Part 1 as a straightforward application of triangular numbers and solved it without bothering to write code. Not me, I wrote code. The second part played with my assumptions from the first part.

Day 18 was either a graph theory puzzle, or a particularly involved cellular automation puzzle. I did it both ways. I still think I could have made graph theory work but after ALL DAY on it, I just did whatever would make it work.

[Day 19 broke me](https://adventofcode.com/2021/day/19). I noticed I could ignore most of the weird stuff going on in Part 1 and just do a quick and simple solution that ignored orientation differences and just gave the answer. Part 2 was all about the orientation differences. Days 18 and 19 were where people starting falling behind. It wasn't until days later that I could understand other people's solutions well enough. And yeah, I was mining other people's solutions here. I could just not wrap my head around it.

Day 20 was just 2D cellular automation with custom rules. AKA Conway's Game of Life, which can also be simulated in this puzzle solution. Everyone enjoyed it. There's a CA puzzle every year, apparently.

Day 21 was another "lanternfish" puzzle, where the easy solution was easy and the part 2 solution was exponentially hard. I saw a hint on the subreddit that this was a "memoization" problem, and if I arranged my solution such that it could be cached, then I could solve it pretty quick.

`from functools import cache, reduce
from timeit import default_timer as timer
from itertools import cycle, islice, product
from tupleops import addtuple, multuple
`

I sure used a lot of libraries, though. "tupleops" is mine :-) I realized that if I wrote something I thought I could use in the future, I really ought to start separating those functions into their own modules so that I could find them again.

Day 22 was a constructive solid geometry problem. More than a couple people solved it by importing the problem data into a graphics modeling program and just using those tools for the answer. I found a library that would intersect and difference rectangles and extended it for 3D. Some people used octree, which I might have done if I'd remembered it existed. My faves were the people who printed it in 3D. Of course there were better solutions that ignored CSG entirely.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/12/image-3.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/12/image-3.png)Day 23 problem

Day 23 was a sliding block puzzle which a lot of people solved with Dijkstra, and some others with graph theory. I just solved it manually. Worked for me.

Day 24 was a dirty trick. The problem told us we needed to write an Arithmetic Logic Unit for a mythical computer, but the actual problem was entirely encoded in the puzzle input, which tripped me up for awhile until I started noticing how regular the program we were supposedly going to execute looked. It wasn't long after that that I got the solution -- again, not a solution that required code, though some people did manage to write code that could do the analysis programmatically.

Day 25 -- Christmas morning -- the last puzzle. This one was an implementation of the [Biham-Middleton-Levine traffic model](https://en.wikipedia.org/wiki/Biham%E2%80%93Middleton%E2%80%93Levine_traffic_model) that comes straight out of Wikipedia. There's even a hint in the puzzle itself that directs you there. My solution wasn't elegant but, heck, it was Christmas, and I was in a hurry.

I learned so much with AoC, but I'm glad it's over. I didn't learn a new language, as I'd hoped, but that was fine. I learned a lot about algorithms and learned to think through problems before writing code. AoC'll bite you there, every time.
