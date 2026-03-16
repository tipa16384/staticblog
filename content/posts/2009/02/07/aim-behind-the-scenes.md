---
date: '2009-02-07T19:19:20-05:00'
draft: false
title: "AiM: Behind the scenes"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2009/02/07/aim-behind-the-scenes/"
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
summary: ""
description: "Desc Text."
tags:
  - "Adventures in Monopoly"
featured_image: "https://chasingdings.com/wp-content/uploads/2009/02/pat1.jpg"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2009/02/pat1.jpg"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

I was working on the next Adventures in Monopoly comic, and thought it would be fun to show how I created the first panel.

I wanted a boat going over an ocean, and I wanted the ocean to be a game board. I couldn't find any good ocean game boards at Toys R Us despite all the wonderful ideas given by people on Twitter, so I decided I would make my own in Photoshop and render it for extra realism in a 3D ray tracer, POVRay.

First, making the pattern in Photoshop by building up layers -- rendering clouds, blending them with fibers, desaturating it all so it worked nicer, adding a coloring layer and then some text. The pattern would also be used as a bump map for that paper glued over cardboard feel, so I made two, one with and one without the text. Otherwise the text would have rendered as huge letter-shaped holes in the ocean.

![](https://chasingdings.com/wp-content/uploads/2009/02/pat1.jpg "pat1")

![](https://chasingdings.com/wp-content/uploads/2009/02/pat2.jpg "pat2")

![](https://chasingdings.com/wp-content/uploads/2009/02/pat3.jpg "pat3")

![](https://chasingdings.com/wp-content/uploads/2009/02/pat4.jpg "pat4")

I photographed the Lego ship on the back of my Monopoly board so I could get an idea for how to render the image and so the shadow of the ship would be generally in the area of the right color.

![](https://chasingdings.com/wp-content/uploads/2009/02/ship1.jpg "ship1")

Matching the angle of the light in the photograph, I rendered the board in POVRay.

![](https://chasingdings.com/wp-content/uploads/2009/02/fin1.jpg "fin1")

I separated the ship's shadow from the ship in Photoshop and made it a new layer using the "Hard Light" blending mode to let the board show through. I had to patch the shadow a bit to give it all the coverage it needed.

![](https://chasingdings.com/wp-content/uploads/2009/02/fin2.jpg "fin2")

Then I added the ship itself -- just need to add dialog and the first panel is done!

![](https://chasingdings.com/wp-content/uploads/2009/02/ship.jpg "ship")

Elapsed time -- about two hours...
