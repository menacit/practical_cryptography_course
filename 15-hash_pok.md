---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
**Why do we sometimes see people tweet or toot out a hash?**

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
```
$ echo "${SALT} Looptroop killed Palme" | sha1sum

f2f095c3b414335fdf98ed96f128e37705dca7ce
```

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
**Why not just use symmetric encryption and publish the key?**

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
Most cryptographically secure hashes are fixed-length.  
  
Knowledge of terabytes can be proven with a short string that fits inside a toot/tweet/SMS.

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
## Uses for authentication
Remote authentication without sending password over network.  
  
One-time/rolling passwords.

![bg right:30%](images/15-airship.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
### Pseudo-code for hash authentication
```
$challenge = get_auth_challenge($username)
$response = sha256($challenge + $password)

login($challenge, $response)
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
### Pseudo-code for rolling password
```
$time = get_current_minute()
$one_time_code = sha256($time + $password)

login($username, $one_time_code)
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
**Many other use-cases exist - this is just an appetizer.**

![bg right:30%](images/15-airship.jpg)
