---
date: '2022-08-30T23:51:54-05:00'
draft: false
title: "Blaugust theme week: Lessons learned"
categories:
  - "Blaugust"
  - "Blaugust 2022"
  - "Midjourney"
  - "OpenAI"
tags:
  - "Craiyon"
  - "Dall-E 2"
  - "Gpt-3"
  - "Tiddlywinks"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/08/DALL·E-2022-08-30-23.00.58-35mm-long-range-photograph-of-a-woman-warrior-reading-a-book-while-sitting-against-a-sleeping-green-dragon-near-a-mountain-lake-pastel-colors-peacef.png"
cover: "https://chasingdings.com/wp-content/uploads/2022/08/DALL·E-2022-08-30-23.00.58-35mm-long-range-photograph-of-a-woman-warrior-reading-a-book-while-sitting-against-a-sleeping-green-dragon-near-a-mountain-lake-pastel-colors-peacef.png"
---

I spent the 31 days of Blaugust working to see if I could get AI to show some creativity in game design, and if I could get AI image generation programs to produce the art I want at a price I could afford. I learned some things.

I used OpenAI's GPT-3 "text-davinci-002" text completion tool. I chose this because most of the alarm over how the rise of AI would be the death of writing tended to surround this particular tool.

After the short trial period, GPT-3 is not free. It's also not particularly expensive -- pricing is on a per-token basis, where a token is a word. I've used it heavily this past month for all sorts of things; blog posts, but also plays, fantasies about video game heroes, bunches of other stuff. I've also started writing a Python program that will upload a bunch of facts that it will then be able to use to become a targeted, intelligent query system. I'll write more about that when I get to it.

Price is reasonable -- US$21.28 for everything I have done so far. They substantially decreased the price per token for all their text tools, including davinci, midway through the experiment and so there's not really any reason not to use it.

The problem is, is that it's like a stubborn child who really doesn't want to talk about their day at school.

> Me: Did your friends do well on the history test?
> You: I don't know.
> Me: What was the math test about?
> You: It was about basic operations like addition, subtraction, multiplication, and division.
> Me: Did you know that division is just multiplication upside down?
> You: Yeah, I learned that in class.
> Me: I know a song about fractions.
> You: Please don't sing.
> Me: Do you need help with your homework?
> You: No, I'm good. Thanks.
> GPT-3, when told to pretend it was a stubborn child who wasn't telling its mother much about their day at school.

This shows davinci's strength -- that of a chatbot that can take on a role you define. And it shows its weakness -- it really can't hold a creative conversation. The prompt set up the basic situation, and it didn't stray far from it.

During the Blaugust AI experiment, it could occasionally surprise me with game ideas, but if it strayed too close to something in its database, it would refuse to move on from it. For instance, on day 24, it refused to generate any ideas that didn't involve the TV show "24" in some way, though it could be sneaky. Similarly, any text adventure it suggested had a private detective as the main character. Every single time.

It also has a lot of trouble following a plot and keeping characters consistent. Here, I set up a situation where Alice would speak English, and Betty would speak only German, and they would struggle to make a lunch date downtown. I was really explicit about this.

> Betty: Ach du Lieber! Alice, mein freund! Wie geht es dir?
> Alice: Hey, Betty. I'm sorry, I don't understand what you're saying.
> Betty: Oh, I'm sorry. I've been speaking only German lately.
> Alice: Yeah, I noticed. It's been a little tough to communicate with you.
> Betty: Ja, I know. But it's so much fun to practice my German!
> Alice: Well, that's great. But can we speak English so we can make plans for lunch?
> Betty: Of course! Let's meet at the restaurant downtown at noon.
> Alice: Sounds good to me! See you then!
> Alice and Betty, GPT-3

We'll have to forgive Betty misgendering Alice. Also, I'm pretty sure nobody says Ach du Lieber in real life anymore. Point is, that davinci will always take the easy way out. So I rewrote some of Betty's dialog in German to keep her on track, and things went better.

> Betty: Alice! Hallo! Wie geht's?
> Alice: Oh, hi Betty. I'm sorry, I don't speak German.
> Betty: Ach, das ist schade. Ich will mit dir nur Deutsch sprechen.
> Alice: Well, that's too bad. I don't understand German.
> Betty: Wie schade. Kannst du nicht ein bisschen Deutsch sprechen?
> Alice: I'm sorry, Betty, but I don't know any German. Do you think we can meet for lunch downtown? I know a great place.
> Betty: Ja, das klingt gut. Wann sollen wir uns treffen?
> Alice: How about noon? Does that work for you?
> Betty: Ja, das ist perfekt. Wo sollen wir uns treffen?
> Alice: Meet me at the corner of Main and Elm. I'll text you the address of the restaurant.
> Betty: Gut, bis bald!

GPT-3 solves the communication issue by having Alice magically learn to understand German halfway through, though perhaps she actually did know the language but was just pretending not to.

This isn't an extreme example. I worked harder at the beginning of the project to keep GPT-3 on track, but toward the end, I just let it do whatever, asking it leading questions to get it to suggest more. I got a few good ideas out of it, but every one of the 31 game ideas were ideas that I had to pull together from the fragments it would give me that I thought sounded cool. And then once I had got a good foundation, GPT-3 would often be able to fill in the blanks -- the names of Madame Miracle's cats, and their powers, for instance, on day 6.

But press a button, watch it spit out great articles with no interaction -- no, really. Just no. Though I did get a good seven paragraphs out of it about recent Tiddlywinks championships, though it was entirely fictional (I checked). Similar articles about Chess and League of Legends seemed to have facts. If GPT-3 knows the answer, it will tell you. Otherwise, it will happily make something up.

How I'll use it in the future? It's not bad at writing summaries, and sometimes it will suggest a post title that works. Who knows, maybe I'll try to use it to generate ideas. I'd love it to interview me about something and then go write an article about it (and I did do that, in my review of Stray, and it was fun), but working with GPT-3 is just like working with any other tool. You get out of it what you put into it.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/08/4dragons.png" title="Four similar pictures at increasing resolution" class="align-center" >}}

**The Art -- Midjourney, Craiyon, and Dall-E 2**

The prompt here was, "woman reading a book sitting against a sleeping green dragon". I modified it to make it a little more realistic each time. I then used Dall-E 2's editing function to expand a fifth one out to a larger scene.

I'm pretty sure what AI does best is to make mashups of stuff it already knows. It clearly does that for text -- if you ask it about something fairly well known, I guarantee the consistent, well-written text it generates was copied from someone else's writing. If you ask for some art, I bet it steals from only the best, mashes it up, and applies a filter to it.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/08/image-12.png" title="A newspaper photograph of the winner of the World Singles Tiddlywinks Championships using his squidger to flip the final wink into the cup." class="align-left" >}}

Or something. I honestly don't know the details of how it uses its training to come out with images that match your prompt. During my AI project, some of the images that came out were so appropriate and so perfect, I knew they had to have been stolen. The art for the Day 30 banner, for instance. The man in the middle was no creation of any AI.

I relied on Craiyon heavily in the beginning, as it was a really good, and free, way to refine prompts until it felt like I had a good enough handle on what I wanted to bring it to the paid services, Midjourney or Dall-E 2.

OpenAI's Dall-E 2 charges US$15 for 115 prompts, and gives free prompts every month. I'll be getting 15 free prompts today, I think. I know I'll use them. I meant to go to Midjourney once my first batch of prompts ran out on Dall-E 2, but then I didn't. All these AI art generators have learning curves.  If you have an idea of what you want to see, getting Dall-E 2 to generate is very possible, but you have to know how to ask, and understand that anything you don't explicitly specify will be randomly decided.

This randomness is both Dall-E 2's strength and weakness. Most of us can't create usable illustrations. Almost none of us can create finished art in 15 seconds.

In the examples of the woman and dragon above, I specified a sleeping dragon. In the first image, the woman has apparently killed the dragon with a sword through its head. The next two have a very awake dragon. The last one has what might be part of a dragon toward the bottom. The banner image has a non-sleeping dragon, and what looks like the head of a second dragon next to the woman.

The art Dall-E 2 generates is fast, and usually wrong. It's fun to just type in random things and see what you get, but if it's something specific you want -- well, good luck. If someone else's art had something similar, then it can probably do it. Ask it for something that is outside its training, like the photograph of the Tiddlywinks champ above, and it just tosses things together.

Now comes the really fun part. What if I wanted the champ there to stand up and receive his well-deserved championship trophy? I would never, ever, generate anyone who resembled him in any way, ever again.

This is Dall-E 2's greatest weakness -- repeatability. Dall-E 2 does allow the uploading of images to use as seeds for new images, but it doesn't allow the uploading of realistic humans in order to prevent abuse. So, I couldn't tell Dall-E 2 to say, "more like him, but standing, with a trophy!". It won't do copyrighted characters at all. There's a new AI tool coming up which doesn't have these restrictions, but I haven't used it.

Even with unrealistic characters, everything is more or less a one-shot. DE2 will generate something for you, but if you want to work with it, you'll probably end up importing the result into a paint program and working on it yourself. Like GPT-3, DE2 has no memory.

Now, you *can* load your own facts and prompts in GPT-3, which will give it domain knowledge over that subject, and it will be able to use that, for instance, to give Alice and Betty a lot of context that davinci could then use when writing their conversation. If davinci generated some fact you liked, you could add that to the uploaded context and it would take that into account from then on. If you were writing a novel, for instance, you could perhaps encode all the relevant facts about characters, plot, and setting, and then perhaps GPT-3 could work with you.

DE2, though -- not so much. If I wanted DE2 to illustrate a children's book for me, it would be hard-pressed to generate the characters in any two images that would in any way resemble one another.

GPT-3 won't put any writers out of business. DE2 won't put any artists out of business. They might get there, someday, but they aren't there now. The text, and the art, they generate isn't going to replace words or art that would have been bought from a writer or an artist. They are just -- new tools.
