---
date: '2024-12-02T07:00:00-05:00'
draft: false
title: "Advent of Code 2024.1:"
author: "Tipa"
summary: "Where is that darned elvish historian?"
categories:
  - "Advent of Code"
tags:
  - "AI"
  - "Counter"
  - "Elves"
  - "Python"
  - "Sort"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2024/12/DALL·E-2024-12-01-15.45.53-A-serene-scene-of-Tolkien-style-elves-sorting-numbers-written-on-thin-ivory-slabs-and-placing-them-into-a-wall-hanging-reminiscent-of-hymn-boards-in-a.webp"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/12/DALL·E-2024-12-01-15.45.53-A-serene-scene-of-Tolkien-style-elves-sorting-numbers-written-on-thin-ivory-slabs-and-placing-them-into-a-wall-hanging-reminiscent-of-hymn-boards-in-a.webp"
---
Where is that darned elvish historian?
<!--more-->

A word about AI images:

Yes, I use them, because I think "what if Tolkien elves instead of Christmas elves?" is funny. I got added to a BlueSky block list, a list for "AI and Crypto shills", probably because I posted an AI-generated image there.

Hey, AI is coming for my job, too. Nobody escapes this. But to prove just what kind of person I am, when I post this on BlueSky, I will use a real piece of art I found on the web, maybe this one:

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/12/image.png" title="A monk presumably named Alamy writing stuff in a book" classes="center" >}}

When I was looking for stock images of monks writing stuff in books, up came licensable AI images. Even stock image brokers are using AI.

Well! That said, let's get into the puzzle. [The story that is going to carry us through the Advent season](https://adventofcode.com/2024/day/1) is a search for the Chief Historian, who must be in one of fifty locations (and I'm guessing, the last one).

Part 1 tasks us with sorting two lists of numbers and finding the sum of the absolute differences between the items in the two lists.

I was going to use Rust to solve these but didn't get around to learning Rust, so here it is in Python:

`def sum_diffs(left, right):
    return sum(abs(l - r) for l, r in zip(left, right))
`

My file reading function already took care of sorting the lists. The `zip` function in Python takes two lists and returns a list of pairs (`tuples`) which are placed in the variables `l` and `r`. The difference is calculated for each pair, and these are summed up. I believe the `zip` function actually returns a *generator*, which is a Python function that returns the next value each time it is called. This allows Python to handle lists of any size, potentially infinite size, without crashing. It's kind of neat.

The second part of the problem asks us to return the sum of the products of each value in the left list and the number of times it appears in the right list. I wrote a solution and then asked Github Copilot -- a tool we are *required* to use at work -- to see if it could do better. It could, and did.

`def sum_similar(left, right):
    similarity_dict = Counter(right)
    similarity = sum(l * similarity_dict[l] for l in left)
    return similarity    
`

My bespoke solution was to make a dictionary (collection of key-value pairs) where the key would be left value, and the right would be the number of times it appeared in the list, then do the product sum for the answer. This worked.

But Copilot said this Python class, `Counter`, would do all that for me. `Counter `appears to the program as a dictionary, that magically knows how many times a key appears in the list it takes as an initializer.

That's one for you, AI. I didn't know about `Counter`.
