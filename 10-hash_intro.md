---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Hashing introduction"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to hashing and its cryptographic uses"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
# Cryptographic hashing
### AKA "one-way encryption"

![bg right:30%](images/10-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gytis B (CC BY-SA 2.0)" -->
Before we dig into cryptographic hashing,
let's talk about **check digits** and **checksums**.

![bg right:30%](images/10-vechicle_graveyard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gytis B (CC BY-SA 2.0)" -->
[Check digits](https://en.wikipedia.org/wiki/Check_digit) provide input error detection.  
  
Used for credit card numbers, Bitcoin addresses, patient identifiers, social security numbers...
  
The [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) is a common solution.

<!--
https://simplycalc.com/luhn-calculate.php
https://simplycalc.com/luhn-validate.php
-->

![bg right:30%](images/10-vechicle_graveyard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gytis B (CC BY-SA 2.0)" -->
[Checksums](https://en.wikipedia.org/wiki/Checksum) allows data integrity verification.  
  
Detect if information/files have been corrupted during network transfer or disk storage.  
  
The same input data should always result in the same output checksum.
  
[CRCs](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) are commonly utilized.

![bg right:30%](images/10-vechicle_graveyard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gytis B (CC BY-SA 2.0)" -->
```
$ cksum /etc/passwd
1530034959 1930 /etc/passwd

$ echo "Polar bears are cool" | cksum
3234477472 21
```

![bg right:30%](images/10-vechicle_graveyard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gytis B (CC BY-SA 2.0)" -->
```
$ echo "Polar bears are cool" | cksum
3234477472 21

$ echo "Polar beers are cool" | cksum
3688108819 21
```

![bg right:30%](images/10-vechicle_graveyard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
## The downsides
Different input values may produce the same output checksum.  
  
Not likely a problem, unless someone actively tries to find collisions.  
  
Used to attack data authenticity controls.  
  
[Cryptographic hashing](https://en.wikipedia.org/wiki/Cryptographic_hash_function) to the rescue!

![bg right:30%](images/10-gnome.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mauricio Snap (CC BY 2.0)" -->
Cryptographic hash functions are like checksums,
but designed to **never collide** in practice.  

Produces a **digest** as output,
more commonly called "hash".
  
Output shouldn't be predictable,
unless fully computed.  

Output shouldn't help you guess
contents of input data.

The output digest will be the same size
regardless if input data is 1kB or 10TB.  

![bg right:30%](images/10-eye.jpg)

---
```
$ echo "Polar bears are cool" | sha256sum
09c123f289f05677dbfa38dad697ae86ab2f3ef25c8935cfc8cd68a59f2f4d0a

$ echo "Polar beers are cool" | sha256sum
f170488bc43c691d3b9055567952d05d1cd43fbebd54c2098a0d5d7685d2eaa1

$ head --bytes 5G /dev/zero | sha256sum
7f06c62352aebd8125b2a1841e2b9e1ffcbed602f381c3dcb3200200e383d1d5
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mauricio Snap (CC BY 2.0)" -->
## Use-cases for hashing
- Data integrity checking
- Password storage/validation
- Authentication
- Fingerprinting
- Pseudo-random number generators
- Append-only databases/ledgers
- Proof of Knowledge
- Proof of Work

....

![bg right:30%](images/10-eye.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mauricio Snap (CC BY 2.0)" -->
## Notable families
- **MD:** Historically common, now broken
- **SHA:** Standards specified by [NIST](https://en.wikipedia.org/wiki/NIST)
- **BLAKE:** Commonly used in [KDFs](https://en.wikipedia.org/wiki/Key_derivation_function)

![bg right:30%](images/10-eye.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Elly Jonez (CC BY 2.0)" -->
Like other cryptography methods, hashing algorithms have a best-before date.  
  
Check out ["SHAttered"](https://shattered.io/):

```
$ shasum shattered-1.pdf 
38762cf7f55934b34d179ae6a4c80cadccbb7f0a

$ shasum shattered-2.pdf 
38762cf7f55934b34d179ae6a4c80cadccbb7f0a
```

If you wanna learn more about collision techniques and play with them, have a look at:
[github.com/corkami/collisions](https://github.com/corkami/collisions).

![bg right:30%](images/10-caution.jpg)

<!--
https://shattered.io/static/shattered.png
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Elly Jonez (CC BY 2.0)" -->
## TL;DR
Avoid MD4, MD5 and SHA-1.

SHA-2 _(AKA SHA256)_, SHA-3 _(AKA Keccak)_
and BLAKE\* are fine!

![bg right:30%](images/10-caution.jpg)
