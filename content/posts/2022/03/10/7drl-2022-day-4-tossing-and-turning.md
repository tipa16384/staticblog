---
date: '2022-03-10T07:35:45-05:00'
draft: false
title: "7DRL 2022 Day 4: Tossing and Turning"
categories:
  - "7DRL"
tags:
  - "Messiah"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/yata-screenshot-2.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/03/yata-screenshot-2.png"
---

Halfway through the 7DRL and I have finally finished the major building blocks for the game by introducing the main game mechanic (finally)! But it *is *the halfway point, and a good time to wonder if this was the correct game to write for 7DRL?

After 7DRL 2022 is done, I'll be trying out as many of the other 7DRL games as I can, and write about them here. There's been a few that I really want to play, and I really want to play them because they have a central new idea, and they build a small game around that idea. You're hitting that new gameplay mechanic from the first second, and it builds from there.

The ones I don't much connect with are the ones, oddly, that just look like variations of Rogue. Yes, this is 7 **D**ay ***Rogue***-**L**ike, but this isn't the 80s, the bar has been raised for computer games in general and roguelikes in particular.

The central idea for *You Are the Amulet* is that you take control of NPCs and use their items, positioning -- what have you -- to work through the dungeon. There's no healing (yet, anyway), and the true win condition means defeating the wizard at the end with the character you started with, who only has ten health to last through however many dungeon levels I can come up with.

[![](https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-4.gif)](https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-4.gif)Battle log showing the main game mechanic

This game doesn't show that central possessing-NPCs mechanic very well. There's been a bunch of games with that same mechanic; *[Messiah](https://en.wikipedia.org/wiki/Messiah_(video_game))* is the first one that comes to mind. You played there a baby angel who possesses people to solve puzzles, so pretty much the same deal.

*My* game looks like a Final Fantasy Tactics Advance ripoff. So much so that the of the friends I've shown it to, a good percentage of them just told me how much they liked FFTA. Right? It's a great game. A little difficult to get to the true ending (and I still have not done that), but great game. I totally should not have used those sprites. But, after playing FFTA for weeks, all I really wanted to do is write a game like FFTA. And I did, twice now -- once for Advent of Code, and now here.

So, I'm having fun and making something I wanted to make, but it is not going to do well in the 7DRL judging because, stolen assets aside, it doesn't lean into its central game mechanic. At the very least, I'd have to animate the Amulet being tossed around, and animation of an NPC becoming possessed while the other NPC reacts to no longer being possessed. 

**So anyway.**

Last night, I added the ability to Rest (so that enemies could approach into range), Wield/unWield weapons, and Toss items. I also added something called a "roadmap".

`roadmap:
  - *rm0202
  - *rm0201
`

Like everything else, it's a new section of the YAML that defines the game. This is simply the list of puzzle rooms in the game, once through the intro. Room 0202 is the training room with the frog knight, and 0201 is the Wizard of Yendor's room.

The Wizard will be taking the Amulet with her when you enter the room, though, so no cheating the ending by possessing the Wizard and then killing the one you brought to the dance. The header image with the Wizard being possessed clearly doesn't have that mechanic yet.

Anyway, get through those rooms without dying and the game is won.

The only mechanic I need to add to the game is the concept of a limited number of uses. Powerful items, such as the wand of fire, will have very few uses. Bows will have several more, while melee weapons will be fairly reliable, though the more damaging ones may lose their edge.

So that's the plan for tonight. Tomorrow I am taking a day off work and that day will be entirely spent on level design (and we can shuffle them for *more roguelike*)! Saturday will be polish and finishing touches and perhaps more levels and then turning it in.
