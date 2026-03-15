---
date: '2022-03-02T07:54:11-05:00'
draft: false
title: "7DRL: Building an Engine -- and it ends."
categories:
  - "7DRL"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/03/deathscreenshot.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/03/deathscreenshot.png"
---

Working through my checklist of "must have" features for the game.

I have a checklist of the bare minimum features I need to implement in the game engine before I can even think of implementing a real combat system. They are:

- T~~he game *must* begin~~- The game *must* have a win condition- ~~The game *must* let you lose~~- ~~The game *must* let you defeat enemies~~- ~~The game *must* let you be defeated by enemies~~

Yesterday's update covered the introduction to the game, and how I wrote a dispatcher to bring the player from the introduction and into the main game. At that time, the introduction was written entirely in code, but that was a problem.

Ideally, there will be no Python code necessary to write the 7DRL game, or future games built on the engine. Anything specific to a certain game needs to be in the YAML. So, my first task was to move the intro to the YAML.

This is how those old, great LucasArts adventures worked. Maniac Mansion, Monkey Island and all them were written as [SCUMM](https://en.wikipedia.org/wiki/SCUMM) files. Even back in the early 80, Infocom was writing their games in[ ZIL -- the Zork Implementation Language. ](https://en.wikipedia.org/wiki/Infocom#:~:text=Infocom%20games%20were%20written%20using,machine%20called%20the%20Z%2Dmachine.)More recently, [RPG Maker](https://en.wikipedia.org/wiki/RPG_Maker) allows creation of Legend of Zelda and Final Fantasy-type games. All three of those allow fairly sophisticated programming without being tied down to one sort of computer or computer language.

From the start, though, I knew I wanted to write my own game engine, but I think it's important to look back on what others have done.

[![](https://chasingdings.com/wp-content/uploads/2022/03/deadmog.png)](https://chasingdings.com/wp-content/uploads/2022/03/deadmog.png)Dead Mog :-(

With the intro written, and a way to kill the player written, I just needed a couple more things to get death finished.

First, I needed to allow actors the state of being alive, so I could cruelly take it away. I went back to their sprite files and got their death sprites -- some of them had corpses in all four directions, some I had to simulate with flip and mirror. I talked about flags recently; since "alive" was a new flag, I had to ripple that through the code. Actors without the alive flag couldn't attack, couldn't move, couldn't path find, couldn't animate, couldn't be attacked. If they happened to be the player, then they couldn't respond to movement keys, or the special keys to swap to another actor ("P") or kill all NPCs in the room ("K"). (Those debugging keys won't be in the final game).

*Every* new flag will have these sorts of side effects. That doesn't make implementing them any less necessary. It does mean I have to be cautious about which ones I take up.

With that done -- and after adding a short pause when the player dies so that they could see their corpse and reflect on the mistakes that brought them to this disastrous end -- I cloned the intro module into an outro module in the YAML, changed up some text and assets to make it look different, *et voilà*, a whole new part of the game done without extra coding.

One last checkbox item before I can start expanding on the combat and item system. Having a win condition. The rules say that this must be encoded in the YAML. I know what the win condition will be in my 7DRL entry, but I can't code that yet. But my solution, whatever it turns out to be, should be able to handle both the game engine demo code (probably just killing all the NPCs), *and* the mystery win condition of the actual game (which, spoiler alert, will not be killing a boss or anything -- sorry).

But, that's a problem for future Tipa to solve.
