---
date: '2022-12-24T16:02:44-05:00'
draft: false
title: "Advent of Code Day 24 -- Blizzard Basin"
summary: "The Christmas elves don't like the snow for some reason? They have the wrong boss, I think. Well, we better help them get through those couple hundred blizzards."
categories:
  - "Advent of Code"
tags:
  - "A*"
  - "Blizzard"
  - "Elf"
  - "Memoization"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-24-15.36.17-a-hundred-Christmas-elves-in-a-blizzard-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-24-15.36.17-a-hundred-Christmas-elves-in-a-blizzard-by-Bob-Eggleton-detailed-and-intricate.png"
---

I was nervous, starting [today's puzzle](https://adventofcode.com/2022/day/24). I saw last night that it was a "shortest path" problem, and since the path had a defined start and end, it was an "[A-star](https://en.wikipedia.org/wiki/A*_search_algorithm)" problem, and that's what it turned out to be.

I was nervous because I am constantly expecting myself to fail, now. [Day 22](https://adventofcode.com/2022/day/22) left scars.

Two days left, after this -- tomorrow's, and [Day 13](https://adventofcode.com/2022/day/13), that I didn't do as I was away from computers and haven't had time to do two puzzles in a day since.

**Python 3.11**

I've tried to shorten this to make it easier to get through, if not easier to read. I initially had classes for the blizzards and for the elf that is moving through them, but converted those to tuples as I didn't really need much of the class functionality, and it slows stuff down.

The blizzards move in their direction every round, and wrap around the map once they reach and edge. So their position is a function of time, modulo the width or height of the board. Since the blizzards will always be in the same spot at the same time, I used a map to memoize the blizzard positions so we only have to do the calculations once for a given time.

Part 1 is retracing end back to start and back to end again, so I just rerun it twice for part 2, with the time marching forward as usual.

```
from collections import defaultdict
import heapq

def read_input():
    dirdict = {'': (1, 0), '^': (0, -1), 'v': (0, 1)}
    with open(r"2022\puzzle24.txt") as f:
        lines = f.read().splitlines()
        board_height = len(lines) - 2
        board_width = len(lines[1]) - 2
        elf_start = (lines[0].index(".") - 1, -1)
        elf_end = (lines[-1].index(".") - 1, board_height)
        blizzards = [((x-1, y-1), dirdict[lines[y][x]]) \
            for y in range(1, board_height+1) for x in range(1, board_width+1) if lines[y][x] in dirdict]
        return elf_start, elf_end, blizzards, board_width, board_height

def move_blizzards(blizzards, time):
    if time in blizzard_dict: return blizzard_dict[time]
    stuff = defaultdict(list)
    for blizzard in blizzards:
        x, y = (blizzard[0][0] + blizzard[1][0] * time) % board_width, \
            (blizzard[0][1] + blizzard[1][1] * time) % board_height
        stuff[(x, y)].append(blizzard)
    blizzard_dict[time] = stuff
    return stuff

def calc_moves(pos, blizzards, time):
    delta_force = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    stuff = move_blizzards(blizzards, time+1)
    moves = []
    for delta in delta_force:
        x, y = pos[0] + delta[0], pos[1] + delta[1]
        if (x, y) not in stuff and ((x, y) == elf_end or (x, y) == elf_start or  x >= 0 and x = 0 and y < board_height):
            moves.append((x, y))
    
    return moves

def find_path_time(blizzards, start_pos, end_pos, time):
    heap = []
    heapq.heappush(heap, (0, start_pos, time))
    visited = set()

    while heap:
        _, pos, time = heapq.heappop(heap)
        if pos == end_pos: return time
        if (pos, time) not in visited:
            visited.add((pos, time))
            for move in calc_moves(pos, blizzards, time):
                heapq.heappush(heap, (abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1]) + time, move, time+1))

elf_start, elf_end, blizzards, board_width, board_height = read_input()
blizzard_dict = {}

part1_time = find_path_time(blizzards, elf_start, elf_end, 0)
print ("Part 1:", part1_time)
print ("Part 2:", find_path_time(blizzards, elf_start, elf_end, 
        find_path_time(blizzards, elf_end, elf_start, part1_time)))

```
