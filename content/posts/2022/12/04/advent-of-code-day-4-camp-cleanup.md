---
date: '2022-12-04T19:39:29-05:00'
draft: false
title: "Advent of Code Day 4 -- Camp Cleanup"
summary: "As well as my Day 4 solutions in Python and Java, I talk about the AI solving controversy in Advent of Code, and teach the chat bot to speak a language I just now invented."
categories:
  - "Advent of Code"
  - "OpenAI"
  - "Programming Language"
tags:
  - "AI"
  - "Gpt-3"
  - "Java"
  - "Lua"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-04-18.27.11-Several-Christmas-elves-doing-chores-around-a-campsite-in-the-jungle-painted-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-04-18.27.11-Several-Christmas-elves-doing-chores-around-a-campsite-in-the-jungle-painted-by-Bob-Eggleton-detailed-and-intricate.png"
---

There's a[ bit of a kerfuffle](https://old.reddit.com/r/adventofcode/comments/zbpq5g/gpt_openai_solutions_should_be_removed_from_the/) on the Advent of Code subreddit over people using GPT-3's new text-davinci-003 to solve puzzles and submit them automatically. Someone has been submitting correct answers in seconds in the past few days.

It operates essentially just like my TerraChat. My chatbot takes user input, combines it with background information and a certain amount of conversation context, and calls GPT-3 with it and sends back the result.

The AI here adds a first step -- actually going to the Advent of Code website and reading the puzzle and the puzzle input before also giving those to the AI -- and if it seems to work with the sample, it then submits its answer, moves on to Part 2, and does the same again. (I'm not totally sure it verifies the solution with the sample data; I haven't seen the bot myself).

So, I was wondering how people solve this so quickly, while I am still reading the problem. It's because I don't work at machine time.

I was curious how this would work with older problems. I hadn't done any of 2017's problems, so I just pasted in the first couple days and asked for it to write a solution. Here, unmodified, is the output for 2017's [Day 1, Part 1](https://adventofcode.com/2017/day/1):

`# Initialize the sum to 0
sum = 0

# Iterate through the digits in the input string
for i in range(len(input_str)):
    # Get the current digit and the next digit
    # Be careful to handle the case where the next digit is the first digit
    cur_digit = int(input_str[i])
    next_digit = int(input_str[(i + 1) % len(input_str)])

    # If the current digit and the next digit are equal, add the current digit to the sum
    if cur_digit == next_digit:
        sum += cur_digit
`

It absolutely works. I tried this for part 2, and it worked. Same with Day 2. Day 3, it couldn't do at all -- and everyone expects that the AI won't be able to continue this year much longer. I could have written this more cleanly, but there's not really any point.

It gets *better*. Here's someone who [defined a new computer language](https://6502.is-a.dev/posts/aoc-2022/), but he didn't have any way to run it. So he described the language to the chat bot, then had it write the puzzle solution in that language (which it had never seen before), and then run that program in that invented language and output the answer.

Just for fun, I created a new human language, taught it to the chat bot, and tried to have a conversation with her in it.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/12/image-2.png" title="The phrase was \"I am riding my horse to work\", so it was pretty close. Especially for a language I made up on the spot. It also speaks the language, but as it points out, with only ten or so words defined, it's hard to really be certain what was meant. ('bik' is leg, 'hok' is tall, so 'hokbikbikbikbik' is a tall four legged animal)." >}}

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/12/image-3.png" >}}

I should point out that the past tense of "nahg" is "nahgbahg" in my language. 

Wow. So.... so wow. Anyway, onto the solutions.

**Python 3.11**

The "correct" answer was probably, as it was yesterday, to use sets. I didn't. The problem was finding completely overlapped and partially overlapped ranges -- Part 1 and Part 2. My entry didn't use the lambdas, but I did clean it up before I posted it on Reddit.

`def overlap(s, f):
    a, b = s.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    # check if the ranges overlap
    return f(a1 

**Java 14**

I took that lambda idea into my Java solution.

`package com.chasingdings.y2022;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Puzzle4 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle4.dat";

    @Override
    public Object solve1(String content) {
        Boolinator andMe = (a, b) -> a && b;
        return process(content, andMe);
    }

    @Override
    public Object solve2(String content) {
        Boolinator orMe = (a, b) -> a || b;
        return process(content, orMe);
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 4 - Camp Cleanup";
    }

    interface Boolinator {
        boolean pleaseDo(boolean a, boolean b);
    }

    private int process(String content, Boolinator boolinator) {
        var assignmentList = getInputDataByLine(content);
        return assignmentList.stream()
                .filter(task -> isOverlap(task, boolinator))
                .collect(Collectors.toList())
                .size();
    }

    private boolean isOverlap(String s, Boolinator boolinator) {
        var tokens = Arrays.stream(s.split("[,-]")).mapToInt(Integer::parseInt).toArray();
        int x1 = tokens[0];
        int x2 = tokens[1];
        int y1 = tokens[2];
        int y2 = tokens[3];
        return boolinator.pleaseDo(x1 

Lambdas exist in Java, but passing them around as first order objects like you can do in Python is a little trickier. I actually learned this trick at work. Again, I could have used sets, just didn't feel it was necessary. Looking at some other Java entries, I might have made the parsing a little cooler.

**Today's game -- Elf Defense**

Since the story behind today's puzzle was cleaning up the camp, I had a bunch of ideas. My boyfriend suggested I do a tower defense. But it took me so long to get started that I didn't have time for any of that. I got the elf moving around and then I tossed in some monsters and some potions which were treasures and the concept was grabbing the treasures before the monsters did.

Go ahead and try it, but it's not my favorite.

Going forward, I need to make a good game template that has all the score and timer and that stuff built in so I can quickly get going on the actual game. I am partway there, but I need to formalize it. We'll see what happens tomorrow. Back to the weekday so not as much time each night.
