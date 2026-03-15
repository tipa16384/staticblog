---
date: '2024-05-09T07:00:00-05:00'
draft: false
title: "ADVENT: Twisty Passages, All Alike"
summary: "A pirate stole our treasure! Time to steal it BACK. But first, we have to find our way through one of the most notorious mazes of all time..."
categories:
  - "Adventure"
  - "Text Adventure Game"
tags:
  - "Colossal Cave"
  - "Colossal Cave Adventure"
  - "Pygame"
featured_image: "https://chasingdings.com/wp-content/uploads/2024/05/cc-pirate.png"
cover: "https://chasingdings.com/wp-content/uploads/2024/05/cc-pirate.png"
---

I think someone who knew what they were doing could finish ADVENT in half an hour at most. It's taken me days. I lose points every time I save, but I'm always getting so excited about finally replaying a game that meant so much to me when I was a kid; I just want to make it special.

I could say that I might never play it again, but that's not the case -- I'm playing it again right after this one, the graphical, 3D version.

In yesterday's episode, the pirate, who had been stalking us through the Colossal Caves, finally managed to catch us by surprise. If we'd turned toward him as he entered our location, he would have been startled, and scurried off. As it was, though, we had no idea he was nearby. When we dropped the treasure we were carrying to fight him, he stole it all and ran off to hide it in his treasure chest deep in a maze.

It would be perilous to go into the maze without a map.

Springy!

A couple nights ago, I was trying to write a physics simulation that would move rooms around on a map so that rooms close to each other would appear close to each other, saving me the time of doing it. That didn't work out so well. Then I had the bright idea to see if I could just find some physics package that would do all the hard stuff *for* me. And there was!

PyMunk is a 2D physics package for Python. Super simple to use; you add objects to the scene, tell how they are connected, and let fly. I could have added my own graphics in, but I just let PyMunk handle the drawing just to see how things looked.

Well, it looks entirely unusable. It looks cool, but unusable. Even with lines connecting things instead of springs, and circles with the room code in them instead of nothing, it would be unusable.

Next, I thought I wasn't really that interested in pretty pictures. I just wanted to know how things were arranged, left to right, up to down. I could then print that out and we'd be done.

Python has a package -- several, really -- for doing graph projects. I chose **networkx**, and put in some simple relations and watched as it cheerfully arranged them correctly and easily, in more or less the correct orientation that would make a useful map.

I then added the "all alike" maze, and...

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/image-6.png" title="During handling of the above exception, another exception occurred..." class="align-center" >}}

Rooms point to themselves. Rooms are mutually to the south or above each other. There was no way to connect the rooms of the maze in any physically possible way. Such is the teaching of ADVENT.

So, I plugged the maze into last night's code, and laboriously marked it up with the correct directions.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/alikemaze-1024x460.png" title="\"ALL ALIKE\" Maze" class="align-center" >}}

There's at least two entrances into the maze; there may be more. The program I wrote to rip the rooms from the ADVENT YAML file tends to forget things around the edges. But this was enough.

The stalactite (middle, second row) is easily found, but can drop you into one of three rooms. This isn't terrible; if you can go north, you're almost there. If you go up, then you're in that same place. Otherwise, go west. From there, it's N, E, E, NW.

I didn't think this through clearly, though, and I opted to go from the west end of the Hall of Mists. But, going west from the Hall of Mists brings you to the fissure puzzle. I had to do some crawling around in a parallel tunnel to get to the correct location, and I dropped into the maze pretty far from the pirate's hoard. Probably burned a lot of lamp to finally get there.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/deadend-1024x699.png" title="The pirate's treasure chest is here!" class="align-center" >}}

We found all our treasures, and the treasure chest itself is a treasure! The emerald is particularly important, as I don't believe you can safely get one of the other treasures without it. If you are holding the emerald in the "Y2" room and say "plover", you get teleported to the Plover Room where you got the emerald. But unlike the first time, where you had to drop everything, including the lamp, in order to squeeze into the room, you now *have* the lamp and can go to the next room and grab the platinum pyramid. Then "plover" back to "Y2", and "plugh" back to the building to deposit the stash.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/05/treasures-so-far-1024x702.png" title="Treasures so far" class="align-center" >}}

And that's where I left off. MANY more treasures to get. I think tomorrow, I'll go have a talk with a troll and make a new friend along the way.
