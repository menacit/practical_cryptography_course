---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
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
We rely on randomness to keep competitions
fun and fair (and legal, in some cases).

**Predictable** VS **Random**.  

Human actions/choices are quite predictable,
tools like dice and tombolas can help us. 

![bg right:30%](images/34-dice.jpg)

<!--
https://i.redd.it/w4gz0wzz1i821.png
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
The security of computer systems
often rely on it as well.  

Generation of salt/IV,
site-unique passwords,
asymmetric private keys,
ephemeral symmetric keys...

Digital computers are however
designed to be very predictable.

![bg right:30%](images/34-golden_cogwheels.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
Yet we can run **Math.random()**. But how?  

![bg right:30%](images/34-golden_cogwheels.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
To help us fight predictability,
we rely on **R**andom **N**umber **G**enerators.  

Despite their name, they often produce
(more or less) random bits.  

RNGs are typically divided into a few
different categories, depending on their
implementation and security promises...

![bg right:30%](images/34-random_numbers.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jusotil_1943 (CC0 1.0)" -->
### PRNG
Pseudo-random _AKA_
"Not really but let's pretend".  
  
Can be implemented in pure software.  

Fast and useful to make things fun,
unsuitable for security applications.

![bg right:30%](images/34-rusted_cards.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
### CSPRNG
Cryptographically secure pseudo-randomness.  
  
Relies on multiple semi-unpredictable inputs,
such as mouse movement, CPU temperature,
disk latency and WiFi signal strength.  

\~AKA "sources of **entropy**".

Guessing the state of one input may
be trivial, but not all at the same time.

![bg right:30%](images/34-abstracts_cubes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yellowcloud (CC BY 2.0)" -->
### HWRNG
Hardware Random Number Generator.

Let some external device provide
us with those random bits.  

Provided by modern chipsets/CPUs,
typically quite fast!

### TRNG
Measuring something we think is
"**t**ruly random", like radioactive decay.

Purpose-built peripherals,
some available as "open hardware".

![bg right:30%](images/34-chip_with_probes.jpg)

<!--
https://leetronics.de/en/shop/infinite-noise-trng/
https://opentrng.org/
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yubinerd (CC BY-SA 4.0)" -->
### You got a HWRNG in your pocket!
```
$ gpg-connect-agent --hex "SCD RANDOM 1000" /bye

D[0000]  63 F8 73 4A 25 32 35 B0  21 3F 57 [...]
```

![bg right:30%](images/34-yubikey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
In practice, we typically utilize a
HWRNG as an entropy input to a CSPRNG.  

The more sources of unpredictable
input, the better output randomness!

![bg right:30%](images/34-one_world_trade.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
Many PRNGs need an **initial seed**
to get started producing output.  
  
(what we use our multiple inputs for)   

We can abuse this to generate
"deterministic randomness"! _:S_

Useful for key derivation and creating
easily sharable worlds in Minecraft!

![bg right:30%](images/34-goose.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Ninara (CC BY 2.0)" -->
You want some decent randomness on Linux?  

Use **/dev/random** or **/dev/urandom**.

```
$ head \
    --bytes 1000 /dev/random \
    > /tmp/unpredictable_bytes
```

/dev/random may (temporarily) run out
of random data - unless you're very
paranoid, utilize /dev/urandom instead.

![bg right:30%](images/34-ahmedabad.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Sometimes your CSPRNG need a bit of
extra help gathering its initial seed.  

Freshly spawned virtual machines in
the public cloud are a common example.

Checkout "RNG forwarding",
[Pollinate](https://github.com/dustinkirkland/pollinate) and
[Haveged](https://www.issihosts.com/haveged/).

![bg right:30%](images/34-chemical_plant.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Julie Cotinaud (CC BY-SA 2.0)" -->
## Wrapping up
Unpredictable randomness is a key
component in computer security.  

Don't rely on a home-grown RNG,
unless you're doing it for fun!  

Standard libraries in programming
languages typically provide both
a PRNG and a CSPRNG - make sure
you know which one you're using!

![bg right:30%](images/34-dice.jpg)
