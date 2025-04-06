---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Cryptography in ransomware"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Use-cases of cryptography in ransomware"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
# Ransomware 
### Use-case study of cryptography

![bg right:30%](images/42-broken_hdd.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
## What is ransomware?
Malware that makes files/data inaccessible, typically using encryption.  
  
Intruders demand payment to release files/data.  

Hard to estimate total global damages,  
[some](https://ransomwarecost.com/) predict it to reach 50B USD in 2025.

![bg right:30%](images/42-broken_hdd.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% John K. Thorne (CC0 1.0)" -->
### What makes it a good showcase?
Basically all cryptography techniques we've talked about are involved.

![bg right:30%](images/42-domes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
# Let's dig in!

![bg right:30%](images/42-cave.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Andrew Hart (CC BY-SA 2.0)" -->
### Initial access / intrusion
The malicious code needs to be deployed somewhere, preferably on a business critical system.  
  
**Initial access brokers** specialize in selling access to user accounts and systems.  
  
Foothold is usually obtained by:
- Credential phishing
- Password leaks and reuse
- Exploitation of vulnerable systems

![bg right:30%](images/42-broken_glass.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
### Bypassing security controls
Various different methods to stay under the radar and avoid detection.  
  
One is to steal or fraudulently obtain code-signing certificates.

![bg right:30%](images/42-cd_macro.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
### Increasing recovery cost
Delete/corrupt backup archives.  
  
Steal sensitive/embarrassing information
for "double extortion".  
  
Target firmware/lower-level code that is tricky
to detect/recover from, especially with
"secure boot" or "measured boot".

![bg right:30%](images/42-outdoors_pcb.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
### Encrypting the data
Symmetric encryption of (all) files
with randomly generated key.  
  
Randomly generated symmetric key is
encrypted against intruder's public key.  
  
Commonly use established standards,
such as AES and RSA.
  
Often relies on the same cryptography
libraries as everyone else, because
it is hard to get right.

![bg right:30%](images/42-cube_wave.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kevin Dooley (CC BY 2.0)" -->
### Establishing contact
So-called "ransom notes" are left of the affected systems.  
  
Instructions describing how victims can get their data back.  
  
Typically contains an .onion-link for more details, payment information and "customer support".

![bg right:30%](images/42-onion.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marco Verch (CC BY 2.0)" -->
### Getting paid
Ransom must typically be paid in a cryptocurrency.  
  
Bitcoin and Monero are the most common options.  
  
Cashing out safely is not trivial,
may require tumbling and trickery.

![bg right:30%](images/42-bitcoin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
## Wrapping up
Organizations take security and disaster
recovery way more seriously these days.  
  
"RaaS" is enabling specialization.  
  
"Cyber insurance" has... interesting side-effects.

![bg right:30%](images/42-broken_hdd.jpg)
