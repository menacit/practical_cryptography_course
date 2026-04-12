---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Course recap"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Quick recap of material in the practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Fredrik Rubensson (CC BY-SA 2.0)" -->
# Course recap
### Potpurri of exciting subjects

![bg right:30%](images/49-barbwire_beach.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stephanie Douglas (CC BY 4.0)" -->
## Protecting network traffic
We can protect confidentiality and integrity
of communicate at different OSI layers:

- **L1**: Signal-level encryption HW
- **L2**: MACsec
- **L3**: IPsec
- **L7**: SSH

Different pros/cons - preferably at
multiple layers for "**defense in depth**".

![bg right:30%](images/49-vlba_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stephanie Douglas (CC BY 4.0)" -->
## Usage of VPN
Software for **V**irtual **P**rivate **N**etworks  
creates an encrypted tunnel between
computers for traffic routing.
  
"Site-to-site" or "user-to-site".
  
Sometimes used to provide anonymous
Internet access (hide source IP).
  
Doesn't solve all security problems.

![bg right:30%](images/49-vlba_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yellowcloud (CC BY 2.0)" -->
## Onion routing
Communication method that relies on
multiple layer of asymmetric encryption
to protect anonymity (source IP) of users.
  
"Tor" is the most popular implementation.

"Onion services" (AKA "hidden services")
also protect the anonymity of network
services (hide their destination IP).

Foundation of the ["dark net"](https://en.wikipedia.org/wiki/Darknet).

![bg right:30%](images/49-nixie_tube.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Massey (CC BY 2.0)" -->
## Password cracking
**Online** cracking involves automated
login attempts using password candidates
against a network service or device.

**Offline** cracking aims to find a
password by feeding password candidates
into a hash function/KDF and comparing
the result against a "protected" value.

[Hydra](https://www.kali.org/tools/hydra/) is used for online cracking.
[Hashcat](https://hashcat.net) and ["John The Ripper"](https://www.openwall.com/john/)
are used for offline cracking.

![bg right:30%](images/49-finch_foundry_wheels.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Massey (CC BY 2.0)" -->
## Cracking hard and smart
GPUs are great for offline cracking,
FPGAs and ASICs are even better!
    
(Unless protected by a special purpose
algorithm like ["yescrypt"](https://en.wikipedia.org/wiki/Yescrypt).
  
By analyzing the psycology behind
password selection, we may provide
more likely candidates and thereby
crack more efficiently.

![bg right:30%](images/49-finch_foundry_wheels.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
## Random Number Generators
In order to produce secure
keys/salts/etc, we use **RNGs**.
  
Most modern computers have a
built-in **H**ard**w**are **RNG**.

Should preferably use a
_truly random_ source for entropy. 
  
**C**ryptographically **S**ecure **P**seudo-**RNG**
may be implemented in software and relies
on a **seed** to get started...  

![bg right:30%](images/49-allen_gardens_street_art.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
## Seeding the CSPRNG
CPU frequency, Wi-Fi signal strength,
mouse movement, disk read latency, etc.
may be combined to an upredictable seed.

HWRNG may contribute to the seed
(increase quality and minimize
risk of nasty backdoors).

If the same seed is provided, the CSPRNG will
produce the same random data after that point\*.

Often not desirable, but may be
used for "reproducible randomness"
to create "recoverable keys" and similar!

![bg right:30%](images/49-allen_gardens_street_art.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Franz van Duns (CC BY-SA 4.0)" -->
## Preventing/Detecting key abuse
A leaked private key could lead to severe
consequences, especially for CAs.
  
The "**CA**/**B**rowser Forum" aims to
enforce rules/guidelines to minimize
the risk for publicly trusted CAs.
  
"**C**ertificate **T**ransparency" helps us
detect maliciously issued certificates.

(more about that in the guest lecture!)

![bg right:30%](images/49-old_door_latch_and_lock.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Franz van Duns (CC BY-SA 4.0)" -->
## Hardware Security Modules
Special-purpose device used to
store/generate keys and perform
cryptographic operations.
  
Aims to enable usage of keys,
but not exfiltration of them.
  
Restrict access by PIN, biometrics,
"Proof of Presence", date/time,
"two-man rule", etc.

Not a "silver bullet", may still
be abused and potentially hacked.

![bg right:30%](images/49-old_door_latch_and_lock.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
## Shamir's Secret Sharing
Encryption method that requires multiple
parties to collaborate for decryption.

Encrypted data is split into multiple
**shares** with a configurable **threshold**
of shares required for decryption.

Any of the shares may be **combined** to
decrypt it (as long as threshold is met).

![bg right:30%](images/49-painted_brick_wall_with_holes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
## SSS example
PIN code for bank vault is split into 12
shares with a decryption threshold of 6.

The branch has 5 employees.

Head manager is given 4 shares
and remaing workers 2 each.

The manager and another worker may
open the vault together.

Three collaborating worker may also do it.

No one can open it by themselves.

![bg right:30%](images/49-painted_brick_wall_with_holes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fredrik Rubensson (CC BY-SA 2.0)" -->
Any questions before we move on?

![bg right:30%](images/49-barbwire_beach.jpg)
