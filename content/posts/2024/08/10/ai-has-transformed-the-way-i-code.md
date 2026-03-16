---
date: '2024-08-10T08:00:00-05:00'
draft: false
title: "AI has transformed the way I code"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2024/08/10/ai-has-transformed-the-way-i-code/"
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
summary: "Github Copilot and other LLM-powered coding tools have become indispensable to many in the software development industry. AI is not a fad; it's here to stay."
description: "Github Copilot and other LLM-powered coding tools have become indispensable to many in the software development industry. AI is not a fad; it's here to stay."
tags:
  - "Blaugust"
  - "Blaugust 2024"
  - "Generative AI"
  - "Copilot"
  - "Github"
  - "Waffle"
featured_image: "https://chasingdings.com/wp-content/uploads/2024/08/copilot.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2024/08/copilot.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

Large Language Models (LLMs) can generate art, but I am not an artist, it isn't coming for me. They can write, but I am not a writer, I'm not affected. They can code... and there's where I come in.

A couple of years ago, I looked at AI-powered coding tools with a lot of anxiety. I was an early beta tester for Github Copilot. As I asked it to generate various bits of code, I was impressed with how good the code was. I could definitely see that at some point in the future, my job would be *gone*. Nobody would ever need to actually code again.

Last year, I was in a pilot program to bring this technology into my actual place of work; and earlier this year, it was opened up to all coders in the company -- hundreds of us, probably. (It's a big company).

I'm more convinced than ever that this technology will not take any programmer jobs; not one. And I hate to generalize, but I can't think it's going to take all that many writing or art jobs, either. I could be wrong! But my own personal experience is that the coding portion of my job goes faster, and the code is of higher quality, and I have more time to do the creative parts of the job. Working on the design, collaborating with other teams, architecting the really complex bits. The boring parts of the job are getting automated.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/08/image-22.png" title="Capture of my Waffle solver" class="align-center" >}}

There's a word game, [Waffle](https://wafflegame.net/daily), which gives you a grid of letters that you have to swap until you find a solution within at least ten but no more than fifteen swaps.

I came up with an algorithm to solve the puzzle (and later, found a better algorithm in a Reddit post).

I described the algorithm to Copilot, and it spit out some code. It was bad code, but it was a starting point. I worked on it, and it kept offering suggestions until we were both on the same page with it.

I wanted it to respond to REST events so that I could write a front end for it in HTML. It gave me the basic skeleton for a Flask app in Python. I then wanted the front end in HTML. I just went ahead and wrote it myself, but then to add the user interaction, I turned again to Copilot to write the Javascript for me, given a description of what I wanted it to be.

Just tonight, I got tired of my programmer UI and asked it to pretty it up a bit, and the result is what you see above.

All the fun stuff -- how it works, how the solutions are displayed and all that -- that's me. The boring stuff about drawing gray squares into a canvas element -- I let Copilot do it.

I asked ChatGPT to continue:

> For writers, LLMs might not be a replacement but could be a helpful tool. From what I’ve seen with coding, these models can handle the more tedious tasks, like generating rough drafts or offering different ways to phrase something, which might allow writers to focus on the creative parts they care about most. I’m not a writer, so I can’t say for sure that it’s the same, but there’s a chance that LLMs could help make the writing process more efficient, maybe even more enjoyable. It’s worth considering them as a tool to support your work, rather than something that could take it over.

Okay, back to the human again. I do like trying to write, and I really don't like the kind of writing it comes up with. It keeps trying to wrap everything up. It doesn't like loose ends.

I was working for awhile on a short story, "The First McDonald's on the Moon". I had it all blocked out. I brought it to ChatGPT and it did a horrible job. Gross and hackneyed and not at all what I wanted. But in trying to describe the story I wanted to the LLM, I got a better idea for how I wanted it to flow, how it would end. In the end, I haven't written it, but I think I *could*. Part of that is due to having the LLM to toss ideas against.

I can't imagine ChatGPT or any of the others could usefully replace any human writer who wasn't doing the most basic, rote stuff.

But I could be wrong. Actual writers may find that ChatGPT can do their job well enough that their jobs are threatened. I'm not one, I can't say that won't happen. But for programming -- it's a useful tool, and it is transforming the industry. No LLM will ever take a programming job. Maybe, in the future, it will be able to take design documents and the body of existing code and spit out solutions, but I can't see that happening in any future I can see. It's not there now, and I don't think it ever will be.
