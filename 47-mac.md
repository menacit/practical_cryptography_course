---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Message authentication codes"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Presentation about message authentication codes in practical cryptography course"
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

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
## "Message authentication codes"

![bg right:30%](images/47-holmen_crane.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
We've talked about how tools like
cryptographic hashing can be used
to protect the integrity of data.  

Would be neat to make sure that
network traffic hasn't been
maliciously manipulated.  

But how is it done in practice?
We can't simply send the expected
digest in plain-text over the wire.

![bg right:30%](images/47-holmen_crane.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Perhaps we could
`asymmetric_sign(hash($data))`
and send the resulting signature
along with our transferred data?  

Sure, but asymmetric cryptography
is typically quite slow.

![bg right:30%](images/47-cherry_trees.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
Another option would be
`symmetric_encrypt(hash($data))`.  
  
Hmm, yes - but there is another
option just based on hashing...

![bg right:30%](images/47-cherry_trees.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
What if we would simply
`hash($data + $secret)`?  

The receiver of traffic could
do something checking like:

```
if (
  $received_integrity_digest !=
  hash($received_data + $secret)):

  return 'Verification failed! :('
```

![bg right:30%](images/47-cherry_trees.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
All of these solutions aim to provide a
"**M**essage **A**uthentication **C**ode".  

The last example was a primitive
**H**ash-based **M**essage **A**uthentication **C**ode.  

Relatively cheap/low overhead, but can
be [tricky to get right](https://en.wikipedia.org/wiki/Length_extension_attack) depending
on the hash function used.  

Stick with purpose built solutions,
like [Python's "hmac" module](https://docs.python.org/3/library/hmac.html).

![bg right:30%](images/47-holmen_crane.jpg)
