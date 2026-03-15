---
date: '2022-07-12T07:42:43-05:00'
draft: false
title: "Streaming from the Nintendo 64"
categories:
  - "Nintendo 64"
tags:
  - "Hdmi"
  - "Nintendo 64"
  - "Retrotink"
  - "S-Video"
  - "Stream"
  - "USB"
  - "Video"
  - "Video Capture"
  - "Video Converter"
featured_image: "https://chasingdings.com/wp-content/uploads/2022/07/vlcsnap-2022-07-12-07h06m02s617.jpg"
cover: "https://chasingdings.com/wp-content/uploads/2022/07/vlcsnap-2022-07-12-07h06m02s617.jpg"
---

It's not pretty and it could be better, but I'm able to stream from my unmodified Nintendo 64 at an acceptable resolution using about $50 of hardware.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/07/IMG_2614-1024x768.jpg" title="The hardware" class="align-center" >}}

Curling around the picture is an S-Video cable. My N64 came originally with composite cables; S-Video provides a slightly better signal. With so much signal processing happening, it's important to start off with the best signal we can get. There is an N64 mod that breaks out the RGB signal before it is processed, but I don't have that.

That feeds into the bigger box, the Video Converter that takes the S-Video as input and gives HDMI as output. If you're just looking to play on a modern monitor, that's all you need to do. I had to fiddle with my monitor to get it to display acceptably, but the aspect ratio and colors were still way off. Amazon has this box for under $32 right now. I'm not going to share links, but it's easy enough to find -- TENSUN HDMI Video Converter.

The dongle with the USB connector on it is an HDMI to USB 3.0 video capture device. The HDMI from the video converter goes in the left end, and a USB 3.0 female to male cable gets attached to the other -- in my case, at least, since my streaming computer is pretty far from the N64. It could be plugged in directly to a USB 3.0 port on my computer if it were closer. And... hey, actually, it IS close enough. Didn't even need that USB cable I bought. Wild.

The video capture card cost about $15.

It took a little fiddling for OBS to capture both video and sound from the device, and for it to send the audio to an external speaker so that I could hear it while playing the game, but there's plenty of clues online on how to set this up and it *just works*.

If you've been wanting to play your vintage game systems on modern hardware and also stream but you thought it would take hundreds of dollars -- no, it doesn't have to.

{{< figure src="https://chasingdings.com/wp-content/uploads/2022/07/image-1.png" title="RetroTINK-5X" class="align-center" >}}

In yesterday's post, [everwake](https://chasingdings.com/2022/07/11/is-playing-on-the-original-hardware-worth-the-trouble/#comment-15490) told me about a device called the [RetroTINK-5X Pro](https://www.retrotink.com/product-page/5x-pro). This would replace the TENSUN Video Converter. It uses an FPGA to do a better job with the signal conversion, and can provide an output resolution higher than the input resolution, and of higher quality as well. It can also take advantage of the N64 RGB output mod that would allow N64 games to be played on the original (but modded) hardware with an image as perfect as possible.

Downside is, this costs $300, and each is made by hand, to order, by the inventor.

Not gonna lie, I kinda want one. But, it's a little out of my price range. I'd do it if I planned to mostly play retro games on their original hardware from now on, but that's unlikely. Now that the N64 is up, I'll play a few games that I've been missing, and then I'll dig out the Saturn from its box and do some of those, so... well, maybe it would be worth it. My birthday's coming up.
