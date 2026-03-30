---
date: '2023-12-09T10:39:23-05:00'
draft: false
title: "Advent of Code Days 8 and 9 -- Ghost Story"
author: "Tipa"
summary: "It took me so long to figure out the Day 8 puzzle that I didn't write it up before bed, so twofer today to catch up."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Camel"
  - "Desert Walk"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_Ghosts_relaxing_next_to_a_watery_spring_in_a_desert_oas_8d6068ef-f97c-49b5-9979-e42e67546244.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_Ghosts_relaxing_next_to_a_watery_spring_in_a_desert_oas_8d6068ef-f97c-49b5-9979-e42e67546244.png"
---
It took me so long to figure out the Day 8 puzzle that I didn't write it up before bed, so twofer today to catch up.
<!--more-->

Every year there is at least one problem where I know what the answer is, but I don't know *why* the answer is. Part of that, on day 8, was my own fault. I was just futzing with things for hours before I decided to submit the puzzle solution. Only when I started looking at *other* solution on the subreddit did I figure out that I was at least partially right all along and I should have gone with my instincts.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/af1af6d5-3feb-4814-98b9-6d17e62c064a-1024x585.webp" title="Day 8: Haunted Wasteland" classes="center" >}}

Midjourney for the header image, Dall-E for the repair guy on a camel in a sandstorm. I've decided, for these AI renderings, to personify the person who is supposed to be solving all these puzzles as a repairman with a safety vest and helmet. Dall-E can do a repair woman without making it all sexy, but I dunno. I've just seen the elf helper as a guy in my head. I like looking at pictures of men. Sue me for liking guys.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-5.png" classes="fig-20" >}}

Anyway. The haunted wasteland is what the desert turns out to be as a sandstorm swirls up and your elf guide vanishes. To be fair, she was just recently talking about ghosts. [Not really surprising that she'd be one](https://adventofcode.com/2023/day/8).

Well grats, you're in a sandstorm now, and you're lost. Luckily, you have a map that gives you a bunch of "turn left, turn right" directions and locations and you think you can follow that. Part 1 of the puzzle is finding the length of the path from your starting point ("AAA") to your destination ("ZZZ") given input like you see in the sample data on the left. The "RL" instructions are meant to be repeated, and you choose either the left or right destination based on your current location and the instruction.

`def trace(current, lr, maps):
    plen = 0
    while current[-1] != 'Z':
        current = maps[current][next(lr)]
        plen += 1
    return plen`

That's what this one does. Takes the current position and applies the "LR" instructions to the map until it reaches the destination -- any location that ends with 'Z'. This is important to Part 2.

In the second part, you decide that you are still lost, and the reason is that this is a map for *ghosts*, and you should find all locations where the final letter is 'A', and follow each path simultaneously until they all reach a location with a final letter of 'Z' *at the same time*. There were six such starting point/end point pairs in the data I had, and since you just kept going if you reached a destination in one path but not at all the others, each of these paths were a cycle.

`def part1():
    lr, maps, _ = readData()
    print ("Part 1:", trace('AAA', cycle(lr), maps))

def part2():
    lr, maps, _ = readData()
    currents = [x for x in maps.keys() if x[-1] == 'A']
    plens = [trace(current, cycle(lr), maps) for current in currents]
    print ("Part 2:", lcm(*plens))`

I early figured out that each starting point reached its own unique end point without crossing any of the others, which made things easier. I also quickly figured out that the cycle repeated at the very first location after the starting one, but *I did not trust that answer*. It seemed like a mistake. It wasn't -- it was the only thing, actually, that made the puzzle possible to solve. Well, I'd read that the answer was the lowest common multiple of all the cycle lengths, so I submitted that and it worked, but I had to keep looking at the code and the problem and trace a few things by hand before I realized *why* that was the solution.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/affa24b2-9776-40ee-a70b-b5d60e023b8f-1024x585.webp" title="Day 9: Mirage Maintenance" classes="center" >}}

I guess I should start specifying the colors of the safety vest and hard hat.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-6.png" classes="fig-20" >}}

So, on to Day 9: Mirage Maintenance. When the sandstorm clears, you find yourself at an oasis! Yay! You see a hang glider nearby and look forward to seeing if you can use it somehow to get to the next floating island, Metal Island. But that's for later. For now, you want to [take some readings at the oasis](https://adventofcode.com/2023/day/9) and see if everything looks good.

For this puzzle, you're given a sequence of integers, and you have to keep reducing the list by finding the differences between them until you get down to a list of all zeroes, then work your way back up to find the next number in the sequence (for part 1) and the previous number in the sequence (for part 2). You can see the sample extrapolation given by the problem just above, there.

`def calc_puzzle_right(val_list):
    # handle case of empty list or all zeros
    if not val_list or all(v == 0 for v in val_list): return val_list + [0]
    new_list = [(val_list[i+1] - val_list[i]) for i in range(len(val_list)-1)]
    return val_list + [val_list[-1] + calc_puzzle_right(new_list)[-1]]

def calc_puzzle_left(val_list):
    # handle case of empty list or all zeros
    if not val_list or all(v == 0 for v in val_list): return [0] + val_list
    new_list = [(val_list[i+1] - val_list[i]) for i in range(len(val_list)-1)]
    return [val_list[0] - calc_puzzle_left(new_list)[0]] + val_list`

**calc_puzzle_right** handles the part 1 case. Both solutions use recursion, so it starts off the with case that the list is empty or all zeroes, in which case it just adds another zero to the list and returns it. Otherwise, it make **new_list**, a list of all the differences between the values, calls itself recursively to find the next difference, then adds that new number to the last number of the current list to make the new last number for the list. (In Python, *a*[-1] returns the last element of *a*.)

**calc_puzzle_left** handles the part 2 case. Same as before, but we are prepending a number to the start of the list instead of the end. And that's it.

Both these days could easily be done in Haskell, and I hope to get to that at some point.
