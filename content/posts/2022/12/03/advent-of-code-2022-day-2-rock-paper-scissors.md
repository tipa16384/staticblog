---
date: '2022-12-03T00:45:56-05:00'
draft: false
title: "Advent of Code 2022 Day 2 -- Rock Paper Scissors"
author: "Tipa"
disqusIdentifier: "2022/12/03/advent-of-code-2022-day-2-rock-paper-scissors"
summary: "So I made it to day 2 of Advent of Code! Not entirely awake. I stayed up past midnight to solve it. I messed up..."
categories:
  - "Advent of Code"
  - "OpenAI"
tags:
  - "2022"
  - "Advent"
  - "Java"
  - "Python"
  - "Rock Paper Scissors"
relatedPosts:
  - url: "/2022/12/10/advent-of-code-day-10-cathode-ray-tube/"
    title: "Advent of Code Day 10 -- Cathode-Ray Tube"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-10-19.36.37-A-woman-in-ragged-clothes-wearing-a-Christmas-hat-playing-a-video-game-in-the-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/03/advent-of-code-day-3-rucksack-reorganization/"
    title: "Advent of Code Day 3 -- Rucksack Reorganization"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/aoc2022.3.jpg"
  - url: "/2022/12/01/advent-of-code-2022-day-1-calorie-counting/"
    title: "Advent of Code 2022: Day 1 -- Calorie Counting"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/1-A_thousand_Tolkien_elves_with_pointy_ears_wearing_backpacks_full_of_snacks_trudging_through_a_tropic_Seed-4368197_Steps-100_Guidance-7.5.jpg"
  - url: "/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/"
    title: "Advent of Code Day 11 -- Monkey in the Middle"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-11-16.50.33-A-woman-wearing-a-Christmas-hat-staring-at-a-monkey-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/Two_elves_playing_rock_paper_scissors_in_an_abandoned_jungle_village__by_Bob_Eggleton__Detailed_and__Seed-6967716_Steps-175_Guidance-7.5.jpeg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/Two_elves_playing_rock_paper_scissors_in_an_abandoned_jungle_village__by_Bob_Eggleton__Detailed_and__Seed-6967716_Steps-175_Guidance-7.5.jpeg"
---
So I made it to day 2 of Advent of Code! Not entirely awake. I stayed up past midnight to solve it. I messed up...
<!--more-->

So I made it to day 2 of Advent of Code! Not entirely *awake*. I stayed up past midnight to solve it. I messed up my first approach, so I went to a more brute force approach that worked. I got my solution logged in in about twelve minutes or so? But I was still 8,000 positions from the leaderboard, so... yeah, I don't really think I need to be staying up late to get the puzzle the moment it drops.

However, I'm *still up* now and about to solve Day 3, because it took so long to write today's game. It's weird -- at this moment in time, I have solved Day 3, but I still have to write Day 2 up. Here goes. It was basically [a puzzle about cheating in Rock, Paper, Scissors](https://adventofcode.com/2022/day/2). We are so used to Rock, Paper and Scissors being in that order that this puzzle really tripped up people in those cultures where they are in different order -- which is to say, a throw always beats the previous throw in the list, and loses to the throw before the previous throw in the list. Knowing that relationship gives the solver a clue to use the *modulo* operator to solve this puzzle.

I didn't do that.

**Python 3.11**

`part1 = { 'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6 }
part2 = { 'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7 }

with open("puzzle2.dat") as f:
    data = f.read().splitlines()

print ("Part 1: ", sum([part1[play] for play in data]))
print ("Part 2: ", sum([part2[play] for play in data]))
`

I was sitting around trying to parse the input and calculate everything when I realized that there are only nine possible ends to a match of Rock Paper Scissors. I could just encode the scores directly and just sum them up. Same deal, different values for part 2. And that was that.

**Java 14**

`public class Puzzle2 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle2.dat";

    private final static Map part1 = new HashMap<>();
    private final static Map part2 = new HashMap<>();

    static {
        /* same maps as in the Python solution, omitted here for space */
    }

    @Override
    public Object solve1(String content) {
        return solveWithMap(content, part1);
    }
    
    @Override
    public Object solve2(String content) {
        return solveWithMap(content, part2);
    }

    private int solveWithMap(String content, Map partMap) {
        return getInputData(content).stream().mapToInt(x -> partMap.get(x)).sum();
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 2 - Rock Paper Scissors";
    }

    private List getInputData(String content) {
        return Arrays.asList(content.split(EOL));
    }
}
`

*solveWithMap* is where all the magic happens here. It uses streams to do what Python does with list comprehensions, but it gives the same result.

The actually important stuff is everything else. You can't see it here, but I have abstracted out all the bits of the puzzles that read from the file, print the output, do timing, handle errors and so on to a parent class. I also implemented a Factory to instantiate the puzzles to be run, an *enum* that holds the codes that are given on the command line to run specific puzzles. I also was a little proactive and converted this beast to a Maven project so that I can easily bring in libraries to do some of the work (for instance, caching) that I don't want to do myself.

It's a real Java program now. SOLID principles, design patterns, all there.

**Rock Paper Scissors -- the GAME!!!**

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/12/image.png" classes="fig-20" >}}

I had a lot of ideas for this game. I wanted it to be like Dance Dance Revolution or Guitar Hero where you had to either win, draw or lose the next throw depending on what mode the game was in at the time. But by the time I finished drawing the throws, I was running out of time to implement anything, so I just implemented a standard game of Rock Paper Scissors. Scoring is as it is in the actual puzzle; you can refer to that if it's important to know why the score does what it does.

I wrote a short bit of music to play, as well as sounds for stuff you do.

**Arrow Keys** -- select throw
**Z** -- start a match
**X** -- restart the game

That's it. I hope you enjoy it. I copied the font from one I found online. I used Dall-E to help me draw the hands. It really is a good tool. I have zero art talent, but with AI, I don't need to have any. I did write the music myself for what it's worth.
