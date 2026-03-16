---
date: '2022-03-04T08:17:29-05:00'
draft: false
title: "7DRL: Building an Engine -- I Screwed Up."
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/03/04/7drl-building-an-engine-i-screwed-up/"
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
  - "Tiled"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/7drlfail.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/03/7drlfail.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

I really thought I had more time. I thought I had a *week* to integrate the new Tiled-based map creation tools, and to make a workable combat system. I did not. I am entirely out of time. 7DRL starts tomorrow.

I honestly, 100%, thought that 7DRL started on the twelfth. I thought that I would just barely be able to get the engine in rough shape by then, but it turns out I didn't have any time at all.

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-1.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-1.png)Oops.

So, I panicked. I was stunned. How could I have been so wrong. I posted on Twitter that I was abandoning 7DRL, I left the jam, and started thinking about how I would go forward with the game, now that I suddenly had all the time in the world.

The last time I did this, a long time ago, I was so stressed by the end of it that, to this day, I still remember the anxiety I felt when the end of the jam came up and I barely had any sort of working engine and the game was just hit stuff until it died. I abandoned it after the jam. I have no idea where that code even is any more, as this was before Git.

All *this* code for *this* jam is backed up on Git and will be available to anyone to see forever. It's safe.

After an hour or so had passed and my panic receded a little bit, and after some nice messages from friends on Twitter, I rejoined the jam, but only after remembering what I read in the event rules:

- You CAN use external libraries, game engines, pre-existing code/algorithms, pre-existing art, etc. You can even start your game from an existing game if you are planning to turn it into something unique. If in doubt, be clear about what resources were reused.- The goal is a finished and reasonably polished game: not the prototype of a game. **Watch your scope!**- Likewise, the goal is a new game, not just another week of work on an existing game.- It is allowed and recommended to have a rough design idea of your project before starting

**Watch your scope!**

That's it. Those were the words.

Character creation -- *gone*. I was going to allow players to choose between at least two character classes, maybe up to four. That's off the table. Gone. Maybe later.

Floor transitions -- *gone*. I was going to interface with one of the AI art generation shops to generate interstitial images that would be at least somewhat related to what the new floor would look like. (Those AI images can look pretty vague). Anyway, those are gone. In fact, *floors* are gone. I haven't implemented switching floors in the engine, so it's gone.

Playable in a browser -- *probably gone*. I'm not worrying about getting this working on Trinket.io. I will limit the game, for now, to working with just Python3 and Pygame and no other libraries, so that people will be able to play it without worrying about dependencies. And at the end, I will try to backport it to Trinket. I'm hoping that won't be an issue, but I can't afford the time to do it. The plan was to rewrite this as a way of learning Unity, and that solves a LOT of issues.

Watching that scope.

I've said it before and I will say it again. This game is going to have a start and an end, first thing. It may be the shortest game 7DRL has ever seen, but I will sweat blood on those two rooms, and once those are done, I will add a room between them, and another and another and however far apart the beginning and end rooms are by the end of seven days is as far as they're gonna get.

Last night, I began the integration of the Tiled map editor I showed yesterday. The maps are generated with the tiles in a very different order than I had been using, and so there remain some occlusion issues between the actors and the terrain that you'll see above.

I switched the enemy in the first room from the melee-oriented Templar to the range-oriented Archer to show how pathfinding deals with obstructions. Even though it might seem like a low bush or a stick on the ground shouldn't block an arrow, *it does*, because if ranged enemies don't face the same restrictions melee enemies face, then melee is useless.

So, that's it -- that's the engine. The family has plans for tonight, and tomorrow is Saturday. I don't usually post on the weekend, so on Monday, I will reveal how far I got on the weekend and what my cool idea was for the game.

This is the last **7DRL -- Building an Engine** post... at least for this year.
