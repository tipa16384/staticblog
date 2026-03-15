---
date: '2022-12-11T17:52:42-05:00'
draft: false
title: "Advent of Code Day 11 -- Monkey in the Middle"
summary: "I thought this was just a puzzle to see if I knew about modulo arithmetic... but then it turned into a puzzle about VERY LARGE NUMBERS! Also, why do I bother with Java?"
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Clojure"
  - "Java"
  - "Jvm"
  - "Lua"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-11-16.50.33-A-woman-wearing-a-Christmas-hat-staring-at-a-monkey-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-11-16.50.33-A-woman-wearing-a-Christmas-hat-staring-at-a-monkey-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
---

This puzzle is the first one where I had to sit and think about the puzzle solution. Well, not really about what the solution was about -- but how to get it to return the answer before the Earth falls into the Sun.

That happens a lot, in Advent of Code.

In [today's puzzle](https://adventofcode.com/2022/day/11), monkeys have stolen everything from your pack, and they're tossing your stuff between them. Part 1 has you follow their game of catch for twenty rounds, while part 2 is ten thousand -- AND, in part 1, your worry is managed, but in part 2, your worry can become nearly infinite.

And infinite numbers are bad. Very bad.

Python has arbitrary precision numbers -- you can have numbers as big as you like. It gets slow and uses a lot of memory, but it can do it. When numbers grow larger than your available memory, it may slow down slightly.

Java has a special class, BigInteger, that does more or less the same thing. But it wasn't needed for either parts. All Java needed was to use long integers to handle a specific calculation and that was all.

The upshot was that Python could solve Part 2 in about half a second, but Java could solve Part 2 in about a tenth of a second. Working within Java's constraints allowed for more speed. I know, I was shocked, too.

Python compiles its code into a byte code, similar to what Java does with its Java virtual machine. This does lead to slower, but more portable, software. It also makes this an apples-to-apples comparison. Usually, Python and Java come in at around the same time, and this is why I haven't really been talking about the executions times here. But now that we are getting to some larger numbers, it's clear that Python's flexibility comes at the cost of speed.

**Python 3.11**

There's a lot going on in this solution, but the important part is the bit with "9699690" in it. This is what keeps our numbers from getting out of control. The idea here is that all the monkeys are doing modulo arithmetic with prime numbers against your "worry" level. So if we can perform an operation that would reduce a number but still return the same answer about whether or not it could be evenly divided by the prime.

If we consider the numbers 3, 24, 192, and, I dunno 107,421 -- they are all evenly divisible by 3. Modulo 3 against all of them leaves zero for everything.

If we want to consider two numbers, say, 3 and 5. If we take 27 and modulo 3, great, the result is zero. But if we take 27 and modulo 5, we get 2, since it doesn't divide evenly into 5. But after modulo with 3, we're left with zero, which is evenly divided by 5, so the properties of the number has been changed.

If we multiply 3 and 5 to get 15, and perform the operation, we get 12 -- which is evenly divisible by 3, and has a remainder of 2 when modulo with 5. So for the purposes of this argument, 12 and 27 are identical.

In the puzzle, we have the first eight prime numbers -- 2, 3, 5, 7, 11, 13, 17, and 19. These are the tests to perform. Multiplying these all together gets us 9699690 -- and this is how we stop from having numbers go way out of control. No number can ever get above this, which is easily held within Java's "Long" type.

Someone pointed out that this works even if the numbers aren't prime, and that's true. But it was seeing that these were prime that led me to this insight, which was the key to the puzzle, and a tribute to the puzzle creator. Some people thought it was unfair for people to have to examine their puzzle input to catch this, but hey, it's Advent of Code. Sometimes you have to dig a little deeper.

`class Monkey:
    def __init__(self, monkey_do):
        monkey_stats = monkey_do.splitlines()
        self.items = eval('[' + monkey_stats[1][18:] + ']')
        self.operation = eval('lambda old: ' + monkey_stats[2][19:])
        self.test = int(monkey_stats[3][21:])
        self.iftrue = int(monkey_stats[4][29:])
        self.iffalse = int(monkey_stats[5][30:])
        self.inspect_count = 0
    
    def play(self, worry_divider):
        while self.items:
            self.inspect_count += 1
            worry = self.operation(self.items.pop(0))
            worry = worry % 9699690 if worry_divider == 1 else worry // worry_divider
            yield self.iffalse if worry % self.test else self.iftrue, worry

def play_a_game(rounds, worry_divider):
    with open(r'puzzle11.txt') as f:
        monkeys = [Monkey(monkey_do) for monkey_do in f.read().split('\n\n')]

    for _ in range(rounds):
        for monkey in monkeys:
            for catcher, worry in monkey.play(worry_divider):
                monkeys[catcher].items.append(worry)

    return (lambda x, y: x.inspect_count * y.inspect_count) \
        (*sorted(monkeys, key=lambda monkey: monkey.inspect_count)[-2:])

part1 = play_a_game(20, 3)
print("Part 1:", part1)

part2 = play_a_game(10000, 1)
print("Part 2:", part2)
`

**Java 14**

The other part about implementing this in two different languages (and three, adding Lua, when I do a PICO-8 game), is to get an idea for the strengths of certain languages. I saw with this puzzle that Java is faster with larger numbers.

Since I solve the puzzle with Python first, and then use that as the basis for my Java solution, why use Java at all?

Well, I use Java at work, and we're still on *Java 8* there, which is way, WAY behind the latest long term supported version, Java 17, or the actual bleeding edge version, Java 19. If I don't start using more recent versions of Java at some point, my skills are going to be out of date. Building familiarity with the current state of the language is important to my real life.

And as I've seen today, for certain problems, Java is faster.

But it goes deeper. Java is built on top of the Java Virtual Machine (JVM), [along with dozens of other languages](https://en.wikipedia.org/wiki/List_of_JVM_languages), and *all of them work together*. I was learning Clojure earlier in the year. It was 100% interoperable with Java. Scala, Groovy, and Kotlin are also 100% Java compatible. There's even a JVM version of Python, but it doesn't support recent versions of the language. Lots of other languages have versions that run on the JVM. Java is the gateway to the hottest languages in use today.

I built a performance and I/O module for this year's Advent of Code in order to run and test my puzzle solutions. I could have that do performance and I/O for a Clojure program without any changes. And maybe I will :-)

The code below is pretty Pythonic. As in past days, I created an inner class (MonkeyWorries) to make up for Java's lack of tuples.

`package com.chasingdings.y2022;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.stream.Collectors;

public class Puzzle11 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle11.txt";

    @Override
    public Object solve1(String content) {
        return playGame(content, 20, 3);
    }

    @Override
    public Object solve2(String content) {
        return playGame(content, 10000, 1);
    }

    @Override
    public void preprocess(String content) {
        // TODO Auto-generated method stub
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 11 - Monkey in the Middle";
    }

    private long playGame(String content, int rounds, int worryDivider) {
        var monkeys = Arrays.stream(content.split(EOL + EOL)).map(z -> new Monkey(z)).collect(Collectors.toList());

        for (int i = 0; i  (int) (a.inspectCount - b.inspectCount))
                .collect(Collectors.toList());
        return sortedMonkeys.get(sortedMonkeys.size() - 1).inspectCount
                * sortedMonkeys.get(sortedMonkeys.size() - 2).inspectCount;
    }

    class Monkey {
        private List items;
        private BiFunction operation;
        private long operand;
        private long test;
        private int iftrue;
        private int iffalse;
        private long inspectCount;

        public Monkey(String monkeyDo) {
            var monkeyStats = monkeyDo.split(EOL);
            this.items = evalList(monkeyStats[1].substring(18));
            if (monkeyStats[2].charAt(25) == 'o') {
                this.operation = (a, b) -> a * a;
                this.operand = 0;
            } else if (monkeyStats[2].charAt(23) == '*') {
                this.operation = (a, b) -> a * b;
                this.operand = Long.parseLong(monkeyStats[2].substring(25));
            } else {
                this.operand = Long.parseLong(monkeyStats[2].substring(25));
                this.operation = (a, b) -> a + b;
            }
            this.test = Integer.parseInt(monkeyStats[3].substring(21));
            this.iftrue = Integer.parseInt(monkeyStats[4].substring(29));
            this.iffalse = Integer.parseInt(monkeyStats[5].substring(30));
            this.inspectCount = 0;
        }

        public List play(int worryDivider) {
            var result = new ArrayList();
            while (!this.items.isEmpty()) {
                this.inspectCount++;
                var worry = this.operation.apply(this.items.remove(0), this.operand);
                if (worryDivider == 1) {
                    worry = worry % 9699690;
                } else {
                    worry = worry / worryDivider;
                }
                result.add(new MonkeyWorries(worry % this.test == 0 ? this.iftrue : this.iffalse, worry));
            }
            return result;
        }
    }

    class MonkeyWorries {
        private int monkeyNumber;
        private long worry;

        public MonkeyWorries(int monkeyNumber, long worry) {
            this.monkeyNumber = monkeyNumber;
            this.worry = worry;
        }
    }
}
`

**The Game**

No game today, but I do have an idea for one. I just didn't have time. This is one of the days I'd like to come back to later, though.

No Advent of Codes for Monday and Tuesday, as I have to fly to Denver.
