---
date: '2024-12-07T19:56:05-05:00'
draft: false
title: "Advent of Code 2024: The First Week"
summary: "AI has changed programming forever. It has changed Advent of Code and the way I work. What's life going to be like when AI can do my job, better than me?"
categories:
  - "Advent of Code"
  - "Generative AI"
  - "Programming Language"
tags:
  - "C"
  - "Clojure"
  - "Haskell"
  - "Java"
  - "Julia"
  - "Python"
  - "Rust"
featured_image: "https://chasingdings.com/wp-content/uploads/2024/12/DALL·E-2024-12-07-11.54.46-A-Tolkien-inspired-scene-depicting-graceful-elves-in-a-Tolkien-inspired-setting-repairing-a-rope-bridge-over-a-serene-river-surrounded-by-lush-vibra.webp"
cover: "https://chasingdings.com/wp-content/uploads/2024/12/DALL·E-2024-12-07-11.54.46-A-Tolkien-inspired-scene-depicting-graceful-elves-in-a-Tolkien-inspired-setting-repairing-a-rope-bridge-over-a-serene-river-surrounded-by-lush-vibra.webp"
---

I had a conversation with ChatGPT regarding people who post their LLM-generated code solutions to the global leaderboards and the r/adventofcode subreddit and try to pass them off as their own. Chat and I agreed that this was a little sketchy. I'd set it to solving a couple of the puzzles to compare with my own solutions and... it didn't do very well, usually going for a brute force, obvious solution over one that would be better approached with some nuance.

It would get the correct answer, but not in a way I would have felt proud to pass off as my own work. I provided some hints on algorithms and approaches it could try, and it came back with better code. Still clearly LLM-generated, but better. I wondered aloud to it if this is the future of coding; a human figures out the approach, and the LLM executes it.

This, of course, works well for me, as I am a tech lead, and my literal job (well, part of it anyway) is to decide upon an approach and ~~threaten~~ ~~coerce~~ convince the junior developers to actually implement it the way I said. I said as much to Chat, and it agreed that *my particular job* would be key to future software engineering. Problem is, developers become tech leads by learning the craft as junior developers, and that could take a decade or more. Once AIs have eliminated the need for junior developers... where do new tech leads come from?

[Someone on Reddit](https://www.reddit.com/r/adventofcode/comments/1h4qeij/i_built_an_agent_to_solve_aoc_puzzles/) invented a program that would use iterative prompts through test-driven development ([TDD](https://en.wikipedia.org/wiki/Test-driven_development), serious software engineering concept here, folks) to gradually and automatically lead the LLM to the correct solution given nothing more than the problem description. The program asks for the TDD test cases, then asks for code to satisfy them, continuing the loop of adding test cases and more code until it's done. Usually takes a couple minutes for the whole process. If they cheated, and they don't, they would place on the global leaderboard, entirely without human intervention.

I am *required* at work to use Github Copilot, an AI-driven coding tool described as automated pair programming (another software engineering term alert!). I also use it at home, and do use it during the AoC puzzles. I don't ask it for a solution until I have already solved the problem, but I do ask it to take a look at my code and find optimizations.

I stayed up late last night and finished the Day 7 problem before I went to bed. It was slow, but it worked. The problem was to take a list of numbers, like "20 2 7 6" and figure out what combination of operators would solve "20 = 2 ? 7 ? 6". So in this case, it would be "20 = 2 * 7 + 6". Well, the actual problem was, does there exist a combination of + and * that would solve that equation, which is a different problem entirely.

You can solve this by finding out every combination of + and * -- ++, +*, *+, ** -- plug them into the equation, try to solve it, etc. This is quick and easy for the small sample data, but quite time consuming for the actual input. This was the approach I tried last night, it was slow but it worked, and I went to bed wondering how to make it better.

I knew, going to bed, recursion was the correct approach, but I was too tired to figure it out. In the morning I went and implemented a much faster recursive approach. I looked at some other solutions on BlueSky and changed mine a little to make it faster, then made it multi-threaded to get it down to less than a second from a starting point of around 20 seconds.

{{< figure src="https://chasingdings.com/wp-content/uploads/2024/12/image-3.png" title="Time (ms) vs Language" class="align-center" >}}

Enter ChatGPT. I asked it to solve the problem and it proposed the exact same *slow* solution I'd come up with the night before. I hinted at the correct solution (well, my solution, which is by the doctrine of infallibility always the correct one) and it generated one pretty close to mine; a little more verbose but it was good. Tech lead powers activate.

Python is a slow language. There's a few libraries available that can run the program in multiple cores; the raw part 2 with recursion was 2140ms, and it was 793ms when done with parallel processing. Could using another programming language be better.

I asked ChatGPT to translate its solution to other programming languages. It might be better if I just used another language besides Python for these problems. I had Julia, Java, C and Rust installed already; I had Haskell and Clojure on my old computer but needed to reinstall them on this one.

ChatGPT's programs didn't always work first try. Most required a little debugging. I finally got them all running and I was a little surprised.

Clojure and Java both run on the same Java Virtual Machine (JVM). They compile down to the same pseudo-code and in fact Java and Clojure can load each other's programs. I would have expected them to take around the same time to run. They did not.

C is usually the fastest language around, as it compiles down to machine language. So does Julia. I'm not sure about Rust, but all three came in around the same time.

Java surprised me. I didn't expect it to end up so fast. I use it at work and don't really consider it a speed demon.

And then, there's Haskell. It first claimed it ran it in one millisecond. Color me dubious. I went over the code and checked the libraries and it all seemed correct. Then I remembered that Haskell is a functional language, and one thing about functional languages is that they are lazy. If the result of a calculation is never used, it is never calculated. The statement printing the output came *after* the statement capturing the end time. The program hadn't even *run* yet. I captured the time after the output was printed, forcing the program to run, and then got a more reasonable time of 7.2 seconds.

Which is really unreasonable, in a way. It's a language that compiles to machine language. It should be super fast, but it's the slowest.

My takeaway here is that I should be using Java :-) My code would no longer fit in screenshots, though. And I'd have to rewrite my back end into SpringBoot with Tomcat, and it just gets super complicated super quickly.

Anyway, that's been the first week of Advent of Code. Two more (and change) to go.
