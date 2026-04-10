---
date: '2010-03-06T16:16:09-05:00'
draft: false
title: "7DRL: Milestone #1"
author: "Tipa"
disqusIdentifier: "2010/03/06/7drl-milestone-1"
summary: "I started working on my entry to the annual 7DRL (7 Day Rogue-like) game design challenge today. I've been working on algorithms for the game..."
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
  - url: "/2010/03/12/7drl-world-of-roguecraft-day-5/"
    title: "7DRL: World of Roguecraft, Day 5"
    thumbnailImage: ""
  - url: "/2010/03/09/7drl-day-3-inventory-messages-improved-targeting/"
    title: "7DRL Day 3: Inventory, Messages, Improved Targeting"
    thumbnailImage: ""
---
I started working on my entry to the annual 7DRL (7 Day Rogue-like) game design challenge today. I've been working on algorithms for the game...
<!--more-->

I started working on my entry to the annual 7DRL (7 Day Rogue-like) game design challenge today. I've been working on algorithms for the game for the past week; today I took the algorithms for map generation and room connectivity and put them into real code.

It turned out pretty much exactly as I imagined -- I am going for a game that looks like it's being played with toys on a map drawn with marker on graph paper. When I got it first working, I realized I needed a way to show where you had already been, so I draw visited rooms in a muted shade to give the player SOME idea when they've cleared the map.

I haven't started writing the UI yet. I have a lot to do before I get to THAT point.

Next step: Adding some monsters -- the player is already a special case of a monster, so most of the code is already written. I just need to add a *little* AI. I won't be adding combat quite yet.

After the monsters, I am going to add something to get to win the game. Yes, the game will initially be won by just wandering around the single map until you come across the object that lets you win. This gives me a full (though very boring) game. After THAT, I just keep adding things until it becomes fun.
