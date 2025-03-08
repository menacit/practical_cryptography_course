---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
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
**Why do we sometimes see
people tweet or toot out a hash?**

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
**Why not just use symmetric encryption
and publish the key when time arrives?**

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
$response = sha256($challenge + $password)

login($challenge, $response)
```

![bg right:30%](images/15-capsule_house.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Rolling password (counter-based)
```
$counter = $counter + 1
$one_time_code = sha256($counter + $password)

login($username, $one_time_code)
```

![bg right:30%](images/15-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
## Rolling password (time-based)
```
$time = get_current_minute()
$one_time_code = sha256($time + $password)

login($username, $one_time_code)
```

(somewhat similar to the
"**T**ime-based **O**ne-**t**ime **P**assword" standard,
used by applications like Google Authenticator)

![bg right:30%](images/15-atomic_clock.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Lars Juhl Jensen (CC BY 2.0)" -->
**Many other use-cases exist -
this is just an appetizer.**  
  
If you wanna play around
and got the time, check out
["resources/labs/extras/otp\_auth/README.md"](%RESOURCES_ARCHIVE%).  

![bg right:30%](images/15-panda.jpg)
