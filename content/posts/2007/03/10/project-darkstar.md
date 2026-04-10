---
date: '2007-03-10T12:41:20-05:00'
draft: false
title: "Project Darkstar"
author: "Tipa"
disqusIdentifier: "2007/03/10/project-darkstar"
summary: "Could this be the first seed of the Metaverse?..."
categories:
  - "MMORPG"
relatedPosts:
  - url: "/2026/03/25/everquest-3-is-officially-dead/"
    title: "EverQuest 3 is officially dead."
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/03/Screenshot-2026-03-25-213122.png"
  - url: "/2026/03/11/dune-awakening-finished-chapter-3/"
    title: "Dune Awakening: Finished Chapter 3"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/03/Screenshot-2026-03-11-073510.png"
  - url: "/2026/02/04/erenshor-rising-shadows-launched/"
    title: 'Erenshor "Rising Shadows" launched!'
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/02/20260204080313_1.jpg"
  - url: "/2026/01/24/dominus-automa-an-idle-mmo-for-busy-dads/"
    title: "Dominus Automa: An Idle MMO for Busy Dads"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/01/dominusautoma.png"
---
Could this be the first seed of the Metaverse?...
<!--more-->

Could this be the first seed of the [Metaverse](http://en.wikipedia.org/wiki/Metaverse)?

Sun has given their [Project Darkstar](https://games-darkstar.dev.java.net/) to the open source community. Project Darkstar is a generic backend that can support any sort of game or other collaborative activity transparently allocating servers and managing data so that if your game is meant for 5 players or 5,000, if you've built it on Darkstar, your game can handle it.

I was asked in an interview how I would write an application that could support thousands of simultaneous users. Aside from just having a server dedicated to redirecting requests to other servers to balance the load (and then the bottleneck would be the database! So we'd have to replicate and sync that as well!), I didn't have a clue (and I only thought of that solution -- which in retrospect is the obvious one -- after I'd left the interview). Now I'd just say, "Well, I guess I'd take a look at... dum duh de dummmmmmm... Project Darkstar!" to their looks of shock and amazement.

From their [announcement](http://research.sun.com/spotlight/2006/2006-03-20_Darkstar.html):

> Sun Labs aims to change that. Project Darkstar, released publicly at the 2006 Game Developer Conference in San Jose, California, is harnessing Sun's expertise in development tools, Java technology, and massively scalable back-end infrastructure to simplify the process of developing games that can be deployed on a massive scale to players using virtually any client device. A freely downloadable, early access SDK for writing client-side and server-side code is now available from Sun Labs at [http://www.projectdarkstar.com](http://www.projectdarkstar.com/).
