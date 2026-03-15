---
date: '2023-12-15T07:00:00-05:00'
draft: false
title: "Advent of Code Day 14 -- Parabolic Reflector Dish"
summary: "We're almost to the mountaintop where everything begins... but first we need to start a little fire."
categories:
  - "Advent of Code"
tags:
  - "AoC2023"
  - "Cycle Detection Algorithm"
  - "Mirrors"
  - "Python"
  - "Volcano"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-14-21.53.41-A-wall-of-mirrors-attached-to-a-cliff-face-on-the-left-side-of-the-image-with-a-dormant-volcano-in-the-background-steaming.-The-sun-is-setting-over-.png"
cover: "https://chasingdings.com/wp-content/uploads/2023/12/DALL·E-2023-12-14-21.53.41-A-wall-of-mirrors-attached-to-a-cliff-face-on-the-left-side-of-the-image-with-a-dormant-volcano-in-the-background-steaming.-The-sun-is-setting-over-.png"
---

So, you've reached your destination, and the dormant volcano is in front of you. Something needs to be done to turn it back *on*, though. Maybe that conveniently placed giant multi-segment parabolic mirror could be of some help?

Turns out it isn't focused very well, and it looks like it might collapse. There's a console nearby that lets you tilt the mirrors in various directions. It's so large that it is covered with rocks, some rounded that can be moved when the mirrors move, some fixed in place (you walked through these mirrors yesterday; now you can see them all at once). You think that if you could tilt the mirror and move some of those rocks, then the mirror might focus well enough to set the volcano alight again. And if that doesn't work, maybe you can *spin* it. [Maybe a billion times or so, just to be sure](https://adventofcode.com/2023/day/14).

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/12/rolling_rocks.gif" title="An animation I made" class="align-center" >}}

Usually I snap a picture of the puzzle input from the puzzle page, but I made an animation showing how the spinning of the mirrors affects the rolling rocks. You can see the score along the right edge develop a cycle, and that is the key to solving the billion spins.

Someone who saw this said I'd given them the hint they needed to finish their solution, which they said ran to completion in 600ms. I was feeling pretty good about that while at work, and was a little disappointed when I finished my solution and it seemed like it would take hours to run. I did some relentless optimization, but I still didn't get it below 17s. I looked at some other Python solutions in the subreddit and they seemed less optimized than mine, but ran faster. It looks like the other solutions are storing the entire puzzle in a cache, detecting the first repeat, subtracting the index of the repeat from the index of the first time it was seen to get the cycle length and the offset to the start of the cycle, then doing a little modulo arithmetic to get the answer.

I should have done something like that. Instead... I'll talk about my solution. But first, I want to talk about the Tortoise and Hare algorithm to find cycles.

The basic idea is that you have one pointer moving through data one element at a time -- the tortoise. You have another moving at twice the speed -- the hare. When they meet, it means that a cycle exists and that they are currently in it. A little more analysis calculates the start of the cycle and the length of the cycle. The Tortoise/Hare algorithm is meant to be used for linked lists -- elements that point to the next element in the list.

I was storing a list of scores. Since scores can repeat with different board configurations, I looked for a run of three scores, which was enough. And since these were just integers and not linked lists, the algorithm really didn't work. So let's look at the code.

`def let_us_rock(data: list) -> tuple:
    # record the (x,y) coordinates of every 'O' in the data
    round_rocks = {(x,y): data[y][x] == 'O' for y in range(len(data)) for x in range(len(data[y]))}
    # record the (x,y) coordinates of every '#' in the data
    rocks = [(x,y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == '#']
    # record the (x,y) coordinates of each space bordering the data
    width, height = len(data[0]), len(data)
    border = [(x,y) for y in range(-1, height+1) for x in range(-1, width+1) if x == -1 or x == width or y == -1 or y == height]
    return (round_rocks, set(rocks+border), height)`

Instead of storing the board as characters, I read all the moving rocks into a dictionary with the (x,y) coordinate as a key and a True/False value to say whether or not it currently contains a rock. This was one of the optimizations. Immovable rocks and a border I added so I didn't need to worry about bounds checking goes into a set of rocks.

`def let_us_roll(round_rocks: dict, rocks: set, offset: tuple) -> tuple:
    # calculate a new list of round_rocks each offset by offset as long as the new round_rocks is not in rocks
    moved = False
    for xy in round_rocks.keys():
        if not round_rocks[xy]: continue
        moved_to = xy
        for i in range(1, 1000):
            new_pos = (xy[0] + i * offset[0], xy[1] + i * offset[1])
            if new_pos not in rocks and not round_rocks[new_pos]:
                moved_to = new_pos
            else:
                break
        if moved_to != xy:
            round_rocks[moved_to] = True
            round_rocks[xy] = False
            moved = True`

These routine looks through the round_rocks dictionary, finds those coordinates that contain a round rock, and moves it as far as it can in the direction of the offset before it hits something. We return True if any rocks moved, so we can keep calling it until the board settles down.

`def score(round_rocks: dict, top_row: int) -> int:
    # calculate the score of the round_rocks
    return sum([top_row - xy[1] for xy in round_rocks if round_rocks[xy]])

def rolling_rock(round_rocks: list, rocks: set, top_row: int, offset: tuple) -> tuple:
    # calculate the round_rocks after they have rolled down the rocks
    # return the round_rocks and the score of the round_rocks
    while True:
        round_rocks, moved = let_us_roll(round_rocks, rocks, offset)
        if not moved:
            break
    return (round_rocks, score(round_rocks, top_row))

def spin(round_rocks: dict, rocks: set, top_row: int) -> tuple:
    for offset in [(0,-1), (-1,0), (0,1), (1,0)]: # north, west, south, east
        round_rocks, score = rolling_rock(round_rocks, rocks, top_row, offset)
    return (round_rocks, score)`

**score** scores the board according to the rules of the puzzle. **rolling_rock** keeps calling **let_us_roll** until the board is in a settled state. **spin** tilts the board in all four directions -- this is what we're doing in Part 2.

`def more_score(round_rocks: dict, rocks: set, top_row: int, scores: list, target: int):
    while target > len(scores):
        round_rocks, score = spin(round_rocks, rocks, top_row)
        scores.append(score)
    return (round_rocks, scores)

def part2():
    round_rocks, rocks, top_row = let_us_rock(read_data())
    scores = []
    round_rocks, scores = more_score(round_rocks, rocks, top_row, scores, 10)
    print ("Score head", scores[:10])
    # use tortoise and hare algorithm to find the cycle in scores
    tortoise, ti = scores[:3], 0
    hare, hi = scores[1:4], 1
    while hare != tortoise:
        ti += 1
        hi += 2
        round_rocks, scores = more_score(round_rocks, rocks, top_row, scores, hi+3)
        tortoise, hare = scores[ti:ti+3], scores[hi:hi+3]
    print ("Met up at", ti, hi, tortoise, hare)
    hi = ti + 1
    round_rocks, scores = more_score(round_rocks, rocks, top_row, scores, hi+3)
    hare = scores[hi:hi+3]
    while hare != tortoise:
        hi += 1
        round_rocks, scores = more_score(round_rocks, rocks, top_row, scores, hi+3)
        hare = scores[hi:hi+3]
    print ("Cycle at", ti, hi, tortoise, hare)
    print ("Cycle length", hi-ti)
    xi = (1000000000 - ti) % (hi-ti)
    print ("Part 2:", scores[ti+xi-1])`

So if it took zero time to calculate new board states during a spin, I'd just make a few thousand and look for cycles there. But since it is *slow*, I keep a list of scores so far, and use **more_score** to get some more scores as the search algorithm requires it.

**part2** shows the tattered remnants of the Tortoise/Hare algorithm. The first part works well enough, but I couldn't get the algorithm to give me the cycle offset and length. That's fine. *I don't need them.* I scan forward to find the first duplicate -- that's the cycle length. I make the *assumption* that the hare and tortoise met at the start of the cycle because it doesn't matter if it is or not, as long as we know they are currently *in* the cycle, which we do. With an ersatz offset but a valid cycle length, we have all the information we need to calculate which score in the cycle is at index one squillion.

So, a little disappointed. I thought I would do better. But it is solved.

Someday I am going to find a valid use case for Tortoise/Hair that actually uses linked lists.
