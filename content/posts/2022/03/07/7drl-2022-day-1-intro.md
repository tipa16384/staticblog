---
date: '2022-03-07T06:54:53-05:00'
draft: false
title: "7DRL 2022 Day 1: Intro"
categories:
  - "7DRL"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/amuletintro.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/03/amuletintro.png"
---

Yesterday was the day I officially started the 7DRL 2022 "Build a Roguelike in 7 Days" challenge. I can now reveal the game concept....

7DRL officially started Saturday, but [the rules say](https://itch.io/jam/7drl-challenge-2022) you can choose any seven days, as long as the submissions are in by the 13th. So I spent Saturday working on the game concept some more and started the official coding on Sunday.

[![](https://chasingdings.com/wp-content/uploads/2022/03/gamelogo.png)](https://chasingdings.com/wp-content/uploads/2022/03/gamelogo.png)

The game is "You Are the Amulet". The original Rogue game had the adventurer delving through fifty levels of a deadly dungeon to wrest the fabled Amulet of Yendor from the evil grasp of the Wizard. They then ascend the dungeon and escape, becoming an "Ascended".

My story picks up after the Adventurer escapes the dungeon, finds out that the fabled Amulet is just a bit of junk, and tosses it aside.

But, the Amulet of Yendor is alive, and it wants to go home, so it patiently bides its time, hoping some innocent passerby will find it and put it on, and then come under the control of the Amulet.

Anything that wears the Amulet will become the player, so the game will have the player using the Amulet to possess creatures in order to pass through the dungeon. However, the true win condition will be if the original player character is the one to hand the wizard the amulet.

Anyone who has followed the progress on the engine can see how very different the actual game is. I spent Sunday first fixing a lot of the bugs -- the terrain stuff no longer has occlusion issues with the player. Mostly.

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-2.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-2.png)Layout

**Intro and Layout**

I used [Wombo.art](https://www.wombo.art/) to generate a lava-filled backdrop for the intro screen, then used [Huemint](https://huemint.com/brand-3/) to generate a color palette based off those colors. I found some free fonts to use for the title and the little monster silhouettes along the bottom. My concept was that the Amulet would form the "Y" in "You", and I played around with that until I found something I liked.

One of the issues the game engine had was message display. For the actual game, I wanted to split everything into panes. This is actually exactly how I did it back the first time I did 7DRL. I settled on a 1024x768 pixel screen. This is outside Trinket.io's screen area, but I'll worry about backporting it to Trinket once I am done.

**Prologue**

Once through the intro, I wanted the player to start in a safe room, where they could learn the basics before heading into the dungeon. This was also going to be where they learn the objective of the game. So for this, I headed back into [Tiled](https://thorbjorn.itch.io/tiled) to create a home for the Amulet to be found.

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-3-1024x648.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-3.png)Tiled

The tile set is the one I used often in the engine building phase. I spent so much time trying to integrate this into the game engine, and it is still not 100%. The rocky terrain really emphasized the sprite occlusion layer issues I was having Friday, so I took some time to fix those before moving on. In the video above, I move the player sprite into a lot of problem areas just to be sure everything is working now.

[![](https://chasingdings.com/wp-content/uploads/2022/03/yata-screenshot.png)](https://chasingdings.com/wp-content/uploads/2022/03/yata-screenshot.png)Game in progress

Now for the coding. I wrote a Layout manager that looks at the game state and displays the game, removing this work from the existing game engine. I added the concept of Items that could appear in the world and then move on to become inventory items. I grabbed the icon for the Amulet of Yendor from the standard Nethack tile set (after I made some small alterations to make it fit better in my game), added code to pick up and put on items, added an inventory (and found out I just don't really have sufficient space there), ripped Ritz from Final Fantasy Tactics Advance (originally the player could have chosen to start with either Marche, FFTA's protagonist, or Ritz, but I removed that bit from the plan).

I needed to guide the player to find and put on the Amulet, so I took the dialog from Portal's turrets when they are aware of you but you are not within targeting range and had the Amulet use one of the phrases at random until the player finally gets to Amulet, where they are instructed how to pick up the Amulet and put it on.

This brings them to the Plotro (we have Intro and Outro and Wintro, and now we have a Plotro) where the player is given their mission, and that's where the game ends for now. Tonight, I will start work on the final room of the dungeon and the win scenario. My goal has always been to write the beginning and the end, and then use the rest of the week to move the beginning and the end further apart. I still have to add a real combat system :-(

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-4.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-4.png)
