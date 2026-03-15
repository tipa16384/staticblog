---
date: '2022-03-11T07:37:23-05:00'
draft: false
title: "7DRL 2022 Day 5: I'm Damaged, and I Like It"
categories:
  - "7DRL"
tags:
  - "Blue Oyster Cult"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-5.gif"
cover: "https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-5.gif"
---

It may seem like I'm not making a lot of progress, but I have a checklist for each night, and I really am doing what needs doing. Last night, I added a lot of new systems and fixed some crazy bugs, clearing the path for today's "jam".

I'm not gonna apologize for my love of Blue Öyster Cult. Here's "Damaged", a song that should have been a hit off an album that should have been a hit. They been done wrong.

Classic.

Here were last night's goals:

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-8.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-8.png)Goals

- **Pick up corpses**
I had a particular problem with corpses. The player can't move through them (although, due to a bug, the NPCs can), so corpses could potentially clog up the map, making completion impossible. I needed a good way to clear corpses. Eating them, as is done in Nethack, seemed yucky, but I thought it might be fun to pick them up and then toss them at NPCs for damage. Unfortunately, my current 'get' code only picks up what is where you are standing, and you can't stand on corpses. I opted to just write a service that checks every 30 seconds for corpses, and then removes any it finds.- **Item uses**
The one behavior I don't want is for the player to run through all the NPCs, get the wand of fire, and then just blast everything away from range. I added a random number of uses to every item. Once those are used up, I wrote another service that quietly removes the item from your inventory. I also limited your inventory to ten items, so stocking up would be more difficult. I also added damage to each weapon (previously, they all did just one damage), and a percent to hit chance (previously, they all always hit). This means that the player will always have to keep finding new items. Powerful items have very few uses, and the NPCs can use up those charges as well.

I'd also thought to just have weapon uses stack, such that if you had a sword with 5 uses, and then you took a sword with 10 uses from an NPC, you would now have a sword with 15 uses. It quickly became clear that the player would soon have all possible items with so many uses that this would stop being any sort of limitation. I don't want to see the player with a Wand of Fire that they can spam to cheese every encounter.- **Wizard room**
Becoming the Wizard of Yendor and blasting the NPC that finally brought the Amulet to the final room would be cheesy, so I wanted the player to lose the Amulet upon entering the final room. The Wizard can then use her lightning wand that does some crazy amount of damage to incinerate the player. Yes, there will be something the player can do to block this attack, but I need to leave *some* surprises.

To test situations where there are multiple NPCs in a room, I loaded up the Training Room with a bunch of them. I immediately found issues where NPCs were unresponsive, moved on top of each other, or kept moving between two spaces when they didn't need to move at all. When I set specific spots for them to spawn in Tiled, sometimes they'd spawn there, sometimes no.

So, that meant a bit of debugging I didn't necessarily want to do, but had to do.

Today, I'm taking a personal day at work to "jam" and create a script that can create an arbitrary number of dungeon levels, and then take it for a spin. Tomorrow, Saturday, the last day of the challenge, will be about tuning.
