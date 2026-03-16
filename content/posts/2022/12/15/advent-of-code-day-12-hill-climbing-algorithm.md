---
date: '2022-12-15T20:11:29-05:00'
draft: false
title: "Advent of Code Day 12 -- Hill Climbing Algorithm"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/12/15/advent-of-code-day-12-hill-climbing-algorithm/"
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
summary: "The title says it all. It's a \"shortest path\" puzzle, you're meant to use Dijkstra's algorithm, and the puzzle has no curve balls to toss at you."
description: "The title says it all. It's a \"shortest path\" puzzle, you're meant to use Dijkstra's algorithm, and the puzzle has no curve balls to toss at you."
tags:
  - "Advent of Code"
  - "Advent"
  - "Dijkstra"
  - "Python"
  - "Vscode"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-15-17.06.41-A-woman-in-a-Christmas-cap-hiking-up-a-steep-wandering-path-to-the-top-of-a-hill-over-looking-a-jungle-river-by-Bob-Eggleton-detailed-and-intricate.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-15-17.06.41-A-woman-in-a-Christmas-cap-hiking-up-a-steep-wandering-path-to-the-top-of-a-hill-over-looking-a-jungle-river-by-Bob-Eggleton-detailed-and-intricate.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Most Advent of Code puzzles expect you to solve them using some sort of Data and Algorithms method. One of the favorites is [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), the first algorithm to find the shortest distant between two points. We had two puzzles last year that used it.

Given the really matter-of-factness of the title, they know we're gonna use Dijkstra, we know we're gonna use Dijkstra, the only possible question is how fancy we're gonna be.

There's plenty of packages that handle graph theory. But since every motion has an equal cost, this is an unweighted graph. According to the rules of the puzzle, you can always go to a neighbor that is the same height or lower, but you cannot go to a neighbor if it is more than one unit above you. So it is directed. This is a unweighted directed graph problem.

My solution uses something called a 'priority queue'. Anything can be put into the queue, but the next thing to come out of it will be the one with the lowest (or tied for lowest) distance covered.

This works like: Start at some starting point. Find every node you haven't already visited that doesn't pass through another node, and add them to your queue, with the distance. So if you have already gone *n* steps, the distance for these new nodes would be *n+1*. Now find the node with the lowest distance, and do all the same calculations. This will eventually arrive at the shortest path.

This algorithm doesn't know how close to the goal you're getting; a variant of this algorithm called **A-Star** (*A**) includes a heuristic encoding this information as part of its distance. But since this ran quickly enough, I didn't feel it was necessary.

I use this algorithm *a lot*.

**Python 3.11**

And this really *is* Python 3.11, now that I fixed the issue in VS Code that was always running it in 3.9. I needed something that was added in 3.10 for this puzzle, so I finally figured out how to get it using the latest.

```
import heapq

def read_grid():
    with open(r"2022\puzzle12.txt") as f:
        return f.read().splitlines()

def value_of(c):
    match c:
        case 'S': return ord('a')
        case 'E': return ord('z')
        case _: return ord(c)

def legal_move(grid, x, y, mx, my):
    if mx = len(grid[0]) or my = len(grid):
        return False
    return value_of(grid[my][mx]) <= value_of(grid[y][x]) + 1

def walk_the_path(grid, f):

    path = []
    backtrack = set()

    for move in [(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if f(c)]:
        heapq.heappush(path, (0, *move))

    while path:
        d, x, y = heapq.heappop(path)
        if grid[y][x] == "E":
            return d

        for mx, my in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if legal_move(grid, x, y, mx, my) and (mx, my) not in backtrack:
                heapq.heappush(path, (d+1, mx, my))
                backtrack.add((mx, my))

grid = read_grid()

print ("Part 1:", walk_the_path(grid, lambda c: c == 'S'))
print ("Part 2:", walk_the_path(grid, lambda c: c == 'S' or c == 'a'))
```
