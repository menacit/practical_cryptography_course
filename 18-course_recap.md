---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
# Course recap
### Basics, symmetric crypto and hashing

![bg right:30%](images/18-party.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
Cryptography helps us ensure
**confidentiality, authenticity** and **integrity**
of information.  
  
**Steganography** is a related practice in which information is **hidden/obscured**.  
  
These have historically been used in unison.

![bg right:30%](images/18-red_plants.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
## Symmetric ciphers
**AES** and **ChaCha20** are good options.  
  
Stay away from **(3)DES** and **RC4**.  
  
[**K**ey **D**erivation **F**unctions](https://en.wikipedia.org/wiki/Key_derivation_function) are 
used to generate fixed-size keys from passwords.

![bg right:30%](images/18-tower.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Filippo Valsorda (CC BY-SA 4.0)" -->
AES and other block-ciphers
supports several different
[**"cipher modes"**](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation).  
  
The "**ECB**" mode is generally considered insecure.  
  
In addition to a key and plain-/cipher-text, most
modes require an [**"initialization vector"**](https://en.wikipedia.org/wiki/Initialization_vector)
for secure operations.

![bg right:30%](images/18-ecb_tux.jpg)

<!--
https://upload.wikimedia.org/wikipedia/commons/d/d6/ECB_encryption.svg
https://upload.wikimedia.org/wikipedia/commons/8/80/CBC_encryption.svg
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ESA (CC BY 3.0 IGO)" -->
Cryptographic hash functions are like checksums,
but designed to **never collide** _in practice_
(different inputs shouldn't produce same output).

A **digest** (AKA "hash") shouldn't help an
attacker guess the input/"plain text" data.

The output hash will be the same size regardless
if input data is 1kB or 10TB.  

![bg right:30%](images/18-satellite_photo.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
The "**S**ecure **H**ash **A**lgorithm"-family
of hash functions are standardized by NIST.  

SHA-2 (AKA "SHA256") is still widely used.  
SHA-3 (AKA "Keccak") is recommended
for new sensitive applications.  

Avoid SHA-1 and especially MD\* algorithms
as they suffer from known security flaws.

![bg right:30%](images/18-watch_out.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
Hashes are commonly used for
ensuring the integrity of data
(detect manipulation).  

Some examples are
**F**ile **I**ntegrity **M**onitoring systems
and "software allow-listing" applications.

![bg right:30%](images/18-wallcrack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fredrik Rubensson (CC BY-SA 2.0)" -->
**Password hashing** is used to avoid
**storing** passwords in plaintext.
  
Users using the same password will
have the generated same hash.  
  
Hashes can be pre-calculated
("**rainbow tables**").  
  
To mitigate these issues, passwords are **salted**
(mixed with other data) **before** being hashed.  
  
In order to avoid handling users "real passwords",
"**client-side hashing**" may be utilized in unison.

![bg right:30%](images/18-razorwire.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Alan Levine (CC0 1.0)" -->
Hashes can be used for
**P**roof **o**f **K**nowledge.  

Provide proof that you know
something without disclosing it.  

Commonly used in authentication protocols,
similar to "**T**ime-based **O**ne-**t**ime **P**assword".

![bg right:30%](images/18-payphone.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Hashes can be used for
**P**roof **o**f **W**ork.  
  
Perform computationally-expensive 
hashing to find a digest containing
some peer-specified data/pattern.  
  
Costly to produce, cheap to verify.  
  
Enables things like bot/spam protection,
rate-limiting and cryptocurrencies.

![bg right:30%](images/18-factory.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
### Challenge
Find some input data with the prefix
"quite\_r4ndom" that produces a
hex digest ending with "4e".

### Attempts
```
hash(quite_r4ndom-abc123) == 3e64[...]ca
hash(quite_r4ndom-abc124) == 910c[...]1c
[...]
hash(quite_r4ndom-abc982) == aad6[...]4e
```

### Result
859 rounds of hashing to solve challenge,
1 round to verify it.

![bg right:30%](images/18-factory.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
Cryptography tools won't hold
their promises forever.  
  
There are always "best-before" dates.

![bg right:30%](images/18-locks.jpg)
