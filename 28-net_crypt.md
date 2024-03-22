---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
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
### Working one to seven

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
5. Session layer
6. Presentation layer
7. Application layer

**Common vocabulary, not reality.**

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Alternative: "TCP/IP model"
1. Application layer
2. Transport layer
3. Internet layer 
4. Data link layer
5. Physical layer

**OCI model still acts as Interlingua.**

![bg right:30%](images/28-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
## "L1": Signal level encryption
Used to protect high-bandwidth/legacy links.  
  
"Transparent encryption" provided by pricey HW.  
  
Easy to implement, suitable for legacy networks and compliance checkboxes.

![bg right:30%](images/28-abstract_data.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jan Hrdina (CC BY-SA 2.0)" -->
## "L2": MACsec / IEEE 802.1AE
Open standard extending Ethernet with encryption.  

Supported in fancy switches at line-rate.
  
Uses AES-GCM for confidentiality and integrity.  

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
Performant alternative to TCP initially developed by Google.  
  
Uses UDP and a subset of TLS version 1.3.  
  
\~Used by HTTP version 3.

![bg right:30%](images/28-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
## Let's talk about VPNs!

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
Virtual Private Network.  
  
Creates a virtual network link between computers.  
  
Access is restricted and traffic encrypted.  
  
"Site-to-site" or "user-to-site".

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
### What about VPNs for anonymity?
Network traffic is routed through VPN provider and forwarded to the Internet.  
  
Typically sold as penicillin for security, don't believe the marketing.

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
### What about VPNs for anonymity?
Network traffic is routed through VPN provider and forwarded to the Internet.  
  
Typically sold as penicillin for security, don't believe the marketing.

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
## Give me some examples!

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
## IPsec in "routed" mode

![bg right:30%](images/28-statue.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mathias Appel (CC0 1.0)" -->
## OpenVPN
Oldie but goldie!  
  
Supports tunneling of L2 and L3 traffic.  
  
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
  
Built-in support in Linux and \*BSD kernels.  

![bg right:30%](images/28-minerals.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Which option should I choose?  

Well, that depends on your use-case -
likely more than one!

![bg right:30%](images/28-face.jpg)
