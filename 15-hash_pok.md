---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Proof of Knowledge"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Usage of cryptographic hashing for PoK"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
# Proof of Knowledge
### An introduction of hashing for PoK

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
Why do we sometimes see mysterious
people tweet or toot out a hash?

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jesse James (CC BY 2.0)" -->
```
$ echo "${SALT} Looptroop killed Palme" | shasum

f2f095c3b414335fdf98ed96f128e37705dca7ce
```

![bg right:30%](images/15-party.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Why not just use symmetric encryption
and publish the key when time arrives?

![bg right:30%](images/15-pyramids.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Most cryptographically secure hashes
are fixed-length.  
  
Knowledge of terabytes can be proven with
a short string that fits inside a toot/tweet/SMS.

![bg right:30%](images/15-boat_sundown.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Uses for authentication
Remote authentication without
sending password over network.  
  
One-time/rolling passwords.

![bg right:30%](images/15-sphere.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bruno Cordioli (CC BY 2.0)" -->
### Pseudo-code for hash authentication
```
$challenge = get_auth_challenge($username)
$response = hash($challenge + $password)

login($challenge, $response)
```

![bg right:30%](images/15-capsule_house.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Rolling password (counter-based)
```
$counter = $counter + 1
$one_time_code = hash($counter + $password)

login($username, $one_time_code)
```

![bg right:30%](images/15-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
## Rolling password (time-based)
```
$time = get_current_date_and_time()
$one_time_code = hash($time + $password)

login($username, $one_time_code)
```

(somewhat similar to the
"**T**ime-based **O**ne-**t**ime **P**assword" standard,
used by applications like Google Authenticator)

![bg right:30%](images/15-atomic_clock.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
That's quite neat - but it comes with a
security trade-off. Did you notice it?

![bg right:30%](images/15-printing_shop_colors.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
We can't utilize hashes to safely
store passwords server-side, since the
server must have access to the plaintext.

Is it worth it? That depends!

These days we have better ways
to protect data in-transit -
more about that later!

![bg right:30%](images/15-printing_shop_colors.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Lars Juhl Jensen (CC BY 2.0)" -->
## Wrapping up
Many other use-cases exist -
this is just an appetizer.  
  
If you wanna play around
and got the time, check out
["resources/labs/extras/otp\_auth/README.md"](%RESOURCES_ARCHIVE%).  

![bg right:30%](images/15-panda.jpg)
