---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
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
  table strong {
    color: #d63030;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Robert Jemimus (CC BY 2.0)" -->
# Symmetric encryption
### An introduction to it's uses

![bg right:30%](images/03-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Reid Campbell (CC0 1.0)" -->
Same key is used for encryption and decryption.  
  
Used primarily for protecting **confidentiality**
of information **at rest** and **in transit**.

How does symmetric encryption of
binary data work?

![bg right:30%](images/03-reflective_lake.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## XOR logical operator
Many symmetric algorithms relies on
the "E**x**clusive **or** logical operator"
to produce ciphertext by mixing a
derived key and plaintext data.

XOR plays the same role as
Vigenère alphabet table.

Let's have a look at the
operator's "truth table"!

![bg right:30%](images/03-rusty_x_chain.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
| Input A (data) | Input B (key)  | Result |
|----------------|----------------|--------|
| 0              | 0              | 0      |
| 0              | 1              | 1      |
| 1              | 0              | 1      |
| 1              | 1              | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
Let's encrypt the byte `0 1 0 1 1 0 0 0` ("X")
with the key `0 1 0 0 1 1 0 1` ("M").

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0  1  1  0  0  0
Key:         0  1  0  0  1  1  0  1
Ciphertext:  ?  ?  ?  ?  ?  ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:  >0< 1  0  1  1  0  0  0
Key:        >0< 1  0  0  1  1  0  1
Ciphertext: >0< ?  ?  ?  ?  ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| **0**               | **0**         | **0**  |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0 >1< 0  1  1  0  0  0
Key:         0 >1< 0  0  1  1  0  1
Ciphertext:  0 >0< ?  ?  ?  ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| **1**               | **1**         | **0**  |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1 >0< 1  1  0  0  0
Key:         0  1 >0< 0  1  1  0  1
Ciphertext:  0  0 >0< ?  ?  ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| **0**               | **0**         | **0**  |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0 >1< 1  0  0  0
Key:         0  1  0 >0< 1  1  0  1
Ciphertext:  0  0  0 >1< ?  ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| 0                   | 1             | 1      |
| **1**               | **0**         | **1**  |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0  1 >1< 0  0  0
Key:         0  1  0  0 >1< 1  0  1
Ciphertext:  0  0  0  1 >0< ?  ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| **1**               | **1**         | **0**  |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0  1  1 >0< 0  0
Key:         0  1  0  0  1 >1< 0  1
Ciphertext:  0  0  0  1  0 >1< ?  ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| **0**               | **1**         | **1**  |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0  1  1  0 >0< 0
Key:         0  1  0  0  1  1 >0< 1
Ciphertext:  0  0  0  1  0  1 >0< ?
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| **0**               | **0**         | **0**  |
| 0                   | 1             | 1      |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
```
Plaintext:   0  1  0  1  1  0  0 >0<
Key:         0  1  0  0  1  1  0 >1<
Ciphertext:  0  0  0  1  0  1  0 >1<
```
| Input A (plaintext) | Input B (key) | Result |
|---------------------|---------------|--------|
| 0                   | 0             | 0      |
| **0**               | **1**         | **1**  |
| 1                   | 0             | 1      |
| 1                   | 1             | 0      |

![bg right:30%](images/03-cross_pattern.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Leah Oswald (CC BY-SA 2.0)" -->
We got `0 0 0 1 0 1 0 1` as our ciphertext!  

How do we perform decryption?

![bg right:30%](images/03-smoke_person.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Leah Oswald (CC BY-SA 2.0)" -->
```
Ciphertext:  0  0  0  1  0  1  0  1
Key:         0  1  0  0  1  1  0  1
Plaintext:   ?  ?  ?  ?  ?  ?  ?  ?
```
| Input A (ciphertext) | Input B (key) | Result |
|----------------------|---------------|--------|
| 0                    | 0             | 0      |
| 0                    | 1             | 1      |
| 1                    | 0             | 1      |
| 1                    | 1             | 0      |

![bg right:30%](images/03-smoke_person.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Leah Oswald (CC BY-SA 2.0)" -->
```
Ciphertext: >0< 0  0  1  0  1  0  1
Key:        >0< 1  0  0  1  1  0  1
Plaintext:  >0< ?  ?  ?  ?  ?  ?  ?
```
| Input A (ciphertext) | Input B (key) | Result |
|----------------------|---------------|--------|
| **0**                | **0**         | **0**  |
| 0                    | 1             | 1      |
| 1                    | 0             | 1      |
| 1                    | 1             | 0      |

![bg right:30%](images/03-smoke_person.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Leah Oswald (CC BY-SA 2.0)" -->
```
Ciphertext:  0 >0< 0  1  0  1  0  1
Key:         0 >1< 0  0  1  1  0  1
Plaintext:   0 >1< ?  ?  ?  ?  ?  ?
```
| Input A (ciphertext) | Input B (key) | Result |
|----------------------|---------------|--------|
| 0                    | 0             | 0      |
| **0**                | **1**         | **1**  |
| 1                    | 0             | 1      |
| 1                    | 1             | 0      |

![bg right:30%](images/03-smoke_person.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Leah Oswald (CC BY-SA 2.0)" -->
```
Ciphertext:  0  0 >0< 1  0  1  0  1
Key:         0  1 >0< 0  1  1  0  1
Plaintext:   0  1 >0< ?  ?  ?  ?  ?
```
| Input A (ciphertext) | Input B (key) | Result |
|----------------------|---------------|--------|
| **0**                | **0**         | **0**  |
| 0                    | 1             | 1      |
| 1                    | 0             | 1      |
| 1                    | 1             | 0      |

![bg right:30%](images/03-smoke_person.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
Not that hard, right?  

A side effect of using XOR this way is
that we can recover (parts of) the key
if we know (parts of) the plaintext.  

Exploiting this fact is called a
**known-plaintext attack**.  

Modern encryption ciphers put a lot
of effort on trying to prevent
it and other similar issues.

![bg right:30%](images/03-canaima.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
```
Plaintext:   0 >1< 0  1  1  0  0  0
Ciphertext:  0 >0< 0  1  0  1  0  1
Key:         0 >1< ?  ?  ?  ?  ?  ?
```
| Input A (plain)      | Input B (cipher) | Result |
|----------------------|------------------|--------|
| 0                    | 0                | 0      |
| **0**                | **1**            | **1**  |
| 1                    | 0                | 1      |
| 1                    | 1                | 0      |

![bg right:30%](images/03-canaima.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
Not that hard, right?  

A side effect of using XOR this way is
that we can recover (parts of) the key
if we know (parts of) the plaintext.  

Exploiting this fact is called a
**known-plaintext attack**.  

Modern encryption ciphers put a lot
of effort on trying to prevent
it and other similar issues.

![bg right:30%](images/03-canaima.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Reid Campbell (CC0 1.0)" -->
Let's move on, shall we?

![bg right:30%](images/03-reflective_lake.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Reid Campbell (CC0 1.0)" -->
Most symmetric ciphers are categorized as
**block ciphers** or **stream ciphers**.  

![bg right:30%](images/03-reflective_lake.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
Block ciphers split plaintext data into
parts of a fixed size (128 bits, for example)
and encrypts each part ("block") separately.

Most commonly used for "at rest" encryption.  

![bg right:30%](images/03-cubes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Brandt (CC0 1.0)" -->
Stream ciphers performs encryption of
each bit "independently" in a stream
of plaintext data.

Commonly used for "in transit" encryption.

![bg right:30%](images/03-tumbler.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
Which approach is the best?  

What are the advantages and disadvantages?

![bg right:30%](images/03-concret_sculpture.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
Hard to answer is a general/honest way.  

Historically, many have considered
block ciphers harder to break and
stream ciphers more efficient.

_(not necessarily true,
depends on algorithms compared)_

![bg right:30%](images/03-concret_sculpture.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Brandt (CC0 1.0)" -->
## Meet the algos

![bg right:30%](images/03-neon_voxel.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rod Waddington (CC BY-SA 2.0)" -->
## (3)DES
**D**ata **E**ncryption **S**tandard.  
  
Block cipher algorithm defined in 1977
by the US government as a part of the
**F**ederal **I**nformation **P**rocessing **S**tandard.  

Key size was deemed inadequate as
computer performance increased rapidly,
replaced by "Triple DES" in mid 90s.

If you see it used, assume it's broken\*.

![bg right:30%](images/03-bamboo_construction.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## AES
**A**dvanced **E**ncryption **S**tandard,
also known as **"Rijndael"**.  

Block cipher standardized in 2001
by the US **N**ational **I**nstitute of
**S**tandards and **T**echnology
after a public competition.

Supports different key sizes and "modes"
(more about that later).

Resource hungry, but accelerated in
hardware by most processors ("AES-NI").

![bg right:30%](images/03-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bruno Cordioli (CC BY 2.0)" -->
## (A)RC4
**R**ivest **C**ipher **4**
(or perhaps "**R**on's **C**ode **4**").  

Proprietary stream cipher developed
by Ron Rivest in 1987, later leaked
and reversed engineered.  

Historically used in network protocols
like WEP/WPA, SSL/TLS and RDP.

Highly efficient, but considered
insecure by modern standards.

![bg right:30%](images/03-sgi_indy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Wolfgang Stief (CC0 1.0)" -->
## ChaCha20
Successor to the "Salsa20" stream cipher,
developed by Daniel J. Bernstein.  

Used in several network protocols,
like TLS, standardized by the
**I**nternet **E**ngineering **T**ask **F**orce. 

Relatively simple to
implement correctly ("securely").

Fast/efficient even without
hardware acceleration.

![bg right:30%](images/03-cooling_system.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Woah, that's a lot of acronyms!  

Let's look at how we can utilize
"at rest" encryption to protect
our precious information.

![bg right:30%](images/03-bismuth.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Data encryption can be implemented at...

- File level
- File system layer
- Block layer
- Hardware layer

![bg right:30%](images/03-bismuth.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pumpkinmook (CC BY 2.0)" -->
## File level
Cherry-pick files and encrypt em'!  

Built-in support in several file formats,
like PDF, DOCX and XLSX.  

Encrypted ZIP archives are a popular option
(often using broken ciphers like 3DES).

Useful for transferring sensitive data
over untrusted networks or easily lost
storage mediums, like USB drives.

![bg right:30%](images/03-censored_smoke.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## File system layer
Modern file systems like
EXT4, BTRFS, ZFS and APFS natively support
encrypting selective parts file system tree,
like specific directories.  

Used to provide per-user data encryption
on Android and MacOS.  

Efficient and seamless, but may leak
metadata about encrypted files and
leave traces in unencrypted parts
of the file system.

![bg right:30%](images/03-clover_face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kevin Dooley (CC BY 2.0)" -->
## Block layer
Application/OS provides a
virtual block device (storage disk)
that transparently encrypts data
before storage on physical disk.

Popular option for
**F**ull **D**isk **E**ncryption-solutions
like BitLocker, VeraCrypt and LUKS.

All data is encrypted, regardless of
sensitivity (for good and bad).

![bg right:30%](images/03-biosphere_2.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
## Hardware layer
Encryption is handled in the
storage drive without assistance
from the host's operating system.  
  
"Opal" is a common standard for
**S**elf-**E**ncrypting **D**rives developed by
the **T**rusted **C**omputing **G**roup.

\~No performance overhead, but require
trust in a proprietary black box.

![bg right:30%](images/03-broken_hdd.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Forsaken Fotos (CC BY 2.0)" -->
## Some final notes
Throughout the course, we'll dig deeper into
tools for symmetric data encryption
at the file and block layer.

Passphrase is not the same as encryption key,
typically used to derive/unlock it.  
  
The devices used to encrypt and decrypt
data must still be trusted.  

![bg right:30%](images/03-airplane_wreck.jpg)
