---
date: '2025-02-21T09:03:44-05:00'
draft: false
title: "Hueforge: High Rez Color Pictures on your 3D Printer"
author: "Tipa"
disqusIdentifier: "2025/02/21/hueforge-high-rez-color-pictures-on-your-3d-printer"
summary: "Hueforge prints using very thin layers so that colors bleed through to create blends, shades and gradients on any printer."
categories:
  - "3D Printing"
tags:
  - "Bambu"
  - "Hueforge"
  - "P1s"
relatedPosts:
  - url: "/2026/03/17/the-bambu-lab-ams-pro-2/"
    title: "The Bambu Lab AMS Pro 2"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2026/03/itsabouttheams.png"
  - url: "/2025/12/22/the-perfect-christmas-gift/"
    title: "The Perfect Christmas Gift"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/12/IMG_5577-scaled.jpg"
  - url: "/2025/06/24/frosthaven-7-the-edge-of-the-world/"
    title: "Frosthaven #7: The Edge of the World"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/06/IMG_5196-1-scaled.jpg"
  - url: "/2025/04/29/frosthaven-scenario-1-town-in-flames/"
    title: "Frosthaven Scenario #1: Town in Flames"
    thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/04/IMG_5077-scaled.jpg"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2025/02/IMG_4988-scaled.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2025/02/IMG_4988-scaled.jpg"
---
Hueforge prints using very thin layers so that colors bleed through to create blends, shades and gradients on any printer.
<!--more-->

Left to right on the picture above: the cover to my Malifaux December deck, showing Rasputina; the astronaut that is the test print for Hueforge; and my blog's logo. Because everyone has to have a logo.

When I printed the ice pillars for my December crew, I saw that the blue of the rune layers was dimly showing through the white layers. It gave it a magical feel that I kinda liked. I had the bright idea that maybe, just maybe, there was something to this, and you could make cool things with depth to them, maybe.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/02/image-8-150x150.png" classes="fig-20" >}}

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/02/tipachu_an_public_service_announcement_warning_people_about_t_85d44236-166a-497f-b763-2576b274a5c4_1-150x150.png" title="SOL? No way, NoHowl!" classes="fig-20" >}}

Google let me know I was far from the first to think of this. There's a technique called "lithopaning" which lets you create 3D-printed images that reveal themselves when held up against a bright light, with fewer layers representing light areas, and more layers representing dark areas.

This [3D print of the Moon](https://www.printables.com/model/23859-designer-moon-lamp) is made by printing overlapping circles, layer after layer, where the width of each segment along each circle is determined by the Moon's topography; thicker for dark areas, thinner for light areas. Put a light source in it and you have a Moon. Doesn't do phases very well, though. This might be a problem if you have sudden-onset lycanthropy (SOL).

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/02/image-9-1024x595.png" title="HueForge editing Hokusai's \"The Great Wave off Kanagawa\" woodprint." classes="center" >}}

HueForge creates color lithopanes that don't require a light source to view. It's based off a concept of "transmission distance", or TD. This is a measure of the opacity of a very thin layer of a particular plastic filament. Every filament by every manufacturer has a different TD; a white filament by Prusa may be more opaque than one by BambuLabs but less opaque than one by Overture, for example.

You start by telling HueForge what filaments you have available. When you load an image, it will give you a rough rendering with black as the first color, white as the last color, and a dark and a lighter color shade between them. In the Hokusai print above, the left four sliders are based off the default settings.

The color graph between the work preview and the original image shows the layers where the color changes. Every printer of which I'm aware allows you to pause the printer at a specific layer in order to change the filament; my Bambu P1S has an automatic filament changer that lets me work with four colors at a time. In this example, with six different colors, I'd have to put in a manual pause in the middle to replace the two darkest filaments with the two lightest ones.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/02/image-10.png" title="Print instructions for the Great Wave" classes="center" >}}

Exporting the finished design gives an STL file and instructions on the print parameters and at what layer to swap to what color. The notes above reflect additional work I did on this print after I took the screenshot.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2025/02/image-11-1024x644.png" title="In Bambu Studio, AKA PrusaSlicer" classes="center" >}}

Importing it into the slicer, setting the filament colors and the color changes gives something like this. The preview is what the slicer thinks this will look like when printed. It's wrong, though, because it doesn't take transmission distance into account. But even in this preview, it shows the writing along the left perfectly readable. How will it look when printed?

We'll find out seven hours after I hit the print button...
