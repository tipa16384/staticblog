---
date: '2023-12-02T15:44:35-05:00'
draft: false
title: "Advent of Code Day 2 -- Cube Conundrum"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2023/12/02/advent-of-code-day-2-cube-conundrum/"
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
summary: "The hands of the Christmas elf are far, far larger than they appear."
description: "The hands of the Christmas elf are far, far larger than they appear."
tags:
  - "Advent of Code"
  - "ChatGPT"
  - "Copilot"
  - "Haskell"
  - "Memoization"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/12/tipachu_A_Christmas_elf_on_the_tundra_surrounded_by_red_green_a_ad0ef918-2e5e-4cad-bb3a-4f76bd9b3c04.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2023/12/tipachu_A_Christmas_elf_on_the_tundra_surrounded_by_red_green_a_ad0ef918-2e5e-4cad-bb3a-4f76bd9b3c04.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

After having been launched via trebuchet to Snow Island, an island in the clouds that doesn't actually have any snow on it. Ignore the image on the top -- Midjourney refuses to believe that a Christmas elf could be somewhere without snow. Something to do with biology, over adaption to the arctic environment, who can tell? The science surrounding Christmas elves has more questions marks than periods.

[It's up to you to fix the snow problem](https://adventofcode.com/2023/day/2), for some reason. The problem is some distance from where you landed, and so the elf proposes a little game. He has a bag filled with cubes colored red, green and blue, and he's going to play a number of games with you where he pulls a random assortment of cubes out of the bag some number of times.

He's an elf. Those cubes are going to be *tiny*. And yet... you can still count them.

So someone pulling randomly colored cubes out of a bag just gives me flashbacks to Probability and Statistics, and I was *sure* we were going to be asked, eventually, how many cubes of each color were in the bag to a given confidence level? But, that didn't happen.

**How did AI help with this puzzle?**

I think there's a graph with learning a new computer language, or even a spoken language, that shows two curves. One starts at zero and is your understanding of the language, and this increases over time. One starts at 100 and is the amount of help you need.

So right now, it's like 5 understanding, 95 help. At some point, the curves will meet, and I'll be proficient enough to need very little help, most of the time. That said, I've used Java and Python for many years, and I still need to look stuff up now and again, so I don't expect that to ever go away.

ChatGPT was handy when I needed to do something that I could do easily in Python or Java, but didn't know how to do in Haskell. There was some discussion about how to do dictionaries in Haskell (possible, but don't), and how to flatten lists of lists (flatMap in Java, concat in Haskell).

Github Copilot was more helpful than yesterday, largely because I was able to be more certain on how to proceed so that it wouldn't just spit out wildly random things.

So like yesterday, the algorithm and approach is all me. I was able to do a few things on my own, but I had considerable help. The goal is to get to that place where the curves meet by the end of the month. After I got this working, I went back and did some optimizations on my own.

**Caching/Memoization**

I was thinking about the kinds of problems that always come up in AoC, and it occurred to me that the inevitable problem requiring memoization -- saving the values from a call to a time-consuming function so that you don't have to call it again with the same inputs -- is something Haskell does for free. I'm looking forward to seeing how that works in action,

Anyway, on to today's puzzle solution...

**Part 1**

In Part 1, the elf asks which of the games would have been possible if the bag only contained 12 red cubes, 13 green cubes, and 14 blue cubes? Sum up the game numbers of the possible games, and that's the answer. Each game is notated like:

`Game 6: 5 red, 20 blue, 3 green; 4 red, 20 blue, 3 green; 12 blue, 3 green, 1 red; 3 red, 3 green, 19 blue`

If I'd been using Python, I'd have *immediately* started doing these with dictionaries -- collections of *key, value* pairs. Haskell, being a functional language, doesn't like things that change, so I was going to have to come up with a new plan.

`import System.IO ()
import Data.List (nub)
import Data.List.Split (splitOn)

main :: IO ()
main = do
    lines  snd x) $ map part1 lines)
    putStrLn $ "Part 2: " ++ (show $ sum $ map part2 lines)

-- function takes a line and returns a tuple of the game number and a boolean
-- representing whether the game is valid or not
part1 :: String -> (Int, Bool)
part1 line = do
    let parsedLine = parseLine line
    -- valid if every checkColorCount x in the ball reveals is True
    (fst parsedLine, foldl (\acc x -> acc && (checkColorCount x)) True $ snd parsedLine)
`

The first thing is to parse the line into a tuple with the game number on the left, and a list of tuples containing (color, count) pairs on the right. The part1 function takes a line of input, parses it, processes every tuple to see if it falls within bounds, and returns True if they all do, False otherwise.

`-- function takes a line and returns a tuple of the game number and a list of
-- (color, count) tuples
parseLine :: String -> (Int, [(String, Int)])
parseLine line = do
    let gameRevealsSplit = splitOn ": " line
        revealsSplit = splitOn "; " (gameRevealsSplit !! 1)
        reveals = concat $ map (splitOn ", ") revealsSplit
        gameNumber = read ((splitOn " " $ head gameRevealsSplit) !! 1):: Int
    (gameNumber, map parseCountColor reveals)

-- function takes a string of the form "count color" and returns a (color, count) tuple
parseCountColor :: String -> (String, Int)
parseCountColor reveal = do
    let revealSplit = splitOn " " reveal
    (revealSplit !! 1, read (revealSplit !! 0):: Int)

-- function takes a (color, count) tuple and checks if the count is valid
-- (less than or equal to the number of balls of that color)
checkColorCount :: (String, Int) -> Bool
checkColorCount colorCombo = do
    let balls = [("red", 12), ("blue", 14), ("green", 13)]
    (snd $ head $ filter (\x -> (fst x) == (fst colorCombo)) balls) >= (snd colorCombo)
`

Diving deeper. parseLine splits the input string at the colon, with the first element being "Game *n*" and the second element being all the cube info. It then splits it at "; " to make a list of reveals, and again at ", " to make a list of "count color" strings. It then flattens all this so we have all the "count color" strings in a list. We then return the tuple with the game number and we call parseCountColor on all the count/color strings to turn them into (color, count) tuples.

Finally, checkColorCount takes a (color, count) tuple and returns True if valid, False if not. "fst" and "snd" are specialized functions that return the left and right values in a tuple. "head" returns the first element of a list, and "filter" finds the ball count information corresponding to the color passed in. Bad things will probably happen if I were to ask if a certain count of yellow or purple balls was valid.

**Part 2**

For Part 2, the elf wants to know what the minimum number of red, blue and green blocks would need to be in order to make each individual game possible. This is simply the maximum of the red, green and blue blocks on the line. Those maximums are multiplied (to make the 'power' of a game), and then summed for the answer.

`part2 :: String -> Int
part2 line = do
    let reveals = snd $ parseLine line
        colors = nub $ map fst reveals
    product $ map (\x -> maximum $ map snd $ filter (\y -> (fst y) == x) reveals) $ colors
`

So this is what I like to see; a Part 2 that builds off of the Part 1. parseLine returns a tuple of the game number and the list of cube count tuples; we discard the game number (not needed in Part 2) and keep only the list of tuples as 'reveals'. The 'nub $ map fst reveals' collects only the colors from the tuples, and then 'nub' leaves us with a list of the colors with no duplicates. It might be possible to have games that are missing a color entirely, so this way, I don't rely on having all colors in all rows.

Haskell is a right-to-left language in some ways. The next line takes a color from 'colors', then goes through all the tuples and collects the count for the color, finds the maximum, and then 'product' multiplies them all together and is implicitly returned.

So that's Day 2. I would have done this entirely differently in a language that supported variables. This Haskell experiment is forcing me to think about problem solving entirely differently.
