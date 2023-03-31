---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Randomness"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to randomness and its importance"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
# Randomness
### Uses in cryptography and security

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
We rely on randomness to keep games
fun and fair (and "legal").

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Security often relies on it as well.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
**Predictability** VS **Randomness**

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Turns out that humans are very predictable.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Computers are designed to be very predictable.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Yet we can run **Math.random()**.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
...which is good because we use it to generate all sorts of keys.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Random Number Generators or
**RNGs**, for short.  

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
### PRNG
Pseudo-random _AKA_
"Not really but let's pretend".  
  
Can be implemented in pure software.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
### CSPRNG
Cryptographically secure pseudo-randomness.  
  
Relies on multiple inputs, such as mouse movement, CPU temperature and WiFi signal.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
### HWRNG
Basically the same, but let some external device provide randomness.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
### TRNG
Generates measuring/observing something very near truly random, like radioactive decay.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Many PRNGs need an initial **seed** to get started.  
  
We can use this to create "predictable randomness" :S

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Many PRNGs need an initial **seed** to get started.  
  
We can use this to create "predictable randomness" :S

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
You want some decent randomness on Linux?  

Use **/dev/random**
or **/dev/urandom**.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
Sometimes you need a bit of extra help.  
  
Checkout "RNG forwarding", Pollinate and Haveged.

![bg right:30%](images/34-dice.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
### You got an RNG in your pocket!
```
$ gpg-connect-agent --hex "SCD RANDOM 1000" /bye

D[0000]  63 F8 73 4A 25 32 35 B0  21 3F 57 [...]
```

![bg right:30%](images/34-dice.jpg)
