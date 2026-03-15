---
date: '2022-12-25T14:27:01-05:00'
draft: false
title: "Advent of Code Day 25 -- Full of Hot Air"
summary: "That's a wrap -- a Christmas wrap! -- on Advent of Code 2022!"
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Balloon"
  - "Elf"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
---

It's the end of Advent of Code 2022, and the end of my second year of participating. Let's see how I did:

One puzzle I couldn't complete alone, despite copious hints. And one puzzle that required those copious hints to complete. The rest I muddled through on.

I was hoping to do each day's puzzle in Python and Java, and to write a little game each day on the theme of the day. I didn't expect to be able to keep up that pace, and I didn't. I only made five games, and I abandoned Java a bit later. I'd *planned* early last year to learn Clojure enough to do it in that language, but that fell by the wayside.

Python just makes things too easy -- it's seducing.

I'd thought, several times, that we were going to build on previous day's puzzles, but that never happened.

This season started with people widely using AI help, but that didn't get through more than a few days. I've been playing with Chat GPT, and if it isn't copying someone else's work, it's really terrible at coding. Some people have gotten results by carefully reviewing the generated code and offering suggestions, but at that point, you're roleplaying a senior developer mentoring a junior developer -- and that's my day job, thanks.

**Python 3.11**

As is tradition, the Christmas Day puzzle has just one part. In this one, the elves have come up with a bizarre base-5 number system (0, 1, 2, =, and - being the digits), and need you to translate both ways for the answer. And that was it, really. I had it done before anyone else even got out of bed.

```
def snafu_to_decimal(s):
    value, power, queue = 0, 1, list(s)
    while queue:
        ch = queue.pop()
        match ch:
            case '0'|'1'|'2': value += int(ch) * power
            case '-': value -= power
            case '=': value -= 2*power
        power *= 5

    return value

def decimal_to_snafu(d):
    value = ''
    while d:
        d, r = divmod(d, 5)
        match r:
            case 0|1|2: value = str(r) + value
            case 3:
                d += 1
                value = '=' + value
            case 4:
                d += 1
                value = '-' + value
    return value

with open(r'2022\puzzle25.txt', 'r') as f:
    print ("Part 1:", decimal_to_snafu(sum(map(snafu_to_decimal, f.read().splitlines()))))

```
