---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
An **asymmetric key pair** consist of a **public key** and a **private key**.  
  
The **public key** can be used by **anyone** to **encrypt** and **verify signed** data.  
  
The **private key** can be used by the **key holder** to **decrypt** and **digitally sign** data.

![bg right:30%](images/21-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
A certificate (typically) contains a **public key** and **metadata**.  
  
Examples of metadata are expiry time and "identities" tied to the key,
such as an email address or a DNS hostname.  
  
Certificates are typically cryptographically signed by third-parties, depending on trust model.

![bg right:30%](images/21-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
The two most common solutions are **RSA** and
**elliptic-curve cryptography (ECC)**.  
  
RSA keys bigger than 2024 bits are usually considered safe.  
  
ECC is more resource efficient/easier to safely implement than RSA and is thereby replacing it.

![bg right:30%](images/21-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
Several different **curves** are available for ECC.  
  
Common examples are **NIST P-256/P-384** and **Curve25519**.  
  
For guidance, checkout the ["SafeCurves" project](https://safecurves.cr.yp.to/).

![bg right:30%](images/21-chip.jpg)
