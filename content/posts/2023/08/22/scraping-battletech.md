---
date: '2023-08-22T07:00:00-05:00'
draft: false
title: "Scraping BattleTech"
author: "Tipa"
summary: "What was that old saying? \"Information wants to be free\"?"
categories:
  - "3D Printing"
  - "Blaugust"
  - "Blaugust 2023"
tags:
  - "Battletech"
  - "Frostgrave"
  - "Warhammer"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/scapingbattletech.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/scapingbattletech.png"
---
What was that old saying? "Information wants to be free"?
<!--more-->

We're mostly board gamers in this house. Sure, we play and enjoy a lot of video games. But board games are a passion. I occasionally blog about what we're up to, and I should do more of that.

But what none of you know, probably, is that we would very much like to be into the tabletop miniatures games. These are games like Warhammer 40K, Star Fleet Battles and other games of similar ilk where you bring your armies of miniatures and set them across the table from someone else's army.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/IMG_2177-1024x768.jpg" title="Part of my Frostgrave army, AKA \"the good guys\"" classes="center" >}}

The first game of this sort we played was Frostgrave, for which I printed -- and painted -- a metric crap tonne of terrain. I used mostly the minis I'd printed after playing Octopath Traveler for my army, with a special custom character for my main wizard. Not sure what units my boyfriend played with. I may have had too much terrain printed for our small kitchen table, actually.

The scenario was fun, don't even remember who "won" but it wasn't really important. I was disappointed that we only played that one time.

Time passed and we slowly started accumulating Warhammer 40K, and I set out to learn the rules and enough about the lore to decide upon a faction to play. I finally decided upon the warrior nuns, the Adepta Sororitas. I haven't really finished or started to assemble or paint an army. It's such a huge task, that I was waiting for my partner to start with his, but recently, his attention has turned to BattleTech.

He's making quite an army. At least one night a week, he puts on his magnifying glasses, fills his airbrush, and starts painting. So I think this is going to be the real thing. (I'll post his army when it's done, as he stopped blogging years ago).

He showed me, last night, an article he'd found on Reddit about a site that had information about all the 9,000 or so units that have made an appearance in BattleTech's 30 year history. It's... it's a lot. Most of them are variations of some other unit, but still, they are distinct enough that they have their own base stat sheets.

My BF wanted to grab all the information about all these units from that site and drop them into a CSV file, so that he can do some data analysis and figure out what his optimal army should look like. The article included Python code, but it was missing some key elements -- like, how to get the list of all the units.

I took a look and figured I could do the whole thing on my own, and so I did. I used one Python library grab the HTML page for a unit, another to parse the HTML, and the CSV package to write it all out. It's a brute force approach, just generating unit numbers sequentially and seeing if they exist. If not, try the next one.

It took a little debugging, but it's been churning for the past couple hours while I played Palia.

Anyway, tl;dr: coding, it's fun.

*The scraping wasn't complete when I wrote this. Now it is; [here's the GitHub repo](https://github.com/tipa16384/battletech) with both this Python source code and a CSV of the BattleTech stats. *
