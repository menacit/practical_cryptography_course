---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
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
  table strong {
    color: #d63030;
  }
  table em {
    color: #2ce172;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Torkild Retvedt (CC BY-SA 2.0)" -->
# Historic usage and basics
### How did we end up here?

![bg right:30%](images/01-cameleon.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Reid Campbell (CC0 1.0)" -->
> URGHH - SUSSO! KEEF.
> HAAAWER NE NE!
> FEVA.

— *Your average caveperson*

![bg right:30%](images/01-minerals.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Reid Campbell (CC0 1.0)" -->
> Greetings! I'm an excellent hunter. See this fancy fireplace I got here? Let's make some babies!

— *Your average caveperson*

![bg right:30%](images/01-minerals.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Ron Cogswell (CC BY 2.0)" -->
### Neat things about the written word
Allows preservation of complex information.  
  
Enables conversions and relaying of detailed information/instructions over vast distances.  
  
_(Kinda necessary for ruling an empire)_

![bg right:30%](images/01-contrails.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Ron Cogswell (CC BY 2.0)" -->
Perhaps you want to keep some things a secret?

![bg right:30%](images/01-contrails.jpg)

<!--
Histiaeus (Greece, 500 BC):
https://www.tattoolife.com/wp-content/uploads/2021/11/Detail-of-an-illustration-by-Giorgio-De-Gaspari.jpeg
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Miguel Discart (CC BY-SA 2.0)" -->
Let's hide the information!  
  
We call this practice [**steganography**](https://en.wikipedia.org/wiki/Steganography).

![bg right:30%](images/01-tree_woman.jpg)


---
<!-- _footer: "%ATTRIBUTION_PREFIX% Miguel Discart (CC BY-SA 2.0)" -->
## Other notable examples
- [Lemon juice ink](https://www.wikihow.com/Make-an-Invisible-Ink-Message)
- [Image file EXIF data](https://securelist.com/vpnfilter-exif-to-c2-mechanism-analysed/85721/)
- [Printer tracking dots](https://en.wikipedia.org/wiki/Machine_Identification_Code)
- [Songs by Aphex Twin](http://www.bastwood.com/?page_id=10)

![bg right:30%](images/01-tree_woman.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Miguel Discart (CC BY-SA 2.0)" -->
## The downsides
Often requires **trust** in
courier(s) of the message.  
  
Mayhaps someone is a bit mad
since you ruined their haircut?  

![bg right:30%](images/01-tree_woman.jpg)

---
![bg center 80%](images/01-scytale.png)

<!--
- Used by ancient Greeks/Spartans
- Requires rod with the same diameter for "decryption"
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jeena Paradies (CC BY 2.0)" -->
Enter the [**"Caesar cipher"**](https://en.wikipedia.org/wiki/Caesar_cipher):

```
F  T F I I  Y X H B  X  Z X H B
```

![bg right:30%](images/01-frosty_lion.jpg)

---
![bg center 75%](images/06-caesar_cipher.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jeena Paradies (CC BY 2.0)" -->
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

![bg right:30%](images/01-frosty_lion.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jeena Paradies (CC BY 2.0)" -->
Probably confusing at first,
but quite easily broken.  
  
Largely **security through obscurity**.

![bg right:30%](images/01-frosty_lion.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Let's not just shift characters,
but substitute them in a random order!  

```
Plain-alphabet:   a b c d e f
Cipher-alphabet:  9 4 7 1 2 5
```

```
Plaintext:   d e a d  b e e f
Ciphertext:  1 2 9 1  4 2 2 5
```

```
Plaintext:     f e e d  d a d 
Ciphertext:    5 2 2 1  1 9 1
```

![bg right:40%](images/01-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## The downsides
Every participant needs to
know the **cipher-alphabet**.  
  
Languages are not random,
there are patterns and rules.  
  
People who try to break
codes/ciphers are called
**cryptanalysts**.

![bg right:30%](images/01-book.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
```
> F  T F I I  Y X H B  X  Z X H B
< J X H B  F Q  P L L K  M I B X P B
```

**F** and **X** appear on their own,
probably **a** and **i**.  

**FQ** is a two-letter word, limited options.
  
Four words begin with a different letter
but end with **XHB**.  

**B** appears five times in the messages,
probably **e**, **o** or **t**.

Method is known as **frequency analysis**.

![bg right:30%](images/01-book.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pyntofmyld (CC BY 2.0)" -->
## Introducing keywords
Everyone can remember the
secret word "**bad**", right?  

Let's try using the **Vigenère cipher**
(anno 1553) to encrypt "**cafebabe**".

![bg right:30%](images/01-bubbles.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f  e  b  a  b  e
Keyword:     B  A  D  B  A  D  B  A
Ciphertext:  ?  ?  ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:  >c< a  f  e  b  a  b  e
Keyword:    >B< A  D  B  A  D  B  A
Ciphertext: >D< ?  ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c >a< f  e  b  a  b  e
Keyword:     B >A< D  B  A  D  B  A
Ciphertext:  D >A< ?  ?  ?  ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a >f< e  b  a  b  e
Keyword:     B  A >D< B  A  D  B  A
Ciphertext:  D  A >C< ?  ?  ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f >e< b  a  b  e
Keyword:     B  A  D >B< A  D  B  A
Ciphertext:  D  A  C >F< ?  ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f  e >b< a  b  e
Keyword:     B  A  D  B >A< D  B  A
Ciphertext:  D  A  C  F >B< ?  ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f  e  b >a< b  e
Keyword:     B  A  D  B  A >D< B  A
Ciphertext:  D  A  C  F  B >D< ?  ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f  e  b  a >b< e
Keyword:     B  A  D  B  A  D >B< A
Ciphertext:  D  A  C  F  B  D >C< ?
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Brendan J (CC BY 2.0)" -->
```
Plaintext:   c  a  f  e  b  a  b >e<
Keyword:     B  A  D  B  A  D  B >A<
Ciphertext:  D  A  C  F  B  D  C >E<
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

![bg right:30%](images/01-arrow_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nicholas Day (CC BY 2.0)" -->
# DACFBDCE!

### How about decryption?

![bg right:30%](images/01-color_glitch.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
```
Plaintext:   ?  ?  ?  ?  ?  ?  ?  ?
Keyword:     B  A  D  B  A  D  B  A
Ciphertext:  D  A  C  F  B  D  C  E
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

![bg right:30%](images/01-lock_pin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
```
Plaintext:  >c< ?  ?  ?  ?  ?  ?  ?
Keyword:    >B< A  D  B  A  D  B  A
Ciphertext: >D< A  C  F  B  D  C  E
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

![bg right:30%](images/01-lock_pin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
```
Plaintext:   c >a< ?  ?  ?  ?  ?  ?
Keyword:     B >A< D  B  A  D  B  A
Ciphertext:  D >A< C  F  B  D  C  E
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

![bg right:30%](images/01-lock_pin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
```
Plaintext:   c  a >f< ?  ?  ?  ?  ?
Keyword:     B  A >D< B  A  D  B  A
Ciphertext:  D  A >C< F  B  D  C  E
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

![bg right:30%](images/01-lock_pin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Dennis van Zuijlekom (CC BY-SA 2.0)" -->
```
Plaintext:   c  a  f >e< ?  ?  ?  ?
Keyword:     B  A  D >B< A  D  B  A
Ciphertext:  D  A  C >F< B  D  C  E
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

![bg right:30%](images/01-lock_pin.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rob Hurson (CC BY-SA 2.0)" -->
## Kerckhoffs' principle
> The security of a cipher
> must be based on the chosen key,
> not keeping the algorithm secret 
> (AKA "security through obscurity")

![bg right:30%](images/01-bunker_tower.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Tero Karppinen (CC BY 2.0)" -->
The cat and mouse game went on,
more or less the same way...

![bg right:30%](images/01-pixel_forest.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Technologies such as the telegraph
and radio really shook things up.  
  
Even commercial enterprises found
the need for encryption.

![bg right:30%](images/01-phone.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
Even if the cipher can't be broken, a lot can still be learned.  
  
From where was the message sent? By whom?  
  
We call this **metadata**.
  
![bg right:30%](images/01-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Raphaël Vinot (CC BY 2.0)" -->
Cryptography became too
complex for _most_ humans.  
  
If machines maketh,
let machine breaketh.

![bg right:30%](images/01-observatory_instruments.jpg)

<!--
https://en.wikipedia.org/wiki/Enigma_machine
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pyntofmyld (CC BY 2.0)" -->
While it had evolved significantly,
encryption algorithms worked more
or less the same until the 1970s.  
  
Let me introduce you to
**asymmetric cryptography**.

![bg right:30%](images/01-pdp11_70.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Miguel Discart (CC BY-SA 2.0)" -->
## Symmetric
Same key is used for encryption and decryption.

## Asymmetric
Different keys are used for encryption and decryption
("public key" and "private key").

![bg right:30%](images/01-led_triangles.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Miguel Discart (CC BY-SA 2.0)" -->
**Everyone can encrypt messages to me, but only I can decrypt them.**

![bg right:30%](images/01-led_triangles.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% A Loves DC (CC BY 2.0)" -->
Also enables **"digital signatures"**.

That's right - cryptography can help us
protect the authenticity of messages from
an author, not only their confidentiality.

![bg right:30%](images/01-steel_w.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Edenpictures (CC BY 2.0)" -->
Did I mention **"cryptographic hash functions"**?  
  
Wide range of use-cases, including:
- Integrity validation
- "One-way encryption"
- Proof-of-Work

\+ a lot of other exciting things we
shall learn about throughout the course!

![bg right:30%](images/01-abstract_house.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Elly Jonez (CC BY 2.0)" -->
So, my dear modern human -
have you relied on cryptography today?

![bg right:30%](images/01-city_night.jpg)

<!--
- Sent a private message to anyone?
- Logged in to a sensitive service over the big bad Internet?
- Signed something with BankID?
- Took the bus or subway?
....
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Gobi (CC BY 2.0)" -->
Cryptography helps us ensure
confidentiality and integrity
of information.  

Should be **infeasible** to break,
but it's never **impossible**.  

Modern cryptography operates
on bits, not letters.

![bg right:30%](images/01-cyborg.jpg)
