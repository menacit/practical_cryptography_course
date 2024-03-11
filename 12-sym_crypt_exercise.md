---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Symmetric encryption exercise"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Symmetric encryption exercise in the practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Jan Hrdina (CC BY-SA 2.0)" -->
## Symmetric encryption exercise
### Can you crack the cipher?

![bg right:30%](images/12-optics.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jan Hrdina (CC BY-SA 2.0)" -->
## [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
Manually decrypt ciphertext **"DACFDBBDEFEC"**
using the key **"BAD"**
  
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |  E  |  F  |
|  A  |  A  |  B  |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |

**[courses+crypto_011201@%EMAIL_DOMAIN%](mailto:courses+crypto_011201@%EMAIL_DOMAIN%)**

![bg right:30%](images/12-optics.jpg)
