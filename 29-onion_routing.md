---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Onion routing"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to onion routing in the practical cryptography course"
keywords:
  - "cryptology"
  - "cryptography"
  - "practical"
  - "encryption"
  - "course"
color: "#ffffff"
class:
  - "invert"
style: |
  section.center {
    text-align: center;
  }
  table strong {
    color: #d63030;
  }
  table em {
    color: #2ce172;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dan Revoy (CC BY 4.0)" -->
# Onion routing
### A tear-free introduction

![bg right:30%](images/29-adventure.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dan Revoy (CC BY 4.0)" -->
VPN providers claim to offer bullet-proof anonymity and protection against hackers.  
  
Things are not that simple, as we've talked about.

![bg right:30%](images/29-adventure.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dan Revoy (CC BY 4.0)" -->
Hmmm... can't we just run a VPN tunnel
inside another VPN tunnel?  

![bg right:30%](images/29-adventure.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dan Revoy (CC BY 4.0)" -->
## Onion routing
Technique for anonymous
messaging/communication over a network.  
  
Protects the source address of the sender.  
  
Relies on heavily on asymmetric cryptography.

![bg right:30%](images/29-adventure.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Ada wants to send a message to Dan without
revealing her identity (source IP address).

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Ada knows the public keys for
Bob, Charlie and Dan.

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Ada encrypts her message against
Dan's public key:
> I know what you did last summer.

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Ada encrypts the encrypted message for Dan against Charlie's public key
with a message added:
> Please forward this to Dan!

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Ada encrypts the encrypted message for Charlie against Bob's public key with a message added:
> Please forward this to Charlie!

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
### Inner layer
Encrypted against Dan's public key:  
> I know what you did last summer.

### Middle layer
Encrypted against Charlie's public key:  
> Please forward this to Dan!

### Outer layer
Encrypted against Bob's public key:  
> Please forward this to Charlie!

![bg right:30%](images/29-skeleton.jpg)

---
## Message transfer
1. Ada sends encrypted message to Bob
2. Bob decrypts the outer layer and forwards the message to Charlie
3. Charlie decrypts the middle layer and forwards the message to Dan
4. Dan decrypts the inner layer and is terrified that his secret is known

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Bob knows that Ada (or rather her source address) wants to send an encrypted message to Charlie.  
  
Charlie knows that Bob sent him an encrypted message that should be forwarded to Dan.  
  
Dan knows that he got an encrypted message from Charlie.

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Bob can't tell that he is "first" in
the forwarding chain.  
  
Granted that chain members aren't gossiping with each other, Ada's involvement remains unknown
to Charlie and Dan.  
  
We could lower the risk by involving
Erin and Frank.

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
**Sounds neat! But can I actually use it?**

![bg right:30%](images/29-skeleton.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kenny Cole (CC BY 2.0)" -->
## Meet the "Tor project"
Largest onion routing network.  
  
Thousands of relays run by volunteers forward encrypted traffic around the globe.  
  
Provides anonymous access to the Internet and "hidden/onion services".  
  
Best enjoyed with [Tails](https://tails.boum.org/) or [Whonix](https://www.whonix.org/).

![bg right:30%](images/29-penguins.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kenny Cole (CC BY 2.0)" -->
## Be aware that...
- Relays can collaborate to lower anonymity
- "Exit nodes" can (and do) intercept traffic
- Usage may by itself be incriminating
- It is damn slow!

![bg right:30%](images/29-penguins.jpg)
