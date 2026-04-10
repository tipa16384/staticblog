---
date: '2022-02-21T08:07:58-05:00'
draft: false
title: "7DRL: Building an Engine -- Line of Sight"
author: "Tipa"
disqusIdentifier: "2022/02/21/7drl-building-an-engine-line-of-sight"
summary: "NPCs don't want to hit their allies while they are attacking you with ranged attacks. Some objects in the room can block them as well..."
categories:
  - "7DRL"
relatedPosts:
  - url: "/2025/03/10/how-to-fail-at-writing-a-game-in-7-days/"
    title: "How To Fail at Writing A Game in 7 Days"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/gamedevadventure.png"
  - url: "/2022/03/13/7drl-2022-retrospective/"
    title: "7DRL 2022: Retrospective"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/1-Dream_TradingCard-4.jpg"
  - url: "/2022/03/11/7drl-2022-day-5-im-damaged-and-i-like-it/"
    title: "7DRL 2022 Day 5: I'm Damaged, and I Like It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-5.gif"
  - url: "/2022/03/10/7drl-2022-day-4-tossing-and-turning/"
    title: "7DRL 2022 Day 4: Tossing and Turning"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/yata-screenshot-2.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/trinketamulet.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/trinketamulet.jpg"
---
NPCs don't want to hit their allies while they are attacking you with ranged attacks. Some objects in the room can block them as well...
<!--more-->

NPCs don't want to hit their allies while they are attacking you with ranged attacks. Some objects in the room can block them as well -- and using the objects in the room to deal with larger swarms of enemies will be an important strategy in the actual game. Today we go over the line of sight algorithm.

As before, you can always test the latest state of the game engine by [following this link to Trinket IO](https://trinket.io/pygame/86b9301490?outputOnly=true). I'd rather work with something that has the latest version of Pygame, or at least let me use a larger screen, but ya work with the tools ya have.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-3.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/02/screenshot-3.png)Playing with Line of Sight

I added some happy little trees to our test room. Based on the scale of the trees and the terrain, our adventurers are probably about 40 feet tall. Just saying.

In my last post, I wrote how each NPC has their own preferred positioning with respect to their target. Babus is the sprite closest to the bottom of the room and is currently representing the player. The templar is just northwest of them, and prefers to strike from melee range. The mog knight is partially hidden by a tree, and chooses to attack from the same row or column and currently cannot get into position to attack because of the tree and the templar. The archer is the Vierra to the right of the mog knight, and prefers an unobstructed view from 3-5 tiles away, and is *also* blocked by the trees.

Good job, Babus!

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/02/babusspeaks.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2022/02/babusspeaks.png)

The line of sight algorithm is an addition to each Actor's "good position" algorithm. Where the first implementation was just concerned with distance and position, we now draw an invisible line between the NPC and its target, and check every space it crosses to see if it's on the list of "bad spaces" we make that contains blocking static items or NPCs that are in the way.

Here's the Archer code:

`    def good_pos(self, pos, player_pos, bad_spaces):
        dist = manhattan_distance(pos, player_pos)
        return self.line_of_sight(pos, player_pos, bad_spaces) and dist >= 3 and dist 

I use a couple different distance algorithms, depending on how the NPC moves. The Archer seems to work best with the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), which is the sum of the absolute values of the differences between the X and Y coordinates of source and target.

This is another formula that came up a few times in Advent of Code.

I didn't make any progress this weekend, as I was playing Horizon: Forbidden West. But next up is map making. Map making should be fun as I currently have no idea whatsoever how I want to approach it for this game engine. I've been wanting to try out the old D&D random dungeon generator because it seems like it would work well with what I'm trying to do here. It does guarantee all rooms will be connected, so that's something.

Get something working, *then* refactor. I may iterate a few times on map creation. But I still have lighting to do, and items, and combat... SO MANY THINGS.
