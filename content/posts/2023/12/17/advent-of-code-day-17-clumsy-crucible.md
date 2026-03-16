---
date: '2023-12-17T16:50:55-05:00'
draft: false
title: "Advent of Code Day 17 -- Clumsy Crucible"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/17/advent-of-code-day-17-clumsy-crucible/"
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
summary: "Edsger Dijkstra is laughing at me from his grave."
description: "Edsger Dijkstra is laughing at me from his grave."
tags:
  - "Advent of Code"
  - "A*"
  - "AoC2023"
  - "Dijkstra"
  - "Elf"
  - "Lava"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-17-16.23.47-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-is-a-birds-eye-view-of-Gear-Island-half-empty-and-half-a-bustling-fac.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-17-16.23.47-Illustration-for-an-Advent-of-Code-puzzle-with-a-16-10-aspect-ratio.-The-scene-is-a-birds-eye-view-of-Gear-Island-half-empty-and-half-a-bustling-fac.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

The *reason* Dijkstra is spinning in his grave is because, *apparently*, the elves have never read his Wikipedia page about his find-the-shortest-path algorithm.

I knew this was an A*/Dijkstra problem the moment I saw it. There's at least one every year. I know the algorithm well. [I read it](https://adventofcode.com/2023/day/17), I understood it, I implemented it and... it failed. *How?*

You can read the whole page about it [here on Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). I'm going to copy out the important part.

> Let the node at which we are starting be called the **initial node**. Let the **distance of node *Y*** be the distance from the **initial node** to *Y*. Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.
> 
> - Mark all nodes unvisited. Create a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) of all the unvisited nodes called the *unvisited set*.
> - Assign to every node a *tentative distance* value: set it to zero for our initial node and to infinity for all other nodes. During the run of the algorithm, the tentative distance of a node *v* is the length of the shortest path discovered so far between the node *v* and the *starting* node. Since initially no path is known to any other vertex than the source itself (which is a path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.[[17]](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#cite_note-17)
> - For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the one currently assigned to the neighbor and assign it the smaller one. For example, if the current node *A* is marked with a distance of 6, and the edge connecting it with a neighbor *B* has length 2, then the distance to *B* through *A* will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
> - When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again (this is valid and optimal in connection with the behavior in step 6.: that the next nodes to visit will always be in the order of 'smallest distance from *initial node* first' so any visits after would have a greater distance).
> - If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
> - Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new *current node*, and go back to step 3.
> 

> https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

`legal_moves = { (0,0): ((1, 0), (0, 1)),
                (0, -1) : ((1, 0), (-1, 0)),
                (1, 0): ((0, -1), (0, 1)),
                (0, 1): ((1, 0), (-1, 0)),
                (-1, 0): ((0, -1), (0, 1)) }

def parts_is_parts(parts: str, mmin: int, mmax: int):
    with open('puzzle17.dat') as f:
        grid = [[int(x) for x in line] for line in f.read().splitlines()]
    destination_coord = (len(grid[0]) - 1, len(grid) - 1)
    heap = [(0, (0,0), (0,0))]
    heat_map = {(0,0): 0}`

The puzzle has a couple of quirks. The path from start to finish can't cross itself, and it also can't go more than a certain distance in one direction before turning. **legal_moves** shows the legal turns given a current direction. **parts_is_parts** takes a string for display later, the minimum distance the crucible can travel in one direction (1 space for part 1), and the maximum distance it can travel in one direction (3 spaces for part 1). Part two changes these to 4 and 10 respectively, but it otherwise the same.

**Step 1** above is missing. I had it, my solution didn't work with it, I took it out based on hints from the subreddit, it worked, I got angry.

**destination_coord** is our destination, the lower right corner of the map. I also use it for bounds checking. **heap** implements step 2 with Pythons heapq library. **heat_map** holds the minimum cost of traveling to a node; it is initially zero for our starting node, (0,0).

`    while heap:
        heat_loss, coord, direction = heappop(heap)

        if coord == destination_coord: 
            break

        for new_direction in legal_moves[direction]:
            new_heat_loss = heat_loss
            for steps in range(1, mmax + 1):
                new_coord = (coord[0] + steps * new_direction[0], coord[1] + steps * new_direction[1])
                if new_coord[0]  destination_coord[0] or new_coord[1] > destination_coord[1]:
                    continue
                new_heat_loss = new_heat_loss + grid[new_coord[1]][new_coord[0]]
                if steps >= mmin:
                    new_node = (new_coord, new_direction)
                    if heat_map.get(new_node, inf) 

While we have nodes to cover, we pop the info from the heap. For the first one, we pop the one we just pushed onto it, so **heat_loss** is 0 and **coord** and **direction** are both (0,0) -- top left corner, not traveling in any direction (yet).

To decide where to go next, we need to push more nodes onto the heap. So we travel in the legal directions (east and south for the first square) the max distance, checking along the way if we have traveled the minimum distance, seeing if we are still on the map, summing up the weights on the map along the way. If our new heat loss is less than the current heat loss value for that position and direction (defaulting to infinity), we substitute the new value, otherwise we continue on.

So that's your basic Dijkstra. The variant commonly used in gaming, **A***, wasn't appropriate here because you have no surety that the lowest cost path proceeds at all times toward the destination. It does, actually, but I put in a basic heuristic and I didn't notice any speed increase, so I took it out again. Needlessly complex.

A key element of Dijkstra is that a node is never visited twice. There's a... **holy f****** ***** ********** I put the "visited" check back in and now my solution runs a third faster. I *swear* this wasn't working with it this morning.

I'm over this one. I am stupid and have no idea what I'm doing. Here's the code.

```
from heapq import heappush, heappop
from math import inf

legal_moves = { (0,0): ((1, 0), (0, 1)),
                (0, -1) : ((1, 0), (-1, 0)),
                (1, 0): ((0, -1), (0, 1)),
                (0, 1): ((1, 0), (-1, 0)),
                (-1, 0): ((0, -1), (0, 1)) }

def parts_is_parts(parts: str, mmin: int, mmax: int):
    with open('puzzle17.dat') as f:
        grid = [[int(x) for x in line] for line in f.read().splitlines()]
    destination_coord = (len(grid[0]) - 1, len(grid) - 1)
    heap = [(0, (0,0), (0,0))]
    heat_map = {(0,0): 0}
    visited = set()

    while heap:
        heat_loss, coord, direction = heappop(heap)

        if coord == destination_coord: 
            break

        if (coord, direction) in visited: continue
        
        visited.add((coord, direction))

        for new_direction in legal_moves[direction]:
            new_heat_loss = heat_loss
            for steps in range(1, mmax + 1):
                new_coord = (coord[0] + steps * new_direction[0], coord[1] + steps * new_direction[1])
                if new_coord[0]  destination_coord[0] or new_coord[1] > destination_coord[1]:
                    continue
                new_heat_loss = new_heat_loss + grid[new_coord[1]][new_coord[0]]
                if steps >= mmin:
                    new_node = (new_coord, new_direction)
                    if heat_map.get(new_node, inf) <= new_heat_loss: continue
                    heat_map[new_node] = new_heat_loss
                    heappush(heap, (new_heat_loss, new_coord, new_direction))
                    
    print (parts, heat_loss)

from timeit import Timer
t = Timer(lambda: parts_is_parts("Part 1:",1,3))
print(t.timeit(number=1))
t = Timer(lambda: parts_is_parts("Part 2:",4,10))
print(t.timeit(number=1))
```
