---
date: '2023-12-11T07:49:29-05:00'
draft: false
title: "Advent of Code Day 11 -- Cosmic Expansion"
summary: "This is why Santa shouldn't let elves do astrophysics."
categories:
  - "Advent of Code"
tags:
  - "AoC2023"
  - "Cosmology"
  - "Observatory"
  - "Starry Starry Night"
  - "Telescope"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-11-07.29.15-An-elf-showing-a-telescope-to-a-repairman-wearing-a-hardhat-and-a-safety-vest.-The-scene-is-set-under-a-dark-sky-filled-with-stars-and-galaxies.-In-th.png"
cover: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-11-07.29.15-An-elf-showing-a-telescope-to-a-repairman-wearing-a-hardhat-and-a-safety-vest.-The-scene-is-set-under-a-dark-sky-filled-with-stars-and-galaxies.-In-th.png"
---

After yesterday, I was hoping for an easier puzzle, and we got an easier puzzle.

I guess we've given up looking for the mysterious Robo-Elf from yesterday's puzzle. That maze of metal pipes was made more for a Mario-type than a repair person-type, like yourself. Thankfully, today you come across a more traditional elf. Striped stocking: check. Pointy ears: check. Impractical curly shoes? Check and *check*. It's an elf, and like all elves, this one really needs your help. He's the official astronomer for Santa, and [he needs your help with some cosmology](https://adventofcode.com/2023/day/11).

"Consider the galaxies," says the elf. "They are all equally distant from us on Earth, but different distances from *each other*, as is plain to see. However, where the sky is *particularly* empty, they are even *further* apart."

Elves and science. They just don't mix. But you humor the elf and go along with his calculations. He hands you a star map with all the galaxies of interest arranged in a grid, and he wants you to calculate the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) between every pair of galaxies, and then sum them up. *But*, every empty row or column in the path between the two galaxies *doubles* the normal measurement. In part two, the distance is a *million* times longer. (This is the only difference between parts 1 and 2.)

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/image-12-1024x643.png" title="Midjourney" class="align-center" >}}

Reading and processing the grid:

`from itertools import combinations

def read_data() -> list:
    with open("puzzle11.dat") as f:
        return f.read().splitlines()

# make a list of the x,y coordinates of every '#' in the grid
def find_galaxies(grid: list) -> list:
    return [(x, y) for y, row in enumerate(grid) for x, galaxy in enumerate(row) if galaxy == '#']

# find the 'x' values for every column in grid consisting entirely of '.'
def find_empty_columns(grid: list) -> list:
    return [x for x in range(len(grid[0])) if all([row[x] == '.' for row in grid])]

# find the 'y' values for every row in grid consisting entirely of '.'
def find_empty_rows(grid: list) -> list:
    return [y for y, row in enumerate(grid) if all([galaxy == '.' for galaxy in row])]`

Python has a generator for taking every combination of elements in a list, so that comes first. Followed by our standard function to read the puzzle data, a function to return a list of the coordinates of every galaxy, empty column, and empty row.

`# find the manhattan distance between two points
def manhattan_distance(p1: tuple, p2: tuple, empty_rows: list, empty_cols: list, multiplier:int) -> int:
    minx, maxx = min(p1[0], p2[0]), max(p1[0], p2[0])
    miny, maxy = min(p1[1], p2[1]), max(p1[1], p2[1])

    temp = (maxx - minx) + (maxy - miny)
    # for every empty row between the two points, add multiplier to the distance
    temp += multiplier * len([y for y in empty_rows if y > miny and y  minx and x 

The Manhattan distance is the sum of the absolute values of the difference between the *x* and *y* coordinates. I add the multiplier (1 or 999,999) to the distance for each empty row and column between those coordinates, and that's the answer.

`def parts_is_parts(multiplier:int = 2):
    grid = read_data()
    galaxies = find_galaxies(grid)
    empty_cols = find_empty_columns(grid)
    empty_rows = find_empty_rows(grid)
    # sum of all the manhattan distances between every pair of galaxies
    return sum([manhattan_distance(g1, g2, empty_rows, empty_cols, multiplier-1) for g1, g2 in combinations(galaxies, 2)])

print ("Part 1:", parts_is_parts())
print ("Part 2:", parts_is_parts(1000000))`

**parts_is_parts** sums up all the expanded Manhattan distances to provide the answer, and finally, the actual call to get those sums given the multiplier. Part 1 doesn't send one, so it uses the default value of 2.

That's it. Day 11 done. Have a great day!
