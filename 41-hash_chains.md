---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Hash chains"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Introduction to hash chains in practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
# Hash chains
### An introduction to its uses

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Cryptographic hashes can be used to detect changes ("tampering") in a file.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
It doesn't tell us what has changed.  
  
Every time a single bit changes, the hash does too.  
  
Quite a lot of overhead for frequently changing data, such as log files and transaction history.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Wouldn't it be nice if there was an efficient way
to protect and validate (historical) integrity of
append-only data structures?  
  
**Hash chains to the rescue!**

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
### Data we want to protect
```
$ ls

1.log  2.log  3.log  4.log
5.log  6.log  7.log  8.log

$ cat *.log

INFO: μBank process started
INFO: Alice deposit 1000€
INFO: Alice transfer 500€ to Bob
INFO: Alice's account balance is 500€
INFO: Alice transfer 500€ to Bob
INFO: Alice's account balance is 0€
INFO: Alice transfer 500€ to Chuck
ERROR: Alice has insufficient funds
```

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
### Generating per-entry hashes
```
$ for LOG_ENTRY in *.log; do
	sha256sum "${LOG_ENTRY}" \
	| tee "${LOG_ENTRY}.hash"
done

c2233cba55[...]9999545d1bf  1.log
1b0f193a78[...]bdd909b589a  2.log
916a28d3dd[...]93cb088d493  3.log
83832ff85d[...]7330137e46f  4.log
916a28d3dd[...]93cb088d493  5.log
a88bd4892d[...]feea520f3ff  6.log
8bc5b584bc[...]1f82909ef64  7.log
a2334cf537[...]ec9ecae2494  8.log 
```

![bg right:30%](images/41-locks.jpg)

---
### Generating hash chain
```
$ HASH_CHAIN=""
$ for LOG_ENTRY_HASH in *.log.hash;
	do HASH_CHAIN="$(echo "${HASH_CHAIN}"+$(cat "${LOG_ENTRY_HASH}") | sha256sum)"
done

$ echo ${HASH_CHAIN}
7dfa6b8f34b77f15fc18924d70c428ec7f0107907baced2e22a756e0a9aef0f6 -
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Validation of a single entry only requires its data and the chain hashes.

Can we make it more efficient?

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
## Other use-cases
Efficient error detection and data replication.  
  
Cornerstone of the [BitTorrent protocol](https://en.wikipedia.org/wiki/BitTorrent).

![bg right:30%](images/41-locks.jpg)
