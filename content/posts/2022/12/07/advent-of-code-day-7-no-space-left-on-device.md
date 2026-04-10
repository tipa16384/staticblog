---
date: '2022-12-07T20:36:28-05:00'
draft: false
title: "Advent of Code Day 7 -- No Space Left On Device"
author: "Tipa"
disqusIdentifier: "2022/12/07/advent-of-code-day-7-no-space-left-on-device"
summary: "Today's coding challenge was, \"Make a file system without making a file system!\" I failed that task."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Java"
  - "Python"
relatedPosts:
  - url: "/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/"
    title: "Advent of Code Day 11 -- Monkey in the Middle"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-11-16.50.33-A-woman-wearing-a-Christmas-hat-staring-at-a-monkey-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/10/advent-of-code-day-10-cathode-ray-tube/"
    title: "Advent of Code Day 10 -- Cathode-Ray Tube"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-10-19.36.37-A-woman-in-ragged-clothes-wearing-a-Christmas-hat-playing-a-video-game-in-the-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/09/advent-of-code-day-9-rope-bridge/"
    title: "Advent of Code Day 9 -- Rope Bridge"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-09-21.18.23-Christmas-Elves-walking-on-a-tattered-rope-bridge-crossing-a-river-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/08/advent-of-code-day-8-tree-top-treehouse/"
    title: "Advent of Code Day 8 -- Tree Top Treehouse"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-08-19.17.41-Several-Christmas-Elves-enjoying-the-view-from-a-Treetop-Tree-House-in-a-forest-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-07-20.16.30-A-Christmas-elf-sitting-at-a-computer-looking-at-a-Windows-error-screen-by-Bob-Eggleton-intricate-and-detaile.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-07-20.16.30-A-Christmas-elf-sitting-at-a-computer-looking-at-a-Windows-error-screen-by-Bob-Eggleton-intricate-and-detaile.png"
---
Today's coding challenge was, "Make a file system without making a file system!" I failed that task.
<!--more-->

[Today's puzzle](https://adventofcode.com/2022/day/7) is one of those puzzles that just test whether you are familiar with some basic computer stuff, like hierarchical file systems and Unix shell commands.

When I saw this puzzle, this morning, I figured I would just make a file system in memory and just build according to the puzzle input, do the parts, and be done. And I did, and it worked, and it was *fiiiiiiiine*. Until I went to Reddit and people there were competing on *alternate* ways of solving this challenge, with stacks, or maps, or dictionaries, or smoke signals or I don't know what.

I tried implementing the Java side with "Deque" and failed and so I just went with making a fake file system, though I did take an idea I saw that said there was no reason to preserve individual files, since the parts were only concerned with folder sizes. So that was something I yoinked.

**Python 3.11**

"day7File" is just the representation of the file system. Careful reviewers will see in makeFileSystem that it ignores the "ls" command (properly) and cheerfully adds all files, folders and otherwise, to the file system. Also note passing lambdas down to the work function.

`from day7file import File

def makeFileSystem(puzzle):
    root = File("/", 0, None, True)
    wd = root

    for l in puzzle:
        # if l starts with '$ cd ', change working directory
        if l.startswith("$ cd "):
            wd = wd.change_working_directory(l[5:])
        elif l.startswith("$ ls"):
            pass
        else:
            wd.add_file(l)
    return root

with open("2022\\puzzle7.txt") as f:
    root = makeFileSystem(f.read().splitlines())

# starting at root, make a list of all folders which have a calcSize of at most 100000
delete_me = root.find_folders(100000, lambda a, b: a = space_needed
delete_me = root.find_folders(space_needed, lambda a, b: a >= b)
print ("Part 2: {}".format(min([f.calcSize() for f in delete_me])))
`

**Java 14**

`
    private File root = null;

    @Override
    public Object solve1(String content) {
        makeFileSystem(content);

        var deleteMe = root.findFolders(100000, (a, b) -> a  a >= b);
        return deleteMe.stream().mapToInt(File::calcSize).min().getAsInt();
    }

    private void makeFileSystem(String content) {
        if (root == null) {
            root = new File("/", null);
            var wd = root;

            for (var line : getInputDataByLine(content)) {
                if (line.startsWith("$ cd ")) {
                    wd = wd.changeWorkingDirectory(line.substring(5));
                } else {
                    var toks = line.split(" ");
                    if (StringUtils.isNumeric(toks[0])) {
                        wd.addFile(toks[0]);
                    }
                }
            }
        }
    }
`

Java is similar. I use a BiFunction to pass lambdas around here, but it is really nearly the same as the Python.

It would have been nice if the Deque stuff worked, but it wasn't any cleaner. I dunno why people felt doing the obvious solution was going to be a bad thing. My aim is to just get these things done.

**The Game**

Still no game. Still in the middle of a family emergency and really don't feel like gaming or writing games. 

But this one in particular -- I'm sure there's a game to be found in file systems (I remember the file system star turns in Jurassic Park, Disclosure and Johnny Mnemonic), but I can't imagine it would be any fun to play.
