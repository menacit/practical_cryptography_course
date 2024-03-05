---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Basics recap"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Recap of basics in the practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Mathias Appel (CC0 1.0)" -->
## Cryptography basics recap

![bg right:30%](images/06-red_panda.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Wolfgang Stief (CC0 1.0)" -->
**Cryptography** helps us ensure
**confidentiality** and **integrity** of information.  
  
**Steganography** is a related practice in which information is **hidden/obscured**.  
  
These have historically been used in unison.

![bg right:30%](images/06-chips_on_pcb.jpg)

---
### Caesar cipher
![bg center 60%](images/06-caesar_cipher.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Theo Crazzolara (CC BY 2.0)" -->
```
Plain-alphabet:
a b c d e f g h i j k l m →
n o p q r s t u v w x y z

Cipher-alphabet:
X Y Z A B C D E F G H I J →
K L M N O P Q R S T U V W
```

```
Plaintext:  i  w i l l  b a k e  a  c a k e
Ciphertext: F  T F I I  Y X H B  X  Z X H B
```

```
Plaintext:  m a k e  i t  s o o n  p l e a s e
Ciphertext: J X H B  F Q  P L L K  M I B X P B
```

![bg right:30%](images/06-lightbulb.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
Let's encrypt "**cafe**"
with the keyword "**bad**"
using the **Vigenère cipher**.

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
```
Plaintext:   c  a  f  e
Keyword:     B  A  D  B
Ciphertext:  ?  ?  ?  ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |  E  |  F  |
|  A  |  A  |  B  |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
```
Plaintext:  >c< a  f  e
Keyword:    >B< A  D  B
Ciphertext: >D< ?  ?  ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |**C**|  D  |  E  |  F  |
|  A  |  A  |  B  |**C**|  D  |  E  |  F  |
|**B**|**B**|**C**| _D_ |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
```
Plaintext:   c >a< f  e
Keyword:     B >A< D  B
Ciphertext:  D >A< ?  ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |**A**|  B  |  C  |  D  |  E  |  F  |
|**A**| _A_ |  B  |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
```
Plaintext:   c  a >f< e
Keyword:     B  A >D< B
Ciphertext:  D  A >C< ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |  E  |**F**|
|  A  |  A  |  B  |  C  |  D  |  E  |**F**|
|  B  |  B  |  C  |  D  |  E  |  F  |**A**|
|  C  |  C  |  D  |  E  |  F  |  A  |**B**|
|**D**|**D**|**E**|**F**|**A**|**B**| _C_ |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steven Kay (CC BY-SA 2.0)" -->
```
Plaintext:   c  a  f >e<
Keyword:     B  A  D >B<
Ciphertext:  D  A  C >F<
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |**E**|  F  |
|  A  |  A  |  B  |  C  |  D  |**E**|  F  |
|**B**|**B**|**C**|**D**|**E**| _F_ |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-pixel_map.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
# DACF!

### How about decryption?

![bg right:30%](images/06-lego.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
```
Plaintext:   ?  ?  ?  ?
Keyword:     B  A  D  B
Ciphertext:  D  A  C  F
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |  E  |  F  |
|  A  |  A  |  B  |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-abstract_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
```
Plaintext:  >c< ?  ?  ?
Keyword:    >B< A  D  B
Ciphertext: >D< A  C  F
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  | _C_ |  D  |  E  |  F  |
|  A  |  A  |  B  |**C**|  D  |  E  |  F  |
|**B**|**B**|**C**|**D**|  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-abstract_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
```
Plaintext:   c >a< ?  ?
Keyword:     B >A< D  B
Ciphertext:  D >A< C  F
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     | _A_ |  B  |  C  |  D  |  E  |  F  |
|**A**|**A**|  B  |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-abstract_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
```
Plaintext:   c  a >f< ?
Keyword:     B  A >D< B
Ciphertext:  D  A >C< F
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |  E  | _F_ |
|  A  |  A  |  B  |  C  |  D  |  E  |**F**|
|  B  |  B  |  C  |  D  |  E  |  F  |**A**|
|  C  |  C  |  D  |  E  |  F  |  A  |**B**|
|**D**|**D**|**E**|**F**|**A**|**B**|**C**|
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-abstract_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Asparukh Akanayev (CC BY 2.0)" -->
```
Plaintext:   c  a  f >e<
Keyword:     B  A  D >B<
Ciphertext:  D  A  C >F<
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  | _E_ |  F  |
|  A  |  A  |  B  |  C  |  D  |**E**|  F  |
|**B**|**B**|**C**|**D**|**E**|**F**|  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-abstract_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Sergei F (CC BY 2.0)" -->
## Kerckhoffs' principle
> The security of a cipher
> must be based on the chosen key,
> not keeping the algorithm secret 
> (AKA "security through obscurity")

![bg right:30%](images/06-rusty_lock.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
### Symmetric cryptography
Same key is used for encryption and decryption.

### Asymmetric cryptography
Different keys are used for
encryption and decryption.
Can also be used for "digital signatures".

### One-way hash functions
The same plaintext always result in
the same ciphertext, but the ciphertext
should not be reversable to plaintext.

![bg right:30%](images/06-toolbox.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Wendelin Jacober (CC0 1.0)" -->
## Symmetric cryptography  
Used primarily for protecting **confidentiality**
of information **at rest** and **in transit**.

Most symmetric ciphers are categorized
as **block ciphers** or **stream ciphers**.  

![bg right:30%](images/06-cyberpunk_mirrors.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
Block ciphers split plaintext data into
parts of a fixed size and encrypts
each part/block independently.

Most commonly used for
"at rest" encryption.  

**DES** is bad example and
**AES** is a good one.

![bg right:30%](images/06-squares_plane.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Scott Merrill (CC BY-SA 2.0)" -->
Stream ciphers performs encryption of
each bit in a stream of plaintext.

Most commonly used for
"in transit" encryption.

**RC4** is bad example and
**ChaCha20** is a good one.

![bg right:30%](images/06-pipes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kristina Hoeppner (CC BY-SA 2.0)" -->
## Cryptography standardization
The US government entity
**N**ational **I**nstitute of
**S**tandards and **T**echnology
are heavily involved standardization
of cryptography.  

They are responsible for
**F**ederal **I**nformation
**P**rocessing **S**tandards,
such as FIPS 46-3 (DES) and FIPS 197 (AES).  

Modern cryptographic algorithms
are commonly audited/chosen through
international competitions.

![bg right:30%](images/06-llama.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Torres (CC BY 4.0)" -->
## Let's move forward!

![bg right:30%](images/06-dragon_fighter.jpg)
