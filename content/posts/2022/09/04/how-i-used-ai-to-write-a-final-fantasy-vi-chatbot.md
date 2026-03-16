---
date: '2022-09-04T21:25:13-05:00'
draft: false
title: "How I used AI to write a Final Fantasy VI chatbot"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2022/09/04/how-i-used-ai-to-write-a-final-fantasy-vi-chatbot/"
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
summary: "GPT-3's real power comes when it can use AI to help people find what they need. In this case, information about Final Fantasy VI. Read on to find out how I used AI to help make a FF6 chatbot -- TerraChat."
description: "GPT-3's real power comes when it can use AI to help people find what they need. In this case, information about Final Fantasy VI. Read on to find out how I used AI to help make a FF6 chatbot -- TerraChat."
tags:
  - "Final Fantasy"
  - "General"
  - "OpenAI"
  - "Celes"
  - "Chatbot"
  - "Dall-E 2"
  - "Gpt-3"
  - "Terra"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/09/DALL·E-2022-09-04-21.21.57-A-magazine-illustration-of-a-woman-with-dark-green-hair-in-a-high-ponytail-wearing-overalls-constructing-a-giant-mechanical-steampunk-chatbot-with-h.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2022/09/DALL·E-2022-09-04-21.21.57-A-magazine-illustration-of-a-woman-with-dark-green-hair-in-a-high-ponytail-wearing-overalls-constructing-a-giant-mechanical-steampunk-chatbot-with-h.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

When I started my Blaugust project to create 31 game ideas using AI as much as possible, the actual end goal was to learn to create AI-powered tools to help me with blogging -- generating ideas, titles, excerpts, correct spellings and grammar, things like that. Things that GPT-3 is actually well suited to handle.

During August, I started playing FF6 on my SteamDeck and on the PC. I haven't played this game all the way through for a long, long time, and I'd forgotten most everything.

So I thought about loading up GPT-3 with all the Final Fantasy VI information I could find on GameFaqs, Reddit, Wikis, anything I could find. Massive copyright violation. And then I could just pack this into a chat bot and ask it anything I needed to know.

I did write the chatbot, picture below. It is real and does work, but since it costs me a small amount of money whenever I ask a question, it would be expensive and pointless to put it on a public facing server where some spammer would eventually land me with a million dollar hosting bill. So this... this is just for me. The code is at [my GitHub page](https://github.com/tipa16384/tinyprogs/tree/main/openai). You'll have to provide your own OpenAI API key. Just run oai.py and point your browser at it.

I'll go into more detail past the pic. 

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/09/image-1024x745.png" title="Actual conversation with TerraChat." class="align-center" >}}

**Telling TerraChat about Final Fantasy VI**

The standard GPT-3 Da Vinci text engine actually has quite a lot of Final Fantasy 6 content built-in, but there's lots of gaps. Da Vinci will happily make stuff up for anything it doesn't know, and there's no way of telling when it's giving actual information versus just spinning an elaborate web of lies.

There are two ways of getting information into the text engine. One is by overloading the prompt with all sorts of background information. You have 4K tokens, minus the expected length of the response and minus the expected length of the question, to just put in any particular information. Right now, the prompt I use just instructs Da Vinci on who it is supposed to be (Terra, from Final Fantasy VI), some information about herself and her goals, and the list of dances Mog can learn.

It was bugging me that she would just put in some random real world dances.

After that, you can just chat with Terra in the GPT-3 Playground all you like. But she won't know anything Da Vinci didn't already know about Final Fantasy VI.

Enter "Fine Tuning". This is where you prepare a large number of sample prompts and answers. Like, "What are Ultros' elemental vulnerabilities and status weaknesses?", and then you'd provide that answer. I wrote a tool that generates various sorts of prompt/answer pairs -- it's in the repo. OpenAI has a tool that takes the CSV that generates and formats it as a JSONL file, making some suggested changes to improve the fine tuning.

Then comes the tuning itself, which cost about a buck each time I ran it. The Da Vinci model isn't available for tuning; it recommends the previous model, Curie, to handle that. It runs through the data several times (called 'epochs'), and you can play with various other parameters to potentially improve results. I built three fine tuned Curie models, each with a different set of prompts and answers, and... it was very disappointing. Using Curie instead of Da Vinci was a HUGE step downward, and it was very hard to get information out of it.

Granted, I only had about four thousand training tuples vs the hundred thousand or so it likes, and I only used the default four epochs. I might have improved it, but I just don't think there's any way that interacting with TerraChat in a natural way could extract that info.

So I abandoned that for now, and overloading the prompt is what current TerraChat uses.

**Writing a chatbot in Python**

This was actually fairly easy, as there are examples online, and I just took one. I also subscribe to an AI code generator, GitHub Co-pilot, so I mostly only had to take all the stuff I'd set up in the OpenAI playground and get it working locally.

That was pretty easy, and that was where I was last night. Nobody wants to use a terminal window, though, and that meant... bringing it onto the web.

**Bringing up a Flask web server**

I mentioned GitHub Co-pilot, right? I opened up my Python chatbot program and asked it to write a web server with parameters I specified, endpoints and the such.

And it did. I added some routes to get the static web page that would be driving all of this, the "favicon.ico" for the tab bar, a route to get the images and stuff I'd be using, and that was that.

I ran the server and hit the test URL and it responded with "Hello, World!" and it was ready for the *fun* stuff, finally.

**Writing the web application**

I'm ages behind the curve for writing web apps. I'm still mostly using jQuery. Fortunately, GitHub Co-pilot knows all about HTML and jQuery. I asked Co-pilot to make a quickie form with a text box, an input box, and a submit button, and it did that. It looked terrible, but it was good enough to get input into the chatbot.

I initially just used straight POST parameters, but then I asked both the back end and front end to write a RESTful JSON-based interface, which it did.

I designed the UI to look like a chat conversation -- this was work I did. The part you need a human for. I set to tune that for a few hours. I designed the CSS (though I had Co-pilot do a little of this work, specifically for the gradients).

**AI is taking my job!**

No, it isn't. There is SO MUCH talk about AI killing jobs for creatives. Well, I am a creative, and AI is coming for coders as much as it's coming for artists or writers.

And you know what? I am FINE with it. I had no desire to pore through online docs for setting up a Flask server or a RESTful service, or the parameters for the $.ajax call, or the URL where Google CDN stashes its jQuery library -- I didn't want to worry about ANY of that. I just wanted to make it fun and look good.

I really can't speak for artists and writers. But I would be shocked if AI didn't turn out to be just another tool in their toolchest. Artists will be able to make *more art*. Non-artists will be able to make *okay art* that wouldn't have otherwise existed.

Because none of these AI tools will do a damn thing without a human guiding the job.

TerraChat was fun to write, and I used a lot of AI to make it, but it was my idea, my algorithms, my design. It just saved several trips to StackOverflow. The icon images were done by an actual artist and the artist released them for any and all uses. Terra chatting on a laptop was done by Dall-E.

No artist was going to draw that for me today. Though if I were going to make this a commercial product for some reason, I'd probably commission something. For a personal project that nobody but me ever uses, I think I'm in the clear here.

Me, though -- I'll be dancing the Ultros Boogie.
