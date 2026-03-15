---
date: '2022-12-08T20:12:31-05:00'
draft: false
title: "Advent of Code Day 8 -- Tree Top Treehouse"
summary: "It's all about taking a break from those busy reindeer games to build a treehouse with a really stellar view. Also, what is code golf?"
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Java"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-08-19.17.41-Several-Christmas-Elves-enjoying-the-view-from-a-Treetop-Tree-House-in-a-forest-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-08-19.17.41-Several-Christmas-Elves-enjoying-the-view-from-a-Treetop-Tree-House-in-a-forest-by-Bob-Eggleton-detailed-and-intricate.png"
---

We're supposed to be hunting for special stars for reindeer magic power, but ya know, why not [build a treehouse](https://adventofcode.com/2022/day/8)?

The first task is to see which trees are visible from the edge of the forest. The naïve and foolish way to do this would be to trudge through *every single tree* in that forest and trace it out to find view lines. The *clever* way would be to just go around the edge and look for trees on the inside. *O*(n) vs *O*(n2). So I solved that quickly and was pretty happy.

So then Part 2 required going through every single tree. Boom.

**Python 3.11**

That meant I now had two methods that did more or less the same thing, in opposite ways. So I spent a few minutes golfing it. Code Golf is the process of using as few characters as possible in a program. It trades readability for compactness, and when you're doing it right, you're using every bit of knowledge of the language to lose one more character.

I didn't get to that level, but I did make it so that Part 1 and Part 2 were as similar as possible.

`from functools import reduce

def getResults(puzzle, x, y):
    results = [(calc_view(puzzle, x, y, dx, dy)) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    return any([r[0] for r in results]), reduce(lambda a, b: a * b, [r[1] for r in results])

def calc_view(puzzle, start_x, start_y, dx, dy):
    height = len(puzzle)
    width = len(puzzle[0])
    start_tree = puzzle[start_y][start_x]
    num_trees = 0
    x, y = start_x, start_y
    is_visible = 0

    while True:
        x += dx
        y += dy

        if x = width or y = height:
            is_visible = 1
            break

        num_trees += 1

        if puzzle[y][x] >= start_tree:
            break

    return is_visible, num_trees

with open("2022\\puzzle8.txt") as f:
    puzzle = f.read().splitlines()

grid = [getResults(puzzle, x, y) for x in range(len(puzzle[0])) for y in range(len(puzzle))]

# count the number of True values in vis_grid
print("Part 1: {}".format(sum(r[0] for r in grid)))

# find the max value in grid
print("Part 2: {}".format(max(r[1] for r in grid)))
`

**Java 14**

This is cool. I copied the Python code into the Java file and Github CoPilot just translated it into Java. It wasn't perfect, and I had to do some cleanup and use the Java-specific ideas such as the inner class I use in place of tuples, but after about ten minutes cleaning it up, it just worked.

Impressive.

`package com.chasingdings.y2022;

import java.util.ArrayList;
import java.util.List;

public class Puzzle8 extends AbstractPuzzle {
    private static final String DATA_FILE = "2022\\puzzle8.txt";

    private List grid = null;

    @Override
    public Object solve1(String content) {
        parsePuzzle(content);
        return grid.stream().mapToInt(r -> r.visible).sum();
    }

    @Override
    public Object solve2(String content) {
        parsePuzzle(content);
        return grid.stream().mapToInt(r -> r.treeCount).max().getAsInt();
    }

    private void parsePuzzle(String content) {
        if (grid != null) {
            return;
        }

        var puzzle = getInputDataByLine(content);

        grid = new ArrayList<>();
        for (int x = 0; x  puzzle, int startX, int startY, int dx, int dy) {
        int height = puzzle.size();
        int width = puzzle.get(0).length();
        char startTree = puzzle.get(startY).charAt(startX);
        int numTrees = 0;
        int x = startX;
        int y = startY;
        int isVisible = 0;

        while (true) {
            x += dx;
            y += dy;

            if (x = width || y = height) {
                isVisible = 1;
                break;
            }

            numTrees++;

            if (puzzle.get(y).charAt(x) >= startTree) {
                break;
            }
        }

        return new TreeInfo(isVisible, numTrees);
    }

    private TreeInfo getResults(List puzzle, int x, int y) {
        List results = new ArrayList<>();
        results.add(calcView(puzzle, x, y, 1, 0));
        results.add(calcView(puzzle, x, y, -1, 0));
        results.add(calcView(puzzle, x, y, 0, 1));
        results.add(calcView(puzzle, x, y, 0, -1));

        int anyVisible = results.stream().mapToInt(r -> r.visible).max().getAsInt();
        int totalTrees = results.stream().mapToInt(r -> r.treeCount).reduce(1, (a, b) -> a * b);

        return new TreeInfo(anyVisible, totalTrees);
    }

    @Override
    public String getDataFilePath() {
        return DATA_FILE;
    }

    @Override
    public String getPuzzleName() {
        return "Day 8 - Tree Top Treehouse";
    }

    class TreeInfo {
        int visible;
        int treeCount;

        public TreeInfo(int visible, int treeCount) {
            this.visible = visible;
            this.treeCount = treeCount;
        }
    }
}
`

**The Game**

The family situation is maybe easing up a bit, maybe I'll be able to start writing games again, especially with a week vacation coming up -- though some of that may be driving a car back from Colorado. That will be a fun several days.

Not sure what the game here would be -- something about growing trees, I guess. But I'm saving up ideas. I saw a Pico-8 first person Doom-style package that could be fun for the upcoming 7DRL. I should work on that.
