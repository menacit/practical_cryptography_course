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

Most symmetric ciphers are categorized
as **block ciphers** or **stream ciphers**.  

![bg right:30%](images/03-reflective_lake.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
Block ciphers split plaintext data into
parts of a fixed size and encrypts each
part/block independently.

Most commonly used for
"at rest" encryption.  

![bg right:30%](images/03-cubes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Brandt (CC0 1.0)" -->
Stream ciphers performs encryption of
each bit in a stream of plaintext.

Most commonly used for
"in transit" encryption.

![bg right:30%](images/03-tumbler.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Brandt (CC0 1.0)" -->
## Meet the algos

![bg right:30%](images/03-neon_voxel.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rod Waddington (CC BY-SA 2.0)" -->
## (3)DES
**D**ata **E**ncryption **S**tandard.  
  
Block cipher released in 1977
by the US government as a part of the
**F**ederal **I**nformation **P**rocessing **S**tandard.  

If you see it, assume that it's broken.

![bg right:30%](images/03-bamboo_construction.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## AES
**A**dvanced **E**ncryption **S**tandard,
also known as **"Rijndael"**.  

Block cipher standardized in 2001 by
the US **N**ational **I**nstitute of
**S**tandards and **T**echnology.

Supports different key sizes and modes
(more about that later).

Heavy, but accelerated in hardware by
most modern processors ("AES-NI").

![bg right:30%](images/03-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bruno Cordioli (CC BY 2.0)" -->
## (A)RC4
**R**ivest **C**ipher **4**
(or perhaps "**R**on's **C**ode **4**").  

Proprietary stream cipher developed
by Ron Rivest in 1987.  

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

Fast/efficient even without
hardware acceleration.

![bg right:30%](images/03-cooling_system.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## "At rest" encryption
We want to keep some information
secret, don't we?

Data encryption can be
implemented at...
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

![bg right:30%](images/03-censored_smoke.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## File system layer
Modern file systems like
EXT4, BTRFS, ZFS and APFS natively support
encrypting selective parts file system tree.  

Used to provide per-user data encryption
on Android and MacOS.  

Efficient, but may leak metadata
about encrypted files.

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

All data is encrypted,
regardless of sensitivity.

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

No performance overhead, but require
trust in a proprietary black box.

![bg right:30%](images/03-broken_hdd.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Forsaken Fotos (CC BY 2.0)" -->
## Some final notes
Passphrase is not the same as encryption key.  
  
Your device must still be trusted.  

![bg right:30%](images/03-airplane_wreck.jpg)
