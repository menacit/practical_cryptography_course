---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Asymmetric introduction"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to asymmetric cryptography and its uses"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% RoboticSpider (CC BY 4.0)" -->
# Asymmetric cryptography
### A somewhat gentle introduction

![bg right:30%](images/19-robot.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% RoboticSpider (CC BY 4.0)" -->
This is not a math course.  

We won't cover how the
algorithms actually works.  

Neither do we need to, thankfully!

![bg right:30%](images/19-robot.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Greg Lloy (CC BY 2.0)" -->
Also known as "**public-key cryptography**".  
  
Spooks and researches have been
using it since the late 70s.  
  
Requires usage of electronic computers
(sorry, humans!).

![bg right:30%](images/19-computer.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Greg Lloy (CC BY 2.0)" -->
Doesn't require a **pre-shared key**.  
  
Holder of the **private key** can decrypt and sign/authenticate data.  
  
The corresponding **public key** can be used to encrypt and verify authenticity of signed data.  

![bg right:30%](images/19-computer.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Greg Lloy (CC BY 2.0)" -->
[**RSA**](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is a
commonly used cryptosystem.  

Rivest, Shamir and Adleman.  
  
~~Not to be~~ confused with
the company "RSA Security".

Patented in 1983,
freely usable since 2000.
  
Typically 512, 1024... 4096 bits large keys.

![bg right:30%](images/19-computer.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Greg Lloy (CC BY 2.0)" -->
**D**igital **S**ignature **A**lgorithm.  

Standardized by NIST in 1994,
usable without license trouble.  

Focused on signatures/authentication,
not encryption.  

Several design flaws and
insufficient key size - avoid it!

![bg right:30%](images/19-computer.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
[Elliptic-curve cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) (**ECC**)
is replacing RSA.  
  
It's faster, requires smaller keys and
is generally considered easier
to safely implement.  
  
RSA still has better
software/hardware support.

![bg right:30%](images/19-arch.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
```
$ time ssh-keygen -q -N '' -t rsa -f /tmp/key_rsa
real	0m1.022s

$ time ssh-keygen -q -N '' -t ed25519 -f /tmp/key_ed
real	0m0.008s
```

![bg right:30%](images/19-arch.jpg)

---
```
$ cat /tmp/key_rsa.pub | cut -d ' ' -f 2 
AAAAB3NzaC1yc2EAAAADAQABAAABgQC0KDu1jlpyMbqGNAU5NEPmN8LXNeybJHRHiLHg
aMRVTsmOsQzBlQhC8GAxHCvrQDpfqDVRtp0eepJtYTHuu7RZPOvHEMH7U35/xP/jRUMM
Z81k1DAQ6LoezQKj7bKJuvJo3P/JTdrWwMVejwNAXL4IIDce3G/TQx6HQlF3YmW8hCFZ
j30frRqVPF/KT9Zgh4IyeEdWnlAP0bLA9x/lvsZuTDIGy3D89aPW41z0jQbcVVFips1v
QGWrSQZYGgBeX8TUqTcg0Zuu9K19MZx6Jdnu+Qdxukk+omkDmSODvRQ6U/LGY3Cx8NEY
fZZfeXo+TVmKHUQwNntuvpW074UqVedOfrrN8lsJmnjjPivXG2MHVF6fDAYe0WubPUEv
ZZIzyTZFEOpt9tPeOg6s38mhF/cgr17p8lapMHx4HFn0ljlgejgKNzm5rI4AqNWjgj1+
HvcX3BkhU91xDiTV5sAIqAPddk3ePsiFZiBpvzrlQagiY+VNf/VJq8x4vN98aTtGMqc=

$ cat /tmp/key_ed.pub | cut -d ' ' -f 2 
AAAAC3NzaC1lZDI1NTE5AAAAIFmgY7uVLZqx/tOLPJ22JBi7TAJwmmClu66+mb2sOfUA
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
Several different "**curves**" can be utilized.  
(\~think different ciphers).  
  
Common examples are
**NIST P-256/P-384** and
**Curve25519**.  
  
For guidance, checkout the ["SafeCurves" project](https://safecurves.cr.yp.to/).

![bg right:30%](images/19-arch.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% RoboticSpider (CC BY 4.0)" -->
Asymmetric cryptography
is relatively slow.  
  
Most often combined with
hashing (digital signatures) and
symmetric cryptography (key exchange).  

Curious about how these type of
algorithms actually work?
Check out ["KidRSA"](https://macs4200.org/chapters/11/1/kidrsa.html).

![bg right:30%](images/19-robot.jpg)
