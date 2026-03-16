---
date: '2022-12-06T21:49:59-05:00'
draft: false
title: "Advent of Code Day 6 -- Tuning Trouble"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/12/06/advent-of-code-day-6-tuning-trouble/"
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
summary: "What is probably the first puzzle in the theme for the rest of Advent of Code started today... with the easiest puzzle so far."
description: "What is probably the first puzzle in the theme for the rest of Advent of Code started today... with the easiest puzzle so far."
tags:
  - "Advent of Code"
  - "Advent"
  - "Java"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-06-21.33.38-Christmas-elves-trying-to-fix-a-broken-radio-in-the-style-of-Bob-Eggleton-detailed-and-intricate.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-06-21.33.38-Christmas-elves-trying-to-fix-a-broken-radio-in-the-style-of-Bob-Eggleton-detailed-and-intricate.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

It's been a rough day for me in real life. I have a potentially terrible family issue, and the plumber says it's going to cost $10,000 to fix our pipe out to the city sewer. Which is too bad, because in a better day, I'd have just the game to write for [today's puzzle challenge](https://adventofcode.com/2022/day/6).

**Python 3.11**

The idea was to find the first sequence of four unique letters in a string. The second idea was to find the first sequence of fourteen unique letters in a line of text.

`with open("puzzle6.txt") as f:
    puzzle = f.read()

def seek_unique(puzzle, packet_size=4):
    for i in range(len(puzzle)):
        if len(set(puzzle[i:i+packet_size])) == packet_size:
            return i+packet_size

print ("Part 1:", seek_unique(puzzle))
print ("Part 2:", seek_unique(puzzle, 14))
`

This wouldn't have taken any time at all at midnight, but I'd firmly decided that I wasn't staying up until midnight for AoC anymore this year. I expected this puzzle to be harder. The code makes a set (which can only contain unique elements) out of every four letters, and the first one where the set is the same size as the packet size is the answer.

**Java 14**

My Java solution even sparked some discussion, mostly over someone saying it didn't work for the test data (then later admitting it did). But another commenter said I could make this faster by using parallel streams -- trying to solve for all possible patterns at once, and retaining the one that was first.

`
    private int process(String content, int packetSize) {
        var testLine = content.split(EOL)[0];
        logger.info("test line is {} and packet size is {}", testLine, packetSize);

        return IntStream.range(packetSize, content.length())
                .mapToObj(i -> content.substring(i - packetSize, i))
                .filter(s -> s.chars().distinct().count() == packetSize)
                .mapToInt(content::indexOf)
                .findFirst()
                .getAsInt() + packetSize;
    }
`

This code doesn't show that, but I did try it, and it was faster. I also added Log4j2 logging instead of System.out.println, which is bad to use. Some would say that security vulnerabilities would call Log4j2 bad to use as well, but they fixed those, and in any event, this isn't a server running on the internet. It's a program that runs, prints output, and quits.

**The Game**

The game would have been an oscilloscope deal where you would have to adjust the input to match a waveform. It still sounds like a cool thing to do, but I doubt I could get it done in the couple hours I would have. Plus, it's been a bad day and things could get worse, and so right now I am focusing on that.
