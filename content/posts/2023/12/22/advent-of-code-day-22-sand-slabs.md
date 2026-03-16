---
date: '2023-12-22T17:28:03-05:00'
draft: false
title: "Advent of Code Day 22 -- Sand Slabs"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/22/advent-of-code-day-22-sand-slabs/"
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
summary: "I almost gave up on this one. Then I started playing around with it in a 3D render package and I found the issue."
description: "I almost gave up on this one. Then I started playing around with it in a 3D render package and I found the issue."
tags:
  - "Advent of Code"
  - "AoC2023"
  - "Babylonjs"
  - "Jenga"
  - "Pygame"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/jenga.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/jenga.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

This is one of those that looked easy to begin with, but then I just had a bunch of issues. I gave up, started playing with 3D rendering packages for fun, and then while flying around the rendered puzzle -- I found the issue.

In this puzzle, you have liberated sand from the Desert Island, and it is falling to the Snow Island, all ready to filter the water... except it isn't.[ It's coming in solid slabs.](https://adventofcode.com/2023/day/22) They're stacking so prettily and so precariously that we don't want to disturb it too much. That's part 1 -- seeing which blocks we can destroy without bringing the whole tower down. In part 2, we change our minds -- and try to see just how must destruction we can cause.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/b201b9252361064b-300x256.png" class="align-left" >}}

The input is a set of blocks, like Jenga bricks, but they can be all different sizes) though always rectangular. They are hanging suspended in space. The very first step is to see how the fall; this is common to both parts.

So, one way to do this is to implement some sort of physics engine and just see where they end up. And this was the first thing I tried.

Sometimes you start down a road, and you *know* it's the wrong road, but it's the only road you see, and so that's the one you take.

And it worked! It worked fine... for the sample input. I used Pygame and then decided to use the Babylon 3D engine to do it in the browser. My solution *didn't* work with the real input, and it took a *long* time for it to run and tell me the wrong answer.

So that was it. I gave up. Why am I even writing physics engines? This is dumb.

But it was fun to play with someone else's physics engine. Just blowing stuff up.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/jenga-1024x711.gif" title="Me, just blowing stuff up. That's the input. Being blown up. Boom." class="align-center" >}}

While I was getting the physics worked out, I found out that pieces that were only touching at a corner or an edge, *weren't falling*. My *overlap* code was wrong.

`def overlap(a, b):
    if a == b: return True
    # a and b are two ranges
    # return true if they overlap
    return a[0] 

UNIT TESTS, BABY. This code was going to WORK now.

So yeah stuff worked after that. It was slow, but it *worked*.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/7ddd6132-bad8-4e68-9b4a-d1b654ae9563-1024x585.webp" title="Dall-E's illustration, but I like mine better" class="align-center" >}}

`def drop(falling: list, scanning_for_drop: bool = False) -> int:
    drop_count = 0
    for i, piece in enumerate(falling):
        if i == 0: continue
        maxz = -100000
        for j in range(i):
            lower_piece = falling[j]
            if overlap((lower_piece[0][0], lower_piece[1][0]), (piece[0][0], piece[1][0])) and \
                overlap((lower_piece[0][1], lower_piece[1][1]), (piece[0][1], piece[1][1])) and \
                    lower_piece[1][2] > maxz:
                maxz = lower_piece[1][2]
        deltaz = piece[0][2] - maxz
        if deltaz > 0:
            if scanning_for_drop:
                return True
            falling[i] = ((piece[0][0], piece[0][1], piece[0][2] - deltaz), (piece[1][0], piece[1][1], piece[1][2] - deltaz), piece[2])
            drop_count += 1
            
    return drop_count`

**drop** takes the pieces and moves them to touch the next block down until everything is settled. The pieces are sorted, when I read them, vertically, so we are processing them from bottom up, so we only need to settle things once. Still super slow. The **scanning_for_drop** flag is used by part 1 to exit as soon as anything drops, as that's all we need to know for part 1. We return the drop_count for part 2 so that we can calculate *maximum destruction.*

`def part1(falling: list):
    safe_to_destroy = len(falling) - 1
    
    # for each piece in falling after the first, call drop with the list of falling excluding that piece and subtract
    # 1 from safe_to_destroy if drop returns True
    for i in range(1, len(falling)):
        if drop(falling[:i] + falling[i+1:], True):
            safe_to_destroy -= 1
    
    print ("Part 1: It is safe to destroy {} pieces".format(safe_to_destroy))

def part2(falling: list):
    
    number_obliterated = 0
    
    # for each piece in falling after the first, call drop with the list of falling excluding that piece and subtract
    # 1 from safe_to_destroy if drop returns True
    for i in range(1, len(falling)):
        number_obliterated += drop(falling[:i] + falling[i+1:])
    
    print ("Part 2: {} pieces could be obliterated".format(number_obliterated))

def common(parts_is_parts):
    falling = [((-100,-100,-1), (100,100,0), (20,20,20))] + list(read_data())
    # sort falling by the third element of the first tuple
    falling.sort(key=lambda x: x[0][2])

    drop(falling)

    parts_is_parts(falling)`

**part1** and **part2** take a list of settled blocks and (in part 1) removes a block at a time to see if anything moves, and counts the blocks that can be safely removed. In part 2, we destroy each block and count how many pieces end up falling. It would have been a good idea to feed the blocks detected in part 1 into part 2, as those we could safely skip, but it takes like ten minutes for each part with this solution, and I decided just to let it go.

So, not a fast solution, probably not the best solution, but a solution.

Three more days.
