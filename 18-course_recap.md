---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Course recap"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Recap of covered topics in practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Jennifer Morrow (CC BY 2.0)" -->
# Course recap
### Basics, symmetric crypto and hashing

![bg right:30%](images/18-spheres.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## Today's agenda
- Recap of covered topics
- Introduction to asymmetric cryptography
- Certificates and trust models
- Test!
- Lab / Q&A time

![bg right:30%](images/18-pandas.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
**Don't forget the lab deadline and use available time!**

![bg right:30%](images/18-pandas.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
**Don't forget the lab deadline and use available time!**

![bg right:30%](images/18-pandas.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
**Brasklapp: We'll revisit and dig deeper into the covered topics throughout the course.**  

![bg right:30%](images/18-pandas.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
**Cryptography** helps us ensure **confidentiality, integrity and origin/source** of information.  
  
**Steganography** is a related practice in which information is **hidden/obscured**.  
  
These have historically been used in unison.

![bg right:30%](images/06-pixel_forest.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
## Symmetric
Same key is used for encryption and decryption.

## Asymmetric
Different keys are used for encryption and decryption.

![bg right:30%](images/06-pixel_forest.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
## Symmetric encryption is...
- Typically used for confidentiality
- Relatively fast
- Often used in unison with hashing and asymmetric encryption

![bg right:30%](images/06-pixel_forest.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
**AES** is a well-supported standard and commonly used for at-rest encryption.  
  
**ChaCha** is a popular stream cipher alternative that is performant in software.  
  
[Key derivation functions](https://en.wikipedia.org/wiki/Key_derivation_function) (KDFs) are used
to generate keys from passphrases or similar.

![bg right:30%](images/06-pixel_forest.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Filippo Valsorda (CC BY-SA 4.0)" -->
AES supports several different
["cipher modes"](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation).  
  
The "**ECB**" mode is typically considered insecure.  
  
Most require an "[initialization vector](https://en.wikipedia.org/wiki/Initialization_vector)"
for secure operations.

![bg right:30%](images/18-ecb_tux.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mauricio Snap (CC BY 2.0)" -->
Cryptographic hash functions are like checksums, but designed to never collide in practice.  
  
Hash shouldn't be predictable, unless fully computed.    

The output hash will be the same size regardless if input data is 1kB or 10TB.  
  
Sometimes called "one-way encryption".

![bg right:30%](images/10-eye.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mauricio Snap (CC BY 2.0)" -->
## Use-cases for hashing
- Data integrity checking
- Password storage
- Authentication
- Fingerprinting
- Pseudo-random number generators
- Append-only databases/ledgers
- Proof of Knowledge
- Proof of Work

....

![bg right:30%](images/10-eye.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Lord Jaraxxus (CC BY-SA 4.0)" -->
**Password hashes** are used to avoid storing passwords in plaintext.
  
Users using the same password will have the generated same hash.  
  
Hashes can be pre-calculated ("rainbow tables").  
  
To mitigate these issues, passwords are **salted** (mixed with other data) before being hashed.

![bg right:30%](images/13-neon_sign.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Lord Jaraxxus (CC BY-SA 4.0)" -->
**Password hashes** are used to avoid storing passwords in plaintext.
  
Users using the same password will have the generated same hash.  
  
Hashes can be pre-calculated ("rainbow tables").  
  
To mitigate these issues, passwords are **salted** (mixed with other data) before being hashed.

![bg right:30%](images/13-neon_sign.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
**Cryptography solutions won't hold their promises forever. There are "best-before" dates.**

![bg right:30%](images/18-pandas.jpg)

