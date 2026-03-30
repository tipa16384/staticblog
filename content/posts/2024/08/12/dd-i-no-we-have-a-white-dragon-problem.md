---
date: '2024-08-12T07:00:00-05:00'
draft: false
title: "D&amp;D: I -- no, WE -- have a white dragon problem"
author: "Tipa"
summary: "The problem is, we're about to battle the final boss battle of the Icespire campaign, but Cryovain refuses to come out of his dressing room."
categories:
  - "3D Printing"
  - "Blaugust"
  - "Blaugust 2024"
  - "Dungeons & Dragons"
  - "Miniatures"
  - "Tabletop Games"
tags:
  - "Dragons"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2024/08/IMG_4558-EDIT-scaled.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2024/08/IMG_4558-EDIT-scaled.jpg"
---
The problem is, we're about to battle the final boss battle of the Icespire campaign, but Cryovain refuses to come out of his dressing room.
<!--more-->

I have a 3D printer downstairs.

Well, to be totally honest, I have *three* 3D printers downstairs. And my boyfriend has another two -- his are resin printers, mine are filament printers. Between us, we have five printers that are capable of bringing into reality almost any conceivable object, if it isn't all that large. You can imagine that when we're playing a game that needs minis or terrain, friends and family look to us to provide. Sure, that's why we *bought* the things.

Aside from my first 3D printer, a Creality Ender 3 Pro, all of our printers are advertised as plug and play. You perhaps do some light assembly, but after that, the printers just do what they do.

This, of course, is a lie. Kasul has completely redone the optics of one of his printers. My Ender has a bunch of new parts. My Prusa lies broken beyond my ability to repair it -- spitzen und sparken, wie wir auf Deutsch sagen. But my AnkerMake M5, the one I kickstarted -- that could never fail.

Until of course, it did. In so, so many ways. I've had to take the hot end apart, change the nozzles, clean it, it wants to be lubed now... nothing unusual, normal wear and tear. But what I hate is when I do all these things and I still fail to get decent prints out of it. It was perfect when I first put it together and plugged it in.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/08/image-23-1024x589.png" title="We should just use LEGO instead of minis." classes="center" >}}

I think the current problems stem from when I had to replace the nozzle of the AnkerMake. It uses a 17mm long nozzle; I didn't have one of those, so I used the shorter ones I had on hand for the Ender and the Prusa. I'm thinking now that I really needed to use the correct size.

The printer always leaks melted filament, and that leaves blobs everywhere. It still printed decently for all that, but... look at the dragon on the right in the first picture. That goes beyond a bit of blobbing. I believe *that*... was due to bad software.

AnkerMake provided their own slicer for their printer, which worked fine, I guess. Then they moved to a new product which was based on a third party slicer called AnkerMake Studio. This was terrible in so many ways, but I wasn't sure just *why* it was terrible.

That dragon on the right was the clue. The filament was not being retracted when it was done with a stroke. Molten filament just kept on running free. I looked at the retraction settings in the default profile. No retraction. What I suspected was true.

{{< image src="https://tipa16384.github.io/wkblog/uploads/2024/08/image-24-1024x641.png" title="We should just use clay instead of minis" classes="center" >}}

I could have started modifying the settings to add retraction back in, but there's a lot of nuance to those settings and I felt this is the sort of stuff someone else had probably already done.

The best slicing software for my money (i.e., *free*) is Ultimaker Cura. I'd used their stuff awhile back for my other printers, and remembered they also had a fan-made configuration for the AnkerMake printers. I reinstalled that software and loaded in the correct configuration and went immediately to the retraction settings: yup, there were a lot of them.

The back middle dragon was the result of those. I printed it as one piece with a lot of supports. It lost a leg to the support, but the difference between the one on the right and that one is significant (even given that I used a different model, as I felt the one sort of sitting peacefully wasn't the pose we needed for this fight). The model is fairly smooth. Blobbing is still an issue, but at least it isn't looking like it's covered in Elmer's glue.

The sculptor had also provided the same model in parts, so I printed the parts separately and glued them together afterward. The one on the left is the final one. Still not perfect, but perfection will have to wait until I get the new, correctly-sized nozzle. Some light stringing, some blobbing, but it's good enough.

We're just going to kill it, after all.
