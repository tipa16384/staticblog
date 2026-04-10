---
date: '2022-03-03T08:21:20-05:00'
draft: false
title: "7DRL: Building an Engine -- Winner."
author: "Tipa"
disqusIdentifier: "2022/03/03/7drl-building-an-engine-winner"
summary: "The last element of the 7DRL engine's \"must haves\" -- a win condition for the player. With that out of the way, let's talk about..."
categories:
  - "7DRL"
tags:
  - "Rogue"
  - "Tiled"
relatedPosts:
  - url: "/2022/03/07/7drl-2022-day-2-dungeon-room/"
    title: "7DRL 2022 Day 2: Dungeon Room"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-2.gif"
  - url: "/2022/03/04/7drl-building-an-engine-i-screwed-up/"
    title: "7DRL: Building an Engine -- I Screwed Up."
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/7drlfail.png"
  - url: "/2024/08/13/breakhack-fight-die-repeat/"
    title: "Breakhack: Fight, Die, Repeat"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/08/1-20240812215759_1.jpg"
  - url: "/2024/06/12/heroquest-return-to-barak-tor/"
    title: "HeroQuest: Return to Barak-Tor"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/06/return-14.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/screenshot.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/screenshot.png"
---
The last element of the 7DRL engine's "must haves" -- a win condition for the player. With that out of the way, let's talk about...
<!--more-->

The last element of the 7DRL engine's "must haves" -- a win condition for the player. With that out of the way, let's talk about localization, combat, and making the game look a little less like crap.

**Win Condition**

Determining win conditions without using code is a challenge, and it's a challenge I don't yet know how to solve. It's similar to the behaviors attached to weapons -- I can define behaviors in the Python code and then select them in the YAML, but I can't define them entirely in the YAML without writing some code in the YAML that knows about the game state somehow.

It's the kind of challenge that I don't have time to answer at the moment, and so I just define behaviors in code, and select them in the YAML, because it's all I can do right now. The trick with programming is to do what you can, and then later, when there is a better understanding of the scope of the problem, refactor -- come back and do it better.

It's the same for the win condition. I don't know how to put a particular win condition in the YAML -- *yet*. It's enough now that there *is* a win condition that can trigger the winning state in the application. I implemented a win condition which is simply to be the last actor alive. I'll have to revisit this when I do 7DRL, and maybe I'll figure out a better way.

I don't have time for blocks.

**Localization**

One of the benefits of extracting the game into an easily-editable text file is being able localize the game. The native German speakers reading the header image will tell me how poor it is (for one thing, I use the familiar case instead of the formal).

But the important point here is that at least some of the readable text of the game can be swapped to another language. It took a little debugging to get the umlaut to show, but that was necessary work. I can add "put all readable text in the YAML" to my ever-growing list of things that have to be done -- although it's going to be a low priority, as nobody is asking for localization of a game that doesn't exist. Still, now that I have a handle on it, future text will come from the YAML and I will transfer it all there as I work.

**Game Looks Like Crap**

Well, I never expected the engine itself to look like anything, I really don't like how it looks right now. I was looking around, and found an open source tool called "[Tiled](https://thorbjorn.itch.io/tiled)" that can generate isometric maps from terrain sheets, which is... just what I want.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/03/image.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/03/image.png)Tiled

This editor gives me the power to control exactly the look and feel of each room. I said before that I'm probably not going to have random rooms for this game, just because the story I want to tell is specific. Take away some Roguelike points for that, I guess.

Tiled outputs stuff in JSON, XML or CSV, where they can be easily read by any program. I can already generate a room from one sprite or randomly from a collection of sprites, but this gives me full control over that, AND allows me to decorate the rooms how I like. This is simply incredible.

So for tomorrow, I will be integrating the Tiled output into the game engine and recreate the three test rooms with it. This is going to allow me the ability to make navigating each room its own little puzzle, something I'd always planned to do, but wasn't sure how I would go about it. This is the answer.

**Combat**

I've been thinking a lot about combat. The original Rogue used a simplified D&D system, and I think there is no reason why I shouldn't just use that as well. I am going to have to figure out a way to target someone. The original Rogue did it by direction -- you selected up, right, down, left, up-right, down-left, down-right and up-left, and your weapon did its thing in that direction. I'm going to have to add a flag for being targeted by a player, add some visual indication, some means of selecting the target (does Trinket.io allow for mouse clicks?), perhaps some means of indicating the range of the weapon (Rogue just had "melee" and "until it hits a wall", depending). It's a lot to work on, but it is the last big remaining piece to this puzzle.

I'm still feeling overwhelmed, but I believe I can make it. How I feel now is nothing compared to how I'll feel when 7DRL is actually here. I'll be happy when it's over.
