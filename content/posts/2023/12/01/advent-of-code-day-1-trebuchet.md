---
date: '2023-12-01T08:03:44-05:00'
draft: false
title: "Advent of Code Day 1 -- Trebuchet?!"
author: "Tipa"
summary: "Elves can't fly, but maybe YOU can... with a little help from a friendly Christmas trebuchet..."
categories:
  - "Advent of Code"
tags:
  - "Advent"
  - "Haskell"
  - "Trebuchet"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_catapult_surrounded_by_Christmas_elves_af0eba66-cf81-40e8-8736-e61609b50fdd.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/tipachu_A_catapult_surrounded_by_Christmas_elves_af0eba66-cf81-40e8-8736-e61609b50fdd.png"
---
Elves can't fly, but maybe YOU can... with a little help from a friendly Christmas trebuchet...
<!--more-->

When I posted about Advent of Code yesterday, I planned to do the puzzles in my comfort language, Python. But as I went through the day, I wondered if I could just go a *little bit* out of my comfort zone, and use an entirely different language which operated entirely differently -- Haskell.

Haskell is what they call a "functional" programming language. Almost every computer language has the concepts of numbers and strings of characters. Functional languages have functions (like *f(a) = a + a*) where the function itself (*f* here) is a core object, just as much a fundamental type as integers or text.

Functional languages also don't have variables. Once you assign a symbol to the value of a function, it cannot be changed.

Functional languages are also lazy. They don't do any calculations until you print out a result. In Haskell:

`let a = 2 * 2
let b = a * a
let c = 3
print $  show c`

"a" and "b" are never actually calculated. Haskell will see that the results of those calculations are never displayed, and so it will skip them.

Laziness means that Haskell is comfortable with infinity.

`let a = [0,1..]
let squares = map (\x -> x * x) a
print $ show squares !! 10`

The first line makes 'a' equal to a set of all integers from 0 to infinity. The second line makes 'squares' equal to the squares of every whole number, up to infinity squared. Nothing gets done until the third line, where it sees the only value I'm interested in is the square of 10. It calculates 10*10 and prints out 100.

Anyway. On to my solution.

I hadn't used Haskell before yesterday, so I was starting from zero. Or not quite zero, since I have some tools to help. I had ChatGPT open. I emphasized that it was never to generate code for me, only to answer Haskell questions and to suggest language features I could use. And it *did that job*. It was as if someone were sitting next to me, explaining how to do what I needed without actually doing it for me.

I also had Github Copilot, which absolutely had no idea what it was doing. In the second part of the puzzle, its suggestions were so far off the mark that it would have been more helpful if it had just suggested nothing. That said, as I started working through the problem, it would have useful suggestions here and there. And this morning, when I opened up my project, it suggested some optimizations that I gladly took.

So yeah, I did have help from AIs. But this is still very much my solution.

So the first problem is extracting numbers from lines of text and adding them up. The tens digit is the first digit encountered, and the ones digit is the last digit encountered, so a string that looking like "thisis1andthisis2andthisis3okay" would return as "13". Add up each line and that is the part 1 solution.

`import System.IO ()
import Data.List ( elemIndex, isPrefixOf, isSuffixOf )
import Data.Maybe ( fromJust )
import Data.Char ( isDigit )

main :: IO ()
main = do
    lines 

We start off with some imports and our main function. We define the main function as something that does I/O. First line reads the input into the list "lines". We then call "parseLine" on each line, and sum it up for part 1. Part 2 does something similar, but it processes the lines in a different way.

`readLinesFromFile :: FilePath -> IO [String]
readLinesFromFile filePath = do
    contents  Int
parseLine line = do
    let numbers = filter isDigit line
        value = head numbers : [last numbers]
    read value :: Int
`

'readLinesFromFile' again suggests that it takes in a FilePath object and does I/O, returning a list of String. The "lines" function breaks the input into a series of strings, one for each line.

'parseLine' takes a string and returns an integer. The 'let numbers =...' line returns only those characters that are digits into a string, 'numbers'. The next line makes a string from the first and last characters in that string. The last line converts it into an integer. It is implicitly returned as the value of the function.

The second part of the puzzle noted that the digits might be written out in English -- "xyzone2threeabc" would return "13".

`parseWordLine :: String -> Int
parseWordLine line = do
    let digitWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        match = lrcrawl line digitWords
        leftDigit = if length match == 1 then match else show (1 + fromJust (elemIndex match digitWords))
        match2 = rlcrawl line digitWords
        rightDigit = if length match2 == 1 then match2 else show (1 + fromJust (elemIndex match2 digitWords))
    read (leftDigit ++ rightDigit) :: Int

lrcrawl :: String -> [String] -> String
lrcrawl [] words = ""
lrcrawl line words = do
    let matches = filter (`isPrefixOf` line) words
    if not (null matches) then head matches else lrcrawl (tail line) words

rlcrawl :: String -> [String] -> String
rlcrawl [] words = ""
rlcrawl line words = do
    let matches = filter (`isSuffixOf` line) words
    if not (null matches) then head matches else rlcrawl (init line) words`

The function 'lrcrawl' takes a string -- the line -- and a list of strings -- the written out numbers -- and returns a String -- the first match it sees, using "isPrefixOf" as it works its way through the line from left to right. The 'lrcrawl [] words = ""' line indicates what to do when the line is empty -- return an empty string. Otherwise it calls itself recursively until it finds a match,

The function 'rlcrawl' does the same, but in reverse, using "isSuffixOf" and lopping off the final character of the string recursively until it finds a match.

'parseWordLine' calls lrcrawl and rlcrawl in turn. If the matching string was a single character, then it was '1'..'9' and just use that. Otherwise, it takes the index into digitWords and adds one to it to get the value. This is a little cheesy. It concatenates the first and last digit, converts it to an integer, and returns it.

Asked for commentary, ChatGPT said my recursive line scanning was slow and prone to breaking on large strings. It also said I didn't put in enough checks for failures. But it reluctantly conceded that it would work -- which it does. (I did not feed the puzzle into ChatGPT, all it knew of it was what my code did).

So, Day 1 done, and in a new language. I might try it in Python later just to see how I would do it in a language I actually know.

Listing image by Midjourney, this time. The Dall-E 3 one was nightmare inducing.
