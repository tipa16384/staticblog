---
date: '2024-10-26T15:23:33-05:00'
draft: false
title: "Last Call BBS: Puzzle Games for the Retro-Inclined"
summary: "The last game from the makers of TIS-100, SpaceChem, Exapunks and many other puzzle games feels like a Greatest Hits collection."
categories:
  - "Puzzle Games"
  - "Steam Games"
tags:
  - "Exapunks"
  - "Last Call Bbs"
  - "Zachtronics"
featured_image: "https://chasingdings.com/wp-content/uploads/2024/10/2-20241026104137_1.jpg"
cover: "https://chasingdings.com/wp-content/uploads/2024/10/2-20241026104137_1.jpg"
---

I don't know who the target market is for Zachtronics games, other than to have a deep and certain knowledge that I am in that market. They're known for a specific kind of puzzle game -- puzzles that take inspiration not from fantasy or science fiction, but from real-world engineering. Chemical engineers, mechanical engineers, software engineers, industrial engineers -- you're going to find a game that you'll recognize from your day-to-day. Not to say that only engineers can appreciate and enjoy these games, but if you aren't, and you like Zachtronics games, then maybe, just maybe, you might want to look into a change of profession? Because to be totally honest, I can't imagine what a non-techie would see in these games. For me, who has been programming since I had to flip switches to load a program on the school's PDP-8e to writing O/S kernels for the company of my dreams -- this is like *heroin*. Right into the vein.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/1-20241013203726_1-1024x575.jpg" title="\"The Graveyard of the Vernal King\", a Dungeons & Diagrams puzzle" class="align-center" >}}

"Last Call BBS" tells a story (yes, a *story*) of a man who has given you his Sawayama Z5 Powerlance, a fictional 90s Japanese computer that could perfectly emulate arcade games, though that was not its main purpose. He worked for Sawayama as a US sales rep and ran the titular BBS in the Kansas City area, where it became known as the place to go for "warez". The computer as given to you only has Solitaire for games; to download the others, you have to dial the Last Call BBS and download them, one at a time. And downloads are metered; only one download per session.

As you play through the games, PDA notes pop up telling you a little more about the game you're playing, his experiences while working for Sawayama, the history and eventual fate of the BBS and so on.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/3-20241026104215_1-1024x576.jpg" title="20th Century Food Court" class="align-center" >}}

**The Games**

There's seven games apart from the built-in Solitaire game:

- Kabufuda Solitaire -- a Solitaire variant using Japanese Kabufuda cards, where you match four cards to remove them rather than arranging them in stacks.

- Dungeons & Diagrams -- a cross between Minesweeper and Sudoku, where you place walls so that the dungeon follows certain rules.

- ChipWizardtm Professional -- supposedly software for designing integrated circuits, it's really a skinned logic game using PNP transistors, NPN transistors and capacitors as game pieces.

- Steed Force Hobby Studio -- not really a game; you assemble Gundam-like plastic models and paint them.

- 20th Century Food Court -- in the far future, our distant descendants are on a journey to rediscover what people of our time ate. They may have gotten some of the details wrong. If you love Factorio, you'll like this.

- JUiCEbox Arcade/HACK*MATCH -- the "original arcade version" of one of the pack-in games that came in with one of their other games; I believe Exapunks. I think I remember they released this as an NES cartridge? [Yes, they did](https://zachtronics.itch.io/hackmatch-for-the-nes). Move descending bricks down to form matches and combos before they overwhelm you.

- X'BPGH: The Forbidden Path -- an edgelord reskin of a cellular automata game where you set up an initial state and a rules sequence that will end in the desired state after a number of iterations.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/7-20241026104432_1-1024x575.jpg" title="Instructions for a soda dispensing machine" class="align-center" >}}

**20th Century Food Court**

I've tried all the games; 20th Century Food Court is my favorite. As in all of Zachtronic's puzzle games, you're given a toolbox with very few tools and must use those to complete the assigned task using the least amount of steps and components -- and you are scored against other players, so you'll very much understand where you could improve your solution.

In the one above, we're given an order -- Coke, Diet Coke, Pepsi, Diet Pepsi -- and must dispense a tray, dispense a cup, paint the cup the appropriate colors, give it two pumps of soda, dispense a lid, put the soda on the tray and the lid on the soda, and send it out. (The joke here is that the only difference between the sodas is the color of the cup).

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/5-20241026104332_1-1024x576.jpg" title="20th Century Food Court game screen" class="align-center" >}}

On the right side of the screen is a bunch of conveyer belts. The tray dispenser is at the top left; the output is bottom left; and the stacker is just above it. The output displays the order, and will reject it if it doesn't match. Cups and lids are dispensed from the machine in the top right. The belt just to the left with blue and yellow arms sorts things to the left, right, or straight through. This one sends lids to the left and cups down. The one just below it sends the cup to be painted with red on the bottom, if a Coke product, or blue on the bottom, if a Pepsi product. I could probably tighten that up a little. The last one passes non-diet orders to get a red top bar painted, or pass to the left if diet. It then passes a machine that beeps when something is in front of it, triggering the dispenser to dispense a lid and set the first sorter to pass through. The soda table gets two pumps, and then all three parts meet for stacking and delivery.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/20241026151227_1-1-scaled.jpg" class="align-left" >}}

The left part of the screen is the logic and control. Most of it is programming the sorters; the red component toward the right in the middle row controls the number of pumps of soda. The sequencer on the bottom left used to do a lot more, but now it just tells the stacker to release the tray after a certain time. I could replace that with another counter probably.

(Above, in the thumbnail: I did add a counter, sequencer now dispenses the lid and sets the first sorter correctly. Time went from 23 to 18, cost from 289k to 274k. Faster and cheaper).

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/10/6-20241026104423_1-1024x575.jpg" title="Scoreboard and customer reactions. Getmeouttahere still gave it two stars." class="align-center" >}}

I was writing this blog post and thought of a way to make the soda factory more efficient, and this is what always happens to me with Zachtronics games. Always a way to make solutions just a little better. The building blocks are like LEGO; each one is so simple that they'd never be used in real life, but you can eventually build almost anything you want with them -- if you weren't constrained, like the puzzles in Last Call BBS, by available space or components.

So, if you have ever played and enjoyed a Zachtronics game, you'll like Last Call BBS. The games run from the simple to the complex, and each one has sooo many levels that you won't finish the game any time soon. I haven't completely finished any of the games; not even close. There's more game here than in the whole of Exapunks or SpaceChem -- easily. So, give it a shot.
