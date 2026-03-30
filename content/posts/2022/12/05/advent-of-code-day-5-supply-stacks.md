---
date: '2022-12-05T22:57:46-05:00'
draft: false
title: "Advent of Code Day 5 -- Supply Stacks"
author: "Tipa"
summary: "The promised difficulty boost for Day 5 failed to materialize, instead being largely a puzzle about reading formatted input."
categories:
  - "Advent of Code"
  - "Game Development"
tags:
  - "Java"
  - "Lua"
  - "Pico-8"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-05-22.32.41-Several-Christmas-elves-unloading-crates-from-an-old-riverboat-painted-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-05-22.32.41-Several-Christmas-elves-unloading-crates-from-an-old-riverboat-painted-by-Bob-Eggleton-detailed-and-intricate.png"
---
The promised difficulty boost for Day 5 failed to materialize, instead being largely a puzzle about reading formatted input.
<!--more-->

[Today's puzzle](https://adventofcode.com/2022/day/5) had our star-seeking elves unloading Yet More Supplies from their old steamship. For elves with a hard deadline of Christmas Eve staring them in the face, they sure are taking their sweet time getting ready to head out to the star groves.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/12/image-4.png" title="What could it be" classes="center" >}}

Topaz (who runs the contest) likes to put hints into the picture that is slowly drawn as the challenges open about what's going on, and here it looks like we are definitely going to end up in a Mosquito Coast/African Queen scenario. So drag out your Joseph Conrad, because things are gonna get sweaty.

But, not yet. We're still dealing with the fatally disorganized pointy-ear set, and they need to get those crates unloaded and you need to let them know what the top of those crate stacks are gonna be so they can get the elve-edores ready to shift supplies.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/12/image-5.png" classes="fig-20" >}}

The puzzle input is actually a drawing of how the crates are currently stacked on the dock. In the example given, there are three stacks with 1-3 crates already placed. The rather confused and quite possibly drunk elf with the crane is shifting the crates, Tower of Hanoi-like, from one stack to another.

Your job is to translate that ASCII drawing into some sort of data structure that you can then manipulate according to the instructions.

The fast coders just noped out of there. They looked at their input and just hardcoded the starting positions in their code -- just skipped over the parsing entirely and just did the pretty trivial stack shuffling.

Me, I'm not a fast coder, and so I parsed it both with my Python and Java solutions.

**Python 3.11**

This is wordier than it needs to be, but bytes are free. I just use a laboriously tedious method to parse the stack drawing, and then regular expressions for the instructions. Someone I follow on Mastodon used the stat analysis package NumPy to rotate the drawing 90 degrees and just read the stack contents as strings. Nice.

`import re

def crate_me(input_str: str, is9001: bool) -> str:
    crates = [[] for i in range(9)]

    for i in range(7, -1, -1):
        for j in range(1, 36, 4):
            crate_num = (j-1) // 4
            box = input_str[i][j]
            if box != " ":
                crates[crate_num].append(box)

    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

    # for each line from 10 to the end
    for line in input_str[10:]:
        # match the pattern
        match = pattern.match(line)
        # get the number, from, and to
        num = int(match.group(1))
        frm = int(match.group(2)) - 1
        to = int(match.group(3)) - 1

        if not is9001:
            # move the number from the from crate to the to crate
            for i in range(num):
                crates[to].append(crates[frm].pop())
        else:
            tomove = crates[frm][-num:]
            crates[frm] = crates[frm][:-num]
            crates[to] = crates[to] + tomove
    
    return "".join(crates[i][-1] for i in range(9))

with open("puzzle5.txt", "r") as f:
    input_str = f.read().splitlines()

# Part 1 answer is a string of the last element in each crate
print ("Part 1:", crate_me(input_str, False))
print ("Part 2:", crate_me(input_str, True))

`

**Java 14**

The Java solution is much the same. I used string manipulation instead of the stacks I used in Python. Note that my solution, either of them, can't be used to solve the sample input, as I didn't write code to see how many stacks there are. I should have just gone for broke and hardcoded the strings, but I just didn't think of it. I guess that's why I don't get on the leaderboard.

`package com.chasingdings.y2022;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Puzzle5 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle5.txt";

    @Override
    public Object solve1(String content) {
        return process(content, false);
    }

    @Override
    public Object solve2(String content) {
        return process(content, true);
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 5 - Supply Stacks";
    }

    private void fillStack(String line, List crates) {
        IntStream.range(0, 9).forEach(i -> {
            Character c = line.charAt(i * 4 + 1);
            if (c != ' ') {
                crates.set(i, crates.get(i) + c);
            }
        });
    }

    private List readCrates(List inputData) {
        var crates = Arrays.asList("", "", "", "", "", "", "", "", "");

        IntStream.range(0, 8)
                .mapToObj(i -> inputData.get(7 - i))
                .forEach(line -> fillStack(line, crates));

        return crates;
    }

    private void moveCrates(String line, List crates, boolean is9001) {
        var tokens = line.split("\\s+");
        var num = Integer.parseInt(tokens[1]);
        var from = Integer.parseInt(tokens[3]) - 1;
        var to = Integer.parseInt(tokens[5]) - 1;

        var toMove = crates.get(from).substring(crates.get(from).length() - num);
        crates.set(from, crates.get(from).substring(0, crates.get(from).length() - num));
        
        // if not is9001, reverse toMove
        if (!is9001) {
            toMove = new StringBuilder(toMove).reverse().toString();
        }
        
        crates.set(to, crates.get(to) + toMove);
    }

    private String process(String content, boolean is9001) {
        var inputData = getInputDataByLine(content);
        var crates = readCrates(inputData);

        // inputData = sublist of inputData from 10 to end
        inputData.subList(10, inputData.size())
                .forEach(line -> moveCrates(line, crates, is9001));

        // answer is the concatenation of the last character of all the crates
        return crates.stream()
                .map(s -> s.substring(s.length() - 1))
                .collect(Collectors.joining());
    }
}
`

**The Game -- Crates**

I'm having a lot of fun writing these nightly games, but I doubt anyone actually plays them and they do take several hours each to design, code, and do the art and sound. I'm pretty sure I could code a game of some sort in a game jam in PICO-8. I don't know if it would be any good, but I'm sure I could.

So that said, I am probably going to be easing back on writing these games unless I get super inspired. I might just starting working on my 7DRL entry. Yes, yes, I know the coding should be done in those seven days, but they allow you to do prep work, like art and sound and stuff. In fact they will allow anything if you tell what your starting base was and you feel that you are working on the spirit of the competition. So my idea is, like last time, to try to make a framework that a game can fit within.

This game, use X to drop a crate and X to pick up another. The lights and music will let you know in which order to drop them. Play continues until you mess up.
