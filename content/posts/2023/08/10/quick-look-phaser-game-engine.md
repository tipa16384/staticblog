---
date: '2023-08-10T07:00:00-05:00'
draft: false
title: "Quick Look: Phaser Game Engine"
author: "Tipa"
disqusIdentifier: "2023/08/10/quick-look-phaser-game-engine"
summary: "I've been spending a few hours trying to get this Asteroids clone to some sort of playable state. Since I haven't really done anything else..."
categories:
  - "Blaugust"
  - "Blaugust 2023"
tags:
  - "Aws"
  - "Godot"
  - "Javascript"
  - "Othello"
  - "Phaser"
relatedPosts:
  - url: "/2023/08/05/adventures-in-bad-game-development/"
    title: "Adventures in Bad Game Development"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/DALL·E-2023-08-04-23.05.25-classic-video-game-box-art-of-a-space-ship-shooting-a-centipede-with-asteroids-in-the-sky.png"
  - url: "/2023/08/28/retro-world-expo-scorecard/"
    title: "Retro World Expo Scorecard"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/sailormoonpikachu.png"
  - url: "/2021/09/01/resurrecting-west-karana/"
    title: "Resurrecting West Karana"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/b0d5f94a61f128683568fec95571fa8e.jpg"
  - url: "/2024/06/25/its-not-writers-block-its-distraction/"
    title: "It's not writer's block, it's distraction"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/06/distracted.jpg"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/gameover.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/gameover.png"
---
I've been spending a few hours trying to get this Asteroids clone to some sort of playable state. Since I haven't really done anything else...
<!--more-->

I've been spending a few hours trying to get this Asteroids clone to some sort of playable state. Since I haven't really done anything else blog-worthy today, I guess we're talking about Phaser.

I mocked up yesterday's header image from assets I made with Inkscape; they weren't actually from a real game. Today's image is from a real game.

Asteroids isn't the toughest game to write. You spawn a ship, you spawn some rocks, you spawn a laser, rocks go away. Since there's not much to the game itself, it's perfect to use as a test bed to gain familiarity with a new game engine.

My game engine of choice, for many years, has been PyGame. It runs in Python, and everything about it just seems to make sense to me. Problem is that it is very hard to distribute any game written in PyGame, and I have tried -- and failed -- many times.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-22.png" title="Reversi and/or Othello" classes="center" >}}

I tried a test, a couple months ago, to just write a game -- any game -- in straight JavaScript and HTML. That worked really well. My version of Othello leveraged the native HTML objects and attached JavaScript to them to make things happen.

But it was hard to work around JavaScript's limitations, especially around asynchronous events and having things display on the screen precisely when I wanted them to. Also, you can see in the image above that I had to have little shadow disks placed on the board so that people could tap them to move. This is a problem; people shouldn't have crutches like this. But I needed to have *something* there.

For Othello, I would like to have the logic on a remote server and just have the user interface running on people's browsers. For many reasons that I won't go into just now.

In order to best leverage the code I'd already written, I went looking for JavaScript-based game engines. Phaser was at the top of the list.

It has been a struggle.

The Asteroids game used the Phaser demo as a base -- its logo bouncing around a starfield with red particles blowing all over the place.

This was my first and probably worst mistake, as the version of Phaser used by the demo was waaaaay out of date. A lot of the examples for stuff I needed, like keystroke and controller input, plain didn't work, and I spent too much time looking for workarounds. Once I noticed in a different demo that their version was well ahead of mine, I updated mine, and suddenly everything started working better.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-23.png" title="Aster-assets" classes="center" >}}

My original design goal was to construct the game board out of object groups, right down to the line segments used to draw the asteroids and the ship. This is how the original Asteroids game was written; it used a vector display, and what it displays is literally a list of line segments.

I couldn't get that working (probably due to the version issue), so I relented and drew vectory-looking asteroids and ships in Inkscape and exported them as sprite sheets. Not vectors. Just plain old bitmaps, being rotated and moved with Phaser's sprite commands.

It's clear that I wouldn't be able to write a game engine like Phaser in any reasonable amount of time. The last few times I did program games with animation in JavaScript, I did it using the HTML Canvas object, which is a blank slate you can draw on. Phaser can use Canvas, but preferentially uses WebGL, a far more capable graphics engine that can do many cool things.

I'd also considered Godot and Unity, which both can be exported to the web. Unity, in particular, has an object based scripting language that I like. But what I'm really looking for is an engine that works in the browser without having to load any sort of runtime module. Phaser fits the bill, for now.

I don't think I'll make the Asteroids clone into my "Real Asteroids" idea. I could, but I think I have learned enough now to start on something else. Maybe "Bug Pong". I have one thing left to do, well, two things. I need to record high scores on AWS, and I need to be able to display a high score table. Then I'll probably put it on itch.io and move on.
