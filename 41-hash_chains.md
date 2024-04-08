---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
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
You got a fancy suite and
work with IT security at a bank.  

Protecting the customers'
transaction history against
manipulation would be greeeeat.  

Can cryptography help us?

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Cryptographic hashes can be used to
detect changes ("tampering")
in data/a file.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
It doesn't tell us what has changed.  
  
Every time a single bit changes,
the hash changes completely
(as it should).  
  
Quite a lot of overhead for
frequently changing data,
such as log files.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Can't we just split the data into
multiple parts (for example, lines)
and hash each independently?

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Sure, but what about ordering?

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Let's just throw the
transaction data hashes
in a file, append new hashes
and store the file's own digest!

Anyone who wants to validate the
history could just compute hashes
and check for themselves, right?! 

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
How do you cryptographically prove
that you only appended a transaction
and didn't manipulate any historic ones?

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Wouldn't it be nice if there was
an efficient way to protect and
validate (historical) integrity
of append-only data structures?  
  
**Hash chains to the rescue!**

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
We're talking about links in a chain,
not hyperlinks.  
  
Each link in the chain consists of 
_hash(\$PREVIOUS\_LINK\_HASH \+ \$DATA)_.  

Confusing? Let's look at an example.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
### Transaction data we want to protect
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
7dfa6b8a\[...\]9aef0f6 is the last
link of the hash chain.  

Manipulation of historic data
can be detected, as it will change
the hash for all following links
and thereby also the last.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Validation of a single entry
only requires its data and
the chain hashes.  

The last link hash can be
publicly documented, as it doesn't
reveal the actual data (transaction).

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Any limitations?  

Can only prevent manipulation of
previous links in the chain,
a fraudulent transaction
could be appended.  
  
Requires the latest link digest
for proper validation.

![bg right:30%](images/41-locks.jpg)

<!-- https://dl.acm.org/cms/attachment/53f3a0fa-d90c-49e5-82bd-09e2ca003487/f3.jpg -->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Can we make it more efficient?  
  
Yes, using a [**Merkle tree**](https://en.wikipedia.org/wiki/Merkle_tree).

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% © David Göthberg (CC0 1.0)" -->

![bg center 70%](images/41-merkle_tree.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Sounds neat,
but is anyone using it?  
  
Guardtime digests in newspapers
are one example.  
  
The chain part of blockchain.

![bg right:30%](images/41-locks.jpg)

<!-- https://dl.acm.org/cms/attachment/53f3a0fa-d90c-49e5-82bd-09e2ca003487/f3.jpg -->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
## Other use-cases
Efficient error detection and data replication.  
  
Cornerstone of [Git repositories](https://git-scm.com/).  

Used by TPMs to provide
["measured/trusted boot"](https://opensource.com/article/20/10/measured-trusted-boot).

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
If you see the term
"trusted timestamping service/authority",
some type of hash chaining is likely used.

![bg right:30%](images/41-locks.jpg)
