---
date: '2022-12-23T21:22:45-05:00'
draft: false
title: "Advent of Code Day 23 -- Unstable Diffusion"
author: "Tipa"
disqusIdentifier: "2022/12/23/advent-of-code-day-23-unstable-diffusion"
summary: "...because Stable Diffusion was already used, I guess. This is the annual cellular automata puzzle. Plus, why no puzzle 22?"
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Crippling Failure"
  - "Elf"
  - "Python"
relatedPosts:
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  - url: "/2022/12/25/advent-of-code-day-25-full-of-hot-air/"
    title: "Advent of Code Day 25 -- Full of Hot Air"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-25-14.03.31-Christmas-elves-on-a-snowy-mountain-top-colorful-hot-air-balloons-in-the-sky-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/09/advent-of-code-day-9-rope-bridge/"
    title: "Advent of Code Day 9 -- Rope Bridge"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-09-21.18.23-Christmas-Elves-walking-on-a-tattered-rope-bridge-crossing-a-river-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2023/12/06/advent-of-code-day-6-wait-for-it/"
    title: "Advent of Code Day 6 -- Wait For It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-06-20.55.25-A-whimsical-and-vibrant-scene-depicting-an-island-with-a-small-ferry-dock-and-numerous-toy-boats-ready-for-a-race.-The-island-is-surrounded-by-water-a.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-23-21.02.08-Several-Christmas-elves-standing-in-a-grid-in-a-jungle-clearing-a-volcano-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-23-21.02.08-Several-Christmas-elves-standing-in-a-grid-in-a-jungle-clearing-a-volcano-in-the-background-by-Bob-Eggleton-detailed-and-intricate.png"
---
...because Stable Diffusion was already used, I guess. This is the annual cellular automata puzzle. Plus, why no puzzle 22?
<!--more-->

I got both stars on Day 22, "[Monkey Map](https://adventofcode.com/2022/day/22)", but I am not taking credit for it. I did Part 1 fine, no troubles. Part 2 required folding the whole thing into a cube, and that didn't work. I made a physical cube to help visualize. I wrote an interactive visualization to make sure things were working (in curses, in a terminal, so it doesn't look cool). I wrote *unit tests*! I only do that at *work*, but even though they all passed and everything look like it worked -- I was getting the wrong answer.

I was up past midnight yesterday working on it, and several hours this morning. Eventually I used someone else's solution. I probably shouldn't have used it, but I just wanted it to be *over*. This is my first failure this year. Not happy about it.

*Thankfully*, [today's puzzle](https://adventofcode.com/2022/day/23) was a cellular automata -- a puzzle played on a 2D grid where elements on the grid transform simultaneously based on rules applied to every cell in the grid. In this case, the cells were elves, and they were slowly spreading out until they had sufficient room to plant a star flower.

Part 1 was to run the simulation for ten rounds. Part 2 was to run the simulation until every elf was sufficiently spread out.

**Python 3.11**

**read_input** makes a *set* of elf positions from the input. Noobs run CAs on a fully simulated grid. Old hands just keep a list of interesting bits. This uses *enumerate* to get both the element and its position.

**move_elves** runs the rules; they're described in the puzzle and I won't go over them here. The return indicates that no elves have moved for Part 2.

**solve_part_1** counts the spaces in the minimum enclosing rectangle that have no elves on them. **solve_part_2** returns the number of rounds before no elf moved.

Both parts ran correctly first time. I was so happy. I start these things thinking that this year, I will be able to figure out the algorithms and stuff they expect me to know, and then I find out I am wrong -- SO wrong. The first person to solve both parts of Day 22 did so in about 26 minutes. Sheesh. Day 23? *10* minutes, though admittedly this one was easier.

```
from itertools import cycle
from collections import defaultdict

def read_input():
    with open (r'2022\puzzle23.txt') as f:
        return set((x,y) for y, l in enumerate(f.readlines()) for x, c in enumerate(l) if c == '#')

def move_elves(elves, first_direction):
    proposals = defaultdict(list)
    start_facing = next(first_direction)

    for elf in elves:
        if not any((elf[0] + looking[0], elf[1] + looking[1]) in elves for looking in omni_elf):
            continue

        for i in range(4):
            crowded = False
            for direction in directions[(start_facing + i) % 4]:
                if (elf[0] + direction[0], elf[1] + direction[1]) in elves:
                    crowded = True
                    break
            if not crowded:
                direction = directions[(start_facing + i) % 4][1]
                proposals[(elf[0] + direction[0], elf[1] + direction[1])].append(elf)
                break
    
    for proposal in proposals:
        if len(proposals[proposal]) == 1:
            elves.remove(proposals[proposal][0])
            elves.add(proposal)
    
    return len(proposals) == 0

def solve_part_1():
    elves = read_input()
    first_direction = cycle(range(4))

    for _ in range(10):
        move_elves(elves, first_direction)
    
    min_x = min(elves, key=lambda x: x[0])[0]
    max_x = max(elves, key=lambda x: x[0])[0]
    min_y = min(elves, key=lambda x: x[1])[1]
    max_y = max(elves, key=lambda x: x[1])[1]
    
    return sum((x, y) not in elves for y in range(min_y, max_y + 1) for x in range(min_x, max_x + 1))

def solve_part_2():
    elves = read_input()
    first_direction = cycle(range(4))

    round = 0
    while True:
        round += 1
        if move_elves(elves, first_direction):
            break
    
    return round

directions = [[(-1, -1), (0, -1), (1, -1)], [(1, 1), (0, 1), (-1, 1)], [(-1, 1), (-1, 0), (-1, -1)], [(1, -1), (1, 0), (1, 1)]]
omni_elf = [(-1,-1), (0,-1), (1,-1), (1,1), (0,1), (-1,1), (-1,0), (1,0)]

print ("Part 1:", solve_part_1())
print ("Part 2:", solve_part_2())

```
