---
date: '2023-12-19T07:00:00-05:00'
draft: false
title: "Advent of Code Day 18 -- Lavaduct Lagoon"
author: "Tipa"
disqusIdentifier: "2023/12/19/advent-of-code-day-18-lavaduct-lagoon"
summary: "We had game night tonight, more HeroQuest (yay!), so I didn't have a lot of time to work on this...."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Elf"
  - "Lava"
relatedPosts:
  - url: "/2023/12/17/advent-of-code-day-17-clumsy-crucible/"
    title: "Advent of Code Day 17 -- Clumsy Crucible"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-17-16.23.47-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-is-a-birds-eye-view-of-Gear-Island-half-empty-and-half-a-bustling-fac.png"
  - url: "/2023/12/16/advent-of-code-day-16-the-floor-will-be-lava/"
    title: "Advent of Code Day 16 -- The Floor Will Be Lava"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-16-10.31.52-A-reindeer-leading-the-way-into-the-depths-of-a-giant-cave-that-serves-as-a-Lava-Production-Facility.-The-caves-walls-doorways-and-floor-are-all-na.png"
  - url: "/2023/12/21/advent-of-code-day-21-step-counter/"
    title: "Advent of Code Day 21 -- Step Counter"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
  - url: "/2023/12/19/advent-of-code-day-19-aplenty/"
    title: "Advent of Code Day 19 -- Aplenty"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-19-20.12.32-A-whimsical-and-detailed-illustration-set-on-Gear-Island-where-a-magical-workshop-is-bustling-with-activity.-Elves-dressed-in-colorful-attire-are-b.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-18-22.42.07-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-shows-a-large-newly-constructed-lagoon-near-a-machine-parts-factory-on.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-18-22.42.07-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-shows-a-large-newly-constructed-lagoon-near-a-machine-parts-factory-on.png"
---
We had game night tonight, more HeroQuest (yay!), so I didn't have a lot of time to work on this....
<!--more-->

We had game night tonight, more HeroQuest (yay!), so I didn't have a lot of time to work on this.

Basically, you're[ digging out a lagoon into which lava will flow](https://adventofcode.com/2023/day/18). Part 1 could easily be calculated using a basic flood fill algorithm, so I did it that way, got the first star for the day, and went to work. I'd already seen that, as expected, part 2 would resist something that easy.

I started working on algorithms during meetings. There was a lot of talk about the "shoelace" algorithm back in the Metal Maze puzzle. I solved it a weird way that worked for me. When I was reading hints that the [shoelace algorithm ](https://en.wikipedia.org/wiki/Shoelace_formula)was the answer for this one, I typed up the sample data into Excel, plugged the data into the formula and it just didn't work. The missing element had something to do with the perimeter -- the puzzle makes that clear. Jabbing at it in various ways didn't help. Turns out I was really close. I'd already summed up the total lengths of all the segments. Turns out, because of their non-zero width, they had to be considered to be half a unit closer. So, half of the sum of the steps, plus one unit to honor Santa, whose lagoon this is.

Since the only difference between parts 1 and 2 was in the details on how to read the input data, I broke the interpreting the input data into generators, and called the work procedure twice, once with each generator.

`import re

# in part 1, UDLR are directions, in part 2, they are hex digits (0..3)
dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0),
        '3': (0, 1), '1': (0, -1), '2': (-1, 0), '0': (1, 0)}

# split the input into tuples of (direction, steps, code)
def read_data():
    pat = re.compile(r'(\w)\s(\d+)...([\w]{6})')
    with open('puzzle18.dat') as f:
        return map(lambda x: pat.match(x).groups(), f.read().splitlines())

# shoelace formula for area of a polygon
def shoelace(vertices):
    shoelace = 0
    for i in range(len(vertices) - 1):
        shoelace += vertices[i][0] * vertices[i + 1][1] - \
            vertices[i + 1][0] * vertices[i][1]
    return abs(shoelace) // 2

# generators for part 1 and 2
def part1generator():
    yield 0, 0, 0
    for uplr, steps, _ in read_data():
        yield (*dir_map[uplr], int(steps))

def part2generator():
    yield 0, 0, 0
    for _, _, code in read_data():
        yield (*dir_map[code[-1]], int(code[:-1], 16))

# create a list of vertices, sum the perimeter and shoelace area
def calcarea(part_num, pgen):
    vertices = [(0, 0)]
    perimeter = 0
    for dx, dy, steps in pgen():
        vertices.append((vertices[-1][0] + dx * steps,
                        vertices[-1][1] + dy * steps))
        perimeter += steps

    print('Part {}: {}'.format(part_num, shoelace(vertices) + perimeter // 2 + 1))

# run both generators
calcarea('1', part1generator)
calcarea('2', part2generator)`

I was reading my code from AoC last year and found I not only didn't remember the puzzles that well, I honestly had little idea how the code worked. Problem is, most of my actual programming job doesn't need these algorithms...
