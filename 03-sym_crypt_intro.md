---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Symmetric encryption introduction"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to uses of symmetric encryption"
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
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
# Symmetric encryption
### An introduction to it's uses

![bg right:30%](images/)

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Same key is used for encryption and decryption.  
  
Used primarily for protecting confidentiality of information **in transit** and **at rest**.

![bg right:30%](images/)

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
### DES
If you see it, assume that it's broken.

### AES
- Industry standard block cipher
- Supports different key sizes and "modes"
- Commonly hardware accelerated

### ChaCha20-Poly1305
- Popular stream cipher
- Highly efficient

![bg right:30%](images/)

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## At rest
- File level
- File system
- Block layer
- Hardware layer

![bg right:30%](images/)


---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Passphrase is not the same as encryption key.  
  
Your device must still be trusted.  

![bg right:30%](images/)
