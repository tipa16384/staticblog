---
date: '2023-12-07T22:10:13-05:00'
draft: false
title: "Advent of Code Day 7 -- Camel Cards"
author: "Tipa"
summary: "I really tried with Haskell this time. Oh well, looks like we'll have to play Camel Poker in Python instead."
categories:
  - "Advent of Code"
tags:
  - "AoC 2023"
  - "Card Game"
  - "Elf"
  - "Python"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-07-21.36.26-In-a-desert-setting-a-Christmas-elf-mom-and-a-repair-person-in-a-safety-vest-and-hard-hat-are-riding-camels.-Both-characters-are-holding-a-hand-of-pl.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/12/DALL·E-2023-12-07-21.36.26-In-a-desert-setting-a-Christmas-elf-mom-and-a-repair-person-in-a-safety-vest-and-hard-hat-are-riding-camels.-Both-characters-are-holding-a-hand-of-pl.png"
---
I really tried with Haskell this time. Oh well, looks like we'll have to play Camel Poker in Python instead.
<!--more-->

I solved this one, in Python, before work today. It wasn't that hard. During the rare free moments during work today, I was poring over the Haskell tutorials, and I thought I had a decent approach to re-implement it in Haskell. When it came time to put hands to keyboard, though, I got a couple small functions done, but the larger, important functions, the ones that did the real work, no clue. And I couldn't explain to the AIs what I was looking for, so... it's Python again. Sorry.

The setup for Day 7: Hey, we made it to the source of the sand! We're on the wrong side of the island, though, so we're going to have to take camels across to the other side, a journey of days. The elf suggests we play a game she calls "Camel Cards", which has [some weird rules that make it a little different from the poker we know](https://adventofcode.com/2023/day/7).

The input is a list of card hands and matching bids. We have to score each hand according to their rules, rank them from weakest to strongest hands, multiply their rank by their bid, and sum the whole shebang up. This is the pattern for both parts. Part 2 differs in that the Jack is now a wild card that is always the exact value needed to make the hand it is in the best hand it can be.

`print ("Part 1:", play_game(translatePart1, "23456789TJQKA"))
print ("Part 2:", play_game(translatePart2, "J23456789TQKA"))`

In Part 2, the Jack is the weakest card. The string is the ranking of card values in a hand; the card values are used to break ties is comparing, for instance, two full house hands. The **translatePart1** and **translatePart2** are functions that help score the hands.

My idea with this was to translate each hand into a hexadecimal number, then we could just sort it and score it. So the first digit would be the rank of the hand (high card, two pair, etc), and the remaining digits are the cards in the hand, in order, because that is important, in hex. That's what those translation strings do -- map from cards to hex.

`def score(groups: list, card_values: str, hand: str) -> int:
    value = str(5 + len(groups[0]) - len(groups))
    # in the hand, translate all T to A, J to B, Q to C, K to D, A to E
    return value + ''.join(["0123456789ABC"[card_values.index(card)] for card in hand])`

I rewrote this when I was reading the subreddit and someone noted that the rank of a hand could be the length of the largest group of cards in the hand, less the number of groups. I worked it out by hand and yeah, that works. I was using a huge **match** statement. The return statement creates the hex number with that value as the first digit.

`def hand_to_groups(hand: str) -> list:
    # sort and group the characters in the hand
    groups = [list(g) for _, g in groupby(sorted(hand))]
    # sort groups by the length of the sublists, highest first
    return sorted(groups, key=lambda x: len(x), reverse=True)`

This function takes a hand and groups the cards in it so they are together, and sorts those groups so that they are in order. For instance, a hand like **2QJQQ** would become **[['Q','Q','Q'],['J'],['2']]**. I was excited by this since I'd been doing the sub lists and groupby stuff in Haskell and I figured that would come over pretty well. Probably would have. It was the **score** function I couldn't figure out, with that card-to-hex translation.

`def play_game(translator, card_values):
    data = [(translator(token[0], card_values), int(token[1])) \
            for line in readData() \
                for token in [line.strip().split()]]
    # value is the sum of the second element of each tuple multiplied by its index in data + 1
    return sum([i * x[1] for i, x in enumerate(sorted(data), start=1)])`

This function reads the data, calls the translator to turn the hand into a hex string, then sorts it, uses its rank to multiply with the bid, sums it and returns it.

`def translatePart1(hand: str, card_values: str) -> str:
    return score(hand_to_groups(hand), card_values, hand)`

The translator for part 1 takes a hand and the card values and simply uses the score function to convert the hand to hex.

`def translatePart2(hand: str, card_values: str) -> str:
    groups = hand_to_groups(hand)
    # if there is more than one group, and the first group has a 'J' in it, merge 
    # the first and second groups
    if len(groups) > 1 and 'J' in groups[0]:
        groups[0] += groups[1]
        groups.pop(1)
    # otherwise if there is more than one group and any group but the first has a 'J' in it,
    # merge it with the first group
    elif len(groups) > 1 and any('J' in group for group in groups[1:]):
        for group in groups[1:]:
            if 'J' in group:
                groups[0] += group
                groups.remove(group)
                break
    return score(groups, card_values, hand)`

The part 2 translator has to handle the Jack wild card. If the largest group is all jacks, then we merge it with the second group to boost it up. If any other group has jacks in it, it is merged with the largest group. Then we score as before. I could probably optimize that.

That's it, that's the game. Both parts return nearly instantly.

I was thinking of trying to put it in Atari BASIC again... but trying to figure out how to get all the data into those simulated disk drives was more than I wanted to take on tonight.
