---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
## Today's agenda
- Basics recap
- Demo of symmetric encryption tools
- Symmetric encryption security
- Lab / Q&A time
- Quiz!
- Reflection exercise

![bg right:30%](images/06-pixel_forest.jpg)

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
### Caesar cipher
![bg center 65%](images/06-caesar_cipher.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
Let's encrypt **cafebabe** with the keyword **bad** using the **Vigenère cipher**.

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!--
_footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)"
-->
```
Plaintext (Vertical):  c  a  f  e  b  a  b  e
Keyword (Horizontal):  B  A  D  B  A  D  B  A
Ciphertext:            ?  ?  ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical): >c< a  f  e  b  a  b  e
Keyword (Horizontal): >B< A  D  B  A  D  B  A
Ciphertext:           >D< ?  ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c >a< f  e  b  a  b  e
Keyword (Horizontal):  B >A< D  B  A  D  B  A
Ciphertext:            D >A< ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a >f< e  b  a  b  e
Keyword (Horizontal):  B  A >D< B  A  D  B  A
Ciphertext:            D  A >C< ?  ?  ?  ?  ?
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

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a  f >e< b  a  b  e
Keyword (Horizontal):  B  A  D >B< A  D  B  A
Ciphertext:            D  A  C >F< ?  ?  ?  ?
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

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a  f  e >b< a  b  e
Keyword (Horizontal):  B  A  D  B >A< D  B  A
Ciphertext:            D  A  C  F >B< ?  ?  ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |**B**|  C  |  D  |  E  |  F  |
|**A**|**A**| _B_ |  C  |  D  |  E  |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a  f  e  b >a< b  e
Keyword (Horizontal):  B  A  D  B  A >D< B  A
Ciphertext:            D  A  C  F  B >D< ?  ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |**A**|  B  |  C  |  D  |  E  |  F  |
|  A  |**A**|  B  |  C  |  D  |  E  |  F  |
|  B  |**B**|  C  |  D  |  E  |  F  |  A  |
|  C  |**C**|  D  |  E  |  F  |  A  |  B  |
|**D**| _D_ |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a  f  e  b  a >b< e
Keyword (Horizontal):  B  A  D  B  A  D >B< A
Ciphertext:            D  A  C  F  B  D >C< ?
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |**B**|  C  |  D  |  E  |  F  |
|  A  |  A  |**B**|  C  |  D  |  E  |  F  |
|**B**|**B**| _C_ |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
```
Plaintext (Vertical):  c  a  f  e  b  a  b >e<
Keyword (Horizontal):  B  A  D  B  A  D  B >A<
Ciphertext:            D  A  C  F  B  D  C >E<
```
|     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|
|     |  A  |  B  |  C  |  D  |**E**|  F  |
|**A**|**A**|**B**|**C**|**D**| _E_ |  F  |
|  B  |  B  |  C  |  D  |  E  |  F  |  A  |
|  C  |  C  |  D  |  E  |  F  |  A  |  B  |
|  D  |  D  |  E  |  F  |  A  |  B  |  C  |
|  E  |  E  |  F  |  A  |  B  |  C  |  D  |
|  F  |  F  |  A  |  B  |  C  |  D  |  E  |

![bg right:30%](images/06-cyberpunk_city.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
# DACFBDCE!

### How about decryption?

![bg right:30%](images/06-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
```
Plaintext (Vertical):     ?  ?  ?  ?  ?  ?  ?  ?
Keyword:                  B  A  D  B  A  D  B  A
Ciphertext (Horizontal):  D  A  C  F  B  D  C  E
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

![bg right:30%](images/06-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
```
Plaintext (Vertical):    >c< ?  ?  ?  ?  ?  ?  ?
Keyword:                 >B< A  D  B  A  D  B  A
Ciphertext (Horizontal): >D< A  C  F  B  D  C  E
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

![bg right:30%](images/06-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
```
Plaintext (Vertical):     c >a< ?  ?  ?  ?  ?  ?
Keyword:                  B >A< D  B  A  D  B  A
Ciphertext (Horizontal):  D >A< C  F  B  D  C  E
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

![bg right:30%](images/06-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
```
Plaintext (Vertical):     c  a >f< ?  ?  ?  ?  ?
Keyword:                  B  A >D< B  A  D  B  A
Ciphertext (Horizontal):  D  A >C< F  B  D  C  E
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

![bg right:30%](images/06-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
```
Plaintext (Vertical):     c  a  f >e< ?  ?  ?  ?
Keyword:                  B  A  D >B< A  D  B  A
Ciphertext (Horizontal):  D  A  C >F< B  D  C  E
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

![bg right:30%](images/06-chip.jpg)
