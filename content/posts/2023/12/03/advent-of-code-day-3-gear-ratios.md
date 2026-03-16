---
date: '2023-12-03T13:01:35-05:00'
draft: false
title: "Advent of Code Day 3 -- Gear Ratios"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/03/advent-of-code-day-3-gear-ratios/"
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
summary: "My Haskell experiments end. Even though I got the answer, have I failed?"
description: "My Haskell experiments end. Even though I got the answer, have I failed?"
tags:
  - "Advent of Code"
  - "Advent"
  - "Elf"
  - "Haskell"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

I am super disappointed in myself today. I spent the entire morning working, on Haskell, to parse the input for this problem, but I just couldn't do it. It's not that Haskell isn't suited for it; it's just that the way I think about solving these problems is incompatible with Haskell.

I've looked at the Haskell solutions for the first two days of Advent of Code and they are *nothing like mine* whatsoever. In fact, I can barely follow what's going on. There's a mindset you get with a computer language, where you just naturally think fluently. I have that with Python and Java. I do *not* have that with Haskell. I dunno. This is my failure, not the language's.

Anyway. So the deal here is that[ you are taking a gondola from the tundra island](https://adventofcode.com/2023/day/3) you were trebucheted to yesterday to the place where the snow machine lives. The gondola is, of course, broken. There is an elf fixing it, but they're not having much luck. Some parts are missing!

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/image.png" class="align-left" >}}

To the left here is the sample input, which is the blueprint to the machine we're trying to fix. We're trying to find the sum of all the part numbers, where a part number is any string of digits that is adjacent to a symbol that is not a period. In this example, the only numbers that are not part numbers are 114 and 58.

So that's not too tough, right? Well, I couldn't figure it out in Haskell. I got like 80% of the way there.

Part 2 of the problem focuses on the "*" symbol, those stars that have exactly two part numbers adjacent to them. They want the product of those numbers to form the gear ratio, and then they want the sum of all those products.

Not super hard, right? Well, for me, in Haskell, it was.

So let's see it in Python.

`import re
from itertools import chain

def part1(data, width, height):
    numbers = [n for n in numberGenerator(data) \
            if any([isSymbol(data[srow][scol]) for srow, scol in getAdjacent(height, width, n)])]
    print ("Part 1:", sum(x[3] for x in numbers))

def part2(data, width, height):
    # make a list of coordinates of every '*' in the data
    stars = [(row, col) for row, line in enumerate(data) for col, ch in enumerate(line) if ch == '*']
    starDict = {star: [n for n in numberGenerator(data) if star in getAdjacent(height, width, n)] for star in stars}
    print ("Part 2:", sum([x[0][3] * x[1][3] for x in [v for v in starDict.values() if len(v) == 2]]))
`

I'm going to use regular expressions, hence importing the '**re**' library, and I want to flatten a list of lists like I did yesterday with '**concat**' in Haskell, so importing '**chain**' from **itertools **that does the same thing.

Part 1 and Part 2 do as I mentioned above, so not going to dive deeper into those.

`# numberGenerator: take a list of strings, extract all the numbers from it, returning a generator of tuples
def numberGenerator(data):
    for n in chain(*[extractNumbers(line, row) for row, line in enumerate(data)]):
        yield n
`

Generators are a Python object that return a series of values, one at a time. It's friendlier than just making a huge list, because it doesn't take memory, and also because there can be logic around what it's returning. On the other hand, this *does* just make a list and iterate through it, so this could just have returned the list, but I only realized I didn't need a generator particularly just now. Well, there it is. We'll look at **extractNumbers **soon. **enumerate** is a Python operator which returns items and their index as a tuple from a list. So it would return [(0, "line 0 data"), (1, "line 1 data")] etc. **extractNumber** returns a list, so **chain** flattens that out. **yield** returns the next value. When it runs out of values, the generator terminates.

`# extractNumbers: take a string, extract all the numbers from it, returning a list of tuples containing row,
# column, length, and the number itself as a string
def extractNumbers(line, row):
    return [(row, x[1], len(x[0]), int(x[0])) \
            for x in zip(re.findall(r'\d+', line), [x.start() for x in re.finditer(r'\d+', line)])]
`

Does what it says on the label. It takes a row of input (and the row number), uses a regular expression to find all the numbers and then another regular expression to find the starting position of all the numbers, uses **zip** to make these two separate list into one list of tuples, then uses that to make a list of tuples that includes the row number, column number, length of the number and the number itself as an integer.

`# given a width, a height, and a tuple from extractNumbers, return a list of coordinates adjacent to the
# number
 string
def getAdjacent(height, width, number):
    adjacentCoords = [(number[0] - 1, number[1] -1 + x) for x in range(number[2]+2)] + \
                     [(number[0] + 1, number[1] -1 + x) for x in range(number[2]+2)] + \
                     [(number[0], number[1] - 1), (number[0], number[1] + number[2])]
    return [x for x in adjacentCoords if x[0] >= 0 and x[0] = 0 and x[1] 

This returns a list of coordinates that surround the position of the number in the data. The height and width parameters sets the bounds. So it makes a list of the coordinates, then the **return** statement only returns those elements that are within bounds.

`# return True if the character is not a digit and is not a period
def isSymbol(ch): return not ch.isdigit() and ch != '.'

# readData: read the data file into a list of lists stripping newlines
def readData():
    with open("puzzle3.dat") as f:
        return f.read().splitlines()
`

**isSymbol** just checks to see if the character given is a symbol as defined by the puzzle. **not ch.isDigit()** isn't necessary for the puzzle input, though I feel it should be there.

**readData** reads the input file. This screwed me up for awhile because I was initially using **f.readLines()**, which does not strip out the line feeds, and the code was seeing those as a symbol. That took *way* too long for me to debug.

`if __name__ == "__main__":
    data = readData()
    width, height = len(data[0]), len(data)
    part1(data, width, height)
    part2(data, width, height)

`

And finally, the main routine. We read the input, get the dimensions, call **part1** and **part2**, and we're done. Part 1 returns instantly, part 2 takes a couple seconds, not entirely sure why it is so slow, but I have ideas on how to fix it, if I cared, which I don't. Been working on this in Haskell, Python and writing this post for six hours now and I am done.

*Edit: I fixed the performance issue. You can see [the corrected code in the AoC subreddit](https://old.reddit.com/r/adventofcode/comments/189m3qw/2023_day_3_solutions/kbucba8/)*.
