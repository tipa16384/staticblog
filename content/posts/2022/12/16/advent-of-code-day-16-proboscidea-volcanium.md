---
date: '2022-12-16T23:17:07-05:00'
draft: false
title: "Advent of Code Day 16 -- Proboscidea Volcanium"
author: "Tipa"
disqusIdentifier: "2022/12/16/advent-of-code-day-16-proboscidea-volcanium"
summary: "Trying to save elephants trapped in an erupting volcano? Sure. My solution worked for my input but not that of other people's, so let's try something a little different."
categories:
  - "Advent of Code"
  - "TV Recaps"
tags:
  - "24"
  - "Elephant"
  - "Gpt-3"
  - "Python"
relatedPosts:
  - url: "/2022/12/21/advent-of-code-day-21-monkey-math/"
    title: "Advent of Code Day 21 -- Monkey Math"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-21-21.48.47-A-large-group-of-monkeys-shouting-at-a-woman-wearing-a-Christmas-stocking-cap-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/17/advent-of-code-day-17-pyroclastic-flow/"
    title: "Advent of Code Day 17 -- Pyroclastic Flow"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-17-22.26.37-An-elephant-wearing-a-Christmas-stocking-cap-looking-at-a-giant-statue-of-a-Tetris-game-in-a-cave-lit-with-lava-by-Bob-Eggleton-detailed-and-intrica.png"
  - url: "/2022/12/04/advent-of-code-day-4-camp-cleanup/"
    title: "Advent of Code Day 4 -- Camp Cleanup"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-04-18.27.11-Several-Christmas-elves-doing-chores-around-a-campsite-in-the-jungle-painted-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2024/12/07/advent-of-code-2024-the-first-week/"
    title: "Advent of Code 2024: The First Week"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/12/DALL·E-2024-12-07-11.54.46-A-Tolkien-inspired-scene-depicting-graceful-elves-in-a-Tolkien-inspired-setting-repairing-a-rope-bridge-over-a-serene-river-surrounded-by-lush-vibra.webp"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-16-23.05.05-A-publicity-photo-of-Jack-Bauer-from-_24_-leading-an-elephant-through-a-lava-tube-lit-up-with-the-red-glow-of-molten-magma.-Tubes-and-pipes-line-the-l.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-16-23.05.05-A-publicity-photo-of-Jack-Bauer-from-_24_-leading-an-elephant-through-a-lava-tube-lit-up-with-the-red-glow-of-molten-magma.-Tubes-and-pipes-line-the-l.png"
---
Trying to save elephants trapped in an erupting volcano? Sure. My solution worked for my input but not that of other people's, so let's try something a little different.
<!--more-->

Jack Bauer: (sitting at his computer) "Ok, I've got the data from the sensors. It looks like there's a network of pipes and pressure-release valves here. If we open these valves and follow the tunnels, we might be able to stop the terrorist threat."

(starts typing on his computer) "First, I need to import some libraries to help me process this data."

(types quickly)

(pauses, then speaks into his headset) "Chloe, I'm going to need you to send me the data file for the network of pipes and pressure-release valves. I need to create a class for the nodes in this network."

(waits for Chloe to send the file)

(types)

"Ok, got it. Now I'm creating a class for the nodes in the network."

(types)

"Now I'm reading in the input and creating the nodes for the network."

(types)

"Now I need to create a function to traverse the network and find the most pressure we can release."

(types)

"And now I can use this function to find the most pressure we can release in 30 minutes, or in 26 minutes if we take into account the time it will take us to get the elephants out."

(types)

"Alright, running the function now. Chloe, I'm going to need you to keep an eye on the timer. We've only got 30 minutes before the terrorists launch their attack."

(stares intently at the computer as it processes the data)

(exhales deeply) "Ok, got it. The most pressure we can release in 30 minutes is X. And if we factor in the time it will take us to get the elephants out, the most pressure we can release in 26 minutes is Y."

(pauses) "Chloe, send this data to the field team. They need to follow these routes and open these valves to release the most pressure possible. We've got to stop this attack before it's too late."

**Python 3.11**

There were algorithms to simplify the puzzle space; I rolled my own because I didn't know about the others. Part 1 *worked*. Part 2, where you had to share tasks with an elephant that showed an interest, worked *for me*. I chose the best route for the human and the best route through what remained for the elephant.

Apparently that is the incorrect strategy. I played around with some other algorithms but stuff was just not working, so... put it aside. Always a new puzzle. I have my two golden stars for the day.

```
from time import time_ns
import re
from collections import defaultdict

class Node:
    def __init__(self, data):
        self.name = data[0]
        self.flow = int(data[1])
        self.neighbor_map = defaultdict(int)
        for neighbor in data[2:]:
            self.neighbor_map[neighbor] = 1

    def __repr__(self):
        return f"Node({self.name}, {self.flow}, {self.neighbor_map})\n"

def read_input():
    nodes = []

    with open(r"2022\puzzle16.txt") as f:
        for l in f.read().splitlines():
            nodes.append(Node(re.findall(r"[A-Z][A-Z]|\d+", l)))

    for node in nodes:
        for a_node in nodes:
            if node != a_node and node.name in a_node.neighbor_map:
                current_distance = a_node.neighbor_map[node.name]
                for my_neighbor in node.neighbor_map:
                    if my_neighbor == a_node.name:
                        continue
                    if my_neighbor not in a_node.neighbor_map:
                        a_node.neighbor_map[my_neighbor] = current_distance + \
                            node.neighbor_map[my_neighbor]
                    else:
                        a_node.neighbor_map[my_neighbor] = min(
                            a_node.neighbor_map[my_neighbor], current_distance + node.neighbor_map[my_neighbor])
                if not node.flow:
                    del a_node.neighbor_map[node.name]

    return {node.name: node for node in nodes if node.name == starting_node or node.flow}

def traverse(node_map, current_node, visited=[], time=0, max_time=30):
    if time >= max_time:
        return 0, visited

    node = node_map[current_node]
    score = node.flow * (max_time - time)
    new_visited = visited + [current_node]

    child_scores = max([traverse(node_map, neighbor, new_visited, time + node.neighbor_map[neighbor] + 1, max_time)
                        for neighbor in node.neighbor_map if neighbor not in visited])

    return (score + child_scores[0], [current_node] + child_scores[1])

def part1():
    score, _ = traverse(node_map, starting_node)
    return score

def part2():
    score, path = traverse(node_map, starting_node, max_time=26)

    # remove the nodes in 'path' from the neighbor_map of all nodes
    for node in node_map.values():
        for p in path[1:]:
            if p in node.neighbor_map:
                del node.neighbor_map[p]

    elephant_score, _ = traverse(node_map, starting_node, max_time=26)
    return elephant_score+score

starting_node = 'AA'
node_map = read_input()

start = time_ns()
print(f"Part 1: {part1()} in {(time_ns()-start)/1e6}ms")
start = time_ns()
print(f"Part 2: {part2()} in {(time_ns()-start)/1e6}ms")

```
