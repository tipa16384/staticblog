---
date: '2022-12-20T08:21:19-05:00'
draft: false
title: "Advent of Code Day 19 -- Not Enough Minerals"
summary: "Okay, this one took a long time. I knew what to do, but what to do was super slow."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Depth First Search"
  - "Memoization"
  - "Python"
  - "Robots"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-20-08.04.02-A-woman-wearing-a-Christmas-hat-directing-mining-robots-with-a-handheld-device-in-a-jungle-by-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/12/DALL·E-2022-12-20-08.04.02-A-woman-wearing-a-Christmas-hat-directing-mining-robots-with-a-handheld-device-in-a-jungle-by-a-lake-by-Bob-Eggleton-detailed-and-intricate.png"
---

VERY late on this one, but then I was up very late finishing it. The code I'm going to show gives the wrong Part 2 answer, though what it prints out is sufficient to figure out what the correct answer is. It just takes some unknown amount of time to run, so I have only ever run it once, while I was sleeping.

If this ran faster, I'd be able to fancy it up some.

In [this puzzle](https://adventofcode.com/2022/day/19), you've noticed that the recent volcanic eruption has left geodes scattered around -- spherical droplets of stone with crystals inside. You'd love to mine some of them and break them open for the lulz, but you need a geode-breaking bot to do that with. Thankfully, you can make geode-breaking bots from obsidian and ore. Now all you need are obsidian and ore-mining bots. Well, obsidian bots take ore and clay, so now you also need clay-mining bots.

You have a bot factory and one ore-mining bot in your backpack, somehow, Christmas magic I suppose. You also have a couple dozen blueprints that show how to make all these bots. The puzzle challenge (for Part 1) is to sum the quality of the blueprints, which is defined as the product of the blueprint number and the number of geodes that can be opened in 24 minutes.

I used a [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) with [memoization](https://en.wikipedia.org/wiki/Memoization), along with some [heuristics](https://en.wikipedia.org/wiki/Heuristic) to move things along, and at the end I was solving Part 1 in just a few minutes.

Part 2 just wants the product of the number of geodes opened with the first three blueprints, with the time extended to 32 minutes -- eight extra minutes, and the time increases exponentially with each minute. I dunno how long this took.

**Python 3.11**

I'd been slowly making some optimizations as I worked through Part 1. I used classes for the blueprints and the game state, but I should have been using tuples instead. I partially converted GameState, but once I got Part 1 working, I just wanted to get to Part 2 asap, it being past midnight already with work the next day (today). Memoization is done with lru_cache, though that imposes limitations I could have worked around using a dictionary. **get_new_states** is the heart of the solution, taking the current game state (number of bots, amount of resources) and generating all possible, or at least feasible, next states to feed into the DFS.

That's it. It could be improved, but I doubt I will bother. It's done. Time to move on.

```
import re
from functools import lru_cache

class Blueprint:
    def __init__(self, deets):
        deeters = map(int, re.findall(r"\d+", deets))
        
        self.number = next(deeters)
        self.ore_robot_ore_cost = next(deeters)
        self.clay_robot_ore_cost = next(deeters)
        self.obsidian_robot_ore_cost = next(deeters)
        self.obsidian_robot_clay_cost = next(deeters)
        self.geode_robot_ore_cost = next(deeters)
        self.geode_robot_obsidian_cost = next(deeters)

    def __repr__(self):
        return f"Blueprint({self.number}, {self.ore_robot_ore_cost}, {self.clay_robot_ore_cost}, {self.obsidian_robot_ore_cost}, {self.obsidian_robot_clay_cost}, {self.geode_robot_ore_cost}, {self.geode_robot_obsidian_cost})"

class GameState:
    def __init__(self, from_tuple=None):
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.name = "initial state"

        if from_tuple:
            self.ore, self.clay, self.obsidian, self.geode, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots = from_tuple
    
    def __repr__(self):
        return f"GameState({self.ore}, {self.clay}, {self.obsidian}, {self.geode}, {self.ore_robots}, {self.clay_robots}, {self.obsidian_robots}, {self.geode_robots})"

    def __str__(self):
        return f"GameState({self.name})"

    def to_tuple(self):
        return (self.ore, self.clay, self.obsidian, self.geode, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots)

    def copy(self):
        new_state = GameState()
        new_state.ore = self.ore
        new_state.clay = self.clay
        new_state.obsidian = self.obsidian
        new_state.geode = self.geode
        new_state.ore_robots = self.ore_robots
        new_state.clay_robots = self.clay_robots
        new_state.obsidian_robots = self.obsidian_robots
        new_state.geode_robots = self.geode_robots
        new_state.name = self.name
        return new_state

def read_blueprints():
    with open(r"2022\puzzle19.txt") as f:
        return [Blueprint(deets) for deets in f]

def produce(game_state_tuple):
    new_state = GameState(game_state_tuple)
    new_state.ore += game_state_tuple[4]
    new_state.clay += game_state_tuple[5]
    new_state.obsidian += game_state_tuple[6]
    new_state.geode += game_state_tuple[7]
    return new_state

@lru_cache(maxsize=None)
def get_new_states(game_state_tuple, blueprint_number):
    game_state = GameState(game_state_tuple)
    blueprint = blueprints[blueprint_number-1]
    max_ore = max(blueprint.ore_robot_ore_cost, blueprint.clay_robot_ore_cost, blueprint.obsidian_robot_ore_cost, blueprint.geode_robot_ore_cost)
    new_tuples = []

    if game_state.ore >= blueprint.geode_robot_ore_cost and game_state.obsidian >= blueprint.geode_robot_obsidian_cost:
        new_state = produce(game_state_tuple)
        new_state.ore -= blueprint.geode_robot_ore_cost
        new_state.obsidian -= blueprint.geode_robot_obsidian_cost
        new_state.geode_robots += 1
        new_state.name = "produced geode robot"
        return [new_state.to_tuple()]

    if game_state.obsidian_robots = blueprint.obsidian_robot_ore_cost and game_state.clay >= blueprint.obsidian_robot_clay_cost:
        new_state = produce(game_state_tuple)
        new_state.ore -= blueprint.obsidian_robot_ore_cost
        new_state.clay -= blueprint.obsidian_robot_clay_cost
        new_state.obsidian_robots += 1
        new_state.name = "produced obsidian robot"
        new_tuples.append(new_state.to_tuple())

    if game_state.clay_robots = blueprint.clay_robot_ore_cost:
        new_state = produce(game_state_tuple)
        new_state.ore -= blueprint.clay_robot_ore_cost
        new_state.clay_robots += 1
        new_state.name = "produced clay robot"
        new_tuples.append(new_state.to_tuple())

    if game_state.ore_robots = blueprint.ore_robot_ore_cost:
        new_state = produce(game_state_tuple)
        new_state.ore -= blueprint.ore_robot_ore_cost
        new_state.ore_robots += 1
        new_state.name = "produced ore robot"
        new_tuples.append(new_state.to_tuple())
        
    new_state = produce(game_state_tuple)
    new_state.name = "produced nothing"
    new_tuples.append(new_state.to_tuple())

    return new_tuples

@lru_cache(maxsize=None)
def done_yet(game_state_tuple, blueprint_number, minute=0, max_minute=24):
    if minute >= max_minute:
        #print (minute, game_state, game_state.geode)
        return game_state_tuple[3]
    return max(done_yet(new_state, blueprint_number, minute+1, max_minute) for new_state in get_new_states(game_state_tuple, blueprint_number))

def solve(solve_blueprints, max_minute):
    initial_game_state = GameState().to_tuple()
    quality_level = 0
    for blueprint in solve_blueprints:
        done_yet.cache_clear()
        get_new_states.cache_clear()
        geode = done_yet(initial_game_state, blueprint.number, 0, max_minute)
        print (geode, geode * blueprint.number)
        quality_level += geode * blueprint.number
    return quality_level

blueprints = read_blueprints()

print ("Part 1:", solve(blueprints, 24))
print ("Part 2:", solve(blueprints[:3], 32))

```
