---
date: '2023-08-12T09:19:16-05:00'
draft: false
title: "A Cheater's Guide to Wordle, Waffle and Squaredle"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/08/12/a-cheaters-guide-to-wordle-waffle-and-squaredle/"
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
summary: "There's a really good reason why I solve these daily puzzles in full view of my family, at the kitchen table, now. It's to stop me from cheating."
description: "There's a really good reason why I solve these daily puzzles in full view of my family, at the kitchen table, now. It's to stop me from cheating."
tags:
  - "Blaugust"
  - "Blaugust 2023"
  - "Cheating"
  - "Squaredle"
  - "Waffle"
  - "Wordle"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/08/DALL·E-2023-08-12-09.16.41-clip-art-of-a-woman-solving-a-crossword-puzzle-that-is-drawn-on-a-chalkboard.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/08/DALL·E-2023-08-12-09.16.41-clip-art-of-a-woman-solving-a-crossword-puzzle-that-is-drawn-on-a-chalkboard.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

When the Wordle craze started a couple years ago, toward the beginning of the pandemic, I jumped on that bandwagon. I used to share my solution to Twitter, before it became clear that doing so was very much a bad thing for those who use screen readers due to sight issues. Screen readers would laboriously describe each of the ten or more emojis used to display the Wordle result. So mostly I just keep them in a group chat with my sisters.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-24.png" title="Wordle: arise, all ye puzzle solvers" class="align-center" >}}

Backing up a bit. You *do* know [Wordle](https://www.nytimes.com/games/wordle/index.html), right? You have six chances to guess a five letter English word, given hints as to which letters of your guess are in the same position in the answer, which letters are in a different position in your answer, and which letters are not in the answer. It's a bit like the old Mastermind game, except instead of colored pegs, it's letters, and they form a common English word.

Pages on the Web are usually actually computer programs, and they can do all the things any other program can do. Most browsers let you look at the source code to a page just by hitting a key -- Ctrl-U for Chrome. You'll see a mixture of HTML (describing the organization of the page), CSS (describing the colors and fonts and layout of the page), and JavaScript (describing the functionality of the page). Curious as to where Wordle was getting the English words, I looked at the source code and saw they just had a list of them. In the order in which they would be presented each day. They had another list of all five letter words that included those that were too unusual to ever be chosen as the day's word, but should be allowed to be guessed in case people were trying to zero in on the correct word.

I saved both these word lists to my computer, and went to work.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-25.png" title="My Wordle solver" class="align-center" >}}

One of the first programs I had to write in my introduction to algorithms class in college was the classic Mastermind game. The strategy was simple: make a pool of every possible answer, choose a random guess from that pool, and remove any possible answer that doesn't match the response until only one guess is left, or you have randomly chosen the correct answer from the pool.

Since I had the entire list of possible words from the source code, I had my pool of every possible answer. I wrote a program to do some analysis to choose the word that would contains the most common letters in the remaining words and suggest that a starting word.

I wrote this solver in Python in Linux over a weekend, and soon after stopped playing Wordle, because why bother anymore?

When my sisters started sharing their Wordles in the family chat, I realized I was in deep trouble. I wanted to play, but cheating wouldn't be fair. Out to the kitchen table. The temptation was too strong if I was sitting at the computer.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-26.png" title="Waffle: the game that got me to buy waffle irons" class="align-center" >}}

I'm not sure if it was my sister who started with [Waffle](https://wafflegame.net/daily), or if I was to blame. Whichever of us started it, she's way more into it these days than I am. Be that as it may...

Waffle is typically six English (but not always) words arranged three across and three down in a crossword shape. Variants use seven letter words, or break out of the Waffle shape, but the daily puzzle is consistent. Scoring is the same as with Wordle, with the added hitch that a letter might be in more than one word. The corners and center tiles are given to you. You move by swapping two tiles until you have the solution. Every puzzle can be solved in ten swaps. If you take more than fifteen swaps, you lose.

This puzzle isn't that hard to do manually. I usually figure out the words on a notepad, and then it's usually fairly obvious what the swaps are. Figuring out the words in advance is the key. I usually do this at the kitchen table in ten swaps.

But, I'm a hacker at heart, so, of course, I had to write a program to help.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-29.png" title="Waffle words" class="align-center" >}}

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-28.png" title="Answer key" class="align-center" >}}

Now I really want to emphasize that I don't need this program to solve the puzzle. I am a Waffle Wizard with over 300 solutions without a failure. (I did have a failure about a year ago, or that number would be about 150 puzzles more).

But it was a programming challenge. I hadn't yet made the jump to programming in JavaScript for difficult things, so I wrote a client/server application where the front end, in JavaScript, let the user set up the puzzle, while the Python back end solved it and sent the solution back to the front end for display. I got bored with the project before I could think of a good way to visually and graphically show what the swaps were, so I just dumped them to the console. I'm the only user, after all.

My solver has two parts. Figuring out the words just tries every word that fits in the fixed tiles that also conforms to which other tiles are available using a depth first search. The possibilities are fairly limited and this takes very little time. I think I use the Wordle word list, but I might have switched to the Linux dictionary by this point (I definitely did by the time I solved Squaredle).

There's way, WAY too many possible swaps to just do random guesses, which leaves my old favorite strategy, the Monte Carlo Tree Search, off the table. I decided to do a path seeking algorithm instead. (I believe I just used straight Dijkstra). I wrote a function that calculates the distance between the current guess and the actual solution, pruned any with a distance greater than fifteen, chose the next closest move, and so on. My solver isn't that good, and I can sometimes outperform it manually. Since sometimes it couldn't find a ten swap solution, I used a multi-threaded algorithm to look for 10, 11, 12, 13, 14 *and* 15 swap solutions in parallel, and report back if they'd found one.

The answer key above shows the swaps. the **10** says that this answer was produced by the ten swap thread, which is the best. The number pairs are the swaps, with each tile number from zero and continuing left to right, up to down.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-30.png" title="Squaredle" class="align-center" >}}

[Squaredle](https://squaredle.app/) is a word search puzzle. Words are a minimum of four letters, and the only maximum is the number of letters in the puzzle. You drag through them with your finger on the phone. There's no way to lose at Squaredle, but some of the words are *obscure*. They have some special puzzle with hundreds of words in them. I've done a couple of those, but my sister is the one who really hungrily devours them.

As you find words, you unlock hints. You're first told how many words of each length there are (and are given a hint for a bonus word that, if found, will let you reveal an additional free word to add to the free word every gets. Subscribers get additional free words beyond those). If you find an uncommon word, that counts as a bonus word but does not bring you closer to solving the puzzle. You are given a score at the end determined by your speed in solving the puzzle, how many incorrect guesses you made, and how many bonus words you found. My sister sacrifices accuracy for bonus words, and I'm the opposite, striving for no incorrect guesses.

The solver for this is super easy. There's only a few tens of thousands of words. It takes the computer no time at all to check to see if a particular word is in the puzzle. So I built in some restrictions from the start. I would only allow it to be asked about words that are a given length and start with a given letter. This is the help given by Squaredle when you have guessed sufficient words, or enough time has passed since the puzzle was published. I use it sometimes as a tool when I just can't guess the last couple of words. Given the scoring, it's super obvious when someone is using a tool like this. In the leaderboards, they have perfect accuracy, a time in the seconds, and all possible bonus words. 

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-31.png" title="All you need is l..." class="align-center" >}}

My solver finds all the words in the puzzle, then asks the user (me) to enter a regular expression. It must start with a letter. It should only consist of letters and the wildcard symbol, the dot. It provides the answer. Some of the words it finds may not be valid words, but that's the chance you take.

I used this to solve one of the bonus puzzles that contained almost five hundred words, but I was shamed and just avoid puzzles like that now.

There's no graphical UI for this one. I have a text file where I enter the puzzle, that the solver reads.

According to the leaderboard for today's puzzle, there are 68 words in this puzzle, 29 valid words and 39 bonus words. My solver only found 41 total words. Several someones are using a better solver than mine, apparently :-)

Well, there you have it. If all you have is a hammer, every problem is a nail. And if you're a programmer, every problem can either be solved by a computer program... or it's someone else's problem.
