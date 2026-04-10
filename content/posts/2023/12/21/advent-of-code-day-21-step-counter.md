---
date: '2023-12-21T21:26:36-05:00'
draft: false
title: "Advent of Code Day 21 -- Step Counter"
author: "Tipa"
disqusIdentifier: "2023/12/21/advent-of-code-day-21-step-counter"
summary: "I had 80% of the solution, but that last 20% killed it. This is the day I failed Advent of Code 2023."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Elf"
  - "Gardening"
  - "Python"
relatedPosts:
  - url: "/2023/12/19/advent-of-code-day-19-aplenty/"
    title: "Advent of Code Day 19 -- Aplenty"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-19-20.12.32-A-whimsical-and-detailed-illustration-set-on-Gear-Island-where-a-magical-workshop-is-bustling-with-activity.-Elves-dressed-in-colorful-attire-are-b.png"
  - url: "/2023/12/07/advent-of-code-day-7-camel-cards/"
    title: "Advent of Code Day 7 -- Camel Cards"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-07-21.36.26-In-a-desert-setting-a-Christmas-elf-mom-and-a-repair-person-in-a-safety-vest-and-hard-hat-are-riding-camels.-Both-characters-are-holding-a-hand-of-pl.png"
  - url: "/2023/12/19/advent-of-code-day-18-lavaduct-lagoon/"
    title: "Advent of Code Day 18 -- Lavaduct Lagoon"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-18-22.42.07-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-shows-a-large-newly-constructed-lagoon-near-a-machine-parts-factory-on.png"
  - url: "/2023/12/17/advent-of-code-day-17-clumsy-crucible/"
    title: "Advent of Code Day 17 -- Clumsy Crucible"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-17-16.23.47-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-is-a-birds-eye-view-of-Gear-Island-half-empty-and-half-a-bustling-fac.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
---
I had 80% of the solution, but that last 20% killed it. This is the day I failed Advent of Code 2023.
<!--more-->

Yeah, this is a story of failure.

Part 1 was trivial, as it usually is. You're given a grid and asked how many squares in the grid (that don't have rocks in them) [an elf could walk to](https://adventofcode.com/2023/day/21) given a certain number of steps. The grid looked like it might be a cellular automata puzzle, and we haven't had one of those yet. This was the day! I quickly tossed together a CA for the puzzle and got a part 1 solution in just a couple minutes.

Part 2 extended this to endlessly repeating grids and a mind-blowing number of steps. So I started doing analysis to break this down into smaller problems. My intuition said this was still a CA problem, but where the cells were copies of the grid, kind of like meta-cells.

`# 7577 -- 7596
# starter = 128 7577
# right 1 = 259 7577
# up 1 = 259 7577
# down 1 = 259 7577
# up/right 1 = 390 7577
# period appears to be 131 after the first
# up 2 = 390 7577
# up 3 = 521 7577

#          #

#          #
#         ###
#          #

#          #
#         ###
#        #####
#         ###
#          #

# 1, 5, 13 -- sums of two consecutive squares (2*n*(n+1)+1)`

So I noticed right off that the grids settle into alternating between 7577 and 7596 cells once they settle, and that they settled after 131 generations, which happens to be the size of the grid. The number of completed grids was a sum of squares sequence -- 1, 1+4, 1+4+9, etc. Each new layer out was of opposite polarity. I was able to get an estimate for the solution (or so I thought) fairly quickly.

But I missed some stuff. I missed that the grid had no rocks in the same column or row as the starting position. This means that the elf can just walk in a straight line from the starting spot. In fact, the number of steps he takes -- 26501365 -- brings him to the far end of a full grid. ((26501365-131//2)/131 = 202300 grids, to be exact). So we know the shape of the diamond. We can easily figure out how many full grids using the sequence of squares, and we know they alternate between two states depending on which layer, even odd, they are. Then comes calculations for the grids that are only partially filled. But we know the dividing line goes from end to end, so depending on if they are even or odd squares, we can tell how many positions need to be added or subtracted.

So I got a lot of the way to the solution, but in the end, I used someone else's code to get the star. I'm not calling this one a success. I'll come back to it at some point and see what my own solution might look like.
