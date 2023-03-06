---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: History/Basics"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Historic usage of cryptography and high-level fundamentals"
keywords:
  - "cryptology"
  - "cryptography"
  - "practical"
  - "encryption"
  - "course"
  - "lab"
  - "setup"
color: "#ffffff"
class:
  - "invert"
style: |
  section.center {
    text-align: center;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
# Historic usage and basics
### How did we end up here?

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
> URGHH - SUSSO! KEEF.
> HAAAWER NE NE!

— *Your average caveman*

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
> Greetings! I'm an excellent hunter. You see this fancy fireplace I got here? Let's make babies!

— *Your average caveman*

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
### Neat things about the written word
Allows preservation of complex information.  
  
Enables conversions and relaying of detailed information/instructions over vast distances.  
  
*(Kinda necessary for ruling an empire)*

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
**Perhaps you want to keep some things a secret?**

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Let's hide the information!  
  
We call this practice [**steganography**](https://en.wikipedia.org/wiki/Steganography).

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## Other notable examples
- Lemon juice ink
- Image file EXIF data
- [Printer tracking dots](https://en.wikipedia.org/wiki/Machine_Identification_Code)
- [Songs by Aphex Twin](https://twistedsifter.com/2013/01/hidden-images)

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## The downsides
Requires **trust** in courier(s) of the message.  
  
Mayhaps someone is a bit mad since you ruined their haircut?  

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
**Enter the ["Caesar cipher"](https://en.wikipedia.org/wiki/Caesar_cipher).**

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
```
QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
```
Plaintext:  the quick brown fox jumps over the lazy dog
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->

![bg center:70%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Probably quiet confusing at first, but easily broken.  
  
Largely security through obscurity.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Let's not just shift characters, but substitute them in a random order.  
  
```
Plaintext:  makeprofit
Ciphertext: 1234567890
```

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## The downsides
Every participant needs to know the cipheralphabet.  
  
Languages are not random, there are patterns and rules.  
  
People who try to break codes/ciphers are called **cryptanalysts**.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## Let's introduce keywords
Everyone can remember the word "lemon", right?  

```
Plaintext:  attackatdawn
Key: 	    LEMONLEMONLE
Ciphertext: LXFOPVEFRNHR
```

![bg right:40%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
**The cat and mouse game goes on.**

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Technologies such as the telegraph and radio revolutionized everything.  
  
That includes warfare.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Even if the cipher can't be broken, a lot can still be learned.  
  
From where was the message sent? By whom?  
  
We call this **metadata**.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Cryptography becomes too complex for _most_ humans.  
  
If machines maketh, let machine breaketh.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Things were more or less the same until the 1970s.  
  
Let me introduce you to **asymmetric cryptography**.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
## Symmetric
Same key is used for encryption and decryption.

## Asymmetric
Different keys are used for encryption and decryption.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
**Everyone can encrypt messages to me, but only I can decrypt them.**

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Also enables **"digital signatures"**.

Quite a complex topic that we will dig more into later.

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Did I mention **"one-way hash functions"**?  
  
Wide range of use-cases, including:
- Integrity validation
- Password storage
- Proof-of-Work

![bg right:30%](images/)

<!--
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX%  (CC BY 2.0)" -->
Cryptography helps us ensure confidentiality, integrity and the source of information.

![bg right:30%](images/)

<!--
-->
