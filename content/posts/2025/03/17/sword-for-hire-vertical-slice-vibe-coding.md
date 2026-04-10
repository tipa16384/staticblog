---
date: '2025-03-17T08:00:00-05:00'
draft: false
title: "Sword for Hire: Vertical Slice &amp; Vibe Coding"
author: "Tipa"
disqusIdentifier: "2025/03/17/sword-for-hire-vertical-slice-vibe-coding"
summary: "When it's mapped out, Sword for Hire isn't as large as it looks in the book. But, it is possible to play through the game and level up."
categories:
  - "Text Adventure Game"
tags:
  - "Python"
  - "Tunnels & Trolls"
  - "Vibe Coding"
relatedPosts:
  - url: "/2026/02/18/a-new-tunnels-trolls-in-this-economy/"
    title: "A new Tunnels &amp; Trolls? In this economy?"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/TTnewbanner.png"
  - url: "/2025/03/10/how-to-fail-at-writing-a-game-in-7-days/"
    title: "How To Fail at Writing A Game in 7 Days"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/gamedevadventure.png"
  - url: "/2025/03/03/tunnels-trolls-sword-for-hire/"
    title: "Tunnels &amp; Trolls: Sword for Hire"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/ttbanner.png"
  - url: "/2025/01/25/ai-is-going-to-steal-my-job-and-i-couldnt-be-happier/"
    title: "AI is going to steal my job -- and I couldn't be happier"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/01/minitray.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/swordforhiremap.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/swordforhiremap.png"
---
When it's mapped out, Sword for Hire isn't as large as it looks in the book. But, it is possible to play through the game and level up.
<!--more-->

I was watching a documentary about the creation of the first XCOM game a long, long time ago. The game devs were so focused on the concept of making their "vertical slice" -- enough of the game so that all the important systems could be demonstrated to work.

Yesterday, in a frenzy of typing and coding, "Sword for Hire" hit its vertical slice. You can create a character, head into the dungeon, and get to the end. Along the way you are going to die, a lot, but I added in systems so that you can keep the money and experience you earn in the dungeon so that you can level up your stats enough to survive and crush the dungeon, setting yourself up nicely for part 2: Blue Frog Tavern.

The printed adventure had 157 unique bits of plot; I have 179 because I needed some additional ones to handle the mechanics I implemented -- mainly rooms looking different once you have been there and killed a monster, looting a treasure, etc.

The game, as printed, was punishing. If you just did it as a just-rolled character, you would never get some of the treasure; it would be blocked behind making several consecutive saving throws in a row. I added an arena where the player can gain coin and xp before entering the dungeon (and can continue to while in the dungeon, and this is preserved when you die).

The player won't win their first time through, but they will win if they keep at it and keep leveling up their stats. The second part of the adventure should be just about the right difficulty for someone who has finished this one.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/03/image-6.png" title="No spoilers!" classes="center" >}}

There's a lot of bugs in the game; sometimes options appear when they shouldn't, mostly. I've been madly implementing the mechanisms to update what the player sees when they've got loot or when they have killed monsters; it's not perfect. And it does have to be more perfect than it is. Right now, you can equip stuff you shouldn't be able to equip, like two weapons and a shield. And, I didn't really deal with torches correctly. The printed adventure assumes you can just light a torch on your character sheet, but I'm going to have to give the player opportunities to do it before they enter dark rooms, rather than "You are in a dark room -- do you light a torch?".

Also, torches are going to severely disadvantage those who wield two-handed weapons, like bows. T&T rules say enemies get a free shot when you swap weapons, and what happens to the torch? Torch management is a huge thing in the printed adventure, but I find it unfun. Poison management is a huge thing in the printed adventure as well, and while I do support poison, I don't let it be applied, yet. Most of the items that can be activated, I just have the code do it when necessary so that I don't have to implement a mechanism to do it. The healing amulet heals as needed. If you say you light a torch, I believe you have one, and that you're holding it in your teeth or something.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/03/image-7.png" title="The \"Temple of Khazan\", for leveling up" classes="center" >}}

Other things I added to make things easier. You heal a wound every time you move. (You also heal intellectual exhaustion for wizards, every time you move). If you die and you have treasure, then "a mysterious figure" will take one of your treasures and place you back before you made that bad decision where you died.

The game play loop, as I see it, is a player makes a character, buys some basic gear, eventually finds their way to the bar, goes on the adventure, explores a little, thinks the game is unfair as they never make any saving rolls, head back out, play in the arena a little to get xp, goes to the temple and levels up, goes back in, and now they are making some saving throws. Now they are thinking of something maybe they need at the general store for the next run. Now they are drawing a map. And then, they're done.

There's only about 25 actual locations, and now that I have made my own map, I can go back and fix the room descriptions so that the descriptions are consistent for where you are. I have a tool that tells me which locations I have not run through the AI that generates the room descriptions; currently, I have verified that I have been to every location and have a database full of the LLM responses. I'll have to redo them, as some of them are specific to my character, or were captured when I was debugging and don't reflect the current state of the dungeon.

I find I can't afford to have the descriptions generate every time, so I'll do it once more and will not feed context about the current character into the LLM, so it won't know anything about the specific character.

**Next steps**

- Combat -- combat still uses an LLM, and I really, really enjoy having it narrate the ins and outs and ebbs and flows of the combat. I have to turn that into something algorithmic. 

- Overworld -- the town section will be more "roguelike", or more specifically, "LARN-like"; you'll run around town and enter the various places. I have just started work on that.

- Missile weapons -- you technically can bring a bow in, and use it, but it doesn't get the DEX bonus and doesn't ignore enemy weapon defense.

- Wizard class -- okay, this is a tough one. Wizards get all first level spells for free, but only a very few of those are relevant to this dungeon. The lock and unlock spells are useless in the dungeon; the doors lock and unlock with your own actions. There's one place where the detect hidden doors spell would do anything, and you won't know where it is unless you happened to pass the passive saving roll and notice it. Healing is a second level spell, so new wizards won't know it. The only two first level spells that will be useful, a lot, is the panic spell and the missile spell. Wizard Focuses are a thing. 

- Rogue class -- Rogues are a magic-using class in T&T, but they can't learn spells normally. They have to be the target of a Teach spell that can either grant them some random number of usages of a spell, or teach them permanently, but they won't know they learned it until they realize their usages haven't run out. So, I need to give them a way of connecting with a teacher. There's an item in the dungeon that will allow rogues to buy spells from the Wizard Guild. If you have a good stat, you could (according to the printed adventure) farm an infinite supply of these, learn all the spells, and get all the money. I *nerfed* this.

- Packaging -- this will probably be pretty easy, since I'm not using weird game engines. It will start from a batch file; just tested, it works. The packaging will include a Python interpreter and all necessary libraries.

So once all *this* is done, I'll be able to let other people play it.

Anyway. The 'vertical slice' is done. Now I just have to do all the rest of it... and then do the follow-up adventure. I'm hoping that I'll have completed most of the coding in this adventure. (But, I will have to deal with second level spells and potentially game-breaking loot brought from the first adventure).

**Vibe Coding**

Vibe Coding is coding where you ask a LLM to write some code, and then you keep asking it to write more code until your game is done, and at no point do you really worry much about how the game actually works.

I tried that, with this game. I started this game by asking ChatGPT to write a curses-based interface that mimicked an old terminal RPG... and it failed. It couldn't do it. I debugged it by hand and got it working. Then I started building out the underlying classes for the game and... it really didn't work out well. I find as I worked more and more on this, I relied upon LLMs less and less. The current state of the game stretches over a dozen Python files, a database, several YAML files, some CSV files, and all of these together far, *far* outstrip the ability of any current LLM to keep track of the program.

It can still do smaller things. I did have it generate the SQLite3 scripts, and I have made very few changes to those. That sort of isolated library is very much up its alley.

I "vibed" the overworld, but it came out nonfunctional, so I'm tossing that and will just do it myself. It's easier than trying to explain to the LLM just why the code is shit.

So: vibe coding. This is what they want us to be doing at work (in order to require fewer software developers, presumably). It just isn't up to snuff for production code. Maybe someday.
