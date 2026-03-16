---
date: '2025-03-03T08:43:21-05:00'
draft: false
title: "Tunnels &amp; Trolls: Sword for Hire"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2025/03/03/tunnels-trolls-sword-for-hire/"
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
summary: "I may be committing some light copyright infringement..."
description: "I may be committing some light copyright infringement..."
tags:
  - "CRPG"
  - "Tabletop Games"
  - "Solo Adventure"
  - "Sword for Hire"
  - "Tunnels & Trolls"
featured_image: "https://chasingdings.com/wp-content/uploads/2025/03/ttbanner.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2025/03/ttbanner.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

We were at the [House of Books and Games](http://houseofbooksandgames.com/) in South Windsor the other day. This is a small store squeezed into non-Euclidean space somehow, only open on the weekends. We love going there whenever we're in the area; they have a quirky selection of stuff not seen elsewhere. This time, there was a local author just sitting there at the table. We talked for a long time, and of course, I bought his book -- [Revenants, by B. L. Daniels](https://www.amazon.com/Revenants-B-L-Daniels-ebook/dp/B0DBC93Z2C/ref=sr_1_1?crid=W36WJDF4A6XK&dib=eyJ2IjoiMSJ9.e8hNE4TBtErI0S9mg_gDfz8OiTLrBfRUGvCB9xGVWXhlBYYFjBthhL53NgXEDv8RBa2WrmAsaSy5ArBV-9FRK8pq-UBX2AIDBlGyUS1QxvHp95CMkMm5qHQv262Uhq-Ch1x5wj0k5ivMK7qG3nISrww9p161lvSYUqpVMD9ErNHvF51UiRrc42_Wb37YwpLodveqIHUQQsT4XJKGzLCBuhiBsOsJK7k3wvZpSxJhD_c.N-1xpCGS4jJyzDIu6VFESM3m_iE6pyUEbedAfJtyuR0&dib_tag=se&keywords=b.+l.+daniels&qid=1741007587&sprefix=b.+l.+daniels%2Caps%2C94&sr=8-1). It's also on Kindle Unlimited, so I could have saved the fifteen bucks, but then I couldn't have gotten it *signed*.

Anyway, in their old magazine section was someone's entire old 70s/80s-era Analog SF&F magazine collection. And next to *those* were a half dozen Tunnels & Trolls solo adventures.

I bought several of each.

I've never played Tunnels & Trolls. I'd heard about it, but back in the day, I was all about Advanced Dungeons & Dragons, which was like D&D, except *advanced*. The publishers, Flying Buffalo Inc, were known mostly, at the time, for their wide variety of Play-By-Mail RPGs, where you would fill out a card with your party's actions, send it back, they'd run it through a computer with everyone else's cards, and then they would mail everyone back with a new card, along with a report on what had happened that turn.

I never did do that, but I found the whole concept fascinating. There was a lot of PBM stuff going on back in the 70s and 80s, before the internet. You could buy decks of chess postcards and send those back and forth between you and your opponent. It was a huge deal; all disappeared now, along with Flying Buffalo and its omnipresent founder, Rick Loomis.

Tunnels & Trolls was a tabletop RPG by Ken St. Andre, who had taken a look at Dungeons & Dragons and pronounced it too complicated. He was *right*, and TSR (and later, WotC) have struggled with that ever since. St. Andre decided to simplify combat by having each side roll all their combat dice at once. The team with the larger total won that round of combat and damaged the other side. The losing side could figure out how to divvy up the damage. There wasn't a lot of RPing going on during combat, though the magic spells, with names like "Take That, You Fiend!" and "Get Out Of Here!", could make wizards pretty popular. There were really only two classes; the non-magic-using Warriors and the magic-using Wizards, Rogues, and Wizard-Warriors. (It's explained in the rules that T&T rogues are more or less rogue wizards, and not quite thieves).

{{< youtube Zu78vsxwkaQ >}}

As I played through the first adventure, "Sword for Hire", I was struggling with turning those heavy, aged, 1980s page, and I thought it would be a lot easier if I could just spend dozens of hours writing a program that could run T&T solo adventures, and then dozens more hours transcribing the adventure into a YAML file.

{{< figure src="https://chasingdings.com/wp-content/uploads/2025/03/image-1024x646.png" title="Some of the YAML for the adventure" class="align-center" >}}

I'm only giving a thumbnail of the actual adventure text, because I am doing something I have always wanted to do; I am feeding all the information into a LLM and letting it do the making of the words nice. It knows everything about the current state of the game (its context) and can act out all the parts. Turns out that the only thing missing from a solo adventure was a DM.

This becomes problematic once I let other people into the game, as it requires an OpenAI API key to play, at the moment. I will probably preserve the AI-generated descriptions of the situations so that I can just bake them in, but narrating the ebb and flow of combat will be an issue. I really like how the LLM works with that. But, I can't really see myself releasing a game that would require someone to enter an API key, and I don't want the world using mine, so I'll have to remove it at some point.

I'm having a lot of fun with the game so far, but there is so much to do. I need to build in equipping weapons and armor, I need to make being overweight do something, etc etc etc. All sorts of QoL issues. Me, personally, I don't care, but if I start on adventure #2, "The Blue Frog Tavern", I'll want to have all the stuff I got in "Sword for Hire". Plus, Six Pack can be recruited, for new adventures, so that would be fun. I guess I have to build out a companion system, too...
