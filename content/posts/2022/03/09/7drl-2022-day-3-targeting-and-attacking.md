---
date: '2022-03-09T07:33:04-05:00'
draft: false
title: "7DRL 2022 Day 3: Targeting and Attacking"
author: "Tipa"
summary: "I reached an important milestone, though a day late as I lost a day integrating the new tile set. As I added targeting and combat,..."
categories:
  - "7DRL"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/day3teaser.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/day3teaser.png"
---
I reached an important milestone, though a day late as I lost a day integrating the new tile set. As I added targeting and combat,...
<!--more-->

I reached an important milestone, though a day late as I lost a day integrating the new tile set. As I added targeting and combat, I began to realize what kind of game this was becoming, and I think that understanding is going to let me finish 7DRL with an actual game that is, maybe, fun to play?

Once you get through the Plotro, you're tossed into the training room with a Sprite who can't fight back. That's because she's using imaginary weapons. Unfortunately for her, *you* are using a very real saber.

`- item: &nomove Finger Guns
  itemType: NECKLACE
  canWield: True
  behavior: DUMMY
- actor: *sprite
  room: *rm0202
  inventory:
    - item: *nomove
    - item: *firewand
`

She should have wielded the Wand of Fire she has, but she just equips the first wieldable thing she has in her inventory. The wand will become more relevant later. Finger Guns have the "DUMMY" behavior, which means there is no position she can move to where she could attack the player, and so she does nothing.

NPCs always have their target -- the player. The player, however, can pick and choose their target, and so I had to add the concept of a target. NPCs determine if they are in range as part of their path finding algorithm, but the player doesn't have path finding, so I had to hook up the UI to the "good_pos" algorithm that I think I described back when I was building the engine.

You'll see in the video that the player now can enter a room at a given position and facing a certain way. In fact, everything in the scene is now controlled by Tiled, as I implemented the Tiled Object Layer last night. This gives me the opportunity now to set up specific scenarios.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/03/image-6.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/03/image-6.png)Tiled map with object layer

The first new scenario is actually in the first room. Where before I just had Ritz appear randomly, now she looks to be coming down a path to a clearing where she can encounter the Amulet of Yendor.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/03/image-7.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/03/image-7.png)New "intentional" starting screen

Removing randomness in this way could be seen by some as moving YATA *away* from roguelike, but I disagree. It's moving it *toward* roguelike. Let me explain. This has to do with the epiphany I had while coding last night.

My new conception for the game is that each room is a puzzle. Each room will have a goal, such as defeat all enemies, or pick up a certain item, or whatever I can dream up. Finishing a goal will immediately move to player to the next challenge, and, aside from the first room, you are playing whatever NPC is holding the Amulet. This means that the specific character you are playing has repercussions when you finish the level.

So, the game then becomes making up new puzzle rooms *which could be randomly generated at some point, becoming more roguelike*.

Tonight, we're having Training Room #2, which will have you toss the amulet to the Sprite, have her wield the Wand of Fire and kill an archer that Ritz cannot get to, and then have her either kill Ritz, or, assuming the player remembers to do so, re-equipping the Finger Guns and tossing the Wand of Fire to Ritz before tossing the Amulet back to her. Then Ritz can kill the Sprite and finish the level.

*Multiple ways to approach a problem is ALSO ROGUELIKE.*

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-3.gif" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-3.gif)I also added a list of commands in case someone was curious about them.

I needed someone to explain to the player about the targeting and the combat system, so I enlisted the Frog Knight from Chrono Trigger to help out, as he can look directly down the screen without facing left or right, as HIS game isn't isometric. I implemented him as an item so that he couldn't be targeted, and blocked his space off from the rest of the training area so that nobody would attempt to pick him up. I probably should animate him, though that means *every* item could potentially animate, leading to scope issues now and down the road. Or I could make him an NPC, give him finger guns, and add a flag to make him non-targetable (so that nobody could kill him or toss him an amulet or a weapon, because GUYS HE IS NOT ISOMETRIC, HE CAN'T MOVE AROUND THE ROOM!!!)

Tonight, then, I have to implement wield/unwield and tossing items to a target. Right now, every weapon hits every time and just does a point of damage, but this may not be the time to worry about how weapons differ, since at this time, I am not planning on making items a huge part of the game. I may drop potions in places to increase health or add desired effects to solve a room. I'll also have to add a roadmap through the game to show how the rooms connect and what the win conditions are. This would also allow moving backward to earlier rooms if it becomes important for some reason.

If all goes well tonight, and I don't see why it should, I might be able to put the final room in tonight. Then, all I have to do is construct maybe fifty or so increasingly challenging puzzle rooms and call it done.
