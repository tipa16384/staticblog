---
date: '2021-08-12T23:42:37-05:00'
draft: false
title: "The Most Interesting MMO in the USA, Part Deux."
author: "Tipa"
summary: "I've just spent the entire night with my hands deep in the guts of the Google Trends API and the Python package that calls it...."
categories:
  - "Blaugust"
  - "MMORPG"
tags:
  - "Coding"
  - "Python"
  - "Pytrends"
  - "Runescape"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2021/08/RuneScape_Android_Screen_4.0.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/08/RuneScape_Android_Screen_4.0.jpg"
---
I've just spent the entire night with my hands deep in the guts of the Google Trends API and the Python package that calls it....
<!--more-->

I've just spent the entire night with my hands deep in the guts of the Google Trends API and the Python package that calls it. I've even sprinkled in Google Suggested Searches to sweeten the search. I've implemented a quick sort algorithm. My boyfriend was helping debug the program. But no matter what I do, the answer always comes out the same.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/08/image-4-357x1024.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/08/image-4.png)

I know this ordering doesn't make any sense. I imagine it's based on what people search for, and they're more likely to search for FFXIV than FINAL FANTASY XIV ONLINE.

I did do a lot of tests on the actual Google Trends page, using the browser developer tools to watch the request go to Google. The [pytrends](https://pypi.org/project/pytrends/) package sends slightly different packets. I wrote a routine to manipulate pytrends local variables to make the packet look more like the one the official page sends, but there's still too many differences.

If I wanted to work on this more, I'd fork the pytrends package and then work on it so that it is more exact. But I don't think it's worth it.

The games are ranked as they're ranked. I don't know why. It's a curiosity, and that's all it is.

Guild Wars isn't actually ranked that high. When I called the API for suggestions to improve the Guild Wars search, it only had suggestions for Guild Wars 2.

Remember, this absolutely does not correlate to the popularity of the game, or the size of its userbase. It's just the information Google Trends happened to pass back when using pytrends to call it.

Once again, if you want to check out the code and maybe improve it, [it's all right here](https://github.com/tipa16384/mmotrends) in my Github. I'm not going to go over it here, because I don't believe many of my readers want to do code reviews for random developers on the interwebs :-) But hey, if you have questions about it, I'm right here.

Back to game blogging tomorrow.

Since I happen to still have the run information in my terminal window, here's the categories and suggested search names for all the games.

```
{'keyword': '/m/06jtfl', 'title': 'Age of Conan', 'type': 'Online game'}
{'keyword': '/m/01058kmm', 'title': 'Albion Online', 'type': 'Online game'}
{'keyword': '/m/09rv422', 'title': 'Allods Online', 'type': 'Online game'}
{'keyword': '/m/01cmhx', 'title': 'Anarchy Online', 'type': 'Online game'}
{'keyword': '/m/0v4gvn3', 'title': 'ArcheAge', 'type': 'Video game'}
{'keyword': '/m/0wxpvj2', 'title': 'Aura Kingdom', 'type': 'Online game'}
{'keyword': '/m/0y66zll', 'title': 'Black Desert Online', 'type': 'Online game'}
{'keyword': '/g/11g3z067k2', 'title': 'Bless Unleashed', 'type': 'Online game'}
{'keyword': '/m/03nskfl', 'title': 'Champions Online', 'type': 'Online game'}
{'keyword': '/m/012wn_sf', 'title': 'Crowfall', 'type': 'Online game'}
{'keyword': '/m/01yn8g', 'title': 'Dark Age of Camelot', 'type': 'Online game'}
{'keyword': 'Dark and Light', 'title': 'Dark and Light', 'type': 'Search term'}
{'keyword': '/m/05c1hv', 'title': 'Darkfall', 'type': 'Online game'}
{'keyword': '/m/04cylb0', 'title': 'DC Universe Online', 'type': 'Online game'}
{'keyword': '/m/04gl3z5', 'title': 'Dragon Nest', 'type': 'Video game'}
{'keyword': '/m/03hhnmm', 'title': 'Dream of Mirror Online', 'type': 'Online game'}
{'keyword': '/m/078r86', 'title': 'Dungeons & Dragons Online', 'type': 'Online game'}
{'keyword': '/m/064hbl', 'title': 'Elite Dangerous', 'type': 'Video game'}
{'keyword': '/m/0243qz', 'title': 'EVE Online', 'type': 'Online game'}
{'keyword': '/m/02sw6', 'title': 'EverQuest', 'type': 'Online game'}
{'keyword': '/m/0448yz', 'title': 'EverQuest II', 'type': 'Online game'}
{'keyword': '/m/026653', 'title': 'Final Fantasy XI', 'type': 'Online game'}
{'keyword': '/m/064ln09', 'title': 'FINAL FANTASY XIV Online', 'type': '2010 video game'}
{'keyword': 'Gloria Victis', 'title': 'Gloria Victis', 'type': 'Search term'}
{'keyword': '/m/071kwg', 'title': 'Granado Espada', 'type': 'Video game'}
{'keyword': '/m/02q25c_', 'title': 'Guild Wars 2', 'type': 'Online game'}
{'keyword': '/m/02q25c_', 'title': 'Guild Wars 2', 'type': 'Online game'}
{'keyword': '/m/02pvj25', 'title': 'La Tale', 'type': 'Online game'}
{'keyword': 'Leafling', 'title': 'Leafling', 'type': 'Search term'}
{'keyword': '/g/11b7xq3y50', 'title': 'Lost Ark', 'type': 'Online game'}
{'keyword': '/g/11f647v_xj', 'title': 'Lucent Heart', 'type': 'Video game'}
{'keyword': '/m/05f95hy', 'title': 'Luna Online', 'type': 'Online game'}
{'keyword': '/m/07gf4z', 'title': 'Mabinogi', 'type': 'Online game'}
{'keyword': '/m/04h2l3', 'title': 'MapleStory', 'type': 'Online game'}
{'keyword': '/m/0421t7', 'title': 'Meridian 59', 'type': 'Video game'}
{'keyword': '/m/0dsb1wd', 'title': 'Neverwinter', 'type': 'Online game'}
{'keyword': '/g/11gbzc5578', 'title': 'Old School RuneScape', 'type': 'Online game'}
{'keyword': 'Palia', 'title': 'Palia', 'type': 'Search term'}
{'keyword': '/m/0_82w8b', 'title': 'Pantheon: Rise of the Fallen', 'type': 'Online game'}
{'keyword': '/m/0h3n4wc', 'title': 'Path of Exile', 'type': 'Video game'}
{'keyword': '/m/0ddcdfz', 'title': 'Phantasy Star Online 2', 'type': 'Online game'}
{'keyword': '/m/01270zc6', 'title': 'Pirate101', 'type': 'Online game'}
{'keyword': 'Project Gorgon', 'title': 'Project Gorgon', 'type': 'Search term'}
{'keyword': '/m/027gfj', 'title': 'Ragnarok Online', 'type': 'Online game'}
{'keyword': '/m/064npj1', 'title': 'Rift', 'type': 'Online game'}
{'keyword': '/m/05f7s19', 'title': 'Runes of Magic', 'type': 'Online game'}
{'keyword': '/m/01l8t_', 'title': 'RuneScape', 'type': 'Online game'}
{'keyword': '/m/03cwmn', 'title': 'Ryzom', 'type': 'Online game'}
{'keyword': '/m/08ysgh', 'title': 'The Secret World', 'type': 'Online game'}
{'keyword': '/m/02vmqg', 'title': 'Shadowbane', 'type': 'Video game'}
{'keyword': '/m/0s8tt32', 'title': 'Shroud of the Avatar: Forsaken Virtues', 'type': 'Video game'}
{'keyword': '/m/0n5v7g2', 'title': 'Star Citizen', 'type': 'Video game'}
{'keyword': '/m/04dywj', 'title': 'Star Trek Online', 'type': 'Online game'}
{'keyword': '/m/04q3kvg', 'title': 'Star Wars: The Old Republic', 'type': 'Online game'}
{'keyword': 'Swords of Legends Online', 'title': 'Swords of Legends Online', 'type': 'Search term'}
{'keyword': '/m/07s8gkl', 'title': 'TERA', 'type': 'Online game'}
{'keyword': '/m/0jt2y_q', 'title': 'The Elder Scrolls Online', 'type': 'Online game'}
{'keyword': '/m/0543v3', 'title': 'The Lord of the Rings Online', 'type': 'Online game'}
{'keyword': '/g/11b8061kml', 'title': 'Trove', 'type': 'Video game'}
{'keyword': '/g/11dd_v_40n', 'title': 'KROSMAGA - The WAKFU Card Game', 'type': 'Video game'}
{'keyword': '/m/04yc1jr', 'title': 'Wizard101', 'type': 'Online game'}
{'keyword': '/m/021dvx', 'title': 'World of Warcraft', 'type': 'Online game'}
{'keyword': 'Wurm', 'title': 'Wurm', 'type': 'Search term'}
```
