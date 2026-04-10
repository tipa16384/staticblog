---
date: '2023-12-05T22:37:57-05:00'
draft: false
title: "Advent of Code Day 5 -- If You Give A Seed A Fertilizer"
author: "Tipa"
disqusIdentifier: "2023/12/05/advent-of-code-day-5-if-you-give-a-seed-a-fertilizer"
summary: "This can take no time at all or an eternity."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "AoC 2023"
  - "Python"
relatedPosts:
  - url: "/2023/12/06/advent-of-code-day-6-wait-for-it/"
    title: "Advent of Code Day 6 -- Wait For It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-06-20.55.25-A-whimsical-and-vibrant-scene-depicting-an-island-with-a-small-ferry-dock-and-numerous-toy-boats-ready-for-a-race.-The-island-is-surrounded-by-water-a.png"
  - url: "/2023/12/22/advent-of-code-day-22-sand-slabs/"
    title: "Advent of Code Day 22 -- Sand Slabs"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/jenga.png"
  - url: "/2023/12/21/advent-of-code-day-21-step-counter/"
    title: "Advent of Code Day 21 -- Step Counter"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-21-20.59.37-Illustrate-a-whimsical-and-fantastical-scene-from-the-Advent-of-Code-puzzle-Step-Counter.-The-image-should-depict-an-Elf-in-a-vast-infinite-garden-.png"
  - url: "/2023/12/20/advent-of-code-day-20-pulse-propogation/"
    title: "Advent of Code Day 20 -- Pulse Propagation"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-20-16.57.44-Create-an-illustration-inspired-by-the-aesthetic-of-a-retro-sci-fi-movie-similar-to-Tron-avoiding-direct-references-or-copyrighted-elements.-Visualiz.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_tending_a_wide_variety_of_bizarre_looki_61e5db45-06f1-482c-9242-78720532164f.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_tending_a_wide_variety_of_bizarre_looki_61e5db45-06f1-482c-9242-78720532164f.png"
---
This can take no time at all or an eternity.
<!--more-->

Every year, there is a problem where the first part is easy and trivial, but if you tried the same solution on the second part, stars would burn out before it finished. That's today's puzzle.

We left the scratch card elf behind and sailed off to a farmer elf, who admits he turned off the water because the sand he used to filter it stopped being delivered, and I should really try to find out why. *But before I go*, [could I help him find the best spot to plant some seeds](https://adventofcode.com/2023/day/5)?

Sure. why the heck not?

You're given a list of seed numbers, and a list of mappings to apply -- seed to soil, soil to fertilizer, fertilizer to etc and so on until you come to location. Run through that list and return the lowest location number. Easy.

`def part1(data, seeds, mappers):
    print ("Part 1:", min([translate(mappers, 'seed', 'location', seed) for seed in seeds]))

# translate takes a source, dest, and value and returns the translated value
def translate(mappers, source, dest, value):
    if source == dest:
        return value
    mapping = mappers[source]
    for dest_start, source_start, length in mapping[1]:
        if source_start 

Part 2 on the other hand... well, it turns out that those seed numbers weren't seed numbers, they were *ranges* of seed numbers. And we're talking *millions* of seeds in those ranges. A brute force method could take hours. Here's what the seed numbers looked like in my puzzle:

`seeds: 2880930400 17599561 549922357 200746426 1378552684 43534336 155057073 56546377 824205101 378503603 1678376802 130912435 2685513694 137778160 2492361384 188575752 3139914842 1092214826 2989476473 58874625`

Each pair of numbers is a seed number and a *length*. The second range has over 200 million "seeds" in it, and it's far from the largest range.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/1-IMG_4084.jpg" title="How ranges intersect and overlap" classes="center" >}}

The trick was to pass down ranges instead of individual values. One range doesn't usually do the entire job. I had to write a diagram of how ranges intersect. They might not -- that's one case. It might overlap from the left, or the right, or one range may encompass the entirety of the other range. It turned into five different use cases.

`# expand takes a source, dest, and a range and returns a list of ranges
def expand(mappers, source, dest, seed_range) -> list:
    if source == dest:
        return [seed_range]
    mapping = mappers[source]
    expanded = []
    for dest_start, source_start, length in mapping[1]:
        if seed_range[0]  source_start and seed_range[0] + seed_range[1] = source_start and seed_range[0]  source_start + length:
            left_range = (dest_start + seed_range[0] - source_start, source_start + length - seed_range[0])
            right_range = (source_start + length, seed_range[0] + seed_range[1] - source_start - length)
            expanded = expanded + expand(mappers, mapping[0], dest, left_range) + expand(mappers, source, dest, right_range)
            break
        elif seed_range[0] >= source_start and seed_range[0] + seed_range[1]  source_start + length:
            left_range = (seed_range[0], source_start - seed_range[0])
            right_range = (source_start + length, seed_range[0] + seed_range[1] - source_start - length)
            middle_range = (dest_start, length)
            expanded = expanded + expand(mappers, source, dest, right_range) + expand(mappers, mapping[0], dest, middle_range) + expand(mappers, source, dest, left_range)
            break

    if not expanded:
        expanded = expanded + expand(mappers, mapping[0], dest, seed_range)

    return expanded`

This code breaks the seed range and the map range into one to three subranges and then recursively calls itself to process those until it hits the location map and ends. It's crude, but it works.

The remainder of Part 2 just sets up the call to **expand** and then finds the lowest starting range for the answer.

`def part2(data, seeds, mappers):
    results = [expand(mappers, 'seed', 'location', seed_range) for seed_range in zip(seeds[0::2], seeds[1::2])]
    
    # flatten the list of lists into a list
    results = [item for sublist in results for item in sublist]

    # answer is the minimum value of the first element of each tuple
    print ("Part 2:", min(x[0] for x in results))`

Yeah, I should probably have used Haskell, but I was having trouble with the ranges and I just wanted to use my comfort language. Meine Muttersprache. I had Part 1 done before work and figured out the answer to Part 2 was ranges during work, but knowing the approach and implementing it were two separate things, for me at least.
