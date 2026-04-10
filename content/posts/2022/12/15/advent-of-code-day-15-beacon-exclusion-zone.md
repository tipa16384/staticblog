---
date: '2022-12-15T15:01:04-05:00'
draft: false
title: "Advent of Code Day 15 -- Beacon Exclusion Zone"
author: "Tipa"
disqusIdentifier: "2022/12/15/advent-of-code-day-15-beacon-exclusion-zone"
summary: "This is the kind of puzzle I hate. Puzzles where even the best approach seems to take forever and it's hard to wrap my head around the solution."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Python"
relatedPosts:
  - url: "/2023/12/05/advent-of-code-day-5-if-you-give-a-seed-a-fertilizer/"
    title: "Advent of Code Day 5 -- If You Give A Seed A Fertilizer"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_tending_a_wide_variety_of_bizarre_looki_61e5db45-06f1-482c-9242-78720532164f.png"
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  - url: "/2022/12/25/advent-of-code-day-25-full-of-hot-air/"
    title: "Advent of Code Day 25 -- Full of Hot Air"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/23/advent-of-code-day-23-unstable-diffusion/"
    title: "Advent of Code Day 23 -- Unstable Diffusion"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-23-21.02.08-Several-Christmas-elves-standing-in-a-grid-in-a-jungle-clearing-a-volcano-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-15-14.20.23-A-woman-in-a-Christmas-hat-looking-at-a-handheld-device.-Around-her-beeping-sensors-are-scanning-for-a-distress-beacon-by-Bob-Eggleton-detailed-and.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-15-14.20.23-A-woman-in-a-Christmas-hat-looking-at-a-handheld-device.-Around-her-beeping-sensors-are-scanning-for-a-distress-beacon-by-Bob-Eggleton-detailed-and.png"
---
This is the kind of puzzle I hate. Puzzles where even the best approach seems to take forever and it's hard to wrap my head around the solution.
<!--more-->

Wow, okay, this same sort of puzzle came up last year, [Day 19](https://adventofcode.com/2021/day/19), and I really, really hated it. I took all day without making much progress and I finally went to the r/adventofcode subreddit for help. One of only twice I had to do so.

Anyway, [in today's puzzle](https://adventofcode.com/2022/day/15), we have to find the one spot in a 4,000,000 x 4,000,000 grid that is not within scanning distance of one of 32 sensors scattered around the grid.

Calculating every one of these 160,000,000,000,000 positions would take awhile. In essence, this is really a problem with ray tracing -- find the one pixel on a 1.6x1013 pixel screen that doesn't have something displayed on it. It is *possible* -- someone on the subreddit seems to have used a 20 core computer to solve it in this brute force way in 200ms. Other people probably thought about using a GPU to do it, but I'm not gonna learn all about programming GPUs for this puzzle (though it might be handy to know).

I got hints for this from Reddit, but not code. But the hint was: Find all the points on the peripheries of all the sensors, and find a point that was just beyond four of them. I wrote a small version of this on their small test data and verified it worked, and then I collected sets of all those points, and tried all 32! combinations of sensor peripheries to look for common ones, and then at the end, keeping track of the duplicates I found, I ran through the list of those that had four or more shared coordinates and checked them individually to see if they were open. Only one was, and that was the solution.

Part 1 (which was a misdirection, you couldn't really solve it using the method they floated there on any normal computer), took about 1.8 seconds. Part 2 took fully 5 minutes. Coding and debugging the solution took *hours*.

This is the kind of puzzle I do not like. Thankfully, there weren't a lot of these last year, but there's always a couple. This wont be the last time I get stuck.

**Python 3.11**

Here's the Python solution. I don't want to spend any more time on this puzzle than I have to, so again, no Java solution. I was even thinking of doing the Java solution first... until I got online this morning and saw just what the puzzle was.

`from time import time_ns
import re
from collections import defaultdict
from itertools import combinations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def read_input():
    sensor_data = []
    with open(r"2022\puzzle15.txt") as f:
        data = f.read().splitlines()
        for line in data:
            sx, sy, bx, by = map(int, re.findall(r"([\-\d]+)", line))
            sensor_data.append(
                (sx, sy, bx, by, manhattan_distance(sx, sy, bx, by)))

    return sensor_data

def query_sensors(sensor_data, row):
    scanned_positions = set()

    for sx, sy, bx, by, mdist in sensor_data:
        md = manhattan_distance(sx, sy, sx, row)

        if md = 0 and x = 0 and y = 4:
            if not is_inside(sensor_data, *c):
                return c[0] * 4000000 + c[1]

    return 0

sensor_data = read_input()

start = time_ns()
part1 = query_sensors(sensor_data, 2000000)
print(f"Part 1: {part1} in {(time_ns() - start)/1e6}ms")

start = time_ns()
part2 = find_gaps(sensor_data)
print(f"Part 2: {part2} in {(time_ns() - start)/1e9}s")
`
