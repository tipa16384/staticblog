---
date: '2022-03-01T07:38:11-05:00'
draft: false
title: "7DRL: Building an Engine -- It Begins"
author: "Tipa"
summary: "Yesterday I mentioned a few things that were required to be part of any roguelike game engine. Today, I add two of them -- an..."
categories:
  - "7DRL"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/mar01roguelikeintro.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/mar01roguelikeintro.jpg"
---
Yesterday I mentioned a few things that were required to be part of any roguelike game engine. Today, I add two of them -- an...
<!--more-->

Yesterday I mentioned a few things that were *required* to be part of any roguelike game engine. Today, I add two of them -- an introduction, and a way for the player to be defeated.

To recap: Here are the things that I felt needed to be addressed in order to even begin thinking about the actual game I'll be building in a week and a half:

- The game *must* begin- The game *must* have a win condition- The game *must* let you lose- The game *must* let you defeat enemies- The game *must* let you be defeated by enemies

When I start programming the game, I am going to start with these five things. The player will probably be able to win in just a minute or two, or perhaps be defeated. Once I have these five things done -- which really should happen in the first day or two -- then I can start adding content between the beginning of the game and the end of the game, while *always* being able to draw a line from start to end, such that, at any point in time, I could say the game was fully playable.

Maybe not *fun*, maybe not *complete*, but playable.

{{< image src="https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/The_Hartford_Financial_Services_Group_logo.svg/1200px-The_Hartford_Financial_Services_Group_logo.svg.png" classes="center" >}}

Every year, my company has a code-a-thon for all of its developers. We form into teams and then are given an application to write in about three hours. I've learned that those teams that score the best tend to have come into the challenge prepared, usually with a generic application already written upon which they can do the challenge. The organizers sometimes give hints about what the challenge might be -- the challenge might be to do data analysis using a cloud application built on AWS, for instance -- that provides a starting point.

The one time we won, this is how we did it. Those teams that don't start with something already running, don't finish in time.

This is why I am doing what I am doing. Day 1 of 7DRL, I want a running application, so that by Day 7, I have a running *game*.

Until today, the main program just does what it does -- create actors and rooms and let you move things around in them. I've changed that now so that that entire portion of the engine is just a service called by a main dispatcher.

This new dispatcher knows about all the different parts of the player experience. I wrote a new service that just puts up an introductory splash screen where the plot (such as it is) could be told before heading into the main game. For the game, I will probably have the intro lead to character creation before dropping the player into the main game. I could split the game into several chapters, each one telling a portion of a story, and never, ever be in a spot where I couldn't deliver a working game, with this dispatcher. When the player wins or loses, this could dispatch to the correct chapter, and BAM. Just like that. A working game with a beginning and an ending, and all I have to do is just keep adding stuff to push them further apart, and at no time will the game ever be unplayable.

I never said anything about fun. I hope that comes, too.

I told my boyfriend last night that I was going to add combat to the game, but then I got excited about writing this dispatcher and an intro. He was kinda disappointed that I wasn't writing the combat.

Fine. I updated the YAML so that all the actors have health. I'd already given them weapons, though I hadn't really worked on how damage and defense worked. Still, a promise is a promise. Now, when enemies are at an appropriate distance from you depending on the weapon they are wielding, they will attack, and hit, and take away a point of health.

I haven't added any way for the player to target or attack, so you run around until you die.

Progress!
