---
date: '2022-12-10T19:54:04-05:00'
draft: false
title: "Advent of Code Day 10 -- Cathode-Ray Tube"
author: "Tipa"
summary: "Turns out the elves just really loved the Atari 2600 so much, they built their little handheld computers around them. And now it's up to us to fix one."
categories:
  - "Advent of Code"
  - "Game Development"
tags:
  - "2022"
  - "Advent"
  - "Java"
  - "Lua"
  - "Pico-8"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-10-19.36.37-A-woman-in-ragged-clothes-wearing-a-Christmas-hat-playing-a-video-game-in-the-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-10-19.36.37-A-woman-in-ragged-clothes-wearing-a-Christmas-hat-playing-a-video-game-in-the-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
---
Turns out the elves just really loved the Atari 2600 so much, they built their little handheld computers around them. And now it's up to us to fix one.
<!--more-->

This is the first puzzle that doesn't feature any elves, just the presumably human protagonist, and so I use a human for today's picture.

Part 1 of [today's puzzle](https://adventofcode.com/2022/day/10) is mostly just getting you ready to solve Part 2. You're trying to write a display driver for the handheld machine they gave you, which was destroyed when you plummeted into the river when the rope bridge broke yesterday.

As the puzzle points out, the old Atari 2600 game system used to make multiple sprites appear while using just one sprite by repositioning the sprite between every scan line. Today's Part 2 does just that -- you interpret a program that moves the sprite (basically a rectangle) every few clock cycles so that when the CRT beam hits it, it lights up the pixel at the correct spot. I have a visualization for that below.

**Python 3.11**

But first, the Python implementation.

I could have saved some space by recognizing that, with only two instructions, I don't need to build a mechanism that can handle any number of commands, but I did, anyway. I'm thinking at some point we'll need to extend this machine at some point, and I might as well prepare. Last year we had a programming thing as the very last day, which of course wasn't extended. But in 2019, a similar scheme was extended throughout all of Advent, and ended with an actual text adventure game at the end :-) I doubt that will happen again, but there's no reason to go for a *little* clarity now and then.

`def run_program(commands):
    command_list = {'noop': (1, lambda x, _: x),
                    'addx': (2, lambda x, y: x + y)}
    x, clock = 1, 1
    program_state = [(0, 0)]

    for command in commands:
        toks = command.split()
        op = toks[0]
        arg = int(toks[1]) if len(toks) == 2 else None
        x = command_list[op][1](x, arg)
        clock += command_list[op][0]
        program_state.append((clock, x))

    return program_state

def state_at(program_state, t):
    for i in range(len(program_state) - 1):
        if program_state[i][0] 

**Java 14**

Someone on Reddit said he admired the lack of encapsulation in my Java solutions. I think he was being sarcastic, as he is a high school teacher who teaches for the Advanced Placement Computer Science (APCS) exam. I guess I opened myself up for that when I asked why he was using such primitive Java in his solutions -- it turns out he was programming to a very minimum subset of Java, just that small portion taught in APCS courses.

As before, and as yesterday, it is similar to the Python solution, and uses inner classes to make up for the lack of tuples in Java.

`package com.chasingdings.y2022;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Puzzle10 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle10.txt";
    private static final int WIDTH = 40;
    private static final int HEIGHT = 6;

    private List programState;

    @Override
    public Object solve1(String content) {
        return IntStream.range(0, HEIGHT)
                .map(clock -> clock * WIDTH + 20)
                .map(clock -> stateAt(programState, clock).x * clock)
                .sum();
    }

    @Override
    public Object solve2(String content) {
        final var spritePos = IntStream.range(0, WIDTH * HEIGHT)
                .mapToObj(pixel -> stateAt(programState, pixel + 1))
                .collect(Collectors.toList());

        final var screen = IntStream.range(0, WIDTH * HEIGHT)
                .mapToObj(pixel -> spritePos.get(pixel).x - 1  screen.substring(i * WIDTH, (i + 1) * WIDTH))
                .collect(Collectors.joining("\n"));
    }

    private List runProgram(List commands) {
        List programState = new ArrayList<>();
        programState.add(new State(0, 0));

        var currentState = new State(1, 1);

        for (var command : commands) {
            var toks = command.split(" ");
            var arg = toks.length == 2 ? Integer.parseInt(toks[1]) : null;

            currentState = OP_MAP.get(toks[0]).execute(currentState, arg);
            programState.add(currentState);
        }

        return programState;
    }

    private State stateAt(List programState, int t) {
        for (int i = 0; i  OP_MAP = Map.of(
            "noop", new Instruction(1, (x, y) -> x),
            "addx", new Instruction(2, (x, y) -> x + y));

    class Instruction {
        int clockCycles;
        BiFunction func;

        public Instruction(int clockCycles, BiFunction func) {
            this.clockCycles = clockCycles;
            this.func = func;
        }

        public State execute(State state, Integer arg) {
            return new State(state.clock + clockCycles, func.apply(state.x, arg));
        }
    }

    class State {
        int clock;
        int x;

        public State(int clock, int x) {
            this.clock = clock;
            this.x = x;
        }
    }

    @Override
    public void preprocess(String content) {
        programState = runProgram(getInputDataByLine(content));
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 10 - Cathode-Ray Tube";
    }
}
`

**The Game**

Well, I didn't write a game today, *per se*, but I did write up a visualization. So if you want to see what the output of Part 2 looks like, here it is. Simply run it.
