---
date: '2022-12-01T23:39:10-05:00'
draft: false
title: "Advent of Code 2022: Day 1 -- Calorie Counting"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/12/01/advent-of-code-2022-day-1-calorie-counting/"
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
summary: ""
description: "Desc Text."
tags:
  - "Advent of Code"
  - "Game Development"
  - "2022"
  - "AoC"
  - "Elf"
  - "Java"
  - "Lua"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/1-A_thousand_Tolkien_elves_with_pointy_ears_wearing_backpacks_full_of_snacks_trudging_through_a_tropic_Seed-4368197_Steps-100_Guidance-7.5.jpg"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/12/1-A_thousand_Tolkien_elves_with_pointy_ears_wearing_backpacks_full_of_snacks_trudging_through_a_tropic_Seed-4368197_Steps-100_Guidance-7.5.jpg"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

I am committing myself this year to solving every puzzle in the Advent of Code, an annual coding competition taking place over the Advent season each year.

Each day brings a new puzzle, in two parts. They start out pretty easy, and top programmers (not me) solve them in seconds. By the end of the challenge, top programmers can take even half an hour to solve a puzzle. Me, I'll take hours.

But that's fine.

Last year was an education. I *did* solve all 25 puzzles, two with help. And the last couple of puzzles, I was inspired to write a game engine that I later used as the basis for my 7 Day Roguelike game jam entry. That... that didn't work out so well, but I had fun.

So this year, as well as trying to solve each puzzle the day it drops, but I also want to write a small game with the "fantasy" retro console [PICO-8](https://www.lexaloffle.com/pico-8.php) that is inspired by the puzzle, if not a direct visualization of it.

We'll get to that. First: [Day 1](https://adventofcode.com/2022/day/1). Read the puzzle description at the link if you like, I'm not going to go over it here.

The input is a huge list of integers, separated by the occasional blank line. Part 1 of the puzzle is to find the sum of the largest group; part 2 is to find the sum of the largest three groups. My solution was to split the input file at blank lines, sum the groups into an array, sort the array, and then use the first element as the answer to part 1, and the sum of the first three elements as the answer to part 2.

**Python 3.11**

You can find [the full source here](https://github.com/tipa16384/adventofcode/blob/main/2022/puzzle1.py). This could be better -- and I did make it better later, but I discarded those changes. This is what I wrote at midnight and it's okay to be honest about that. "data" should have been sorted when initialized, and Python can take things off the end of an array as easily as the beginning, so there was no need to sort descending.

`with open("puzzle1.dat", "r") as f:
    data = [sum(int(x) for x in line.split()) for line in f.read().split("\n\n")]

print ("Part 1:", max(data))
print ("Part 2:", sum(sorted(data, reverse=True)[:3]))`

**Java 14**

Java is the language I use at work, so I thought I should at least pretend that this has some relevance to my actual job :-) Since I did this during the day, it takes into account the idea about taking both parts from a sorted list. Java doesn't do arbitrary list slicing as easily as Python, so I still have the reverse sort. The code (with the comments) [you can find here](https://github.com/tipa16384/adventofcode/blob/main/2022/com/chasingdings/adventofcode/y2022/Puzzle1.java).

`public class Puzzle1 {
    private static final String DATA_FILE = "2022\\puzzle1.dat";
    private static final String EOL = "\\r\\n";

    private List readData() throws IOException {
        var content = new String(Files.readAllBytes(Paths.get(DATA_FILE)));

        return Arrays.stream(content.split(EOL + EOL))
                .map(elf -> Arrays.stream(elf.split(EOL)).mapToInt(Integer::parseInt).sum())
                .sorted(Collections.reverseOrder())
                .collect(Collectors.toList());
    }

    private void solve() throws IOException {
        var dataList = readData();
        System.out.println(String.format("Part 1: %d", dataList.get(0)));
        var total = IntStream.range(0, 3).map(i -> dataList.get(i)).sum();
        System.out.println(String.format("Part 2: %d", total));
    }

    public static void main(String[] args) {
        var puzzle = new Puzzle1();
        try {
            puzzle.solve();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}`

**So I made a game**

My boyfriend said he wouldn't buy this game. WELL. It took all of three hours to write, and ... it's kind of based on the day's puzzle. You're an elf, your hunger is ticking up, the music is making you tense, and every time you snack on a star, another tree grows.

This is not a finished game in any sense. There should be an attract screen with the rules, it needs way better art, blah blah blah. I think it's a little bit fun. But in a month I probably won't think so. The idea here is to get familiarity enough with at least SOME game engine -- that I can publish publicly so that people can play -- so that when a game jam comes up, I can take part without having to start from zero.

Hold down the arrow keys to move. Move onto a star to ease your hunger a little. If a tree is blocking you, power up with Z. X to restart. That's pretty much it. [You can find the source here](https://github.com/tipa16384/pico8/blob/master/carts/p2022a.p8). It isn't pretty.

I did have fun making the sounds :-)
