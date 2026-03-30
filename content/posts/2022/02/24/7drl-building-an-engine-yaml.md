---
date: '2022-02-24T00:14:57-05:00'
draft: false
title: "7DRL: Building an Engine -- YAML"
author: "Tipa"
summary: "If someone were to quiz me on how a game engine is different from a game, I'd think about it a bit, and then probably..."
categories:
  - "7DRL"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-4.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-4.png"
---
If someone were to quiz me on how a game engine is different from a game, I'd think about it a bit, and then probably...
<!--more-->

If someone were to quiz me on how a game engine is different from a game, I'd think about it a bit, and then probably explain that a game is run *by* the game engine, but no part of the game is actually *in* the game engine. I'm enforcing that by moving the game (as opposed to the game engine) into YAML, which stands for ***Y**AML **a**in’t **m**arkup language*. The game is data. The game engine runs that data.

The original roguelike, Rogue, was entirely contained in its code. It could only play one game -- Rogue. When its distant child, Nethack, was written, the situation hadn't changed much. Every thing that happened in the game could be traced to some bit of 'C' code.

Modern game development has come a ways from those early games. The game is now separated from the engine that runs it -- look at the thousands of games run in the Unity game engine, and the Unity game engine doesn't know one from the other. It just loads up the C# and runs it.

My roguelike game engine does something similar. I'm currently about halfway through yet another refactoring. Until now, I was describing my test environment in Python code. That was fine for getting things running. But with the move to multiple rooms (and soon, multiple floors), it wouldn't do to keep writing code for these things. Enter: YAML.

Here's the dungeon you can see in the video at the bottom of the post, encoded in YAML:

`- floor: Test Floor
  rooms:
  - room: &rm0101 Entry Room
    width: 10
    height: 10
    tileType: OUTSIDE
  - room: &rm0102 Other Room
    width: &rm0102width 5
    height: &rm0102height 7
    tileType: ROOM
  - room: &rm0103 Corridor
    width: 10
    height: 1
    tileType: GRASS
  exits:
  - exit:
    - room: *rm0101
      x: 3
      y: -1
    - room: *rm0102
      x: 4
      y: *rm0102height
  - exit:
    - room: *rm0103
      x: -1
      y: 0
    - room: *rm0102
      x: *rm0102width
      y: 2
`

The actors and objects aren't yet encoded, but they're next.

YAML has a lot of advantages over Python code. For one, you can just change this one text file instead of learning Python code. A different person could potentially be working on making the actual game while I continue working on the engine. Maybe an artist could be building assets and adding them to a specific YAML file that contained those.

Separating the data of the game from the game engine allows collaboration between many people, and YAML is a simple enough file format that non-coders can do what they do best -- designing games -- while coders do what they do best -- make them go.

Note the labels and references encoded in the YAML -- when I come to building the actors into the YAML file, I will be able to have them in their own section (and perhaps even their own file) and still drop them in their correct room.

**But is it *Rogue-like*?**

One of the things that makes a "Rogue-like" is the random map, monster and item generation. Explicitly setting the rooms, their sizes, contents and connections as is done in the YAML above would seem to make this less Rogue-like, and more like any other RPG.

Nothing about YAML means it couldn't be used to make things random. I intend to craft a very particular game experience when 7DRL starts, and this will work best for me at the moment. As I work through it, if I find out how to get the flow I want and still randomly generate map and monsters, then I will. But, I'm not going to let a feature checklist stop me from writing the game I want to play.

But yes, I would love it if I could tell this story and also hit every rule of Roguelikes. But I'm just not that creative, so I am going to do it this way, and then maybe, when I come to write a second game on the game engine, I will know enough to be 100% Roguelike AND tell a story with a beginning and an end.

Here's the video. I added bad music played badly by me through a bad microphone. Some game dev on Twitter was complaining that they'd waited too long to start adding sound and music to their game and had to crunch at the end, so I took that lesson to heart.
