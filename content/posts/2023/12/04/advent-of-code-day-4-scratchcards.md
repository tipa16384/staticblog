---
date: '2023-12-04T21:07:24-05:00'
draft: false
title: "Advent of Code Day 4 -- Scratchcards"
author: "Tipa"
disqusIdentifier: "2023/12/04/advent-of-code-day-4-scratchcards"
summary: "So, I'm back to solving the puzzle in Haskell again. This puzzle was easy enough for me to figure out."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Haskell"
  - "Java"
  - "Python"
relatedPosts:
  - url: "/2024/12/07/advent-of-code-2024-the-first-week/"
    title: "Advent of Code 2024: The First Week"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/12/DALL·E-2024-12-07-11.54.46-A-Tolkien-inspired-scene-depicting-graceful-elves-in-a-Tolkien-inspired-setting-repairing-a-rope-bridge-over-a-serene-river-surrounded-by-lush-vibra.webp"
  - url: "/2023/12/03/advent-of-code-day-3-gear-ratios/"
    title: "Advent of Code Day 3 -- Gear Ratios"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_working_on_a_giant_machine_with_many_ge_47e1029a-b055-4df9-99f0-1c55a64ca2e8.png"
  - url: "/2023/11/30/advent-of-code-2023-day-0/"
    title: "Advent of Code 2023 -- Day 0"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/11/DALL·E-2023-11-29-23.20.51-A-festive-and-imaginative-illustration-for-a-blog-post-combining-the-themes-of-Advent-of-Code-Python-programming-and-Christmas-in-a-16_10-aspect-ra.png"
  - url: "/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/"
    title: "Advent of Code Day 11 -- Monkey in the Middle"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/12/DALL·E-2022-12-11-16.50.33-A-woman-wearing-a-Christmas-hat-staring-at-a-monkey-in-a-jungle-by-Bob-Eggleton-detailed-and-intricate.png"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_sitting_on_a_giant_heap_of_scratch_off__6f747a63-e079-4e61-aea3-4d9d81e4b203.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_Christmas_elf_sitting_on_a_giant_heap_of_scratch_off__6f747a63-e079-4e61-aea3-4d9d81e4b203.png"
---
So, I'm back to solving the puzzle in Haskell again. This puzzle was easy enough for me to figure out.
<!--more-->

In today's puzzle, we're helping an elf figure out[ if any of the few hundred scratchcards he's scratched off](https://adventofcode.com/2023/day/4) have won him anything.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-1-147x300.png" classes="fig-20" >}}

Why? I have *no idea*. There was a meme in the subreddit today with the top picture of a guy looking like he was totally over it all with the caption, "When my boss asks me to solve a weird problem for money", and the guy on the bottom looking all excited with the caption, "When an elf asks me to solve a weird problem for free".

(Yes, I do recognize Robert Downey Jr and Chris Pratt. Don't @ me.)

So yeah, elf wants our help with scratch cards, we're helping the elf with the scratch cards.

In Part 1, we're explaining to him how these things work. You see the winning numbers, and the numbers you scratched off, and you get points for the number of matches -- 1, 2, 4, 8 etc points, and no points for no matches. Sum them up, and you have the answer to Part 1.

**Java**

This seemed like a problem for sets -- collections that can't contain any duplicate items. If the winning numbers were a set, and the card numbers were a set, then the intersection of those two sets would be the winning numbers. Then just run through them and sum up the points.

`    private void part1() {
        var lines = readFile("2023/puzzle4.dat");

        var part1 = lines.stream().map(this::parse)
            .map(this::intersection)
            .filter(s -> !s.isEmpty())
            .mapToInt(s -> 1 

Java has a problem with requiring extra stuff. But briefly, we read the data, go through each line and map the input into two sets -- winning numbers and card numbers. We intersect them, discard losing cards, then figure out the point value and sum them up.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2023/12/image-2-1024x585.png" title="I've been using Midjourney for the header images. This is Dall-E 3." classes="center" >}}

**Haskell**

`getDuplicates :: String -> Int
getDuplicates str = length $ filter (\x -> length x > 1) (group (sort (drop 2 $ words str)))
`

The Haskell solution is a little different. I was trying not to be spoiled at work today by other people's solutions, but someone mentioned that you could parse the line just by seeing how many duplicate tokens you had, didn't have to split into sets or anything. So that's what this does. Working from right to left, **words str** splits the input into tokens by splitting at spaces. **drop 2 $** drops the first two words, which are "Game *n*:". I was afraid the game number might match one of the other numbers and be a false match, though I guess since it would have a ":" appended, probably unnecessary. **sort** sorts them so that duplicates are lined up next to each other. **group** puts all the items in lists, and those duplicates will be in the same list. **filter...** filters out all the lists with only one element (non-winning numbers). We only care about the number of wins, so **length** just replaces the list itself with the length of it, and that's the number of winning numbers.

`main :: IO ()
main = do
    lines  2 ^ (x-1)) (filter (> 0) duplicates))
`

We read the input, and call getDuplicates on every line, making a list of winning numbers. The last line filters out losing cards, then assigns a score, sums them up, and prints them out.

`-- function takes a list of numbers and returns the sum of the game
playGame :: [Int] -> Int
-- if the list is empty, return 0
playGame [] = 0
-- if head is 0, return 0
playGame (0:xs) = 0
-- otherwise (x:xs) call sum playGame called with the next x elements of xs and add x
playGame (x:xs) = x + sum (map (\z -> playGame $ drop z xs) [0..x-1])
`

In Part 2, we discover that you only win more scratch cards when you win, the number of cards being equal to the number of winning numbers, and the cards you win are copies of the *n* next cards. Of course, you get to scratch off those copies and do the same again... it's recursive.

This was my chance to explore Haskell's pattern matching. **playGame** take a list of integers -- the number of winning numbers in each game -- and returns an integer -- the number of cards you got from scratching off the first card in the list.

**playGame [] = 0** says what to do with the empty list -- simply return 0.

**playGame (0:xs) = 0** says what to do if the first element of the list is zero -- a losing ticket. Just immediately return 0.

**playGame (x:xs) = ...** is what to do if the list has at least one element. It takes the first element and binds it to **x**, and the rest of the list to **xs**. From 0 to the number of winning numbers - 1 (inclusive), skip the first *z* elements of rest of the list and call **playGame** on them, sum them up, add the number of winning numbers for this copy of the card, and return.

`    let part2Sum = sum $ map (\x ->  1 + playGame (drop x duplicates)) [0..length duplicates - 1]
    putStrLn $ "Part 2: " ++ show part2Sum
`

The first line slices the list so that every card has a chance to be first, calls **playGame** on them, adds 1 for the original card we're on to the sum of all the other cards this card won, sums all *those* up, and that's Part 2.

It's recursive, so not super fast -- it takes a second or two to get through Part 2. Haskell is a compiled language, unlike Java (uses virtual machine) or Python (interpreted but can compile to C). I was wondering if Haskell's functionality would make it faster. Let me try running it in Python.

Okay, I rewrote it in Python.

`def part2(data):
    duplicates = [countDuplicates(line) for line in data]
    part2_sum = sum(1 + play_game(duplicates[x:]) for x in range(len(duplicates)))
    return part2_sum
`

It's not much slower, to it's credit. People on Reddit were saying it was taking them over two minutes. Dunno how.

Anyway. On to Day 5.
