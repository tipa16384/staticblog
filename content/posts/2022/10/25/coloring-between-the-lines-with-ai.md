---
date: '2022-10-25T00:29:53-05:00'
draft: false
title: "Coloring between the lines... with AI"
author: "Tipa"
disqusIdentifier: "2022/10/25/coloring-between-the-lines-with-ai"
summary: "A million or so years ago, I worked for Sony New Technologies, writing system software and applications for their Magic Link handheld computer, which ran..."
categories:
  - "OpenAI"
  - "Petalica Paint"
tags:
  - "Game Pack"
  - "Magic Bag"
  - "Magic Link"
  - "Petalica Paint"
  - "Sony New Technologies"
relatedPosts:
  - url: "/2022/12/04/advent-of-code-day-4-camp-cleanup/"
    title: "Advent of Code Day 4 -- Camp Cleanup"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-04-18.27.11-Several-Christmas-elves-doing-chores-around-a-campsite-in-the-jungle-painted-by-Bob-Eggleton-detailed-and-intricate.png"
  - url: "/2022/12/03/advent-of-code-day-3-rucksack-reorganization/"
    title: "Advent of Code Day 3 -- Rucksack Reorganization"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/aoc2022.3.jpg"
  - url: "/2022/12/03/advent-of-code-2022-day-2-rock-paper-scissors/"
    title: "Advent of Code 2022 Day 2 -- Rock Paper Scissors"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/Two_elves_playing_rock_paper_scissors_in_an_abandoned_jungle_village__by_Bob_Eggleton__Detailed_and__Seed-6967716_Steps-175_Guidance-7.5.jpeg"
  - url: "/2022/11/29/crypto-crypto-what-will-you-do/"
    title: "Crypto, Crypto, what will you do?"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/11/1-A_puppy_surrounded_by_stacks_of_Bitcoin__Visual_Novel_Seed-2422298_Steps-50_Guidance-7.5.jpg"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2022/10/1-SonyMagicBagCoverColorized.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/10/1-SonyMagicBagCoverColorized.jpg"
---
A million or so years ago, I worked for Sony New Technologies, writing system software and applications for their Magic Link handheld computer, which ran...
<!--more-->

A million or so years ago, I worked for Sony New Technologies, writing system software and applications for their Magic Link handheld computer, which ran General Magic's Magic Cap operating system. The management came down one day and told us that what the Magic Link needed more than anything else was some games, goshdurnit, and so all of us developers were to take a break from writing serious software and do some games.

And so we did. I wrote Reverse (Othello) using Alpha-Beta minimax and Backgammon using Monte Carlo Tree Search, algorithms I still use a lot today. I got some good feedback, and it was fun, and since then I can always call myself a published game dev.

My boss hired an artist from the local Monterey Peninsula College to do a cover for the box. I don't think SNT ever actually used the box art -- I don't have a copy for myself, and the very few pictures I can find online show something different -- but I did manage to snag the original sketch when SNT shut down after the Magic Link and the whole Magic Cap ecosystem failed. Too early.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/10/IMG_2792-869x1024.jpg" title="Magic Cap Game Pack cover sketch" classes="center" >}}

It has bits and pieces of all the games in the image. There's my backgammon, and that frog is reversing. Because Reversi. I'm sure all the other developers can talk about their games -- Toby Dunn, Phil Corrigan, Curtis Eubanks, Mark Beaulieu. Maybe they'll look for their names someday and find this (in which case: hi, hope you're doing well!)

This has been hanging on my wall ever since, and every day I wonder what it would look like in color. I'm pretty sure we *did* have a colored version, but that is lost to history at this point.

I happened to be looking at it this morning and wondered if... if an AI could color it?

And it turns out, it can.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/10/image-1024x649.png" title="Petalica Paint" classes="center" >}}

From what I can tell from the web page and demos, [Petalica Paint](https://petalica.com/) is made largely to colorize *moe* sketches of anime *waifus*. I wasn't sure how it would do with a photograph of a sketch, but it didn't do too badly. Petalica Paint lets you provide color hints to help it along. You can see I did some proper hinting, and occasionally it even took my suggestions into account.

It's not great? But it's probably a million times better than I could do by myself. 

Here's some drawings of wombats.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/10/YY28CYDL24CNRY9HWASDPDGO20XIJR52_0.jpg" title="A wombat playing backgammon, according to Dall-E." classes="center" >}}

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/10/YUVHYCCRW5XQENADYAIPL0I1BQB4AA86_0.jpg" title="Colorized wombat security guard from the Blaugust series" classes="center" >}}

Dall-E can, of course, colorize its own drawings, but it doesn't do well with ones you upload.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2022/10/DALL·E-2022-10-25-00.25.00-An-ink-and-crayon-drawing-of-a-wombat-playing-backgammon-1024x1024.png" title="Dall-E has nfc what a backgammon board looks like" classes="center" >}}

Anyway. Got a sketch? Want to see it colored? Try Petalica Paint. Bonus points if it's a cute anime girl.
