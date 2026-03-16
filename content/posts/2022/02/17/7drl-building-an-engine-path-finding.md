---
date: '2022-02-17T23:30:32-05:00'
draft: false
title: "7DRL: Building an Engine -- Path Finding"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/02/17/7drl-building-an-engine-path-finding/"
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
summary: ""
description: "Desc Text."
tags:
  - "7DRL"
  - "A*"
  - "Dijkstra"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot-2.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/02/screenshot-2.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Path finding is central to all rogue-likes. If an enemy can't *find* you, they can't *fight* you... and that wouldn't be any fun. Tonight, I go over Dijkstra's famous pathfinding algorithm, the differences between that and A*, and how I implemented them in the engine.

Once again, you can play the engine as it currently exists by [clicking this link](https://trinket.io/pygame/86b9301490?outputOnly=true) and then clicking the "Run" button near the top of the window. New for today: pressing the F5 button on the keyboard creates a new, random map. I don't pretend this is a game -- the game has to wait for 7DRL to officially begin.

Before I got started tonight, I had to do a little more refactoring. Terrain is now managed by a terrain factory -- I tell it what type I want, and it hands me back a terrain all sliced up and measured from the sprite sheet. I also did as promised earlier and moved the Actors -- anything that moves -- into the main game object. Now the entire state of the game is in one place.

Few monsters in a roguelike are content to stay in one spot for long. Some fall asleep now and then, but usually they are on the prowl, patrolling the dungeon and investigating strange clanking noises and *is that an adventurer?*

Path finding forces monsters to follow the same movement rules as adventurers. To get to a spot, they have to go through all the spots between their current location and their destination, and if something's in the way, they will have to figure out how to go around.

In 1956, mathematician [Edsger Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) was drinking coffee at a café and came up with the simple algorithm to find the shortest path between any two points while musing on how to find the shortest route from Rotterdam to Groningen.

The algorithm is simple and elegant. Any particular place you might stop on the way is considered a node; the route from one node to another is called an edge; and the cost to get from one node to another is called the weight. That cost might be money, or time, or distance, or any other way of determining if one route is better than another.

You make two lists; a list of open nodes, which are potential places to travel from where you are now, and a list of closed nodes, which is a list of places where you have been. To find the best path, you choose the node from the list of open nodes with the least accumulated weight, travel there, add it to the list of closed nodes, then add to the list of open nodes all the nodes to which you could travel from your current spot, adding their weights to the accumulated weight. Stop when you arrive at your destination.

This is provably the shortest path from *A* to *B*. The most recent Advent of Code had at least three puzzles that could be solved this way. Here's the specific pathfinding code from the Actor object. The "heapq" is Python's priority heap implementation -- it always returns the cheapest open node. "bad_spaces" are positions which are occupied by something else. If the Actor finds itself in a good position at the start, it returns without setting a path.

`    def pathfind(self, player, bad_spaces):
        if self.room != player.room or self.moving:
            return

        heap = list()
        heapq.heappush(heap, (0, self.pos, []))
        closed_nodes = set()
        while heap:
            dist, pos, path = heapq.heappop(heap)
            if self.good_pos(pos, player.getPos()):
                if len(path):
                    self.move_to(*self.pos, *path[0])
                return
            if pos in closed_nodes:
                continue
            closed_nodes.add(pos)
            for dx, dy in __facing_deltas__:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos in closed_nodes:
                    continue
                if not self.in_room(*new_pos):
                    continue
                if new_pos in bad_spaces:
                    continue
                heapq.heappush(heap, (dist+1, new_pos, path + [new_pos]))
`

The [A* (A-star) algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) is a variant of Dijkstra's. It's identical, except when adding a new open node, you add the sum accumulated weight and a value that represents the distance of this node from the final destination. This tends to favor nodes that are headed generally in the right direction. Dijkstra will happily offer up nodes in the entirely wrong direction if it's cheap to do so. Both algorithms will return the shortest path; but if the A* value is a good indicator of the effort required to get to the destination, it will find the shortest route more quickly.

I chose to just go with Dijkstra, as my rooms will not be placed in some larger map; they will be just connected with exits and entrances and they all have their own coordinate system. A* would still work well within the room, but that search space is so small that there's no difference between that and Dijkstra.

In the demo (as it is today, anyway), you can see the NPCs walking around to get in their best positions. In the actual game, they will only move when you move, but for purposes of getting this working, I let them move as much as they like.

They don't all end up pinned to the player, though. I've set up the Actors so that they can define what a destination node means to them. The archer wants to be between three and five squares away, so she can shoot an arrow from range. The mog knight wants to be on the same row or column as the player, so that he can do a charge attack. The templar wants to be right in your face. When Babus is an NPC, he just wants to stay four squares away so that he can cast spells.

Since each Actor inherits from the main class, it can override the default destination algorithm that Babus uses, with one of their own, without affecting any other Actor, as they are totally separate blocks of code. It's in this way that I'll be making every creature the adventurer encounters a unique experience.

The next big thing is multiple rooms, and after that, level creation. Right now pathfinding only works in the current room, so I'll have to revisit that again once I have a map where it makes sense.

Tomorrow is probably Horizon: Forbidden West, though...
