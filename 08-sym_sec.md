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
## Symmetric security
### Good, bad and the ugly

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
### We want our encryption to be...
- Fast to use, slow to break
- Safe against "known-plaintext" attacks  
- Non-deterministic

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
But isn't AES **MILITARY GRADE ENCRYPTION**?  
  
Let me introduce you to block cipher modes.

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
## AES cipher modes
- ECB
- CBC
- PCBC
- CFB

....

![bg right:30%](images/08-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Skippy (CC BY-SA 2.0)" -->
### CBC
Oldie but goldie

### XTS
Commonly used for FDE

### GCM
Fast and integrity protected!

![bg right:30%](images/08-dice.jpg)
