---
date: '2022-02-17T00:20:41-05:00'
draft: false
title: "7DRL: Building an Engine -- Refactoring"
author: "Tipa"
summary: "I didn't make a lot of visible progress today, but I decided it was time to take a step back and do a vital step..."
categories:
  - "7DRL"
tags:
  - "Test Driven Development"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-1.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-1.png"
---
I didn't make a lot of visible progress today, but I decided it was time to take a step back and do a vital step...
<!--more-->

I didn't make a lot of visible progress today, but I decided it was time to take a step back and do a vital step in any programming project -- refactoring.

As usual, you can "play" the current test engine by [following this link to Trinket](https://trinket.io/pygame/86b9301490?outputOnly=true) and then pressing the "Run" button along the top of the window.

Trinket is a "good enough" solution for now. I'd like to move to a native browser implementation, but it ticks the checkbox that says "can run in browser", so I move on to issues I haven't yet addressed. (For one thing, Trinket doesn't use the latest version of Pygame, so sometimes I find myself using features not yet available there).

There's this concept you'll hear a lot if you're a programmer -- "[TDD](https://en.wikipedia.org/wiki/Test-driven_development)", or Test Driven Development. The philosophy goes, before you write a line of code, you write down all your expected results as a series of tests. For instance, you might be writing a calculator, and wish to add an "addition" function. You could write a test that sends in the numbers 1 and 2, and expects to return 3.

It will fail, of course, because you haven't written any code. So you might write one that simply returns the number 3.

`def addition(n1, n2): return 3`

First test succeeds! So you write a test that sends in 100 and 5 and expects 105. You might write:

`def addition(n1, n2):
    if n1 == 1 and n2 == 2:
        return 3
    else:
        return 105`

Closer -- at least we're looking at the values being sent in. All the tests pass, so we're good. But we can see that there's no way we can specify every possible combination of numbers, so we *refactor* the function.

`def addition(n1, n2): return n1 + n2`

We run the tests, and they still all pass. Then we can think of new tests -- like, what if someone only passes in one of the numbers? Or none of them? There might be more refactoring to do.

The example is silly, but the concept is important. In TDD, the emphasis is on writing code quickly, that is fully testable, so that at any change, you can run your tests and verify things are still working with your changes. And maybe you've thought of new tests, too.

Once the code is working, though, the programmer *must* take the time to go back and clean up the code. The tests they've written will keep them safe from unexpected errors.

That's what I did tonight. The code as of yesterday defined a single, fixed-size room, with fixed actors in fixed places. The game engine itself had no idea where the actors were, or how rooms were collected. I introduced a new class, called Floor. The game engine keeps a list of floors. Floors contain Rooms, and Rooms contain Actors. (I will move the Actors directly into the game engine at some point, as I will need them there to do pathfinding).

Instead of displaying a single room, I now look through the Actors to find the one that is marked as the player, and render the room that they are in. To a player, it looks the same, but internally, more information is being kept centrally, which would make it easier at some later date to save and load a game.

The post-mortem I wrote about my previous attempt at a 7DRL noted that my game state was all over the place, making it nearly impossible to keep track of all the moving pieces. I've taken that to heart. Lesson learned.

I meant to write today about pathfinding, but I really had to do this work, first. It will make everything so much easier.

I also bought a tileset and put that to work in the engine. It's too small -- I didn't realize it when I bought it -- so I'll still need to change it at least once more. Still, it looks nicer.

I fixed a bunch of graphical glitches I hadn't been able to find back when I was using this engine for Advent of Code. Smooth as butter now.

Am I on track? I don't really know. There is SO MUCH to do, it's overwhelming. But, good programming practices can help here.
