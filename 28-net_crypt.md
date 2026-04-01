---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Network encryption tools"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to several tools used for network traffic encryption"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
# Network encryption tools
### Protecting layer one to seven

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Network traffic can be intercepted
anywhere between your phone in a café
and TikTok's fancy data center in Shenzhen.

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% TeleGeography (CC BY-SA 4.0)" -->
![bg center 100%](images/28-sub_cables.jpg)

<!--
https://www.submarinecablemap.com/
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Cryptography is used to protect confidentiality and integrity of communication.  
  
We've talked about TLS, let's have a look at the other network layers.

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## OSI model recap
1. Physical layer
2. Data link layer
3. Network layer
4. Transport layer
5. ~~Session layer~~
6. ~~Presentation layer~~
7. Application layer

**Common vocabulary, not reality.**

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Alternative: "TCP/IP model"
1. Link layer _(most commonly Ethernet)_
2. Internet layer _(IPv4 or IPv6)_
3. Transport layer _(TCP, UDP, ICMP...)_
4. Application layer _(DNS, HTTP, TLS...)_

![bg right:30%](images/28-face.jpg)


---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Mapping the models
| "OSI model" layer  | "TCP/IP model" layer |
|--------------------|----------------------|
| **1:** Physical    | N/A                  |
| **2:** Data link   | **1:** Link          |
| **3:** Network     | **2:** Internet      |
| **4:** Transport   | **3:** Transport     |
| **5:** Application | **4:** Application   |

**OCI model still acts as Interlingua.**

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
## "L1": Signal level encryption
Used to protect high-bandwidth/legacy links.  
  
"Transparent encryption" of all communication
that is provided by pricey HW.  
  
Easy to implement, suitable for legacy networks
and compliance checkboxes.

![bg right:30%](images/28-abstract_data.jpg)

<!--
https://www.advasecurity.com/en/innovation/layer-1-encryption
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jan Hrdina (CC BY-SA 2.0)" -->
## "L2": MACsec / IEEE 802.1AE
Open standard that extends Ethernet.  

Uses AES-GCM for confidentiality and integrity.  

Supported in fancy switches at "line-rate".
  
Leaks a bit of metadata (which MAC addresses
communicate with eachother).

![bg right:30%](images/28-train_tracks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nacho Jorganes (CC BY-SA 2.0)" -->
## "L3": IPsec
Family of open standards to provide a
secure version of IP.  
  
Supported by most OSes and network appliances.  
  
Act in "host-to-host" or "routed" mode.
  
Quiet a mess with gazillion different options for
encryption, integrity checking and authentication.

![bg right:30%](images/28-cow.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## "L4-L6": QUIC
Performant alternative to TCP that was
initially developed by Google.  
  
Uses UDP and cryptographic protections
based on TLS version 1.3.  
  
\~Used by HTTP version 3 and **D**NS-**o**ver-**Q**UIC.

![bg right:30%](images/28-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergei F (CC BY 2.0)" -->
## Let's talk about VPNs!

![bg right:30%](images/28-retro_switchboard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergei F (CC BY 2.0)" -->
**V**irtual **P**rivate **N**etwork.  
  
Creates a virtual network link between computers.
  
Access is restricted and traffic encrypted.  
  
"Site-to-site" or "user-to-site".

![bg right:30%](images/28-retro_switchboard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
### What about VPNs for anonymity?
Network traffic is routed through a
VPN provider and NATed to the Internet.  

Connection peers will see the VPN provider's
IP address as source, not the "real one".
  
Typically sold as penicillin for security,
don't believe the marketing!

How do you really know that they don't log
or try to manipulate your traffic?

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergei F (CC BY 2.0)" -->
## Give me some examples!

![bg right:30%](images/28-retro_switchboard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
## IPsec in "routed" mode

![bg right:30%](images/28-dome_with_pink_flower_bushes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mathias Appel (CC0 1.0)" -->
## OpenVPN
Oldie but goldie!  
  
Supports tunneling of OSI L2 and L3 traffic.  
  
PSK or X.509 for peer authentication.  
  
Supports storing client credentials
on HW token such as the YubiKey.  
  
Tons of configuration options,
for better or worse.

![bg right:30%](images/28-panda.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## WireGuard
Fast, modern and minimal.  
  
Only L3.  
  
Built-in support in Linux and \*BSD kernels,
software available for other OSes.  

![bg right:30%](images/28-minerals.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ESA (CC BY-SA 3.0 IGO)" -->
## Tailscale
Easy to use software for setting up a "mesh VPN"
(direct connections between all peers).

No need to send all traffic through some
centralized servers.

Uses a bag of "NAT hole punching" techniques
and WireGuard under the hood.

Connections are authenticated and established
through a proprietary cloud service, may be
replaced with the self-hostable ["Headscale"](https://headscale.net/stable/about/faq/).

![bg right:30%](images/28-namib_desert.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bixentro (CC BY 2.0)" -->
## Enterprise VPN appliances
Physical and virtual appliances
providing VPN functionality.  

Easy setup and lots of
fancy management functionality.  

Often decent cryptographic algorithms,
but riddled with other vulnerabilities.  
  
You don't want your
edge security products to be broken -
stay away from these!

![bg right:30%](images/28-business_man_graffiti.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Wrapping up
Which option should I choose?  

Well, that depends on your use-case -
more than one, get some defense in depth!

![bg right:30%](images/28-face.jpg)
