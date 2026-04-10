---
date: '2009-02-07T19:19:20-05:00'
draft: false
title: "AiM: Behind the scenes"
author: "Tipa"
disqusIdentifier: "2009/02/07/aim-behind-the-scenes"
summary: "I was working on the next Adventures in Monopoly comic, and thought it would be fun to show how I created the first panel...."
categories:
  - "Adventures in Monopoly"
relatedPosts:
  - url: "/2020/09/15/adventures-in-monopoly-darkfall-part-iii/"
    title: "Adventures in Monopoly -- Darkfall, Part III"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2020/09/aimbomb.jpg"
  - url: "/2020/09/08/adventures-in-monopoly-darkfall-part-ii/"
    title: "Adventures in Monopoly -- Darkfall, Part II"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2020/09/panel3.jpg"
  - url: "/2020/09/01/adventures-in-monopoly-darkfall-pt-1/"
    title: "Adventures in Monopoly -- Darkfall Pt. 1"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2020/09/panel2.jpg"
  - url: "/2020/08/24/adventures-in-monopoly-cash-shop/"
    title: "Adventures in Monopoly -- Cash Shop"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2020/08/panel1.jpg"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2009/02/pat1.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2009/02/pat1.jpg"
---
I was working on the next Adventures in Monopoly comic, and thought it would be fun to show how I created the first panel....
<!--more-->

I was working on the next Adventures in Monopoly comic, and thought it would be fun to show how I created the first panel.

I wanted a boat going over an ocean, and I wanted the ocean to be a game board. I couldn't find any good ocean game boards at Toys R Us despite all the wonderful ideas given by people on Twitter, so I decided I would make my own in Photoshop and render it for extra realism in a 3D ray tracer, POVRay.

First, making the pattern in Photoshop by building up layers -- rendering clouds, blending them with fibers, desaturating it all so it worked nicer, adding a coloring layer and then some text. The pattern would also be used as a bump map for that paper glued over cardboard feel, so I made two, one with and one without the text. Otherwise the text would have rendered as huge letter-shaped holes in the ocean.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/pat2.jpg" title="pat2" classes="center" >}}

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/pat3.jpg" title="pat3" classes="center" >}}

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/pat4.jpg" title="pat4" classes="center" >}}

I photographed the Lego ship on the back of my Monopoly board so I could get an idea for how to render the image and so the shadow of the ship would be generally in the area of the right color.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/ship1.jpg" title="ship1" classes="center" >}}

Matching the angle of the light in the photograph, I rendered the board in POVRay.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/fin1.jpg" title="fin1" classes="center" >}}

I separated the ship's shadow from the ship in Photoshop and made it a new layer using the "Hard Light" blending mode to let the board show through. I had to patch the shadow a bit to give it all the coverage it needed.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/fin2.jpg" title="fin2" classes="center" >}}

Then I added the ship itself -- just need to add dialog and the first panel is done!

{{< image src="https://tipa16384.github.io/wkblog/uploads/2009/02/ship.jpg" title="ship" classes="center" >}}

Elapsed time -- about two hours...
