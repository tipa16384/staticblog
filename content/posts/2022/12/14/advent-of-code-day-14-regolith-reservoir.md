---
date: '2022-12-14T23:39:52-05:00'
draft: false
title: "Advent of Code Day 14 -- Regolith Reservoir"
author: "Tipa"
disqusIdentifier: "2022/12/14/advent-of-code-day-14-regolith-reservoir"
summary: "I thought, for my vacation, I'd have time to really dive deep into these puzzles. Instead, I've been buried deep in sand -- much like the hapless victim in today's puzzle."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Depth First Search"
  - "Python"
relatedPosts:
  - url: "/2022/12/20/advent-of-code-day-19-not-enough-minerals/"
    title: "Advent of Code Day 19 -- Not Enough Minerals"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-20-08.04.02-A-woman-wearing-a-Christmas-hat-directing-mining-robots-with-a-handheld-device-in-a-jungle-by-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2023/12/05/advent-of-code-day-5-if-you-give-a-seed-a-fertilizer/"
    title: "Advent of Code Day 5 -- If You Give A Seed A Fertilizer"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_tending_a_wide_variety_of_bizarre_looki_61e5db45-06f1-482c-9242-78720532164f.png"
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  - url: "/2022/12/25/advent-of-code-day-25-full-of-hot-air/"
    title: "Advent of Code Day 25 -- Full of Hot Air"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-14-23.21.55-A-woman-wearing-a-Christmas-hat-caught-in-a-cave-with-sand-pouring-down-from-an-opening-in-the-ceiling-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-14-23.21.55-A-woman-wearing-a-Christmas-hat-caught-in-a-cave-with-sand-pouring-down-from-an-opening-in-the-ceiling-by-Bob-Eggleton-detailed-and-intricate.png"
---
I thought, for my vacation, I'd have time to really dive deep into these puzzles. Instead, I've been buried deep in sand -- much like the hapless victim in today's puzzle.
<!--more-->

So, Monday and Tuesday, I flew to Denver and back to pick up my son, who'd gotten stuck on an impromptu trip across country to see the Grand Canyon. Today, I found that the $10,000 sewer pipe we just had replaced on the outside of the house needs a $5,500 mate on the inside of the house.

All in all, it hasn't been my most favoritest of vacations. But I really did want to do Advent of Code again.

[For this one](https://adventofcode.com/2022/day/14), I really didn't know what the trick was. The problem description asks you to simulate a grain of sand falling and piling up over a series of obstacles, and then counting them. I started with a couple of strategies including just simulating the whole thing as a grid, before settling on just having spaces with stuff in them be in a set, to which sand is added as it comes to rest.

That worked. Part 2 extended it a bit. I fiddled, and then that worked, too. No big deal. It was a little slow, at about a second and a half for part 2, but I got it down to just over a second with some fiddling.

But times this slow means there is a problem of understanding. Almost every puzzle in AoC has an obvious solution, and a correct solution. Usually the correct solution uses some computer science incantation that clearly is the right solution, and I just couldn't find it.

After I finished mine, I went looking for that correct solution. And it looks to be a Depth First Search (DFS). I haven't implemented it, so I don't know that it is definitely faster, but the idea is that you drop one particle of sand, then back it up a step and try the other two ways it could fall. In Part 1, until it falls into infinity, or in Part 2, until it plugs up the hole it's falling from. I dunno for sure, but it really seems like that's what the puzzle was trying to teach.

Well, a second isn't the fastest, but it is fast enough.

**Python 3.11**

I didn't do a Java version. I was going to wait on that until I figured out what the trick was, and I never did until I went looking, and now it's too late.

`from time import time_ns
import re

def read_world():
    global all_world

    all_world = set()

    with open(r'2022\puzzle14.txt') as f:
        for l in f.read().splitlines():
            vertices = map(int, re.split(r' -> |,', l))
            x1, y1 = next(vertices), next(vertices)
            for x2, y2 in zip(*[iter(vertices)]*2):
                add_line_segment(x1, y1, x2, y2)
                x1, y1 = x2, y2

def add_line_segment(x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            all_world.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2)+1):
            all_world.add((x, y1))

def drop_sand(bounds, part2=False):
    x, y = 500, 0
    while True:
        if (x, y) in all_world or y > bounds:
            return False
        elif not (x, y + 1) in all_world:
            x, y = x, y + 1
        elif not (x - 1, y + 1) in all_world:
            x, y = x - 1, y + 1
        elif not (x + 1, y + 1) in all_world:
            x, y = x + 1, y + 1
        else:
            all_world.add((x, y))
            return True

for part2 in False, True:
    read_world()
    bounds = max(all_world, key=lambda k: k[1])[1]
    if part2:
        bounds += 2
        add_line_segment(500-bounds, bounds, 500+bounds, bounds)

    num_sand = 0
    start = time_ns()
    while drop_sand(bounds, part2): num_sand += 1

    print (f"{'Part 2' if part2 else 'Part 1'}: {num_sand} sand in {(time_ns() - start)/1e6}ms")
`

I really don't like the **drop_sand** method. It was worse; I asked ChatGPT for help optimizing it, and it, for once, had a useful suggestion. This is where DFS would go. I wasn't wild about the parsing in **read_world**, either. In fact I am not very happy with this at all.

Well, tomorrow, I hope I can catch up some of the days I missed.
