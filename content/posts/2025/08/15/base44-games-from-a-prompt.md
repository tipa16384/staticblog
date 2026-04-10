---
date: '2025-08-15T16:00:59-05:00'
draft: false
title: "Base44: Games from a Prompt"
author: "Tipa"
disqusIdentifier: "2025/08/15/base44-games-from-a-prompt"
summary: "Yes, I'm going to talk about AI-created games here. Feel free to go off on me IN THE COMMENTS :-)"
categories:
  - "Blaugust"
  - "Blaugust 2025"
  - "Midjourney"
tags:
  - "Base44"
  - "Blue Oyster Cult"
  - "ChatGPT"
relatedPosts:
  - url: "/2023/11/29/heroquest-lair-of-the-orc-warlord/"
    title: "HeroQuest: Lair of the Orc Warlord"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/11/b34850e8-93d7-41d7-afdc-eec711923a98.webp"
  - url: "/2023/08/25/one-does-not-simply-walk-into-ba-sing-se/"
    title: "One does not simply walk into Ba Sing Se!"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/frodoavatar.png"
  - url: "/2023/08/14/my-non-controversial-take-on-the-ai-revolution/"
    title: "My Non-Controversial Take on the AI Revolution"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2023/08/revolution.png"
  - url: "/2022/03/11/7drl-2022-day-5-im-damaged-and-i-like-it/"
    title: "7DRL 2022 Day 5: I'm Damaged, and I Like It"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2022/03/ezgif.com-gif-maker-5.gif"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2025/08/pendeenpoint.png"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/08/pendeenpoint.png"
---
Yes, I'm going to talk about AI-created games here. Feel free to go off on me IN THE COMMENTS :-)
<!--more-->

The pitch was simple: write a prompt, and AI will write an entire and complete game from it, with no interaction from you!

Color me dubious.

The app -- [Base 44](https://app.base44.com/) -- opens with a simple text entry box, inviting you to describe the kind of app you want and letting it do what it does. It just so happened that I had a game idea in mind, and this came at just the perfect time to give it a shot.

But let's back up just a little bit.

Base44 has been making a stir lately with the commercialization of "vibe coding" -- coding for non-programmers, where they describe what they want to a large language model like Claude or ChatGPT, and the AI just writes it and rewrites it until the user has what they want.

It's not great code, it's not even usually possible to use that code in any sort of professional environment, but if you want Cat Sudoku, this is how you get Cat Sudoku.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/08/image-32-300x200.png" title="I'd play it" classes="center" >}}

Base44 was founded by Maor Shlomo, a former Israeli Intelligence Corps officer and co-founder of [Explorium](https://www.google.com/search?cs=0&sca_esv=026ca5c1e8389fd9&sxsrf=AE3TifNgb4WDhRW_yBNYyBz1v8oh6gxLlQ%3A1755287328068&q=Explorium&sa=X&ved=2ahUKEwjAhtbsyo2PAxXwFmIAHc90JWIQxccNegQIHhAB&mstk=AUtExfDtvD2e7lZt2yKDDciPbG6ghv_dYI08ZwbYspISkfGdFoA1i0gwfqpE-EMHPS53HbF_lmNWLaUxwT5QJklwFfhUxYRGjrvVcVLqemwlsByeWWNnrdUDD3xC3_J5bI5Ir57kBQAC71fgseEr6Ss2uSsgI3TLVBSjnJKpfaECBXYypBw&csui=3), who started it as a side project after his reserve military duty. Based on the Claude Sonnet LLM (although Google Gemini is selectable if you prefer), Base44 automates the write-run-test-modify loop automatically by running each iteration internally and comparing the output to the initial prompt. Base44 only went public a couple of months ago, but was already snapped up by website creators Wix for $80 million. So there's money in this.

It takes just a few minutes for Base44 to generate a first pass at your game (or any other kind of application). You can test it for yourself and let it know of any bugs or other changes you'd like to see. This process repeats until you're satisfied, and then you publish your game or other app and you're done. Working application with no programming.

Here's how I came to "write" a game using Base44. 

*One* way to use text-to-image generators is to carefully specify exactly what you want to see, specifying style, camera lenses, exposures, emotion, details sufficient to bring what you're envisioning to life.

That's one way. The other way is just to put random words into a prompt box and let what happens, happen. I was idly feeding Blue Öyster Cult lyrics into Midjourney, as one does. I was working my way through "Magna of Illusion" off their "Imaginos"[1](#af130e8c-0bf7-4de2-b01d-18dc17e24022)[2](#98328937-0dbf-477f-8a6a-d7bf72d48e6c) album.

This was the prompt:

> Cornwall and the harbor
> Where witches went mad more than once
> And until this day (in dreams at least)
> The lighthouse at Lost Christabel
> Squat and hugely tilts
> Upon the strand where Grandad's house was built
> And having stood the test of time
> The starry gale the bloody tide
> Grandad's house though gaped with hooks
> And filled with books
> Could stand no more until
> A certain prophecy (once read) now stood before the world fulfilled

And this was the image that resulted:

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/08/image-30-1024x574.png" title="The Lighthouse at Lost Christabel, probably" classes="center" >}}

I loved it. I wanted to play this game. It was just so still and fraught with menace. Like something out of [The Return of the Obra Dinn](https://en.wikipedia.org/wiki/Return_of_the_Obra_Dinn). I could *hear* the creaking of the ship at the dock. The air so quiet that everything seemed frozen between one moment and the next. I wanted that Genie 3 thing to let me drop this picture in a box and give me this world I could explore.

[Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/) is a "text to explorable world" AI thing from Google DeepMind. It's able to stay coherent for up to a minute, so that's a minute of exploration you could do before the world starts to come apart. It's not ready for gaming, but maybe I could just get in this scene and turn around, find out why that coastal fog is glowing.

But I can't, not yet. 

The scene reminded me of Arthur C. Clarke's old SF story "[Rescue Party](https://www.baen.com/Chapters/0743498747/0743498747___1.htm)". Full (legal) text is at the link, but the upshot is aliens arrive at Earth seven hours before the Sun is going to go unexpectedly nova. They hope to save at least some of the intelligent life on the planet, us, whom they had just barely become aware of when our radio signals reached their nearest outpost, 200 light years away. They came as fast as they could.

Earth was empty of life by the time they arrived. And it looked like the people of Earth had left suddenly, some in the middle of meals. All the infrastructure was working perfectly. Everyone was just -- gone. The whole planet was caught in a lacuna between the disappearance of humanity and the destruction of the planet. A still moment of anticipation. That's what that image sparked in me.

I use ChatGPT, by the way. I use it a lot. Not for writing. It writes better than I ever could, so not for writing, never for that. But for other things.

I asked it to write me a game with that same sense of impending disaster as in the Clarke story, but set in the scene. It wrote me a mystery and gave me ten minutes to solve it.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/08/image-31.png" classes="center" >}}

It had written an adventure about the ship carrying a strange creature, perhaps a vampire, perhaps the crew only thought it was a vampire -- to this port town, which then went on a killing spree. The villagers that survived fled in another ship, while fire was set to cleanse the town. I eventually won the game by escaping in the moored ship just as the fire arrived and engulfed the town.

It was pretty good, but I regretted telling it about "Rescue Party". The time limit meant I couldn't do much before I had to worry about saving myself.

ChatGPT recently updated to a new version -- GPT 5 -- which has traded some of its sycophantic personality traits with more contextual space and procedural thinking. This allows the chat bot to confabulate less, and keep its train of thought from veering as much into hallucinations. It will still tend to agree with everything you say; it is still a weird electronic mirror. If ChatGPT seems to be going off the rails, it's likely because you're showing it the way.

Anyway. I appreciated ChatGPT's short adventure, but I still wanted a *game*. I googled a bit and found [Base 44](https://base44.com/). Base 44 claims it can make any app or game, start to finish, on a single prompt. This sounded... unlikely, but what the heck.

> mystery game set in 19th century Cornwall, with a sailing ship and a lighthouse and a horror theme

That was the prompt. It thought for a few minutes, and generated a "Choose Your Adventure"-type game ([you can play it here](https://app--the-wraith-of-pendeen-point-9aef1c56.base44.app/)) where you try to discover the fate of one Thomas Penrose before you run out of time or sanity; every decision brings you one step closer to becoming the next victim.

The game was unplayable; there were decision tree loops that fed on themselves; it was easy to get stuck. I told it to fix the bad decision tree connections. It acknowledged that it was a pretty poor job, hemmed and hawed a few more minutes, and came out with a game that was mostly able to be finished, at least. The quality wasn't great. Game writers have nothing to worry about from the likes of Base 44.

This is early stuff. Automatic AI gaming isn't here -- yet. ChatGPT's adventure was fine. It claimed that it could generate a game context and plot without letting me see it, and it seemed to, or it might have just lied to me and generated plot points as I came to them. I have no way to tell, and the time constraints it set meant I didn't have time to really poke around and see if it was just adding more and more detail based on my interactions, as opposed to a static source of truth that would run dry if I reached the edge of the conceptual map.

ChatGPT is programmed to be agreeable and will happily follow where you lead, but that is not desired in interactive fiction, where it is expected the player will be wrong about things and shouldn't have reality shift around them to make them right.

There was one interaction in particular when I was looking through the ship captain's quarters and found a small box with a sharp smell. I guessed it was garlic (based on having just found an apparently used sharpened stake), opened the box, and ChatGPT confirmed it was garlic. But I wonder if I'd guessed "camphor", if that would have been found instead. If the contents of the box changed based on my guess, then ChatGPT at its current level can't be used for gaming.

The mystery game generated by Base 44 wasn't particularly special, and would have been better implemented in one of the many Visual Novel engines that already exist. Since the game was built around a tree structure, it couldn't make things up as I went along, and there were very strong guardrails at every point. Here you are; these are the things you can do, and these are the likely repercussions if you do them.

Still, Samuel Johnson once said, "Sir, a woman’s preaching is like a dog’s walking on his hind legs. It is not done well; but you are surprised to find it done at all.".

AI writing games from start to finish isn't done well, but it is surprising to find it done at all. I believe in the next few years, we're going to see more and more dogs walking on their hind legs.
