---
date: '2022-12-25T14:27:01-05:00'
draft: false
title: "Advent of Code Day 25 -- Full of Hot Air"
author: "Tipa"
disqusIdentifier: "2022/12/25/advent-of-code-day-25-full-of-hot-air"
summary: "That's a wrap -- a Christmas wrap! -- on Advent of Code 2022!"
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Balloon"
  - "Elf"
  - "Python"
relatedPosts:
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  - url: "/2022/12/23/advent-of-code-day-23-unstable-diffusion/"
    title: "Advent of Code Day 23 -- Unstable Diffusion"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-23-21.02.08-Several-Christmas-elves-standing-in-a-grid-in-a-jungle-clearing-a-volcano-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/09/advent-of-code-day-9-rope-bridge/"
    title: "Advent of Code Day 9 -- Rope Bridge"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-09-21.18.23-Christmas-Elves-walking-on-a-tattered-rope-bridge-crossing-a-river-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2023/12/06/advent-of-code-day-6-wait-for-it/"
    title: "Advent of Code Day 6 -- Wait For It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-06-20.55.25-A-whimsical-and-vibrant-scene-depicting-an-island-with-a-small-ferry-dock-and-numerous-toy-boats-ready-for-a-race.-The-island-is-surrounded-by-water-a.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
---
That's a wrap -- a Christmas wrap! -- on Advent of Code 2022!
<!--more-->

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
