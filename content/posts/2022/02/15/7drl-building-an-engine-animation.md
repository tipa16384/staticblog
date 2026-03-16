---
date: '2022-02-15T22:50:18-05:00'
draft: false
title: "7DRL: Building an Engine -- Animation"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/02/15/7drl-building-an-engine-animation/"
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
summary: ""
description: "Desc Text."
tags:
  - "7DRL"
  - "Rogue-Likes"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Tonight, I made it so my sprites had a walking animation, decided to show all four walls of the room, and found out some things about Trinket I didn't know before. Also, what is a roguelike, anyway? And why not use something like Unity that solves most of the problems I am having?

I am building a rogue-like engine to use in the upcoming "7DRL" game jam. You can see my current progress by heading to Trinket [via this link](https://trinket.io/pygame/86b9301490?outputOnly=true) and pressing the "Run" button up along the top.

I was going to make a new "Trinket" for each day of development, so that the progression would be traceable, but, it looks like only the first Trinket can have image files for some reason.

It's likely that most of the people who would read this post already have a fairly good idea what a "Roguelike" game is.

[![](https://chasingdings.com/wp-content/uploads/2020/10/roguebat.jpg)](https://chasingdings.com/wp-content/uploads/2020/10/roguebat.jpg)Rogue, the first Rogue-like

A Rogue-like, to me, has most of the following features: Top-down, ASCII graphics, random dungeon generation, unidentified items have unknown effects, monsters only move when you move, death means game over.

A lot of modern "Rogue-likes" dispense with some or all of these. From watching reviews of many indie games on YouTube, I get the impression that the one attribute that separates "roguelikes" from "not a roguelike" is the "death means game over".

My "Rogue-like" engine will keep the "death means game over", "monsters move when I move", and "unidentified items have unknown effects". I may or may not have random dungeon generation -- that decision will probably wait until the challenge begins. I'll be using an isometric view with sprites for monsters. I may or may not stick with Final Fantasy Tactics sprites -- that decision probably also will have to wait for the actual game challenge.

Why? A couple reasons. First is, it's the kind of game I want to write. I love strategy tactics games and have always wanted to write one. Second is, I want to stand out from the crowd. Tile graphics are pretty common in roguelikes, but I haven't seen isometric done very often.

Animation is hard. Even when you already have the sprites.

It's easy enough to just teleport sprites everywhere. It's here but wants to be there? Okay, now it's there. If I want to animate actual motion from here to there, I have to plan every frame, and make those frames happen at the correct time.

Pygame can run at any given frames-per-second, and that would be one way of managing the animations. Just set the FPS to the number of frames of animation/number of seconds you'd like that to take, and just increment the animation and position every frame.

For this engine, I let Pygame run at whatever speed it can manage, and I load up all the in-between points in a move queue. I have a timer that fires about eight times a second that checks the move queue and does the in-betweening for that tick. I have a second timer that fires about four times a second that cycles every sprite through its walking animation (just like in Final Fantasy Tactics). No matter how fast or slow the host computer is, these things should run around the same time.

Each Actor -- a sprite that can move -- has its own move queue, so everything can move at the same time, if necessary. In practice, everything will move one-at-a-time so that I don't have to worry about two things potentially colliding. I may rethink that later,

Why not Unity?

I do want to use Unity. I think it's more or less inevitable. I have a couple issues. First of which is that it's entirely new to me -- I have no experience with it. Second is that I haven't used C# for years. The one project I did do with C# was really tiny -- an Outlook plugin.

I have to limit the scope of "new things" if I want to have any chance of getting *anything* working. My current plan, if I do actually finish a game, is to port this to Unity afterward. And then I will know it.

Next few things:

- Pathfinding for enemies- Multiple rooms- All game state saved in the game object- Less ugly temporary room art
