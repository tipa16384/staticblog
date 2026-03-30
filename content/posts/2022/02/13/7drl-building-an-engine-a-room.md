---
date: '2022-02-13T19:58:14-05:00'
draft: false
title: "7DRL: Building an Engine -- A Room"
author: "Tipa"
summary: "The annual 7DRL -- 7 Day Rogue-Like -- game hackathon is next month. I did this a really long time ago, but I didn't know..."
categories:
  - "7DRL"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/7drlengine1.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/7drlengine1.jpg"
---
The annual 7DRL -- 7 Day Rogue-Like -- game hackathon is next month. I did this a really long time ago, but I didn't know...
<!--more-->

The annual 7DRL -- 7 Day Rogue-Like -- game hackathon is next month. I did this a really long time ago, but I didn't know at that time that I could start the competition with a game engine already programmed. By the time I finished the engine, I only had a day left to build some sort of game on it. This time, I'm building the engine ahead of time.

There's actually a bunch of roguelike engines out there. Some of them even support the Final Fantasy Tactics-like isometric view, that I am hoping to use this time. Starting with one of those would leave me only having to build the actual game on top of it.

I looked at them. They were really, really good. Some of them would work right in the browser, so people could play it without having to get Python and PyGame running on their local computers. All the problems I would face, they have already dealt with.

But I am not going to use any of them. For Advent of Code, I wrote a basic isometric tile system and animation system to support the visualization of one of the puzzles, and I intend to build that out to an actual, if probably very basic, game engine.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/02/puzzle23_0-1024x867.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/02/puzzle23_0.png)Rotating a room

I intend, in the game, to only display one room at a time, with the isometric view. Final Fantasy Tactics Advance characters are standing in for whatever characters I will use in the actual game -- my AoC visualization used them, so I have already formatted and animated their sprites.

Today's tasks were to render the floor of the room, some sort of walls, and to rotate the view so that the player can see things (doors, etcetera) that are on the near walls. My boyfriend says I should implement a compass so that people can keep oriented, so I will probably implement that pretty soon.

The graphics are all placeholders. I may still move to a 3D tileset for the floors and walls. Since I'm not an artist, it depends on what I can source -- but *that does not matter for the engine*. By the rules of 7DRL, I cannot work on actual gameplay until those seven days begin, pencils down seven days later.

More later...

Here's how I used similar assets for Advent of Code.
