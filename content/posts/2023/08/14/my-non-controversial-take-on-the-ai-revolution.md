---
date: '2023-08-14T08:10:52-05:00'
draft: false
title: "My Non-Controversial Take on the AI Revolution"
summary: "At least, I haven't heard anyone contravene my take, yet."
categories:
  - "Blaugust"
  - "Blaugust 2023"
tags:
  - "ChatGPT"
  - "Copilot"
  - "Github"
  - "Programming"
  - "Substack"
featured_image: "https://chasingdings.com/wp-content/uploads/2023/08/revolution.png"
cover: "https://chasingdings.com/wp-content/uploads/2023/08/revolution.png"
---

At least, I haven't heard anyone contravene my take, yet.

My first personal experience with what we're calling AI these days was with Github Copilot. Breaking this down a little; Github is one of the most popular source code control systems used today; lots of people use it. I use it for my personal projects. The place where I work uses an enterprise version for all its source. Github has an almost unimaginable access to programming source code from around the world, working on every conceivable problem.

Github Copilot is a large language model (LLM) AI trained on this entire corpus of source code. It watches what you type and suggests completion, based on what it has learned from other programmers. In its most helpful mode, it will read your comments on what the code should do, and just offer you the complete solution.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-32.png" title="I asked for a C++ program to return a list of primes. This is probably someone's verbatim code." class="align-center" >}}

The first time I tried this, I felt like my job was in danger; if not now, then within a very few years.

I don't feel like that any more. My job may someday be on the line, but not with LLM-based AI.

If my job was actually concerned with writing small, standalone functions, I'd be scared. But that isn't my job, at all, and in all my years being a programmer, has never been my job. My current project has tens of thousands of lines of source code. Maybe hundreds of thousands. It all has to interact with systems across the company and outside of it. It has to conform to security concerns. It has to be written to a specific style. The unit tests must be written to a certain standard, and the test cases themselves are defined by the business. Actual humans have a tough time with all this and it takes months for a new developer to be comfortable working with our legacy codebase that stretches back a decade or more.

Copilot is blocked at our company, but I have enough experience with it now to know that it would be entirely useless.

However, Copilot does have its place.

{{< figure src="https://chasingdings.com/wp-content/uploads/2023/08/image-33.png" title="Copilot code" class="align-center" >}}

I know nothing about how to make a web page scraper in C++. I asked Copilot to write a function that would read the Google homepage and return the number of HTML DIV elements on it. Copilot kindly worked its way through the CURL library to hand me this solution.

It's just incidental that the code as written wouldn't work (it simply returns the entire web page). At least it would be a starting point. I do use Copilot in my personal projects, but it works for me as a "smart autocomplete". I certainly wouldn't trust it to do anything too complex.

One time, I was writing a comment for something, and it suggested, as autocompletion, code I had written for a different project. That was creepy.

So here's the pros and cons of Copilot:

- Pro: useful as a starting point

- Con: probably stole some other programmer's code to do it

- Con: code is usually buggy

- Pro: Once it has enough context with the source you're working with, can actually suggest helpful things

- Con: That it probably also stole

Copilot is a tool that was trained on code that was probably used without the knowledge of its original author. But it is *just a tool*. Anyone who relies on it too heavily is going to end up jobless.

**ChatGPT**

Now, here's the controversial take: anyone who thinks ChatGPT is going to replace them is crazy. It has all the same limitations as Copilot here. Works on stolen text. Cannot create anything on its own. If the writing isn't self-contained -- if it depends on previous work -- ChatGPT isn't going to be able to help.

In short, if your work is such that ChatGPT could do it... you need to find better work. Put another way, all ChatGPT can produce is garbage content. If your job is producing garbage content... well. [I have a Substack](https://tipa.substack.com/) where I put some of the stuff I asked ChatGPT to generate. Some of it is funny, but it's all actually garbage.

The header picture up top was what Dall-E 2 generated when I asked for a picture of the AI revolution. It's garbage.

The AI revolution, as it currently stands, is just a generator of garbage. You can find gems in garbage, but you have to dig through a lot of garbage to find it.
