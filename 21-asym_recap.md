---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Asymmetric recap"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Recap of asymmetric cryptography in the practical cryptography course"
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
# Asymmetric cryptography
### A somewhat quick recap

![bg right:30%](images/21-sphere.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## Symmetric
Same key is used for encryption and decryption.

## Asymmetric
Different keys are used for encryption and decryption.

![bg right:30%](images/21-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
An **asymmetric key pair** consists of a
**public key** and a **private key**.  
  
The **private key** can be used by
the **key holder** to **decrypt** and
**digitally sign** data.
  
The **public key** can be used by
**anyone** to **encrypt** and
**verify signed** data.  

![bg right:30%](images/21-big_ben.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
The most common solutions are **RSA** and
those based on **E**lliptic-**C**urve **C**ryptography.  
  
RSA keys bigger than 2048 bits are
usually considered acceptable,
but NIST recommends 3072.
  
ECC is more resource efficient and
easier to correctly/safely implement
than RSA - thereby replacing it.

![bg right:30%](images/21-parallel_pipes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
Several different **curves** are available for ECC.  
  
Common examples are
**NIST P-256/P-384** and **Curve25519**.  
  
For guidance, checkout the ["SafeCurves" project](https://safecurves.cr.yp.to/).

![bg right:30%](images/21-curly_purple.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
A certificate (typically) contains
a **public key** and **metadata**.  
  
Examples of metadata are expiry time
and "identities" tied to the key,
such as an email address or a DNS hostname.  
  
They are cryptographically signed
by one or more third-parties,  
depending on trust model.

![bg right:30%](images/21-east_side_gallery.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Any questions? :-)

![bg right:30%](images/21-sphere.jpg)
