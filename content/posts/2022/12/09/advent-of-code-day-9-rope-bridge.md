---
date: '2022-12-09T21:35:30-05:00'
draft: false
title: "Advent of Code Day 9 -- Rope Bridge"
author: "Tipa"
summary: "The elves are crossing a bridge, but it is a really short bridge -- in fact it is the shortest bridge possible. So what did the protagonist fall into when it snapped?"
categories:
  - "Advent of Code"
  - "Programming Language"
tags:
  - "Advent"
  - "Bridges"
  - "Elf"
  - "Java"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-09-21.18.23-Christmas-Elves-walking-on-a-tattered-rope-bridge-crossing-a-river-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-09-21.18.23-Christmas-Elves-walking-on-a-tattered-rope-bridge-crossing-a-river-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
---
The elves are crossing a bridge, but it is a really short bridge -- in fact it is the shortest bridge possible. So what did the protagonist fall into when it snapped?
<!--more-->

The plot takes a turn today as the protagonist, who is, I believe, human, is separated from the jungle-delving elves when the rope bridge they are crossing snaps under their weight.

Since the bridge is [just one Plank length long](https://adventofcode.com/2022/day/9), far, far smaller than the diameter of a proton, you'd think even the clumsiest human would be able to cross the gap. But it is what it is.

Part 1 of the problem considers a rope with a head and a tail, with the head moving randomly and the tail moving to keep within two units of the head. The answer is how many unique locations the tail visits. Part 2 extends the rope to 10 units long, but same deal otherwise.

**Python 3.11**

I do the Python in the morning without looking at anyone else's solutions. So sometimes I miss obvious stuff. I'm sure there are much better ways to do this. More "Pythonic" ways, but it is what it is.

`from math import sqrt

def walk_the_snake(puzzle: list, rope_size: int) -> int:
    snake = [(0,0)] * rope_size
    dir_map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    tail_visited = set()
    tail_visited.add(snake[0])

    for command in puzzle:
        snake[-1] = (snake[-1][0] + command[1] * dir_map[command[0]][0], snake[-1][1] + command[1] * dir_map[command[0]][1])
        anything_moved = True
        while anything_moved:
            anything_moved = False
            for i in range(len(snake) - 1, 0, -1):
                head = snake[i]
                tail = snake[i-1]
                dist_from_tail = sqrt((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2)
                if dist_from_tail  int:
    return 0 if a == b else int(abs(a - b)/(a - b))

with open(r"2022\puzzle9.txt") as f:
    puzzle = [command for command in code_gen(f.read().splitlines())]

print ("Part 1: {}".format(walk_the_snake(puzzle, 2)))
print ("Part 2: {}".format(walk_the_snake(puzzle, 10)))
`

**Java 14**

The Java solution is informed by the stuff I found out reading other people's solutions. Specifically, that Part 2 also solves Part 1. So there was no need to call it twice.

`    @Override
    public void preprocess(String content) {
        final var puzzle = getInputDataByLine(content);
        final int ropeSize = 10;

        List snake = new ArrayList<>();
        Set part2Visited = new HashSet<>();
        Set part1Visited = new HashSet<>();
        final var origin = new Point(0, 0);

        snake = IntStream.range(0, ropeSize).mapToObj(i -> origin).collect(Collectors.toList());

        part2Visited.add(snake.get(0));
        part1Visited.add(snake.get(0));

        var curPoint = origin;

        for (var command : puzzle) {
            curPoint = movePoint(curPoint, command);

            snake.set(ropeSize - 1, curPoint);

            Boolean anythingMoved;
            do {
                anythingMoved = false;

                for (int i = ropeSize - 1; i > 0; i--) {
                    var head = snake.get(i);
                    var tail = snake.get(i - 1);

                    if (Math.sqrt(Math.pow(head.x - tail.x, 2) + Math.pow(head.y - tail.y, 2)) >= 2.0) {
                        snake.set(i - 1,
                                new Point(tail.x + justOneStep(head.x, tail.x), tail.y + justOneStep(head.y, tail.y)));
                        anythingMoved = true;
                    }
                }

                part1Visited.add(snake.get(ropeSize - 2));
                part2Visited.add(snake.get(0));
            } while (anythingMoved);

            part1Solution = part1Visited.size();
            part2Solution = part2Visited.size();
        }
    }
`

Otherwise it's more or less the same as before.

**The Game**

I might start writing the games again. Tonight's game would have just been a Snake variant... obviously :-)
