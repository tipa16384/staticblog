---
date: '2023-12-12T21:44:16-05:00'
draft: false
title: "Advent of Code Day 12 -- Hot Springs"
author: "Tipa"
disqusIdentifier: "2023/12/12/advent-of-code-day-12-hot-springs"
summary: "I narrowly avoided yesterday's trap only to walk right into today's."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Caching"
  - "Python"
  - "Springs"
  - "Volcano"
relatedPosts:
  - url: "/2023/12/15/advent-of-code-day-14-parabolic-reflector-dish/"
    title: "Advent of Code Day 14 -- Parabolic Reflector Dish"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-14-21.53.41-A-wall-of-mirrors-attached-to-a-cliff-face-on-the-left-side-of-the-image-with-a-dormant-volcano-in-the-background-steaming.-The-sun-is-setting-over-.png"
  - url: "/2023/12/14/advent-of-code-day-13-point-of-incidence/"
    title: "Advent of Code Day 13 -- Point of Incidence"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-13-22.52.31-An-ash-field-dotted-with-boulders-and-large-frameless-standless-mirrors-over-six-feet-tall-reflecting-each-other-the-ash-and-the-rocks.-In-the-f.png"
  - url: "/2022/12/18/advent-of-code-day-18-boiling-boulders/"
    title: "Advent of Code Day 18 -- Boiling Boulders"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-18-19.03.10-An-elephant-watching-a-flaming-meteor-crash-into-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/17/advent-of-code-day-17-pyroclastic-flow/"
    title: "Advent of Code Day 17 -- Pyroclastic Flow"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-17-22.26.37-An-elephant-wearing-a-Christmas-stocking-cap-looking-at-a-giant-statue-of-a-Tetris-game-in-a-cave-lit-with-lava-by-Bob-Eggleton-detailed-and-intrica.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-12-20.48.05-A-repairman-in-a-safety-vest-and-hardhat-looking-at-a-damaged-map-in-a-landscape-reminiscent-of-Iceland-near-a-dormant-volcano.-The-scene-includes-ste.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-12-20.48.05-A-repairman-in-a-safety-vest-and-hardhat-looking-at-a-damaged-map-in-a-landscape-reminiscent-of-Iceland-near-a-dormant-volcano.-The-scene-includes-ste.png"
---
I narrowly avoided yesterday's trap only to walk right into today's.
<!--more-->

After your cosmological stylings yesterday, you're back on the job today, looking for the famed Hot Springs where you've been told you may find help. You don't have to travel long before you come to a land filled with steaming pools of comfortably heated water. A sign nearby confirms that these are indeed the Hot Springs.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-14.png" classes="fig-20" >}}

An elf silently appears beside you. "These are the hot springs?" you ask. The elf looks at you quizzically. "No, no... these are the *onsen*. *Those* are the hot springs!" The elf points off to the other side of the onsen, where you see giant coiled metal springs in various states of disrepair. "But they aren't very hot these days. Not since the lava stopped flowing." The elf hands you a map showing which springs are working and which are not. Unfortunately, the map is damaged and all you can do for those is guess if they are working or not. Luckily, the elf that drew up the map included a handy checksum that you can use with the information you do have [to figure out which springs are working](https://adventofcode.com/2023/day/12).

In the sample input above, each row corresponds to a row of springs. A dot (".") is a working spring. A hash ("#") is a broken spring. A "?" could be either. The numbers at the end say the broken springs come in a group of one, another group of one, and a group of three. We can see the group of three ("###") broken springs. The "???" must hide two single groups -- it can only be "# #", and so there can be only one solution to that row. The next one down has four solutions, and so on. For Part 1, figure out the number of different solutions for each line, and sum them up.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-15-1024x643.png" title="Midjourney" classes="center" >}}

I brute forced Part 1 this morning, but that didn't work for Part 2. I am coming clean; I looked at other people's solutions to figure out how to make *my* solution work both parts.

The basic strategy here is to look at the next group you have to make. 

- If the list of groups is empty and there are no "#" in the string, return a 1.

- If the list of groups is *not* empty and there are only working springs in the string, return a 0.

- If the input starts with a '.', skip those working springs and recursively call this function starting at the first position after them.

- If you need *n* springs for the next group and you are at a collection of *n* '?' and/or '#' followed by a working spring, a '?', or the end of the input, then this is a matching group! Skip over this and call the function with the rest of the input and the rest of the groups.

- If the first character is a '?', pretend it's a '.' and call the function again starting with the next character.

- Return the sum of all those matches.

So we basically go through the input until we run out of groups and input, or our current position can't supply us with the group we need.

`@lru_cache
def calc_groups(s: str, groups: tuple) -> int:
    # print ('calc_groups', s, groups)
    if not s: return 0 if groups else 1
    if not groups: return 0 if '#' in s else 1
    # if first char is '.', call calc_groups with the string without the leading '.'
    m = match(r"\.+", s)
    if m: return calc_groups(s[m.span()[1]:], groups)
    m = match(getMatchLength(groups[0]), s)
    matches = 0
    # if we have a match, call calc_groups with the string after the match and the groups[1:]
    if m: matches += calc_groups(s[m.span()[1]:], groups[1:])
    # if first char is '?' call calc_groups with the string without the leading '?'
    if s[0] == '?': matches += calc_groups(s[1:], groups)
    return matches`

This code does that. We use caching to improve performance.

`@lru_cache
def getMatchLength(i):
    return compile(r"[\#\?]{%i}(\.|\?|$)" % i)`

I stole this little piece of magic from someone else. I had a regular expression that didn't do as good a job. This matches substrings as in step 4 in the list above. It also caches the return so that it only needs to be calculated once for every string length.

`def part1():
    data = read_data()
    print ("Part 1:", sum([calc_groups(d[0], d[1]) for d in data]))

def part2():
    data = read_data()
    data = [('?'.join([d[0]]*5), d[1] * 5) for d in data]
    print ("Part 2:", sum([calc_groups(d[0], d[1]) for d in data]))`

Part 1 was the simple sum. We could generate this just by setting the question marks to every combination of a working and non-working spring. That's the brute force way, and that's the way I answered Part 1.

An unwritten rule of Advent of Code goes, if Part 1 seemed a little *too* easy to brute force, Part 2 is going to teach you a lesson that will hurt. That's what happened here. See, the map was folded, and all the inputs are five times as long, with five times as many groups.

There were over two hundred trillion solutions for my Part 2. The fastest computer in the world would take some time brute forcing that, and I do not happen to own the fastest computer in the world.

The algorithm up above is meant to bail from a solution as soon as we know it's unproductive. That said, we *still* need to count up to two hundred trillion, one at a time. How? Dynamic programming.

By carefully working our way through the string to increase our chances of calculating something we have before, we only really have to do something once, so (because we have cached stuff carefully) we're not adding things one by one, but by millions and hundred millions.

While debugging, I'd been passing the original string down the function so that I could print out the proposed solutions. And I *couldn't figure out* why it was so slow. It was because of that original string. Since I'd been replacing '?' with '.' or '#', it was different all the time. I removed that parameter (and the ability to really tinker with the innards of the algo) and suddenly everything started working instantly.

We're crossing the halfway point of AoC. Based on the map on the calendar, we'll be going up to another island -- Lava Island -- tomorrow and then working our way back down, island to island, until we end up where we started.
