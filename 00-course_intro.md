---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Introduction"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Introduction of practical cryptography course"
keywords:
  - "cryptology"
  - "cryptography"
  - "practical"
  - "encryption"
  - "course"
  - "introduction"
  - "intro"
color: "#ffffff"
class:
  - "invert"
style: |
  section.center {
    text-align: center;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
# Practical cryptography
### Welcome and thanks for joining!

![bg right:30%](images/00-cyberpunk.jpg)

<!--
Welcome participants and wait for everyone to get settled.
Introduction of the lecturers and their background.

Segue: In this part of the course we'll talk about cryptography...
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ESA (CC BY-SA 3.0 IGO)" -->
## What we will cover
Why cryptography makes the modern world go round and how **you** can practically utilize it.

![bg right:30%](images/00-satellite_photo.jpg)

<!--
- Sounds quite hyperbolic, doesn't it?

- Examples of how you already relied on it today

- Did you go to take the bus/subway this morning? Did you check your bank account? Did you send a
nude/talk to your psychologist online? Did you buy a sandwich? Did you connect to school wifi? Then
you've relied on cryptography. So do spooks, dissidents, mega-corps and criminals.

- What first comes to mind when talking about cryptography is encryption, that is to keep
information secret, but as we'll see throughout the course there are many other use-cases.
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Damien McMahon (CC BY 2.0)" -->
**This isn't a math course.**  
  
**You won't become an expert, but hopefully a power-user!**

![bg right:30%](images/00-satellite_dish.jpg)

<!--
- Cryptography relies on a lot of mathematical voodoo

- While important knowledge, the mathematical/technical implementation details isn't necessarily
required to make use of the technology

- The are lots of great resources online for those interested in dark magic behind cryptography,
but the focus on this course will be highly practical and the majority of time will be spent on how
various cryptographic primitives/technologies can be used and when they shouldn't be

- It's a huge subject, we won't be able to go into details regarding everything but instead focus
on the most relevant areas
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## Requires basic knowledge of...
- Linux
- Shell scripting and Python programming
- Networking
- Virtualisation and Docker

![bg right:30%](images/00-chip_closeup.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Amy Nelson (CC BY 3.0)" -->
## How we will do it
- Lectures and Q&A
- Individual and group presentations
- Lab exercises
- Continuous reflection
- Quizzes and scored tests

![bg right:30%](images/00-lizard.jpg)

<!--
- We'll cover lots of things in a short amount of time

- In order to be able to do this we'll use scientifically proven methods to Make It Stick

- Basically what the slide says

- Don't forget to have fun!

- If available, show detailed course schedule
-->

---
For detailed notes, glossary, labs and similar, see:   
**[%RESOURCES_DOMAIN%/crypto.zip](https://%RESOURCES_DOMAIN%/crypto.zip)**.  
  
These resources should be seen as a complement to an instructor lead course, not a replacement.

![bg right 90%](qr_codes/presentation_zip.link.svg)

<!--
- There are several resources to help you learn

- Speaker notes in slides are heavily recommended for recaps/deep diving

- May also be available through LMS, depending on how the course is consumed

- The course is designed to be instructor lead, won't make the most of it on your own, see as aid

- Presentations may be recorded, but only the speaker side for good and bad
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergio Delgado (CC BY 2.0)" -->
## Acknowledgements
Thanks to [IT-Högskolan](https://www.iths.se/) and Särimner for enabling development of the course.
  
Thanks to [Yubico](https://www.yubico.com/) for providing YubiKeys to in-class students for labs!    
  
Thanks to [Mullvad VPN](https://mullvad.net/) for providing voucher codes a lab rewards.  
  
Hats off to all FOSS developers and free culture contributors making it possible.

![bg right:30%](images/00-sloth.jpg)

<!--
The course wouldn't be available if it wasn't for financial support - Thanks!
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergio Delgado (CC BY 2.0)" -->
## Contributors <3
- [Joel Rangsmo](https://github.com/doctor-love)
- Kristin Karlsson
- [Patrik Gäfvert](https://github.com/patrikgafvert)

![bg right:30%](images/00-sloth.jpg)

<!--
People who have contributed to the course
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jorge Franganillo (CC BY 2.0)" -->
## Free as in beer and speech
Is anything unclear? Got ideas for improvements? Don't fancy the animals in the slides?  
  
Create an issue or submit a pull request to
[the repository on Github](https://github.com/menacit/practical\_cryptography\__course)!

![bg right:30%](images/00-forest.jpg)

<!--
- Encourage participants to make the course better

- Learners are likely the best to provide critique, lecturers are likely a bit home-blind

- No cats or dogs allowed!

- Feel free to share it with friends or use it yourself later in your career
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
# Let us dig in!

![bg right:30%](images/00-lock.jpg)
