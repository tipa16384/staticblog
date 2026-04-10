---
date: '2023-12-15T21:02:37-05:00'
draft: false
title: "Advent of Code Day 15 -- Lens Library"
author: "Tipa"
disqusIdentifier: "2023/12/15/advent-of-code-day-15-lens-library"
summary: "The lack of hands is all that is keeping the world's reindeer from lasering everyone to death. Luckily, THIS reindeer has YOU. Beware."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Hash"
  - "Laser"
  - "Reindeer"
relatedPosts:
  - url: "/2023/12/16/advent-of-code-day-16-the-floor-will-be-lava/"
    title: "Advent of Code Day 16 -- The Floor Will Be Lava"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-16-10.31.52-A-reindeer-leading-the-way-into-the-depths-of-a-giant-cave-that-serves-as-a-Lava-Production-Facility.-The-caves-walls-doorways-and-floor-are-all-na.png"
  - url: "/2023/12/22/advent-of-code-day-22-sand-slabs/"
    title: "Advent of Code Day 22 -- Sand Slabs"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/jenga.png"
  - url: "/2023/12/21/advent-of-code-day-21-step-counter/"
    title: "Advent of Code Day 21 -- Step Counter"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
  - url: "/2023/12/20/advent-of-code-day-20-pulse-propogation/"
    title: "Advent of Code Day 20 -- Pulse Propagation"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-20-16.57.44-Create-an-illustration-inspired-by-the-aesthetic-of-a-retro-sci-fi-movie-similar-to-Tron-avoiding-direct-references-or-copyrighted-elements.-Visualiz.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/aoc2023-15.jpeg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/aoc2023-15.jpeg"
---
The lack of hands is all that is keeping the world's reindeer from lasering everyone to death. Luckily, THIS reindeer has YOU. Beware.
<!--more-->

The header art was used with the permission of the artist, [YellowZorro](https://old.reddit.com/user/YellowZorro). You can find more of their [AoC-themed art here](https://old.reddit.com/r/adventofcode/comments/18ivwtz/2023_aoc_doodles_days_1315/)!

All the light you collected yesterday has to go somewhere, and that somewhere is here -- a light focusing facility with a thousand different lenses... and a reindeer who perhaps works there? They are very happy to see a human, as while they know what needs to be done, they can't actually do it.

That, of course, is [where you come in](https://adventofcode.com/2023/day/15).

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/a67f24e7-3b38-41e1-b11a-f449f2506ec3-1024x585.webp" title="Dall-E 3 redrew the drawing. And this is why AI art is inferior." classes="center" >}}

**Part 1**

The input is a vast number of comma-separated values, looking like this: 

`rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7`

The actual puzzle input is much, much more. The puzzle gives instructions on how to form a hash of a string. A hash is simply a way of turning a string into a number. More than one string can generate the same hash, especially in the case of *this* one, that only has 256 values.

`def deer_hash(s: str) -> int:
    return reduce(lambda h, c: ((h + ord(c)) * 17) % 256, s, 0)

def part1():
    print ("Part 1:", sum(deer_hash(x) for x in read_data().split(',')))`

**deer_hash** applies the hashing algorithm to each character in turn, using **reduce**, a function that takes a list, applies a lambda (AKA anonymous function, et al) to each element, and returns a single value.

**part1** sums the hashes of the input data.

**Part 2**

It turns out that the input data are actually instructions. Tokens of the form (=) are instructions to put the lens of focal length  in the box numbered deer_hash() and the lens would be labeled with that label as well. The order of the lenses is important, so there is to be no shuffling. Tokens of the form (-) are instructions to remove the labeled lens from the deer_hash'd box.

At the end, calculate the power of each lens, which the product of its box number + 1, its position in the box +1, and its focal length, and sum those up for every lens in every box.

What the puzzle describes is an "ordered hash". Python's native dictionary object implements this, so I just made a list of dictionaries, and parsed the commands to add and remove things as necessary.

`def part2():
    boxes = [{} for i in range(256)]
    for x in read_data().split(','):
        # use re to find the label, contiguous letters at the start of the string
        label = re.match(r'^[a-z]+', x).group(0)
        box = boxes[deer_hash(label)]
        if '=' in x: box[label] = int(x.split('=')[1])
        else: box.pop(label, None)
    # sum the product of the box number + 1, the position in the box + 1 
    # and the lens for each lens in each box
    print ("Part 2:", sum((k+1)*(i+1)*v 
                          for k, v in enumerate(boxes) 
                          for i, v in enumerate(v.values())))`

The code works as I mentioned. We make the boxes, each with a dictionary inside. For each command, we extract the label (the letters at the beginning of the command), figure out which box we're working with, and if this is an insert/replace command, doing the needful. Otherwise it is a remove command, and we remove it. Then we score it and done.

A short puzzle for today!
