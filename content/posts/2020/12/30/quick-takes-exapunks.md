---
date: '2020-12-30T09:05:06-05:00'
draft: false
title: "Quick Takes: Exapunks"
summary: "Basically Cyberpunk 2077, except you never leave your bedroom."
categories:
  - "Quick Takes"
  - "Steam Games"
tags:
  - "Exapunks"
  - "Programming"
  - "Puzzle"
  - "Steam"
  - "Zachtronics"
featured_image: "https://chasingdings.com/wp-content/uploads/2020/12/20201230072838_1.jpg"
cover: "https://chasingdings.com/wp-content/uploads/2020/12/20201230072838_1.jpg"
---

Take a hacker plot that mixes up *Hackers*, *The Matrix*, *Johnny Mnemonic*, *The Cuckoo's Egg *and *Neuromancer*.  Add a little *2600 Magazine* and [Captain Crunch](https://en.wikipedia.org/wiki/John_Draper). Mix in the standard Zachtronics programming puzzles you already know from *SpaceChem*, *TIS-100* and *Shenzen I/O*. And now you've got Exapunks all over you.

If you have played any of the other Zachtronics games (aside from [Eliza](https://www.zachtronics.com/eliza/)), then you already know what you're going to be doing here. Learning techniques to solve programming puzzles (graphically in SpaceChem; using pseudocode in the other games), and then fearlessly optimizing your solution in order to make a good showing on the leaderboards.

{{< figure src="https://chasingdings.com/wp-content/uploads/2020/12/20201230074206_1-1024x576.jpg" >}}

In the world of Exapunks, almost all digital communication is done through small nano-machines called "Exas". The Exas are too small to do extensive computation, and each can only perform a very few instructions. However, they can do network traversal and basic file I/O as native commands, and they can communicate easily with external devices and with each other, making them an unusual hybrid of RISC processor and [software agent](https://en.wikipedia.org/wiki/Software_agent).

Exas are represented in the game as little virus-like bots that skitter through the network of devices represented as grids with stylized files and data ports. In the example above, we were asked to hack a highway display sign to display arbitrary messages. I chose to solve it by having one Exa read the file containing the desired message, and another receiving this data, formatting it for display, and sending it to the sign.

{{< figure src="https://chasingdings.com/wp-content/uploads/2020/12/20201230074251_1-1024x576.jpg" >}}

This screen, displayed after a hundred test runs, shows that my solution was entirely average. This isn't surprising; it's still an early puzzle.

Cycles are the number of clock cycles it took, on average, to complete the task. Size is the total number of instructions among all Exas. Activity is the number of network traversals. It's possible to improve on these separately; for instance, by unrolling the loops in each Exa to decrease the number of cycles while vastly inflating the size. Or, we might just use one Exa that brings the file to the highway sign, copies it to the sign, then brings it back to its origin before exiting (since we must leave things as we find them; "leave no trace" is the ethos here). This would reduce the size, at a likely cost of cycles and activity.

{{< figure src="https://chasingdings.com/wp-content/uploads/2020/12/1-IMG_2052.jpg" >}}

As in many of Zachtronics' previous games, Exapunks wants you to print out the reference manual, here in the form of a 'zine called Trash World News, which mixes hacker cred with a description of the Exa instruction set and a walkthrough for the first few puzzles. Pictured above is my own hax0rz setup :-)

If you've played any of their other games, you know what you're in for. If you haven't, but just have some bizarre yearning for the days when microcomputers meant assembly language, this is definitely for you. If you're interested in a gamelike exploration of the creation of software agents, this might also be for you. Puzzle gamers will find a lot to like here as well.

It's a niche game for a niche audience. If you have never programmed, Zachtronics games are a decent introduction to the basics; there's never too many things to learn, unlike modern programming.

{{< figure src="https://chasingdings.com/wp-content/uploads/2020/12/EXAPUNKS-SFCTA-Highway-Sign-4902-164-13-1-2020-12-30-07-43-05.gif" >}}

I always get a certain way into these games but give up at the most difficult problems. I think I'm going to try to finish this one, so I'll write more about it then.
