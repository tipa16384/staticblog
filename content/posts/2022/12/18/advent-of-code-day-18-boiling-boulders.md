---
date: '2022-12-18T20:30:03-05:00'
draft: false
title: "Advent of Code Day 18 -- Boiling Boulders"
summary: "We're about to start on Christmas Week, that week when Advent of Code's most iconic puzzles are released. But today, we're dealing with the aftermath of an exploding volcano."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Python"
  - "Volcano"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-18-19.03.10-An-elephant-watching-a-flaming-meteor-crash-into-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-18-19.03.10-An-elephant-watching-a-flaming-meteor-crash-into-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
---

That little handheld device you have is something else. It only has six rows of 40 characters each, but it can scan for beacons, play trillion piece games of Tetris, and today, [track a molten globule of lava](https://adventofcode.com/2022/day/18) as it crosses the sky and splashes into a lake.

Sure, it's low rez*, but you should be able to find the surface area from the quick scan.

Anyhoo, we have a lump of lava cooling in a lake, and we need to know how much surface area it has to see if it is cooling fast enough to form obsidian (Part 1), and to discover if there are hidden air pockets within the lump that might be causing it to cool too quickly (Part 2).

I solved part 1 by making a map of all the faces of the cubes that comprised the chunk and eliminating any that were shared with more than one cube, implying that that particular face was inside solid rock and didn't exist. The puzzle heavily implied that flood fill would solve the Part 2 problem of whether or not there were hidden faces that were not exposed to the lake water. A literal flood fill. So I implemented that as well.

Looking at the solutions on Reddit, most people had much more optimized solutions. Looks like I made things more complicated than they needed to be by breaking the cubes into faces. Oh well.

**Python 3.11**

I could have done this one in Java, but then I didn't.

`import re
from collections import defaultdict

def read_input():
    "return a list of tuples of 3 numbers"
    with open(r"2022\puzzle18.txt") as f:
        return zip(*[iter(map(int, re.findall(r"\d+", f.read())))]*3)

def face_generator(x, y, z):
    "yield the six faces of a cube"
    yield (x, y, z, x+1, y+1, z)
    yield (x, y, z, x+1, y, z+1)
    yield (x, y, z, x, y+1, z+1)
    yield (x+1, y, z, x+1, y+1, z+1)
    yield (x, y+1, z, x+1, y+1, z+1)
    yield (x, y, z+1, x+1, y+1, z+1)

def today_we_make_faces():
    "set of faces that are only used once"
    faces = defaultdict(int)
    for cube in read_input():
        for face in face_generator(*cube):
            faces[face] += 1
    return set(face for face in faces if faces[face] == 1)

def flood_fill(faces):
    "find the water volume"
    x, y, z, width, height, depth = -1, -1, -1, 23, 23, 23

    water_cubes = set()
    wet_faces = set()
    flood_heap = [(x, y, z)]

    while flood_heap:
        flood = flood_heap.pop()
        if flood not in water_cubes:
            if flood[0] >= -1 and flood[0] = -1 and flood[1] = -1 and flood[2] 

* Back in the olden days, I'd see ads in computer magazines for games with "hires graphics". I had no frickin idea -- at all -- what Hires graphics were. Did... did they have something to do with root beer? It was years later that I suddenly realized they meant "high resolution graphics". Apparently, Apple ][s had a "HIRES" command that triggered this mode, and everyone was supposed to be familiar enough with the Apple // to realize this. I dunno. To this day I think of good graphic resolution being "hires", as in "she hires him to set the best graphics settings".

Me, I had an Atari 800. I was so happy with that machine. Programmed my first game on that thing -- in Forth.
