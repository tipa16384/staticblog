---
date: '2006-10-12T01:04:14-05:00'
draft: false
title: "RL: Raid on ABAC.com"
author: "Tipa"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://chasingdings.com/2006/10/12/rl-raid-on-abaccom/"
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
  - "General"
  - "My Work"
featured_image: "https://chasingdings.com/wp-content/uploads/2006/10/dina-moa2.jpg"
cover:
  image: "https://chasingdings.com/wp-content/uploads/2006/10/dina-moa2.jpg"
  alt: "<alt text>"
  caption: "<text>"
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/tipa16384/staticblog/tree/main/content"
  Text: "Suggest Changes"
  appendFilePath: true
---

![Dina en regalia](https://chasingdings.com/wp-content/uploads/2006/10/dina-moa2.jpg)

(I wanted to head this rant with a picture of my trusty little mail server, Atlas, but he and I are not speaking at the moment, and the digital camera was out of power. So for no real reason, a gratuitous picture of Dina as a Square-Enix heroine.)

About two weeks ago, our email provider, ABAC.com, decided not to allow us to send mail to people within the company *from* within the company. No reason given, and they accepted mail from outside the company (for awhile, anyway) no problem.

We're a company that runs on email. We have our manufacturing in Bali, sales reps all over the world and our own salesladies who travel to shows everywhere all the time. Email HAS to work. This is why we pay someone else to handle our email -- so we have a team of professionals just to make sure it is all working so we can do other, NON-EMAIL stuff. We're a garment manufacturer. You know, we make and sell clothing.

I fix the computers. They hired me because I had my own set of screwdrivers -- AND a multimeter!

I sent a trace to figure out the problem. The old movie, Tron, that showed what it was like to be a program running around in the digital realm? That's where I set Trace free. Here's her messages back to me as she found her way toward the -- .... well.

Tracing route to [smtp2.abac.com](http://smtp2.abac.com/) [[216.55.128.210](http://216.55.128.210/)] over a maximum of 30 hops:

1

3   721 ms   767 ms   786 ms  [(shuffled around on covad\'s LAN)\n

4    84 ms   117 ms    99 ms  ge-5-0-217.hsa1.SanDiego1.Level3.net [209.245.121.29]  \n(sent to the backbone)

5   151 ms   180 ms   207 ms  so-6-1-0.mp2.SanDiego1.Level3.net [4.68.113.37]  \n(Level 3 has an interesting history)

6   358 ms   207 ms    27 ms  ge-7-0-0.gar2.SanDiego1.Level3.net [4.68.97.214]  \n(they were a mining and construction company before becoming one of the Internet\'s major backbones)

7   323 ms   262 ms   279 ms  \nABACUS-AMER.gar2.Level3.net [64.158.218.2]  (...off the backbone to Abacus America)

8   351 ms   373 ms   552 ms  \ngi5-15.cr1.sandiego.abac.net [66.226.66.17]  ",1] );  //-->192.168.19.121 *Covad's LAN is strange. Everyone stares. I can't wait to get out of here.*

4    84 ms   117 ms    99 ms  [ge-5-0-217.hsa1.SanDiego1.Level3.net](http://ge-5-0-217.hsa1.sandiego1.level3.net/) [[209.245.121.29](http://209.245.121.29/)] *The outbound server sent me to Level 3. Level 3 used to be a mining and construction company before acquiring a communications company. Now they are one of the largest internet backbones in the country, carrying a vast amount of the nation's traffic. I've never seen such huge pipes.*

5   151 ms   180 ms   207 ms  [so-6-1-0.mp2.SanDiego1.Level3.net](http://so-6-1-0.mp2.sandiego1.level3.net/) [[4.68.113.37](http://4.68.113.37/)] *All this whizzing about, and I'm still in San Diego!*

6   358 ms   207 ms    27 ms  [ge-7-0-0.gar2.SanDiego1.Level3.net](http://ge-7-0-0.gar2.sandiego1.level3.net/) [[4.68.97.214](http://4.68.97.214/)] *The exit for ABAC.com is coming up.*

7   323 ms   262 ms   279 ms  [ ABACUS-AMER.gar2.Level3.net](http://abacus-amer.gar2.level3.net/) [[64.158.218.2](http://64.158.218.2/)] *Crossing the bridge to ABAC.com. So this is what those dirty, backwater industrial ruins you see on the sides of highways look like from up close.*

8   351 ms   373 ms   552 ms  [ gi5-15.cr1.sandiego.abac.net](http://gi5-15.cr1.sandiego.abac.net/) [[66.226.66.17](http://66.226.66.17/)] *I'm crawling around in ABAC.com now. There's a light up ahead... I feel strangely compelled toward it... *

9     *        *        *     Request timed out.

10     *        *        *     Request timed out.

11     *        *        *     Request timed out.

12     *        *        *     Request timed out.

13     *        *

So, that was the last we heard of poor Trace. It seemed clear she'd run into something bad in ABAC.com-land. I hate talking to their customer support. They are not technicians, and proudly *advertise* that their CS reps use the same online knowledge base that you can use. See, they don't want you to call them.

I called them two Thursdays ago and got the dead phone equivalent of a blank stare, but they promised to fill out a ticket, get a tech on it, and get back to me. They never did. I called Friday. More blank stares/dead wire. A new ticket, a new promise to get back to me with results (I provided the trace clearly showing trouble with their servers.). Monday. I called *again*. The claimed we were blocking outgoing secure connections with our firewall. Our firewalls don't block any outgoing connections at all (very few do). They said it was our ISP, Covad, doing it. NOPE. They don't block any outgoing connections either. The company COO got into the act, and she escalated it twice. They said they knew where the problem was, they would fix it that night, and then -- that night -- send an email with their progress.

Tuesday: still not working, still no email. Our Bali office was wondering why we never sent them email anymore. Nobody was getting email anymore. We called and they insisted -- angrily -- that there was no problem on their end (not what they claimed before), it had to be our ISP, and that maybe we should escalate things twice with THEM this time.

But I could SEE the trace leaving Covad without any trouble! It was clear ABAC was trying to get rid of us. Well. I'd been running my work Linux box, Atlas, as an open outbound mail relay for awhile. I could just add some authentication and bring everyone on board.

That went fine, except that I STILL couldn't send mail to people within the company, as ABAC was still blocking us. So I dug some more and set up a separate system for distributing internal mail to virtual mailboxes -- internal mail would never leave the building.

And that worked, and I felt good about life again. Then Sunday (Monday for Bali), I get frantic IMs from my boss who is over there for a few months, saying there's a problem -- emails from Bali are no longer getting to California. They got their ISP to do a trace and... well, here's what they had to say.

> Setelah kami cek pada mail server kami,

> terlihat indikasi bahwa mail server tujuan dalam keadaan down

> berikut ini Log dari mail server kami

I don't know Indonesian, but apparently it means (and they provided traces of their own) that for no reason anyone could guess, ABAC.com was now blocking inbound mail for us from Bali.

NEVER seen a company try so hard to lose someone's business. My boss registered a new domain and this morning I had all the email troubles just bad distant memories. I was feeling happy. I brought up a webmail interface and IMAP so that people could read their mail wherever they liked.

But one of the salespeople had trouble sending mail through the mail relay ABAC.com provided. If we were going to abandon ABAC.com, we'd have to provide our own open, authenticated mail relay so people could send mail when not at the office.

It wasn't clear how to do this properly, and I fouled stuff up and decided to just restore the Postfix mail server configuration from a backup.

Except, it was the WRONG backup. Now everything is totally flowzered. All incoming email to our old domain is bouncing. The new domain works fine, but who is using that? Postfix documentation is about as clear as tar. I have zero idea how to proceed, yet I have to have it solved and working by the time work starts at 8am tomorrow. I haven't called Covad to open the SSH port on our firewall so I can't work on the server from home so...

I'm REALLY STRESSED OUT. This problem just keeps getting worse and I have to try more and more exotic solutions as it escalates. Now, it did give me an excuse to learn Python -- I wrote Python scripts to set the user settings through the MySQLdb package automatically, so I can tear down a non-working configuration and try a new one without any interruption of emails. Python is a pretty sweet language. I am coming to know the intricacies of configuring and maintaining mail servers far, far too well. And since ABAC.com hosts our web site, I will soon come to know how much fun it is porting that web site, which I wrote using Javascript and ASP, to PHP or Python, I haven't decided yet.

And once this is all working, it needs to be put on real server iron. We have a server we haven't used for awhile. It has a RAID array and can be easily added to our nightly backups.

I just don't see how this is going to get me a job as a designer in the online game industry...

Anyway. Lots of people asked what had happened to me, and this is what -- I'm way too busy and stressed out at the moment to work on my blog.

I hope the next entry will have a picture of my Atlas server with all hearts and smiles floating around it. And then I can start working on finishing "Waiting for Godot" and developing my new MMO which is all about ... crafting :)
