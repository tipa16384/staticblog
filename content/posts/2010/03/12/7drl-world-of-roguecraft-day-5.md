---
date: '2010-03-12T00:27:27-05:00'
draft: false
title: "7DRL: World of Roguecraft, Day 5"
author: "Tipa"
disqusIdentifier: "2010/03/12/7drl-world-of-roguecraft-day-5"
summary: "Monday evening, I understood what my game wanted to be about. Tuesday, I realized that the game was horribly, horribly flawed. Coming in, all I..."
categories:
  - "7DRL"
  - "Other Games"
relatedPosts:
  - url: "/2010/03/24/7drl-world-of-roguecraft-slightly-more-fun-than-clipping-your-nails/"
    title: "7DRL -- World of Roguecraft: Slightly more fun than clipping your nails."
    thumbnailImage: ""
  - url: "/2010/03/13/7drl-day-7-content-content-content/"
    title: "7DRL Day 7: Content, content, content"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/Fullscreen-capture-3132010-35853-PM-480x384-1.jpg"
  - url: "/2010/03/09/7drl-day-3-inventory-messages-improved-targeting/"
    title: "7DRL Day 3: Inventory, Messages, Improved Targeting"
    thumbnailImage: ""
  - url: "/2010/03/07/7drl-day-2-monsters-targets-items/"
    title: "7DRL Day 2: Monsters, Targets, Items"
    thumbnailImage: ""
---
Monday evening, I understood what my game wanted to be about. Tuesday, I realized that the game was horribly, horribly flawed. Coming in, all I...
<!--more-->

Monday evening, I understood what my game wanted to be about. Tuesday, I realized that the game was horribly, horribly flawed. Coming in, all I really knew I wanted to do was the graph paper-like room generation, and I hoped the rest of the game would occur to me as I was doing that.

And it did -- it just turned out to be a different game than the one I was writing.

So my 7DRL is ending up as a game very difficult to extend. By making it graphical, and not basing it off an existing Rogue-like engine, I had to spend a LOT of time on just the basic mechanics. Writing a separate class for every monster and weapon seemed like a good idea at the time -- Swords inherit from Melee Weapons inherit from Weapons inherit from Object. Though that is kind of how you would think you would want to implement stuff in an object-oriented language like Python, I think it limited me.

Well, with an evening and a morning still left to go, perhaps it's too early to do a post-mortem on the project. The unhappy fact is that while I would love to finish this game, to do it properly I would have to rewrite it from scratch, and I just don't have the time. Chalk this one up to a learning experience.

Day 5 of my 7DRL was all about adding combat. My penalty for dying is not harsh; you just pop back in the upper left corner, and the monsters leave you along for a little while.

The damage done by monsters is sometimes fractional because your wielded weapons add a certain amount of physical and magical damage resistance. Wands tend more toward magic resistance, and swords the physical. The idea is that, since you don't gain xp or levels in this game, you would slowly build up nearly 100% resistance in certain areas, so when the dragon came at you and did 1000 points of damage, you'd resist 99% of it. Woe be she who drops her sword without another one handy.

Oh yeah, almost forgot to mention: the screen capture utility on my Linux box kept crashing for some mysterious reason, so I ran it on my Windows machine and captured the game with Windows Media Encoder, which worked really well! So, here's the vid of my 7DRL working on Windows Vista :)
