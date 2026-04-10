---
date: '2022-12-20T23:06:05-05:00'
draft: false
title: "Advent of Code Day 20 -- Grove Positioning System"
author: "Tipa"
disqusIdentifier: "2022/12/20/advent-of-code-day-20-grove-positioning-system"
summary: "As someone remarked today on Reddit, the entire plan hinged upon you remembering a ten digit prime number you randomly overheard twenty days ago."
categories:
  - "Advent of Code"
tags:
  - "Elf"
  - "Python"
relatedPosts:
  - url: "/2023/12/21/advent-of-code-day-21-step-counter/"
    title: "Advent of Code Day 21 -- Step Counter"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
  - url: "/2023/12/19/advent-of-code-day-19-aplenty/"
    title: "Advent of Code Day 19 -- Aplenty"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-19-20.12.32-A-whimsical-and-detailed-illustration-set-on-Gear-Island-where-a-magical-workshop-is-bustling-with-activity.-Elves-dressed-in-colorful-attire-are-b.png"
  - url: "/2023/12/07/advent-of-code-day-7-camel-cards/"
    title: "Advent of Code Day 7 -- Camel Cards"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-07-21.36.26-In-a-desert-setting-a-Christmas-elf-mom-and-a-repair-person-in-a-safety-vest-and-hard-hat-are-riding-camels.-Both-characters-are-holding-a-hand-of-pl.png"
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-20-22.51.19-A-woman-wearing-a-Christmas-hat-looking-up-at-a-starry-sky-above-a-jungle-at-night.-Her-face-is-lit-by-the-glow-coming-from-her-handheld-device.-By-Ha.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-20-22.51.19-A-woman-wearing-a-Christmas-hat-looking-up-at-a-starry-sky-above-a-jungle-at-night.-Her-face-is-lit-by-the-glow-coming-from-her-handheld-device.-By-Ha.png"
---
As someone remarked today on Reddit, the entire plan hinged upon you remembering a ten digit prime number you randomly overheard twenty days ago.
<!--more-->

I'd say this finally caught me up, but I still have Day 13 to do at some point. 

Okay, so after the terror that was Day 19 (for me, anyway, other people solved it WAY FASTER and had WAY FASTER solutions), today was easy. I was busy in the morning and busy in the evening with family game night, so I was pretty happy to read on Reddit today that today was an easy puzzle. And so it turned out to be.

[Today's puzzle](https://adventofcode.com/2022/day/20) was to take a list of numbers, and move it up or down in the list according to its value, wrapping around the beginning and the end, and then summing up three specific numbers from that list.

With modulo arithmetic (again), plus a little nudge for an edge case, the Part 1 answer dropped right out.

Part 2 just did this shuffle ten times after multiplying each number by a ten digit prime that was supplied, and then figuring out the same formula as for Part 1.

That was it; that was the puzzle.

I'm just glad we might be seeing the elves again. Dall-E 2 likes drawing pictures of elves.

**Python 3.11**

read_input returns a list of tuples where the left element is the index in the original list, and the right element is the actual value. I'm not sure how other people did it, but it seemed the best way to me and I'm sure I'll find that's what people did.

The final value depends on counting from the index of zero in the list, so that's what index_of_zero does.

mix does all the fun work. And that is it.

```
def read_input():
    with open(r"2022\puzzle20.txt") as f:
        return list(enumerate(map(int, f.read().splitlines())))

def index_of_zero(number_list):
    for i in range(len(number_list)):
        if number_list[i][1] == 0:
            return i

def mix(mix_count=1, multiplier=1):
    number_list = read_input()
    list_size = len(number_list)

    number_list = [(i, n * multiplier) for i, n in number_list]

    for _ in range(mix_count):
        for i in range(list_size):
            for j in range(list_size):
                if number_list[j][0] == i:
                    num = number_list[j]
                    number_list.pop(j)
                    if num[1] == -j:
                        number_list.append(num)
                    else:
                        number_list.insert((j + num[1]) % (list_size-1), num)
                    break

    zi = index_of_zero(number_list)
    return sum(number_list[(zi + i) % len(number_list)][1] for i in range(1000, 4000, 1000))

print("Part 1:", mix())
print("Part 2:", mix(10, 811589153))

```
