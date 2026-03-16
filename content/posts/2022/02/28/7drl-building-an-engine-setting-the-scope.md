---
date: '2022-02-28T08:33:52-05:00'
draft: false
title: "7DRL: Building an Engine -- Setting the Scope"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/02/28/7drl-building-an-engine-setting-the-scope/"
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
  - "Rogue-Likes"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot-5.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot-5.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

This weekend, I added weapons, monsters only move when you move, and I added flags to tell if items were identified, cursed, wielded or worn. Each flag multiplies the complexity of the code by at least three times, but it is flags like these that are central to the Roguelike experience. How many flags I choose to implement has a direct correlation to how the game plays... and whether I can finish it at all.

But first, regarding the music to the game. That kalimba song I have now is pretty bad. I could make the excuse that for the past few months I have been working on mandolin, if that hadn't sounded even worse when I recorded it. But this past weekend, I saw a tweet that pointed to [an online synthesizer called the Viktor NV-1](https://nicroto.github.io/viktor/). Some of the patches it has are pretty cool. So maybe abandon me performing music and just use *that*.

[![](https://chasingdings.com/wp-content/uploads/2022/02/image-1024x515.png)](https://chasingdings.com/wp-content/uploads/2022/02/image.png)The Viktor NV-1 synthesizer

Back to the fun stuff.

Here's a code snippet from the original Rogue to illustrate what I was saying above about flags:

`for (mp = mlist; mp != NULL; mp = next(mp))
	if (on(*mp, ISINVIS) && see_monst(mp) && !on(player, ISHALU))
	    mvaddch(mp->t_pos.y, mp->t_pos.x, mp->t_disguise);`

[Someone on Reddit broke it down](https://www.reddit.com/r/roguelikedev/comments/9rgb33/original_rogue_source_code_and_compiling_it_on_a/) -- basically, if a player could normally see a monster, but now can't because the monster is invisible, although they could if they were hallucinating, then display the monster as looking like the tile they are standing on.

There are three flags being used here -- is invisible, is hallucinating, and presumably if the room they are on is lit or if the player is close enough to see it even though the room is dark.

This means Rogue has items that can detect invisibility, make things invisible, make things visible, make something hallucinate, cure hallucination, detect hallucination, make a room lit, make a room dark, perhaps make the player blind, cure blindness. All these things are very "Roguelike", by definition, since they were there in Rogue. But each one multiplies the work.

I have less than two weeks to finish this game engine. Right now, every thing I add to the engine multiplies the complexity in the same way, but the more flags I can implement, the more Roguelike the end game will be.

`weapons:
- item: &firewand wand of fire
  itemType: WAND
  behavior: MAGIC
  canWield: True
- item: &longbow longbow
  itemType: BOW
  behavior: ARCHER
  canWield: True
- item: &broadsword broadsword
  itemType: SWORD
  behavior: MELEE
  canWield: True
- item: &lance knight's lance
  itemType: POLEARM
  behavior: CHARGE
  canWield: True
`

The YAML that will encode the game grows larger every day. I also wrote a small compiler that will take the YAML and translate it to the data transmission format JSON, because Trinket.io doesn't support PyYAML but does support the JSON package. A lot of what I am doing or not doing is tuned towards what works or doesn't work on Trinket, which makes me happy I decided to make "getting this running in the browser" the FIRST problem I tackled.

I previously had each enemy's behavior encoded directly to their actor. I have now extracted that and attached behaviors to the weapon itself. This allows actors to pick up or swap weapons and modify their behavior accordingly. For instance, the Viera could see that somehow she ended up within melee range to the player, swap to a dagger and take on the MELEE behavior.

The "itemType" flag will determine which icon is used when it is dropped on the dungeon floor. Picking up and dropping items is yet to be done, and I don't know if I'm going to do it.

Why wouldn't I allow dropping and picking up items? Because then I have to deal with inventory. Actors *do* have an inventory, but right now, I don't have to write a UI to show it to the player, let them choose things from it, and so on. I don't have to implement ways of randomizing the descriptions of unidentified items, or giving players mechanisms to identify them. I don't have to display items on the ground. I don't have to give the user a mechanism to select a tile so they can take a look at it. Trinket doesn't support common Python GUI packages, and so I would have to code these things from scratch.

I *want* to do all these things, but I won't have time. I have to set the scope of what I can reasonably accomplish. Once 7DRL starts, I wanted to be focused on writing the game, not writing the engine (though I will almost certainly continue working on the engine as I find things I need to do).

There are some things the game *must* do.

- The game *must* begin- The game *must* have a win condition- The game *must* let you lose- The game *must* let you defeat enemies- The game *must* let you be defeated by enemies

A game with only these things might not be super exciting or even worth playing, but at least it would be a game. These are the table stakes. Miss any of those, and I miss them all. Right now, less than two weeks out from 7DRL, I don't have *any* of these things.

The precise beginning and ending are going to be part of the game, so I can't implement those yet, but I have to set the groundwork. Combat is pretty central to the Roguelike experience, so that's going to be next, which should set up the "let you lose" checkbox. Combat is one of those things that has to be continually tuned.

So at this point, I am beginning to be a little discouraged. Last year, I said I was going to work on a game engine *all year*, but then I didn't. When the annual contest to go through the roguelike creation process following a tutorial came up, I wanted to take that time to create the engine, but then I didn't. I procrastinated and now here we are. I have what I believe is a great idea for a Roguelike, and this is driving me forward, but I am afraid this is going to end up as disappointing experience as my 7DRL entry was eight years ago.

Last time, I wrote the engine during 7DRL (not knowing then that I could use a pre-written engine as long as I acknowledged that), but it was written so quickly and was such a big gigantic hack that I never wanted to look at it again. I am being quite a bit better with the code this time, so there's a chance I will be able to continue work on the game and the game engine after 7DRL with the goal of eventually porting it to Unity and, who knows, maybe taking part in Turn-Based Thursday someday.

I'll probably have to stop using Final Fantasy Tactics Advance assets, though. At the moment, FFTA is letting me put sprites and animations in the "good enough" column, right up there with Trinket, and using Pygame vs Unity. The current game engine is built around the publicly available sprite sheets for FFTA, and it really isn't so easy to find fully animated isometric fantasy sprites for free as you might think. The Final Fantasy Tactics sheets are *way* more complex. The Ogre Battle sprites don't have as much community support, so... FFTA it is. For now.

The immediate goal is to clear up that checklist. Once that is done, I can worry about implementing flags. I really want to do as many as possible.
