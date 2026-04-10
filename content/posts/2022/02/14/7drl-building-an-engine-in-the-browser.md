---
date: '2022-02-14T22:58:05-05:00'
draft: false
title: "7DRL: Building an Engine -- In the Browser"
author: "Tipa"
disqusIdentifier: "2022/02/14/7drl-building-an-engine-in-the-browser"
summary: "One of the items on my 7DRL checklist for this year is to have the game run in a browser. The last time I did..."
categories:
  - "7DRL"
relatedPosts:
  - url: "/2025/03/10/how-to-fail-at-writing-a-game-in-7-days/"
    title: "How To Fail at Writing A Game in 7 Days"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/03/gamedevadventure.png"
  - url: "/2022/03/13/7drl-2022-retrospective/"
    title: "7DRL 2022: Retrospective"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/1-Dream_TradingCard-4.jpg"
  - url: "/2022/03/11/7drl-2022-day-5-im-damaged-and-i-like-it/"
    title: "7DRL 2022 Day 5: I'm Damaged, and I Like It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-5.gif"
  - url: "/2022/03/10/7drl-2022-day-4-tossing-and-turning/"
    title: "7DRL 2022 Day 4: Tossing and Turning"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/yata-screenshot-2.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/trinket.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/02/trinket.jpg"
---
One of the items on my 7DRL checklist for this year is to have the game run in a browser. The last time I did...
<!--more-->

One of the items on my 7DRL checklist for this year is to have the game run in a browser. The last time I did this, I used Pygame and could only share it with people by handing them the source and hoping they happened to have Python and Pygame installed. As part of the Rogue-like game engine development, I'm looking into ways to get the game playable in the browser, while still being able to use Pygame to develop it. Today, I'm looking at [Trinket](https://trinket.io/).

Trinket is meant for educators and students to share small programs with one another. The free version of Trinket allows programming using turtle graphics in [Blockly](https://blockly.games/) or Python. But, they have a paid tier that allows programming in Python and Pygame.

The way this works is, you upload your code and assets. They run your code in the cloud, and pipe the output into the browser. Inputs go the other way.

So, I signed up for a month of the service, and uploaded the tech test I wrote yesterday, and... well, try it for yourself. The bit embedded below is kind of small; [following this link](https://trinket.io/pygame/86b9301490?outputOnly=true&showInstructions=true) to the Trinket page might work out better. Use the left/right arrow keys to rotate the room counter-clockwise and clockwise. That's it, that's all there is.

I intended to get movement working tonight, but instead I did this. It's good that I'm working through these issues before the game coding starts.

Is this a great solution? Honestly, no. I am imagining a much larger play area. But, we'll see what happens.
