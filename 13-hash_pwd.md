---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Hashing for password storage"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Usage of cryptographic hashing for password storage"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Lord Jaraxxus (CC BY-SA 4.0)" -->
## Hashing for password storage

![bg right:30%](images/13-neon_sign.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Lord Jaraxxus (CC BY-SA 4.0)" -->
What happens when we login to a website?  
  
1. Client submit their username and password
2. Server checks if the submitted password matches the one stored for the user

![bg right:30%](images/13-neon_sign.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nicholas A. Tonelli (CC BY 2.0)" -->
Okay, so the server must store all passwords.  
  
Can't we just symmetrically encrypt them?

![bg right:30%](images/13-abandoned_apartment.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nicholas A. Tonelli (CC BY 2.0)" -->
Server needs plaintext passwords
to enable comparison.  
  
Encrypted data must be "unlocked",
which means that the key is typically
stored on disk or in memory.  
  
Sounds scary.

![bg right:30%](images/13-abandoned_apartment.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rod Waddington (CC BY-SA 2.0)" -->
## Storing passwords using hashing
The same hash function input data should always result in the same output, right?  
  
Wasn't a nick-name for hashing
"**one-way encryption**"?

![bg right:30%](images/13-singapore_gardens.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rod Waddington (CC BY-SA 2.0)" -->
### Pseudo-code for password hashing
```
if (
sha256($submitted_password) ==
$stored_password_hash) {

	accept_login()

} else {
	deny_login()
}
```

![bg right:30%](images/13-singapore_gardens.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jennifer Morrow (CC BY 2.0)" -->
Boom! Let's call it day, shall we?  
  
Not quite.

![bg right:30%](images/13-spheres.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jennifer Morrow (CC BY 2.0)" -->
### Problems with basic password hashing
Users using the same password will have the generated same hash.  
  
Hashes can be pre-calculated ("rainbow tables").

![bg right:30%](images/13-spheres.jpg)

---
![bg center 65%](images/13-hash_search.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jennifer Morrow (CC BY 2.0)" -->
### Problems with basic password hashing
Users using the same password will have the same hash.  
  
Hashes can be pre-calculated ("rainbow tables").

![bg right:30%](images/13-spheres.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Let me introduce you to **salting**!  
  
Random data mixed into the password hashing.

![bg right:30%](images/13-exposed_road.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
### Pseudo-code for password hashing
```
if (
sha256($stored_salt + $submitted_password) ==
$stored_password_hash) {

	accept_login()

} else {
	deny_login()
}
```

![bg right:30%](images/13-exposed_road.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
## Salt should be...
- Quite random
- Unique per user
- Accessible to application in plaintext

![bg right:30%](images/13-exposed_road.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fandrey (CC BY 2.0)" -->
## Operating systems use it too
```
$ sudo head --lines 1 /etc/shadow

root:$y$j9T$P.lVRC/J.KNiBHMob7uli[...]
```

[_$ man shadow_](https://man.archlinux.org/man/shadow.5.en)

![bg right:30%](images/13-console_beastie.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
### Choosing the right hash function
Guessing the password that matches a hash ("hash cracking") should require lots of compute.  
  
The same hash function can be used multiple times ("rounds") to increase cost.  
  
Consider using a purpose built solution like [bcrypt](https://en.wikipedia.org/wiki/Bcrypt).

![bg right:30%](images/13-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Andrew Hart (CC BY-SA 2.0)" -->
Doesn't fully mitigate the risks of password theft.  
  
An attacker with system access may be able to modify the application to log password input.

![bg right:30%](images/13-broken_glass.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bruno Cordioli (CC BY 2.0)" -->
## Client-side hashing
Effectively turns generated hash into a password.
  
Allows server to never gain access to plaintext password, minimizing consequences of breach.  
  
Beware that the client-side code can be modified by a compromised server in web apps.

![bg right:30%](images/13-newton.jpg)
