---
date: '2023-08-05T07:00:00-05:00'
draft: false
title: "Adventures in Bad Game Development"
author: "Tipa"
disqusIdentifier: "2023/08/05/adventures-in-bad-game-development"
summary: "I've never been able to make a good game, but I think I could make some bad ones if I just put a little effort into them."
categories:
  - "Arcade Game"
  - "Blaugust"
  - "Blaugust 2023"
  - "Game Development"
tags:
  - "Asteroids"
  - "Aws"
  - "Centipede"
  - "Javascript"
  - "Phaser"
  - "Space Invaders"
relatedPosts:
  - url: "/2023/08/10/quick-look-phaser-game-engine/"
    title: "Quick Look: Phaser Game Engine"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/gameover.png"
  - url: "/2021/09/01/resurrecting-west-karana/"
    title: "Resurrecting West Karana"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/b0d5f94a61f128683568fec95571fa8e.jpg"
  - url: "/2023/08/17/the-games-that-defined-me-part-2-arcade/"
    title: "The Games that Defined Me, Part 2 -- Arcade"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/startrek.png"
  - url: "/2025/01/09/our-starvaders/"
    title: "Our STAR*VADERS!"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/01/KeyArt_920x430.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/DALL·E-2023-08-04-23.05.25-classic-video-game-box-art-of-a-space-ship-shooting-a-centipede-with-asteroids-in-the-sky.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/DALL·E-2023-08-04-23.05.25-classic-video-game-box-art-of-a-space-ship-shooting-a-centipede-with-asteroids-in-the-sky.png"
---
I've never been able to make a good game, but I think I could make some bad ones if I just put a little effort into them.
<!--more-->

I'm going on vacation this next week. I have some parent visiting to do, but I should have a few days to myself. And I don't want to use it gaming. I have the [Phaser JavaScript game engine](https://phaser.io/) right here, and I want to make some quick games. Though given how slow I am, maybe one game.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-14-1024x567.png" classes="center" >}}

**Real Asteroids**

It always kinda bothered me that the Asteroids arcade game had all these asteroids right next to each other. They really aren't that close. Wouldn't it be more fun if they were a lot further apart?

- Simulate the vector display of the original game. Everything is modeled in line segments.

- Graphics are stored in a graph. Think of it as nested groups. 

- Though the display is in 2D, the line endpoints will be stored in 3D, so we can apply coordinate transformation to each line, so that asteroids can rotate, the ship can rotate, the score can bounce around if we need it to, the GAME OVER text can rotate around. It'll be fun.

- We can also explode the ship and asteroids by choosing a center point and shoving the line segments away from it, similar to the original game.

- So the game itself: You start out over a wireframe representation of Earth, and your ship is near there. Crossing the Earth will slowly refuel the ship.

- Asteroids will spawn somewhere off screen. Triangles along the edge of the screen will, by their size and location, point out the direction and distance to the asteroid.

- Asteroids slowly move toward the Earth. If they hit the Earth, game over.

- You fly out to the asteroid, using fuel. Running out of fuel is game over.

- Asteroids are really large once you get to them. Unsure how big they should be yet.

- It takes a lot of shots to break off bits and destroy them in standard Asteroids fashion. If the asteroid or asteroid bits hit you, it's game over.

- After you destroy one, it's off to the next one.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-13-1024x683.png" classes="center" >}}

**Bug Pong**

What if, in Pong, the paddles took damage when they got hit by the ball?

- Paddles are caterpillars, crawling up and down. They are made of segments, similar to Atari's Centipede.

- The ball is a stinkbug, rolling from side to side, but obeying all the physics of the original game.

- Each segment has its own health pool. Depending on the speed the ball is going when it hits, it can take a little damage or a lot.

- When it takes a lot, the segment disappears and the smaller half either disappears or connects to the larger half, not sure.

- Power ups include extra segments and bandages. Naturally, they will appear far away from the paddle.

- Not sure how smart to make the AI player.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-12.png" classes="center" >}}

**Bad Space Invaders**

The idea here was to make a standard Space Invaders, except the cannon only moves in one direction until it hits the edge of the screen, but refuses to move. Trying to get it to go in the other direction shows a little movement like it's really trying, but no dice.

Not sure this would be fun to play. The others might be.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/08/image-11.png" classes="center" >}}

**AWS Othello**

I wrote Othello in JavaScript and it plays fine, but I would like it to call code in the cloud so that I could save the move trees in a database, allowing it to get smarter over time. I just tonight got the New Game endpoint working; next is to port the Monte Carlo Tree Search code from JavaScript to Python and put that in. This will give me some experience in DynamoDB and S3 and connecting all this stuff up.
