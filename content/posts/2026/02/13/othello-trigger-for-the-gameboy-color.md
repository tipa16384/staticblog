---
date: '2026-02-13T08:21:17-05:00'
draft: false
title: "Othello Trigger for the Gameboy Color"
author: "Tipa"
summary: "\"Othello Trigger\" smashes a Chrono Trigger de-make into Othello using GB Studio. Can drag-and-drop game engines really make worthwhile games?"
categories:
  - "Game Development"
tags:
  - "dissimilar"
  - "gamemaker"
  - "gb studio"
  - "Othello"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/othellotrigger.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/othellotrigger.png"
---
"Othello Trigger" smashes a Chrono Trigger de-make into Othello using GB Studio. Can drag-and-drop game engines really make worthwhile games?
<!--more-->

Having just finished an extremely long fight with an Othello game, it's not that I was really looking for *another* one to play. To conquer. By writing a program that could beat it.

I was just idly looking for anyone who had drawn some Othello piece sprites I could yoink into a UI I would do for that Othello game that I just wrote. My game is great, I guess, if you like running Python programs from the command line, but I don't think anyone wants to do it. I haven't even played it since I used it to beat Othello World.

The easy, and expensive, way would be to toss it up on AWS Lambda and use a web interface to make REST calls blahblahblah. I probably will -- I've done it with other games -- and I doubt I or anyone else will play it enough to cost me any real money.

SO ANYWAY, [OTHELLO TRIGGER](https://greatfoohachi.itch.io/othello-trigger)! Remember Chrono Trigger?

> Ever since its release in 1995, people have been patiently waiting for a true sequel to Chrono Trigger, yet all we got was Chrono Cross, and then radio silence.  Well 30 years is long enough!  Finally, Chrono Trigger has a true sequel.  And just like Metroid, its sequel is on Game Boy, Game Boy Color to be exact!  Do you love Active Time Battle?  Do you love exploring different time periods?  Do you love New Game+ and multiple endings?  Do you love 16-bit RPG's?  Because if you do, then this is *NOT* the game for you.  Seriously, it has none of that, go play Chrono Trigger instead.

Othello Trigger has Chrono and his friends (aside from the Frog Knight, who chooses to spend his time elsewhere) meeting again for a new adventure -- playing Othello.

And it does; it does play Othello, at a basic level. I think it plays at least as well as the Gameboy version of Othello World. But, that's not the cool thing about the game.

The cool thing about the game is trying to fit all those different characters, settings, splash screens, animations and even the Othello disks themselves in such a small amount of memory. Even the author's best compression tricks couldn't actually get it to fit in the Gameboy cartridge's limited memory, requiring them to bring it to the Gameboy Color, even though the graphics are 100% just the standard Gameboy palette.

This was possible because the game was written with [GB Studio](https://www.gbstudio.dev/), which is directly supported by the Analogue Pocket. It's a drag-and-drop way of creating Gameboy and Gameboy Color games without having to get into the nitty gritty of assembly language. It can export into code that could actually play on actual cartridges. Analogue talked up its integrated GB Studio support when it released its Pocket, by far the best retro hardware it has released to date. I took a quick look, but it seemed like it would not be making the kinds of games I wanted to make, but it could be that I was very wrong about that.

I'd thought the same about [GameMaker](https://gamemaker.io/en), but then I find just how many modern, shipping games -- like the recent [Dissimilar](https://store.steampowered.com/app/2904360/Dissimilar/) -- are built with that game engine. "Easy to use" doesn't mean "can only make simple games".

I'm a big fan of Chrono Trigger and Othello. Othello Trigger was a game I couldn't ignore. I didn't bother pitting it against my Othello, as I beat it easily without any help. I had fun, though.
