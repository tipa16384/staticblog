---
date: '2025-01-25T09:00:00-05:00'
draft: false
title: "AI is going to steal my job -- and I couldn't be happier"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2025/01/25/ai-is-going-to-steal-my-job-and-i-couldnt-be-happier/"
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
summary: "Taking an idea to reality takes just minutes, even if you don't know one thing about programming. It's a new world."
description: "Taking an idea to reality takes just minutes, even if you don't know one thing about programming. It's a new world."
tags:
  - "Malifaux"
  - "AI"
  - "ChatGPT"
  - "Python"
featured_image: "https://chasingdings.com/wp-content/uploads/2025/01/minitray.png"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2025/01/minitray.png"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

I'm a programmer. Aside from a few odd jobs, programming is all I've ever done. I think I'm pretty good at it; people keep wanting to pay me to do it, anyway.

But that's all going to change. The place where I work has decided to lean into AI-assisted programming in a big way. We're required to use Github Copilot in our jobs, and we're tracked on how much AI generated code makes it to a finished product. More is better. Our team is among the best with it; 25% of the generated code makes it into a release. Management wants that number far higher.

My job is right in the crosshairs of AI. Maybe I'm fine with it.

I'm headed to CaptainCon in Rhode Island next weekend, where I'll be playing Malifaux. I have a new crew -- December -- and I want to show them off. I've been working my butt off painting them (not done yet), and I want to display them at their best while I'm there.

So I thought it would be fun to 3D print a tray designed to securely hold my team, with no wasted spaces. And, being a programmer, I thought it would be fun to make a program that would take as input the number and sizes of positions I wanted, and have it spit out a completed design.

I've done similar stuff; back at Archipelago, I wrote a Coulomb's Law applet (remember applets?) that arranged charged particles in minimum energy configurations. I thought that I could make that work. And then I did a springs simulation when I was working on a mapping program for Colossal Cave Adventure. Both had solutions that were more dynamic than I'd like.

{{< figure src="https://chasingdings.com/wp-content/uploads/2025/01/image-33.png" class="align-center" >}}

So, I asked ChatGPT (above) to do a little simulation for me. After some discussion and back and forth with different approaches and correcting its errors (it doesn't know when it makes errors), it popped out this chart:

{{< figure src="https://chasingdings.com/wp-content/uploads/2025/01/image-34.png" class="align-center" >}}

I was at work for all this, but I thought I could take this further.

When I got home, I asked ChatGPT to take it a step further. I wanted a program that would let me select a circle size and a position and handle overlaps.

{{< figure src="https://chasingdings.com/wp-content/uploads/2025/01/image-35.png" class="align-center" >}}

And it did, it did just that.

{{< figure src="https://chasingdings.com/wp-content/uploads/2025/01/image-36.png" class="align-center" >}}

And it fixed it. Tied it up in a bow, too. I asked it to add SVG export, and it did. In the header image, you can see the program running, with the shapes. And then I could import it into a 3D printer slicer as a negative space to a cube primitive and then print it. The picture of those minis -- my December crew -- show them in a tray designed by the program.

I did a little correction on the program it wrote, but mostly I was content to just tell it the changes I wanted and let it do the work. ChatGPT sets up a collaborative editing environment and works with you on the program.

So yeah. The days when I have to stare at a blank IDE window and type "from collections import defaultdict" or something are pretty much over. I'm looking forward to not having to do that at work. I'm looking forward to being responsible for coming up with ideas and approaches and letting the computer do the grunt work.

Come on, AI. Take my job. I'm pretty sure they're gonna need someone to tell you what to do. I'll do that job instead.
