---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
## We want our encryption to be...
- Fast to use, slow to break
- Safe against "known-plaintext" attacks  
- Immune to frequency analysis

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
## Keys are key
Symmetric ciphers depend on a key for
encryption and decryption.  

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

The ten-year old ["crack.sh-system"](https://crack.sh/).
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## Size doesn't matter (that much)
Larger keys are nice,
but with diminishing returns
and performance penalties.  

How much more secure is AES 256
compared to AES 128?  

Design issues in algorithms and
faulty implementations are the
primary ways modern cryptography
is broken.  

3DES keys are 168 bits, but in
practice only provides 112 bits.

![bg right:30%](images/08-abandoned_factory.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
But isn't AES
_MILITARY GRADE ENCRYPTION_?  
  
Let me introduce you to block cipher modes.

![bg right:30%](images/08-missile_computer.jpg)

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
Oldie but goldie!

## XTS
Commonly used for FDE.

### GCM
Fast and integrity protected,
but tricky to implement from scratch.

![bg right:30%](images/08-boarded_windows.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
Many block cipher modes exist.  

Most are in practice okay - avoid ECB!  

Typically require a randomly generated
**I**nitialization **V**ector that
should not be reused.

![bg right:30%](images/08-mesh_head.jpg)
