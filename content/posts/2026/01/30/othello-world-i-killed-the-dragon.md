---
date: '2026-01-30T10:00:00-05:00'
draft: false
title: "Othello World: I Killed the Dragon"
author: "Tipa"
disqusIdentifier: "2026/01/30/othello-world-i-killed-the-dragon"
summary: "I've been working on beating this Othello boss for years. Now it's dead and I am one step closer to meeting the Othello master."
categories:
  - "Game Development"
tags:
  - "Othello"
  - "othello world"
  - "super famicom"
relatedPosts:
  - url: "/2026/02/03/the-end-of-the-othello-world-saga/"
    title: "The End of the Othello World Saga"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/Screenshot-2026-02-02-20-11-59.png"
  - url: "/2026/02/13/othello-trigger-for-the-gameboy-color/"
    title: "Othello Trigger for the Gameboy Color"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/othellotrigger.png"
  - url: "/2024/05/25/retro-game-haul-tron-deadly-discs-and-reversi/"
    title: "Retro Game Haul: Tron Deadly Discs and Reversi"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/trondeadlydisks.png"
  - url: "/2024/03/30/retro-game-haul-march-30-2024/"
    title: "Retro Game Haul: March 30, 2024"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/03/IMG_4228.jpg"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2026/01/Screenshot-2026-01-29-21-40-06.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/01/Screenshot-2026-01-29-21-40-06.png"
---
I've been working on beating this Othello boss for years. Now it's dead and I am one step closer to meeting the Othello master.
<!--more-->

I love playing Othello. My mom bought me a set when I was a kid, and I still have it, and it still has all its pieces. In high school and in college, I played Othello a lot. When I was learning how to program, Othello was one of the first games I wrote -- in BASIC.

I'd write it again and again over the years. I wrote it in FORTRAN at university. I wrote it in C at DRI. I wrote it in Python back when Alpha Go was explaining the secrets of the Monte Carlo Tree Search, and then I started writing it in JavaScript and Phaser a couple years back. Oh yeah, I wrote a version for the Sony Magic Link, and it sold, for money, to people who I didn't know. Othello made me a published game developer :-)

In all that time, I was never actually any good at the game. I played a lot, but I lost a lot. I've studied, and I've become better, but it's still easy for me to write Othello games I can't beat.

So I set myself a new task.

I found a Super Famicom version of Othello at some bargain loose cartridge bin -- Othello World. It was never released in English, but the Japanese isn't too tough; it was written for children.

Othello World introduces you to the White Rabbit, who teaches you the basics of Othello and then plays a very basic game with you before he reveals your true destiny: to meet -- and beat -- the world's greatest Othello player, Hideshi Tamenori. But before you can meet him, you have to beat fairytale characters across three different worlds.

The first world offers Pinocchio, Goldilocks and so on. They aren't *too* tough; I could beat them. Defeat three of the five opponents there and you move to Sea World, which has mermaids, krakens and, oh yes, Long John Silver. I could not beat him. I studied Othello, tried to up my game, and came close sometimes, but never did beat him.

Anyway, long story etc, I decided I would write an Othello program that could beat Long John Silver.

I tried writing MCTS again, with an opening book I got off the internet, but that wasn't good enough. I wrote an alpha/beta "negamax" strategy, but *that* wasn't good enough. So this morning, I wrote a genetic algorithm to slowly zero in on the correct weights for a board evaluation heuristic and I ran it all day. (This isn't the first time I tried this, mind). Genetic algorithms were all the rage a few years back. You define the behavior of an algorithm by a few key variables you define, assign values randomly, apply some sort of fitness function, keep the ones that work best, make offspring with values from their parents and mutate some of them, and keep trying again and again until you reach a plateau. (Then you study the variables, see if any are not truly independent, define new variables and try again).

This is, btw, how the first AI image generators worked. They'd start with static and then keep iterating until a second AI thought it looked like a dog or whatever. The generator was a genetic algorithm, the one that determined how close to a dog the picture looked was signal processing.

The algorithm had been chugging away on my Raspberry Pi all day. After work, I took those weights and used them to run a quick and dirty Othello program. Othello World would play black; I'd enter those moves into my program and it would spit out white's move.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2026/01/image-5-1024x679.png" title="My game playing the other side of the game in the header" classes="center" >}}

I still have two more enemies to beat in Cloud World. I don't remember if I meet Tamenori in the next world or there is another level after that.

Anyway, since I have played a bunch today, I can tell that the SNES/SFC Othello World uses an opening book and a min/max algorithm. I don't know if it's "negamax", that algorithm may have been discovered after this game came out. Each new "world" adds another depth to its move search; in this third world, moves are *slow*. 

My game didn't beat the dragon the first try. I kept tweaking the weights between each game. (The weights being things like, how many corners do you own, or you are near to, and how many edge pieces do you have, and are they safe, and toward the end of the game, how many pieces do you have). There's other possible variables, like the number of open regions and whether or not they have an odd or even number of blank spaces in them, how "quiet" you are playing, how many pieces are in danger of being captured, how many of your own pieces are potentially blocking you from making moves, how many moves you have and so on.

Anyway, I don't have the opening book in this implementation, but I'll add it, and I think I will slip in a MCTS after a certain point. In this game I won, my moves were coming in fast. That meant my algorithm thought the game was going to be a landslide for me or the dragon. Othello games are all about forcing your opponent to make the first bad move. And Dragon blinked first; I knew I'd won.

So anyway, that's a thing that happened. And now I'm off to CaptainCon to face my betters on the field of battle, Malifaux-style.
