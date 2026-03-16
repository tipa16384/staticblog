---
date: '2023-12-16T10:54:05-05:00'
draft: false
title: "Advent of Code Day 16 -- The Floor Will Be Lava"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/16/advent-of-code-day-16-the-floor-will-be-lava/"
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
summary: "/u/YellowZorro hasn't posted any more art, so back to Dall-E 3 renderings. Today, we get ready to MAKE SOME LAVA TO SAVE CHRISTMAS!"
description: "/u/YellowZorro hasn't posted any more art, so back to Dall-E 3 renderings. Today, we get ready to MAKE SOME LAVA TO SAVE CHRISTMAS!"
tags:
  - "Advent of Code"
  - "AoC2023"
  - "Laser"
  - "Lava"
  - "Mirrors"
  - "Reindeer"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-16-10.31.52-A-reindeer-leading-the-way-into-the-depths-of-a-giant-cave-that-serves-as-a-Lava-Production-Facility.-The-caves-walls-doorways-and-floor-are-all-na.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-16-10.31.52-A-reindeer-leading-the-way-into-the-depths-of-a-giant-cave-that-serves-as-a-Lava-Production-Facility.-The-caves-walls-doorways-and-floor-are-all-na.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Now that you've got all your lenses together and positioned, the beam of light (from the parabolic mirror outside, remember?) is being focused into a tight and very narrow beam that leads deep into the heart of the mountain. Following the deer and the beam of light into the depths, you find the final arrangement of mirrors that will turn the stones into lava. The beam of light doesn't seem like it's entering the contraption in the correct spot to do the most damage; your job today is to [find out where it should enter](https://adventofcode.com/2023/day/16) in order to heat the most rock.

**Part 1**

Part 1 asks you to simply calculate the energy level for the current entry point. The heart of the puzzle (for both parts) is the **beam** function that takes a coordinate and direction and returns the number of energized tiles as a result.

`def beam(grid: list, energized: dict, coord: tuple, direction: tuple) -> int:
    while coord[0] >= 0 and coord[0] = 0 \
            and coord[1] 

Beams continue in a straight line until they leave the contraption unless they hit a mirror. Diagonal mirrors '/' and '\' send the beam off 90 degrees from where it entered. If it hits a '-' or '|' while traveling perpendicular to the mirror, it splits the beam into two, going off at plus and minus 90 degrees. If it hits edge on, it continues as normal. Every square on the grid any beam passes is considered energized.

The **beam** function continues while the beam is both on the grid and has not entered this space from the same direction -- this avoids infinite loops. It then energizes the space for the direction.

The **match** statement manages special symbols. In the case of the two splitters, if splitting, it bends the current beam but also makes a new beam in the opposite direction. Other solvers did not use recursion, but I did, and that's that.

Then we move the beam in the direction and go through it again. When the beam hits an exit condition, it returns the number of energized tiles.

`def part1():
    print ("Part 1:", beam(read_data(), defaultdict(list), (0,0), (1,0)))`

**part1()** calls beam with the grid, an empty dictionary of energized tiles, and the starting location and direction.

**Part 2**

Part 2 wants us to iterate through all the starting positions on the edge of the grid to find the one with the most energized tiles.

`def part2():
    grid = read_data()
    beam_starts = [((x,0), (0,1)) for x in range(len(grid[0]))] + \
        [((0,y), (1,0)) for y in range(len(grid))] + \
            [((x,len(grid)-1), (0,-1)) for x in range(len(grid[0]))] + \
                [((len(grid[0])-1,y), (-1,0)) for y in range(len(grid))]
    print ("Part 2:", max(beam(grid, defaultdict(list), coord, direction)
        for coord, direction in beam_starts))`

We make a list of **beam_starts** that are all the starting locations and directions, call **beam** for each of these, and print the maximum.

Could be faster (I always say that because it is always true), but even with all the recursion and stuff, it still finishes part 2 in 1.75s, so it's "fast enough".
