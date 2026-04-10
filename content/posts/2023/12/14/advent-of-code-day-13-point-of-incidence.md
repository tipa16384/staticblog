---
date: '2023-12-14T07:08:33-05:00'
draft: false
title: "Advent of Code Day 13 -- Point of Incidence"
author: "Tipa"
disqusIdentifier: "2023/12/14/advent-of-code-day-13-point-of-incidence"
summary: "I think if I went to Iceland and stood on one of those lava fields, I would be convinced I was in another world."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Mirrors"
  - "Volcano"
relatedPosts:
  - url: "/2023/12/15/advent-of-code-day-14-parabolic-reflector-dish/"
    title: "Advent of Code Day 14 -- Parabolic Reflector Dish"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-14-21.53.41-A-wall-of-mirrors-attached-to-a-cliff-face-on-the-left-side-of-the-image-with-a-dormant-volcano-in-the-background-steaming.-The-sun-is-setting-over-.png"
  - url: "/2023/12/16/advent-of-code-day-16-the-floor-will-be-lava/"
    title: "Advent of Code Day 16 -- The Floor Will Be Lava"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-16-10.31.52-A-reindeer-leading-the-way-into-the-depths-of-a-giant-cave-that-serves-as-a-Lava-Production-Facility.-The-caves-walls-doorways-and-floor-are-all-na.png"
  - url: "/2023/12/12/advent-of-code-day-12-hot-springs/"
    title: "Advent of Code Day 12 -- Hot Springs"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-12-20.48.05-A-repairman-in-a-safety-vest-and-hardhat-looking-at-a-damaged-map-in-a-landscape-reminiscent-of-Iceland-near-a-dormant-volcano.-The-scene-includes-ste.png"
  - url: "/2022/12/18/advent-of-code-day-18-boiling-boulders/"
    title: "Advent of Code Day 18 -- Boiling Boulders"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-18-19.03.10-An-elephant-watching-a-flaming-meteor-crash-into-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-13-22.52.31-An-ash-field-dotted-with-boulders-and-large-frameless-standless-mirrors-over-six-feet-tall-reflecting-each-other-the-ash-and-the-rocks.-In-the-f.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-13-22.52.31-An-ash-field-dotted-with-boulders-and-large-frameless-standless-mirrors-over-six-feet-tall-reflecting-each-other-the-ash-and-the-rocks.-In-the-f.png"
---
I think if I went to Iceland and stood on one of those lava fields, I would be convinced I was in another world.
<!--more-->

My boyfriend walked up to me as I was solving this puzzle and thought I was still working on *yesterday's* puzzle, because they looked the same.

They do, kinda.

I read this puzzle before I left to go to work today. Actually back in the actual real office. I didn't have any time to work on it, but I was thinking of it through the day. When I finally sat down to it after dinner, I quickly got part 1 working. Part 2, I had to think about -- but I think my approach to Part 1 made Part 2 pretty easy. Both parts run almost instantly, so I must have done something right.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-16-1024x643.png" title="Midjourney" classes="center" >}}

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-17.png" classes="fig-20" >}}

You were safely launched onto Lava Island by one of the hot springs you found. Unfortunately, there is no lava to be found! Without lava, the elves at Hot Springs can't forge the parts to get Metal Island working to get sand flowing to get purification happening and water flowing and snow falling and everything else you have encountered so far. You resolutely head toward the volcano ahead of you that is suspiciously *not* spewing lava, when you trip over a mirror embedded in the ash. Turns out, there are hundreds of mirrors, and it's your job to map the reflections you see to determine where, exactly, the mirrors are. (Unlike in the renderings, the mirrors on Lava Island only reflect the rocks, the ash, and the other mirrors. They themselves are nearly invisible.)

It is so difficult to navigate the place that you decide to [determine the mirror locations by mapping out the reflections of ash and rock](https://adventofcode.com/2023/day/13). The spot where the reflections meet must be a mirror.

The sample puzzle input is on the left; it shows two mirrors. The one on the top has a vertical reflection between the fifth and sixth column. There seems to be a horizontal one, too, between the third and fourth rows, but the reflections aren't identical.

The puzzle on the bottom does have a horizontal reflection between the fourth and fifth row. There's extra stuff to see at the first row because of the angle of the mirror. Since there is no corresponding row on the bottom, we don't worry about it. Add a hundred for each row before a horizontal reflection, and one for each column before a vertical reflection, and that is part 1.

**Part 1**

I was looking at the puzzle data, and the rocks ('#') and ash ('.') looked to me like they could be 1s and 0s. Each row would just be an integer, super fast to compare. And if you took all those and set them in a matrix, you could tease out numbers from the bits running vertically, and then run the same code again.

And in fact that's exactly what I did.

`def read_data():
    with open("puzzle13.dat") as f:
        return [tobin(puz.splitlines()) for puz in f.read().split("\n\n")]

def tobin(puz: list) -> list:
    return (len(puz[0]), [int("".join(["1" if c == "#" else "0" for c in line]), 2) for line in puz])`

This returns a list of puzzles as lists of integers. I also save the width of a puzzle so I know how many bits to flip when I pivot the table.

`def score_puzzle(lp: list, f) -> int:
    l, p = lp[0], lp[1]
    x = f(p, len(p))
    if x: return x * 100
    p = [bitme(p, l-i-1) for i in range(l)]
    return f(p, l)

def score_helper(p: list, l: int) -> int:
    for i in range(1,l):
        z = zip(p[:i][::-1], p[i:])
        if all([a == b for a, b in z]):
            return i
    return None`

**score_puzzle** takes a puzzle (a list of integers), and a function. For part 1, this function is **score_helper**. **score_helper** does... it's super hard to explain. I'll ask ChatGPT to document this. (It didn't write this function -- I did. I stopped getting AI help when I stopped trying to solve puzzles with Haskell).

This function looks at different parts of a list and checks if one part is a reversed mirror image of another part. When it finds such a mirrored section, it returns the size of that section. If it doesn't find such a section, it returns None.

Thanks, ChatGPT. It splits the list up starting from the left, flips the remainder, zips them into tuples such that they all match up, discarding any excess, and if all the numbers match up exactly, it is a match. So who explained it better, me or ChatGPT?

**score_puzzle** calls **score_helper** on the puzzle, and if it doesn't find a vertical reflection, it creates a rotated version of the puzzle by separating all the bits of all the integers into a binary matrix, rotating that 90 degrees, and reconstituting them back into a list of integers, and then repeating the process.

Let's say we have a list of numbers -- 63, 12, 45, 51, 18 and 33. Let's write them into a six by six matrix, in binary.

`1 1 1 1 1 1 (63)
0 0 1 1 0 0 (12)
1 0 1 1 0 1 (45)
1 1 0 0 1 1 (51)
0 1 0 0 1 0 (18)
1 0 0 0 0 1 (33)`

We're going to read down the matrix from left to right (to make the scoring work) and make new numbers.

`1 0 1 1 0 1 (45)
1 0 0 1 1 0 (38)
1 1 1 0 0 0 (56)
1 1 1 0 0 0 (56)
1 0 0 1 1 0 (38)
1 0 1 1 0 1 (45)`

Our rotated puzzle is now 45, 38, 56, 56, 38 and 45, and now we can see the reflection. So that's how part 1 works.

**Part 2**

Part 2 asks, could we make different reflections if we just randomly changed a '.' to a '#' or a '#' to a '.'? Going through and swapping every symbol one at a time one every puzzle and then checking would take forever. This is where my idea to make them all into binary numbers saved me time. I haven't looked at other solutions, but I'd be shocked if this wasn't the key to everyone's solutions.

I said before that we use a different **score_helper** for Part 2.

`def score_helper_2(p: list, l: int) -> int:
    for i in range(1,l):
        z = list(zip(p[:i][::-1], p[i:]))
        number_same = sum([a == b for a, b in z])
        number_diff = sum([differ(a,b) for a, b in z])
        if number_diff == 1 and number_same + 1 == len(z):
            return i
    return None

# function returns true if a and b differ by only one bit
def differ(a: int, b: int) -> bool:
    n = abs(a-b)
    return n and (n & (n - 1) == 0)`

So part of this is me taking a guess that swapping one of the symbols would invalidate the previous reflection on that mirror, and this turned out to be the case.

We march through the puzzle as before, comparing rows against their reflection. But when we compare the individual numbers, we count the number of ones that are *identical*, and the number of ones that differ by just one digit. We don't care *which* binary digit changed, we're only concerned that it's just one.

We want only one such difference; all the other values should be identical, and the number of same and the number of different-by-1 should be the same size as the full reflection. If so, hey, we had a match, and we didn't have to swap *anything*. We just had to look at it differently,

The **differ** function subtracts two numbers. If the absolute value of the difference is a power of two, that means the numbers differ by just one bit. This is a little trick I picked up from Stack Overflow. Before there was ChatGPT, there was Stack Overflow to provide your coding help.

So, surprising me, I got both Part 1 and Part 2 correct, first try.

We're more than halfway through AoC. It's only going to get harder from here.
