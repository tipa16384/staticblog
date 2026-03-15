---
date: '2022-03-07T23:12:57-05:00'
draft: false
title: "7DRL 2022 Day 2: Dungeon Room"
categories:
  - "7DRL"
  - "Rogue-Likes"
tags:
  - "Berlin Interpretation"
  - "Rogue-Like"
  - "Tiled"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-2.gif"
cover: "https://chasingdings.com/wp-content/uploads/2022/03/ezgif.com-gif-maker-2.gif"
---

The GIF here is basically all I got done for day 2 of 7DRL 2022. It doesn't look like much, but it's something. Also, by the "Berlin Interpretation", is my game even going to *be *a "Roguelike"?

To GET to that GIF, I had to do a LOT of coding. I loved [the tileset I found](https://opengameart.org/content/isometric-dungeon-tiles-60), but each tile was in its own file, and each tile was 256x512 pixels, which was way larger than the 64x64 I'd used for the "outside" room and for the OG tile system I'd written before I decided to move to Tiled for creating rooms.

So I wrote a program to read in all those files, resize them (to 64x128), and create from them a tileset that I then imported into Tiled. I made a quick little room with the new tiles to try and sketch out a place to meet the Wizard of Yendor (the other critter in the room) and then... it didn't work at ALL with my rendering system.

[![](https://chasingdings.com/wp-content/uploads/2022/03/image-5.png)](https://chasingdings.com/wp-content/uploads/2022/03/image-5.png)Wizard room in Tiled

The previous tileset I'd imported kinda shifts the second layer over the first by a position. This new room didn't do that. Also, the drawing surface for the old tiles was toward the top of the tile; this one was WAY at the bottom.

It took time I really didn't have to make adjustments for this, but I should have an easier time bringing in the next tileset. What I would really like to do is *combine* the two tilesets I've made thus far, but I don't see that happening. If I just opt to *only* use the floor tiles for this set (and I may, as the objects are scaled way too small), then I can do another pass, make them 64x64 and put the drawing surface in the same position, and in this way they should be able to interoperate.

Except I'd also have to upgrade my room loader to handle two tilesets. Tiled does put out all the information I need, but I just simplified things by only using the first tileset I see. For the purposes of 7DRL, I will probably just pass on that for now.

Tonight, the intention was to hand the Amulet to the Wizard and then pass control to the Wintro, but I didn't get that far. So that will be a tomorrow thing.

And then I have to connect the prologue room to the end room, and then start moving them apart.

It's doable, I think.

**The Berlin Interpretation**

It's bizarre that I played the original Rogue itself in college in the early 80s, played a lot of what is considered canon in the Roguelike repertoire, but until yesterday, had never heard of the "[Berlin Interpretation](http://www.roguebasin.com/index.php/Berlin_Interpretation)" that is the best guide for how Roguelike something is.

The general feeling is that the two most important roguelike indicators are procedural dungeon generation and permadeath. So, I'm 50% there. When whatever character you are playing dies in YATA, the game is over. As for procedural dungeon generation, I am not even going to attempt that this time. There's nothing that stops me from writing code that generates a Tiled-like level, but it's time I don't have and so I cut out random map making pretty early.

The other high value factors are:

- Turn-based: Yes, YATA is turn-based- Grid-based: Yes, YATA is grid-based- Non-modal: Yes, probably- Complexity: No, this is a no.- Resource Management: Probably not.- Hack'n'slash: Lots of combat? Probably not. Some combat, yes.- Exploration and discovery: Probably not.

Based on the other entries I have been seeing, if some of them are roguelikes, then You Are The Amulet definitely qualifies. I think I have enough of the factors here to qualify, maybe as a "rogue-*lite*" if not a "rogue-*like*". We'll see how the judges feel at the end.
