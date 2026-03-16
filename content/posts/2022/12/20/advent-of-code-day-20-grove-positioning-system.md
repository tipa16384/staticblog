---
date: '2022-12-20T23:06:05-05:00'
draft: false
title: "Advent of Code Day 20 -- Grove Positioning System"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/12/20/advent-of-code-day-20-grove-positioning-system/"
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
summary: "As someone remarked today on Reddit, the entire plan hinged upon you remembering a ten digit prime number you randomly overheard twenty days ago."
description: "As someone remarked today on Reddit, the entire plan hinged upon you remembering a ten digit prime number you randomly overheard twenty days ago."
tags:
  - "Advent of Code"
  - "Elf"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-20-22.51.19-A-woman-wearing-a-Christmas-hat-looking-up-at-a-starry-sky-above-a-jungle-at-night.-Her-face-is-lit-by-the-glow-coming-from-her-handheld-device.-By-Ha.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-20-22.51.19-A-woman-wearing-a-Christmas-hat-looking-up-at-a-starry-sky-above-a-jungle-at-night.-Her-face-is-lit-by-the-glow-coming-from-her-handheld-device.-By-Ha.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

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
