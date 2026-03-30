---
date: '2021-09-08T08:01:16-05:00'
draft: false
title: "Chasing Dings! goes to West Karana"
author: "Tipa"
summary: "I was playing around and wrote a script last week that took an old backup of my previous blog, West Karana, and brought it to..."
categories:
  - "Programming Language"
  - "System Software"
  - "Topic"
tags:
  - "Aws"
  - "Filezilla"
  - "Lightsail"
  - "Python"
  - "SQL"
  - "West Karana"
  - "Wordpress"
coverImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/tara21.jpg"
thumbnailImage: "https://tipa16384.github.io/wkblog/uploads/2021/09/tara21.jpg"
---
I was playing around and wrote a script last week that took an old backup of my previous blog, West Karana, and brought it to...
<!--more-->

I was playing around and wrote a script last week that took an old backup of my previous blog, West Karana, and brought it to life as a GitHub repository. A friend on Twitter challenged me to do even better. Yesterday, I found a more recent backup -- posts up to 2016, that I wrote for Google+, and used that as a source to finally get everything merged to *this* blog. It's an exciting DevOps adventure.

It's always fun to write little scripts in Python to do the heavy lifting in whatever harebrained scheme I come up with. So I often just rush right in with a script without actually doing enough research to understand if what I'm taking is the right approach.

This comes up at work sometimes, too, and I always appreciate a bit of sanity checking before I put a lot of time into a project.

[Nimgimli](https://dragonchasers.com/) was [the calm, wise voice of reason](https://tipa16384.github.io/wkblog/2021/09/01/resurrecting-west-karana/#comment-1466) who suggested I use Wordpress' built-in migration tools to, maybe, do the job.

Basically, his suggestion was to run the SQL scripts in my backup against a fresh Wordpress instance, and then export it from that one in the standard Wordpress XML format, and import that into Chasing Dings!

Um, okay, maybe that would work. I'd have to redirect all the links that pointed into WestKarana-dot-com (can't write that out as Wordpress will make it into a URL and that points to the spam site that stole my domain), copy all the images up to the new host, but maybe it will work?

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-3.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-3.png)

**Step 1: Make a new Wordpress instance**

Since I just got AWS certified, I'm all about using AWS to do fun things on the cloud. [Amazon Lightsail](https://aws.amazon.com/lightsail/) is a turnkey web hosting solution that can be combined with other of their services to not only bring up the blog at some random IP, but to associate that IP with a domain name, make it public, and clone the content to regions around the world to make it fast to access anywhere.

I used their Wordpress templates to make a new blog, installed phpMyAdmin on it, deleted their sample posts and comments, and ran my modified SQL into it. I'd removed all the DROP TABLE/CREATE TABLE statements, as I didn't want to mess with the data structures. I'd also changed all West Karana media links into Chasing Dings! links. The only data I kept was the info for the default user on the new blog, the one with the admin rights.

I hit a roadblock with the wp_comments and wp_posts table, in that both had a "category" column that had been removed somewhere along the way. I used the console to add those columns back, and everything imported fine. Except that I no longer had admin access. I'd preserved the default user, but I'd nuked the wp_usermeta table that set the admin privs. I copied that meta information from my Chasing Dings! blog, and everything was fine.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-4.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-4.png)

**Step 2: Export!**

Next step was the simplest -- just export all the things. This isn't a full backup, like the one I had from WK. This one includes only some of the tables. It doesn't export users, links, options -- tables like that. It does export the posts, post-meta, comments, comments-meta, and all the tags and categories. So, this file alone can't restore a WP blog 100%. It's only useful for migrating blog information to another blog. Fortunately, that's exactly my use case, but someone hoping for a *full* backup would need the same sort of SQL backup that I'd kept from WK.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-5.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-5.png)

**Step 3: Uploading the images**

The export file also doesn't include the images and other non-text information. I'd backed up all this stuff separately, back in the day, which seems weirdly off-brand for me. But I guess at some point I wanted to keep this stuff around. I had to create a new FTP user with my web host because I couldn't remember the info for the old one, but eventually I got to the point where I was having FileZilla upload 10,000+ files. Thank heavens for fiber. It took an hour or so nonetheless and it was after midnight when it completed.

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-6-1024x587.png" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-6.png)

**Step 4: Import the data into the new blog**

[{{< image src="https://tipa16384.github.io/wkblog/uploads/2021/09/image-1.jpeg" classes="center" >}}](https://tipa16384.github.io/wkblog/uploads/2021/09/image-1.jpeg)

The final step was anticlimactic. I imported the file into Chasing Dings! using the console. The tool warned me that it couldn't find the references to any of the images, but that was fine -- I'd put them where they needed to be already. Then it asked me to map old users to new. There were only three post authors from the old blog -- me (I mapped the WK user to my new user), Saylah and Lemons. I opted to not copy their user information over, but to make new, dummy users to protect their privacy.

There it was. Relatively simple. The only really tough part was going through and redirecting links, and changing the schema on the two tables in the temporary blog in order for the SQL to run smoothly. I'd thought about writing a Python script to fix the actual SQL statements to not include that column -- since I already had written a script that parsed the SQL and I could extend it to write it back out corrected -- but opted not to.

And now it's done.

**Next steps**

I have really, really proven the worth of full backups to myself. Next step is to start regularly backing up Chasing Dings! so that when the next time this happens (heaven forbid), I'll be able to quickly recover.
