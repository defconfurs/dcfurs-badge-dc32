
## Firmware

We will be promoting builds from this repo to releases perodically, see the releases section for thje latest firmware.

## Updating

When you load a new firmware uf2 file, it will not delete the existing micropython filesystem, so if you want updated python files, you can either copy them from this repo or delte all the files from that filesystem and hit the reset button on the badge and it will reload them.

## TODO

- Boop is still not complete.   The touch code is working, we just dont have the animation yet.
- **Prize** Get MEshtastic working on the badghe and get a free badge next year!

## Post from the Telegram Chat
So, were going to do a thing this year where the software on the badge is not complete and people are welcome to make it more complete.    On Wednesday or really early Thursday morning of the con, we will make the repo with this years software public.

Things we will work on having done by Wednesday:
- Boop (as well as boop in the 2023 firmware)
- Filesystem exposed over USB.
- Animations, Loial had several, we just need to change them up.
- The radio has some firmware on it already, if we can initialize that and have a way to send and receive using the AT commands, that would be a nice starter.

We will be announcing prizes for certain goals on badge hacking when the repo goes live, some examples would be:  Getting meshtastic to run in the STM32WL.  More animations, Games, etc.

Things you will want to have to hack the badge:
If your going to muck around with the software on the STM32WL chip, you will want to have a breakout for JTAG like the Adafruit 2743, some wirewrap wire and a JTAG probe like the ST-LINK V3.    I will have a limited number of the adafruit breakouts available for people to use.    I will also have various JTAG probes available for people to use as well, and also DEFCON Furs will have a soldering station and wirewrap wire.

The Tag-Connect connector on the badge is not wired in a way thats really helpful, my bad, next time it will be wired correctly.

We have been having a lot of "fun" getting this badge to you this year, PCBWay took extra long this time and DHL and customs is an adventure as always.
