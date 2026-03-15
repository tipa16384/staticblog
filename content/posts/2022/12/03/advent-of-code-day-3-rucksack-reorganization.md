---
date: '2022-12-03T20:59:41-05:00'
draft: false
title: "Advent of Code Day 3 -- Rucksack Reorganization"
categories:
  - "Advent of Code"
  - "OpenAI"
tags:
  - "Advent"
  - "Java"
  - "Lua"
  - "Pico-8"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/aoc2022.3.jpg"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/aoc2022.3.jpg"
---

I did this puzzle last night while writing the post about Day 2. This time I'm not in quite so much of a rush. Weekends.

The puzzle description is best read [on the AoC site](https://adventofcode.com/2022/day/3) -- they're always fun to read :-)

Advent of Code always starts out slowly, getting people used to how things go before they start pouring on the hard stuff. You can see some concepts come up that will undoubtedly become key in later puzzles. Yesterday was modulo arithmetic. Today was sets. Naturally, people did it their own ways, but typically the fast solvers will immediately focus in on the concept being introduced and doing their thing in seconds.

I really don't know how these people are delivering their full solutions while I am still reading the story. They probably don't read the story. Story is the best part.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/12/An_elf_filling_a_backpack_with_gems_at_a_camp_in_a_lush_jungle__Detailed_and_Intricate__by_Bob_Eggle_Seed-679908_Steps-100_Guidance-7.5-1024x1024.jpeg" class="align-left" >}}

You might notice a difference in the header image. I've been using Stable Diffusion for the past couple of days because it is free, but goddamn does it take a million tries to find something usable. And even then... it's pretty bad if you look close. Tonight I got frustrated with Stable Diffusion and just used the exact same prompt on Dall-E and... just what I wanted.

The picture on the left is what Stable Diffusion gave me. Face and hands a mess as usual, the costume was all weird and what is with that hat sticking out of his neck? I've got twenty that look worse. When it works, it works, but... first try with Dall-E.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/12/image-1-1024x252.png" class="align-center" >}}

In fact, all four options were mostly decent. A little extra leg issue on picture 3, but otherwise fine.

Okay, on to the solutions.

**Python 3.11**

`def priority(x):
    return ord(x) - ord('a') + 1 if x >= 'a' and x 

The puzzle assigned a point value to the lower and upper case letters they called "priority". There's actually a Python library which does this for free that I didn't know about.

Part 1 was going through a series of strings and finding the common letter between the two halves of the string, calculating its priority, and summing these.

Part 2 was taking strings in groups of three and finding the common letter in all three of those, calculating the priority, and taking the sum. That's what you see above.

The **zip** part is fun. That bit makes a list of tuples with **data[0], data[1], data[2]** in the first tuple, **data[3], data[4], data[5]** in the second tuple and so on, with the **iter(data)** feeding new lines as necessary, and **zip** bringing everything back together.

Someone mentioned on Reddit that I could have used **a & b & c** to intersect the sets in Part 2. I'll remember that for later.

I made some mistakes, but I don't think it's worth it to turn back the clock and try to appear cleverer than I am.

**Java 14**

`package com.chasingdings.y2022;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Puzzle3 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle3.dat";

    @Override
    public Object solve1(String content) {
        var rucksacks = getInputDataByLine(content);

        return rucksacks.stream().mapToInt(ruck -> {
            var len = ruck.length()/2;
            var left = getSet(ruck.substring(0, len));
        
            left.retainAll(getSet(ruck.substring(len)));
            return left.iterator().next();
        }).sum();
    }
    
    @Override
    public Object solve2(String content) {
        var elfGroups = groupElves(getInputDataByLine(content));

        return elfGroups.stream().mapToInt(eg -> {
            var elf = getSet(eg.get(0));
            elf.retainAll(getSet(eg.get(1)));
            elf.retainAll(getSet(eg.get(2)));
            return elf.iterator().next();
        }).sum();
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 3 - Rusksack Reorganization";
    }

    /**
     * Take a string, map each character to its priority, and return them as a Set.
     */
    private Set getSet(String s) {
        return s.chars().mapToObj(this::priority).collect(Collectors.toSet());
    }

    /**
     * Take a character and if it is a lower case character, return 1..26. 
     * If it is an upper case character, return 27..52.
     */
    private int priority(int c) {
        return c >= 'a' ? c - 'a' + 1 : c - 'A' + 27;
    }

    private List> groupElves(List elves) {
        // select elves in threes
        var groups = elves.stream().collect(Collectors.groupingBy(s -> elves.indexOf(s) / 3));
        return groups.values().stream().collect(Collectors.toList());
    }
}
`

Java is always a lot wordier than Python. I'm sure more than half of solvers just use Python -- including me. I wouldn't even consider doing my leaderboard solution in Java.

Java doesn't have the **zip** functionality, so I had to do it manually with **Collectors.groupingBy**. For the set intersections, I wanted to use Apache's **SetUtils.intersection**, but before I added it to my Maven build, I found that Java had a slightly less useful but still capable function built-in -- **Set.retainAll**. I always prefer to use native language features over third party libraries, so I used it.

As before, all the bolts and gears of the solution are abstracted into other classes, leaving just the bits specific to this puzzle here. This is one of the things that is possible in Python, but integral to Java.

**Today's game -- Gems**

Still managing to make a game a day. 22 to go after this one.

Since the puzzle today was about find a common letter in two strings, the game is about finding the only two gems in each screen that are identical. Select those with the arrow keys, hit X to select one and then the other, and then you get to do it again.

Time limit is 30 seconds, +7 seconds for every correct match. On Game Over, the game pauses to let you find the match you were missing.

I reused most of the music and sounds. Why start from scratch? It took a long time this morning to draw 64 different gems. Longer to get the frickin thing to generate the screen correctly. Turns out Pico-8's Lua uses 1-based indices. Pagans.
