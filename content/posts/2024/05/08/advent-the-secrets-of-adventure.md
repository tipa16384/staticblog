---
date: '2024-05-08T07:00:00-05:00'
draft: false
title: "ADVENT: The Secrets of Adventure"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2024/05/08/advent-the-secrets-of-adventure/"
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
summary: "What you need to know before you begin to play Crowther and Woods' \"Colossal Cave Adventure\"."
description: "What you need to know before you begin to play Crowther and Woods' \"Colossal Cave Adventure\"."
tags:
  - "Adventure"
  - "Colossal Cave"
  - "Colossal Cave Adventure"
  - "RPG"
featured_image: "https://chasingdings.com/wp-content/uploads/2024/05/cca-banner2.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2024/05/cca-banner2.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

You have probably never played an adventure game quite like ADVENT. It wasn't intended to be a commercial product. It was intended to be a fun diversion; you had half an hour free, see how far you could get.

Commercial[1](#69230c98-f1fb-4967-b481-ed65e616f977) adventure games let you take as much time as you liked. You could save the game and come back to it. If you made a misstep, you could just load a save and be back where you were. Adventure games soon helped by letting you know exactly what you could do and where you could go at any particular moment. When they went graphical, they were sort of obliged to have things connected in a way that made sense.

ADVENT doesn't have any of those constraints. Your lamp has 330 turns of light in it. If you are caught in the caves without light, any motion has a chance to fling you into a pit, to your death. Always turn off your lamp before teleporting out of the caverns.

*(If you claim you have not played the game before, the game secretly gives you 1000 turns of light).*

You are not alone in the dungeon. Aside from the monsters which stay in their rooms, more or less (some can be befriended and can come with you), there is a family of dwarves which have decided they don't want some outsider fiddling around with your treasure. They will hunt you down and kill you... unless you kill them first.

Do unto others, etc.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/image-5-1024x291.png" title="Pirate." class="align-center" >}}

Further, you are being stalked by a pirate who wants to take all your treasure. If he finds you before you find him, he *will* take all your treasure, and with it any hope of getting a decent score. You can hunt him down, though, and take it back... and maybe some other treasure he happened to have stashed away.

This time, he got an emerald the size of a plover's egg, and some diamonds. Well, too late to track him down now. He's in one of those terrible endless mazes.

There are three mazes in ADVENT; and two of them are famous.

**You are in a maze of twisty little passages, all alike**

Long thought to be the worst maze in the game, the rooms aren't connected with any geometry a human understands, and each room just says the same thing. I *think* this is the Battery Maze, where you can spend a treasure to put more time on the clock. I haven't started working on the mazes, yet.

**You are in a twisty maze of little passages, all different**

Back in the day, I thought for a moment that this was the "all alike" maze, but I quickly realized that the names of the rooms here are all different, and so it is easy to map. I *think* this is the Pirate Maze, where the pirate hides once he has stolen your treasure. I might have these mixed up.

**You are wandering aimlessly through the forest**

This maze, which is right at the start of the game, didn't exist when I played the game back in college. This is new. I've started mapping it... but it is pretty bad. It might even be the worst maze, *but*... there's at least one item in there you need.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/fullmap-1024x614.png" title="The Map of Room Connections" class="align-center" >}}

So before I go -- I spent some more time on my program to map room connections. I was thinking about the problem at work today, and when I got home, I rewrote it. The rooms are arranged so that they are generally close to the rooms close to them. I colored them from red to green according to their order in the game files. I did not include any of the mazes. Those are too twisty.

I'm not sure how useful this will be. I do have some ideas for a variant of the program that will attempt to connect things in meaningful ways.

Why not just play the game?

This *is* how you play the game! Mapping, thinking about the puzzles, trying to figure out how to leave things where you're gonna need them, and all before the time runs out. In this run, I am of course using the "newbie" mode with 1000 turns.

Okay! Maybe tomorrow we'll map the Pirate Maze and I'll see if I can get my stuff back. (The original game didn't have saves, but *this* one does -- at a point penalty).
