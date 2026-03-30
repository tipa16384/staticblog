---
date: '2021-09-01T07:48:11-05:00'
draft: false
title: "Resurrecting West Karana"
author: "Tipa"
summary: "I was fascinated by UltrViolet's DevOps-ification of his blog, \"Endgame Viable\". The sort of stuff he's doing is the sort of stuff I do every..."
categories:
  - "Blaugust"
tags:
  - "Aws"
  - "Blaugust"
  - "Devops"
  - "Github"
  - "Markdown"
  - "Python"
  - "West Karana"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/b0d5f94a61f128683568fec95571fa8e.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/b0d5f94a61f128683568fec95571fa8e.jpg"
---
I was fascinated by UltrViolet's DevOps-ification of his blog, "Endgame Viable". The sort of stuff he's doing is the sort of stuff I do every...
<!--more-->

I was fascinated by UltrViolet's DevOps-ification of his blog, "[Endgame Viable](https://endgameviable.com/dev/2021/08/status-quest-for-the-one-blog-part-13/)". The sort of stuff he's doing is the sort of stuff I do every day at work. I'm getting paid to get better at doing all of this stuff, but my own blog can't take advantage?

That ends today. Today, I bring my old blog, West Karana, back to life, via the magic of DevOps.

{{< image src="https://lh3.googleusercontent.com/hjM5Ue7WA3y02kAI0heoLwhraDHDktG9N71N_pAGhwlkaDgc_EPb0jMrU3RqgBB0nVWoRZU3hC-wOuL2_P1FZovfTOfTYAOgVsEcab2NdlsEgfPfFGQcZv1wi_UqFiuhpQS6gC6ocI0rHS71n-2YpyJOQCELhkht89o2yyNi8uocPbmnndwXJFvEU3zzqnPihSB63Cl11N5B8TgFJuYnTq5QuX1jNlyz0XwyeIsc6dourSSV8xD9ixiBejcw9cPmREtsuf1nLCzxyzMNjEqgrW4b74mYuf3uh3TBtq1F2hMtEYD7-sddITkxf-F5x45NdEl9DIdEUGtjxUL3FibaA1qWRQYl3zNOBlsBAbPjO4yTeb3kypScf9rmeGfYH6wrHjGMLjOlruX6bzBWFM1mOKiThKkqja5b86Wl7D8uRYVftujcvL2ejfLnb7SCRiP8lONa7LWjAXT4sm2WOtb8xBNySQzJ8G7Yr6OL7SVu6ty8tUFx4aWQD9o2f9Hrqfz1tyD-xg0Mp6Iu4WBAxuzZR6RhkmOOrX7ehEgXQSQi70eWE0il0fT4uBGSOrZt3G7zAw7XPi471REdrsSk7eNbaOxuyP6D7d2A8jERpwdWzYbwQANy9srvyNcTSGmmLk7jxZoyLQjrGEdVnjZBCaJrG0sfO2ire0WHuMy8XgleaLyCfrXbHuRxAmsx1ot4gFRgwzXPRe_Fd4sYuLVr8T3PBFQV=w961-h226-no?authuser=0" classes="center" >}}One of my old banners :-)

DevOps is just a fancy way of bringing every IT position into one person -- the developer.

- We don't need an architect for our code, the developer can do it (lol)- We don't need a QA person for our code, the developer can do it (Cypress and Karate)- We don't need a DBA to manage our databases, the developer can do it (Liquibase)- ...

Jack of all trades, master of none. I present to you the DevOps developer.

Anyway. UltrViolet made a whole new workflow where he creates documents in a text editor marked up in Markdown format, and then has scripts crawl through stuff and do magic and out spits a blog. It's all very magical.

I'm not nearly up to that point. But, I'm sitting on years worth of SQL code that could, in theory, move my old blog, West Karana, to a new place, potentially even this blog. But there's conflicts with newer versions of WordPress, categories, tags, all sorts of cruft. If I could just bring *both* blogs into Python, then I could fix all the inconsistencies and then spit out a new back end that contains both blogs.

First, though, I'd have to start writing code to turn the old SQL backup into something I could work with.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image.png)Python fragment to save a blog post as Markdown

- Open the backup SQL file- For each lineIs this a SQL insert for a new blog post?Use my SQLConsumer action to parse the line into a dictionary of column name: data pairs- Create a new "Post" object with that data- call the "Post" object to write itself to a file in Markdown format
- Is this a SQL insert for a new comment?Worry about this later

So, as a proof of concept, all the text of all the posts (sans images, comments, and meta information) is now backed up, in Markdown format, in GitHub.

Here's [a sample post from the past](https://github.com/tipa16384/westkarana/blob/somethingelse/posts/5144.md):

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-1.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-1.png)Blast from the Past

The link above goes into the actual repo, where, with a little poking around, you can find some of my very dirty, banging together at midnight, code that does the deed.

I don't remember any of this stuff -- especially the DDO stuff. I don't remember Kasul ever playing DDO with me -- and I bet if I asked him, he wouldn't, either. But here it is, in black and white.

Next steps are to get the images loaded. I can put them into GitHub as well, *or* I could copy them into an AWS S3 bucket and then talk to them from there. It would be fun to put them in AWS, but then I might have to pay actual money.

But, for those who've been, for some reason, wanting to look at the old stuff, it's all there, and will only be becoming *more* "there" as time goes on.
