---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Symmetric security"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Presentation about symmetric encryption security"
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

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
# Symmetric security
### Good, bad and the ugly

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
## We want our algorithms to be...
- Fast/cheap to use, slow/expensive to break
- Safe against "known-plaintext" attacks  
- Immune to frequency analysis
- Publicly auditable

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
## Keys are key
Symmetric ciphers depend on a key
for encryption and decryption.  

Fixed size(s) in bits,
defined per algorithm.

![bg right:30%](images/08-rusty_key.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Key != Password.  

Typically created using a
**R**andom **N**umber **G**enerator or
**K**ey **D**erivation **F**unction
(more about these later).

![bg right:30%](images/08-cherry_trees.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## Example key sizes
- **DES**: 56 bits
- **3DES**: 168 bits
- **AES**: 128, 192 or 256 bits
- **ChaCha20**: 128 or 256 bits
  
**What do these numbers mean?!**

![bg right:30%](images/08-random_numbers.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
A two bit key can be either
"00", "01", "10" or "11" (4 possibilities).

A four bit key can be either
"0000", "0001", "0011", "0111", "1111",
"1000", "1100", "1110", "1111", "1001"...
(16 possibilities).

A fifty-six bit key can be arranged in
**72 057 594 037 927 936** possible ways!

![bg right:30%](images/08-planetarium_projector.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Seventy-two quadrillion,
fifty-seven trillion,
five hundred and ninety-four billion,
thirty-seven million, nine hundred and
twenty-seven thousand and nine hundred
and thirty-six.

![bg right:30%](images/08-planetarium_projector.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% The Preiser Project (CC BY 2.0)" -->
With one guess per second,
it would take 2283368000 years.  

The difficulty of key size
doesn't scale linearly.  
  
Sorry, humans -
that's waaay out of your league!  

Is this a big number for computers?

![bg right:30%](images/08-pcb_man.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
## Cracking DES
Got a gaming rig at home?
An Nvidia 4090 GPU can try 
~six billion keys per second.  

The \+ten-year old ["crack.sh-system"](https://crack.sh/).
can try ~seven-and-a-half trillion
keys per second.  
  
That's the whole key-space in
twenty-six hours! \o/

![bg right:30%](images/08-brick_hole.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Randy Adams (CC BY-SA 2.0)" -->
**26 hours \< 2283368000 years.**

![bg right:30%](images/08-mannequin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% D. Essl / ESO (CC BY 4.0)" -->
That is old \~off-the-shelf hardware.

Who knows what _\[REDACTED\]_
have in their basements?

![bg right:30%](images/08-eso_headquarters.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
But what key size is "good enough"?

It depends!™

Let's have a look at what [BSI](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=14),
[NCA SA](https://nca.gov.sa/ncs_en.pdf) and [NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf) have to say.

![bg right:30%](images/08-sleeping_statue_on_rock.jpg)

<!--
BSI: Section 1.1
NCA SA: Section 1.2 and 2.1.2
NIST: Section 5.6.3
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## Size doesn't matter (that much)
Larger keys are nice, but with diminishing
returns and performance penalties.  

Design issues in algorithms and faulty
implementations are the primary ways
modern cryptography is broken.  

3DES keys are 168 bits, but in
practice only provides 112 bits
of security due to design flaws.

How much more secure is AES 256
compared to AES 128? \\\_o\_/

![bg right:30%](images/08-abandoned_factory.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
But AES is fine right?
Isn't it _MILITARY GRADE ENCRYPTION_?  
  
Let me introduce you to block cipher modes.

![bg right:30%](images/08-missile_computer.jpg)

<!--
https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg
https://upload.wikimedia.org/wikipedia/commons/d/d6/ECB_encryption.svg
https://upload.wikimedia.org/wikipedia/commons/9/96/Tux_encrypted_ecb.png
https://upload.wikimedia.org/wikipedia/commons/8/80/CBC_encryption.svg
https://upload.wikimedia.org/wikipedia/commons/0/00/Tux_encrypted_ctr.png
https://upload.wikimedia.org/wikipedia/commons/e/ef/BlockCipherModesofOperation.svg
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kevin Dooley (CC BY 2.0)" -->
## AES cipher modes
- ECB
- CBC
- PCBC
- CFB
- CCM
- GCM
- XTS

....

![bg right:30%](images/08-plants.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## CBC
Oldie but ~~goldie~~ typically okay!

## XTS
Most commonly used for
**F**ull **D**isk **E**ncryption.

### GCM
Fast and integrity protected,
but tricky to implement safely.

![bg right:30%](images/08-boarded_windows.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
Many block cipher modes exist.  

Most are in practice okay - avoid ECB!  

Typically require a randomly generated
**I**nitialization **V**ector (AKA **"nonce"**)
that should not be reused or lost.

![bg right:30%](images/08-mesh_head.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Darkday (CC BY 2.0)" -->
## Wrapping up
If you don't wanna think about it,
use AES with \>=192 bits keys and
a mode that's not ECB.
  
Don't roll your own crypto,
except for learning purposes!

![bg right:30%](images/08-burnt_and_abandoned_computer.jpg)
