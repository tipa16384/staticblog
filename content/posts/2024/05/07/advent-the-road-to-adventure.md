---
date: '2024-05-07T07:00:00-05:00'
draft: false
title: "ADVENT: The Road to Adventure"
author: "Tipa"
disqusIdentifier: "2024/05/07/advent-the-road-to-adventure"
summary: "You can draw a direct line from Crowther and Woods' \"Adventure\" to MMOs such as EverQuest. I'm going to be playing it all the way through... twice."
categories:
  - "Adventure"
  - "Text Adventure Game"
tags:
  - "Colossal Cave Adventure"
relatedPosts:
  - url: "/2024/12/28/the-best-of-2024-adventure-games/"
    title: "The Best of 2024: Adventure Games"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/12/adventurebanner.png"
  - url: "/2024/05/12/advent-colossal-cave-3d/"
    title: "ADVENT: Colossal Cave 3D"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/cc-troll2.png"
  - url: "/2024/05/11/advent-seasoned-adventurer/"
    title: "ADVENT: Seasoned Adventurer"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/cc-troll.png"
  - url: "/2024/05/09/advent-twisty-passages-all-alike/"
    title: "ADVENT: Twisty Passages, All Alike"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/cc-pirate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/cca-banner.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/05/cca-banner.png"
---
You can draw a direct line from Crowther and Woods' "Adventure" to MMOs such as EverQuest. I'm going to be playing it all the way through... twice.
<!--more-->

I've mentioned finding [the original ADVENT game](https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) (as it was called on my university's PDP-10) and having it transform the trajectory of my life. It's such an influential game, that I'm really surprised I haven't played it since my college days.

That changes now :-)

I'll be playing through it twice. The first time, I'm going to play it as closely as possible as I did back in the early 80s -- with text and maps. My original maps are probably long gone, though I know I was saving them for a long time.

My second playthrough will be with[ Ken and Roberta Williams' graphical conversion](https://www.colossalcave3d.com/). There's even a VR version; I won't be playing that, though.

At the end of this, I'll be thoroughly adventure'd out. And it will be nice to see just how close the Williams' stayed to the puzzles in the original game.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/05/image-2-1024x707.png" title="Adventure!" classes="center" >}}

**Challenge 1: Get it running**

The original ADVENT was written in FORTRAN for the DEC-10 mainframe operating system. I wasn't really that interested in tracking down those original sources and getting FORTRAN running on my PC. I mostly just wanted it to run.

I think it might be available commercially, but some casual surfing brought up [Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond)'s *authorized* port of the last *original* ADVENT version to the C language, [open-adventure](https://gitlab.com/esr/open-adventure/tree/master). A lot of companies built upon the original game and made some money off of it, more than the original authors ever did. Many other developers just adapted the game to their design.

If I was going to have the authentic ADVENT experience, I'd want open-adventure.

Downloading the source was easy. Getting it to compile and link was much, much harder. In theory, a potential player would be running in Unix or Linux and have all the build tools available. Me, I'm using WSL on Windows 11 to run a Ubuntu shell with no particular development environment. So, I had to make one.

I spent a couple fruitless hours trying to get their Makefile working before I just started running the commands by hand until I found and fixed the actual issue.

Yay! We were outside a building in a clearing in a forest! But that wasn't going to be enough.

**Challenge 2: Make it look retro**

There's a few projects that claim to provide the legit experience of working at one of those old Lear-Siegler ADM-3A or DEC VT-52 dumb terminals, but WSL doesn't provide a graphical environment in the base package, and I had zero success bringing one up. So I started working on making the default terminal window look... ~~worse~~. Older.

I downloaded the old VT52 and ADM3A fonts, and tried those out. (Screenshot above uses the VT52 font; note that 'g' and 'y' don't descend beneath the font baseline). WSL provides a setting to add scanlines, like an old terminal, to the screen. Yes, please, I think I will. It also allowed my to set the background to an image. I had Midjourney generate an image of one of the early puzzles -- a dragon sleeping on a Persian rug -- and put that in.

Perfect. Instantly brought me back forty years.

Now, playing it.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/05/image-3-1024x926.png" title="PARTIAL map" classes="center" >}}

**Challenge 3: Making a map**

I'm not sure where I got the idea that I would just rip through this based on memories decades old. I mean, there was *no way*. It didn't take long before I started a spreadsheet with all the rooms I encountered, their contents, connecting rooms, etc.

That spreadsheet was impossible to use, so I went to Inkscape and started diagramming the rooms. Better, but still not good enough.

There is a puzzle in the game that challenges you to do a thing, run to a certain spot some distance away, come back, and do another thing. I got lost, even with this map. Dwarves killed me. It was awful. I was traumatized.

I said, I can fix this with software.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/05/image-4.png" classes="center" >}}

I read awhile back about this program that can simulate folding proteins in 3D space. It works by trying to find the lowest energy among all the different molecules involved. That was what I needed -- except in 2D. I needed to make a connection map that would have rooms that are close to one another be close to one another on the map, with connection lines so that I could quickly move from one location to another. I'll worry about the keywords required later. Just interested in the actual connections.

The program I wrote balances the attractive force of rooms with their connections with the repulsive force of other rooms in general. It keeps on calculating this as if the rooms were on springs for 2,000 iterations before it ends.

I only put a few of the rooms in the map I drew in here as a proof of concept, and even the map I drew only has a fraction of the total number of rooms.

**Challenge 4: Making a complete map**

I don't really want to log each room individually, and I'll also want to start logging the treasures in the rooms and how you get from one room to another. Thankfully, this work has mostly been done for me.

Because. I have the game's source code.

The original ADVENT kept all of its text and room connections in a long, long text file. "open-adventure" keeps them in a YAML file, and wouldn't you know it, a simple Python program can read that file and log all the rooms, their contents and their connections, *for* me.

This is getting dangerously close to cheating. Mapping the dungeon is at least 50% of the gameplay. The rest is execution -- you get points for getting treasures (and lots of points for getting all of them), and you get points for doing it quickly (infinite points for doing it faster than the game's author).

I'm not shooting for any records, though the game can be simplified to a traveling salesman problem, probably. Having to have certain items in your very limited inventory space adds a wrinkle. But I'm not worried about doing it fast. I remember the ending from the original game (although not how I got there). When I see that -- I'm done.

I have been doing a lot of delves into the game to build the legit map and to solve some of the puzzles. I remember a few from back in the day, but by no means all of them. It's gonna be fun.

I cannot *wait* to play the graphical version!
