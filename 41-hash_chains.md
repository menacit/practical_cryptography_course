---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
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
    color: #ffca4d;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
# Hash chains
### An introduction to its uses

![bg right:30%](images/41-one_world_trade.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
You got a fancy suit and
work with IT security at a bank.  

Protecting the customers'
transaction history against
manipulation would be greeeeat.  

Useful for detecting theft/fraud
and in customer disputes.  
  
Can cryptography help us?

![bg right:30%](images/41-one_world_trade.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
## Our example log
```
INFO: μBank process started
INFO: Alice deposit 1000€
INFO: Alice transfer 500€ to Bob
INFO: Alice's account balance is 500€
```

![bg right:30%](images/41-one_world_trade.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
Cryptographic hashes can be used to
detect changes ("tampering") in data.  
  
Problem solved, right?

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
Every time a single bit changes,
the hash digest changes completely
(as it should to be considered secure).  

It doesn't tell us what has changed.  

We expect new transactions to be added
to the log all the time - what we really
want to protect is historic transaction data.

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
Can't we just split the data into
multiple parts (per log entry, for example),
hash each independently and store the digests?

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
Sure, but what about ordering?  

Kinda important to validate
account balance and similar.

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
Let's just throw the
transaction data hashes
in a file, append new hashes
and store the file's own digest!

Anyone who wants to validate the
history could just compute hashes
and check for themselves, right?! 

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
How do you cryptographically prove
that you only appended a transaction
and didn't manipulate any historic ones?

![bg right:30%](images/41-clouds_side.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Wouldn't it be nice if there was
an efficient way to protect and
validate (historical) integrity
of append-only data structures,
like our transaction log file?  
  
**Hash chains to the rescue!**

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
We're talking about links in a chain,
not hyperlinks.  
  
Each link in our chain consists of 
`hash($PREVIOUS_LINK_HASH + $DATA)`.  
  
Due to this dependency, we can tell
what historic data has been manipulated
(if any, that is).
  
Confusing? Let's look at an example.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
### Split log per line
```
$ ls

1.log  2.log  3.log  4.log

$ cat *.log

INFO: μBank process started
INFO: Alice deposit 1000€
INFO: Alice transfer 500€ to Bob
INFO: Alice's account balance is 500€
```

![bg right:30%](images/41-locks.jpg)

---
### Generating initial hash chain
```sh
#!/usr/bin/env bash
LAST_LINK_HASH="<nothing>"

for LOG_ENTRY_FILE in *.log; do
  LOG_ENTRY_DATA="$(cat "${LOG_ENTRY_FILE}")"
  
  LAST_LINK_DATA="${LAST_LINK_HASH} + ${LOG_ENTRY_DATA}"
  
  LAST_LINK_HASH="$(echo "${LAST_LINK_DATA}" | sha256sum | cut -d ' ' -f 1)"
  echo "Digest of last link \"${LAST_LINK_DATA}\" is \"${LAST_LINK_HASH}\""
  
done
```

---
```
Digest of last link "<nothing> + INFO: μBank process started" is "f7d6[...]c280"
Digest of last link "f7d6[...]c280 + INFO: Alice deposit 1000€" is "2c11[..]7e26"
Digest of last link "2c11[...]7e26 + INFO: Alice transfer 500€ to Bob" is "ac5b[...]fd0e"
Digest of last link "ac5b[...]fd0e + INFO: Alice's account balance is 500€" is "c075[...]8b5d"
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
`c075[...]8b5d` is the last
link of the hash chain.  

Manipulation of historic data
can be detected, as it will change
the hash for all following links
and thereby also the last.  
  
Confused? Let's look at some examples.

![bg right:30%](images/41-locks.jpg)

---
## Our baseline transaction log
| Previous link digest | Log entry                             |
|----------------------|---------------------------------------|
| \<nothing\>          | INFO: μBank process started           |
| f7d6[...]c280        | INFO: Alice deposit 1000€             |
| 2c11[...]7e26        | INFO: Alice transfer 500€ to Bob      |
| ac5b[...]fd0e        | INFO: Alice's account balance is 500€ |
| c075[...]8b5d        |                                       |

(`c075[...]8b5d` is the expected digest of the last link)

---
## Changing last log entry
| Previous link digest | Log entry                               |
|----------------------|-----------------------------------------|
| \<nothing\>          | INFO: μBank process started             |
| f7d6[...]c280        | INFO: Alice deposit 1000€               |
| 2c11[...]7e26        | INFO: Alice transfer 500€ to Bob        |
| ac5b[...]fd0e        | _INFO: Alice's account balance is 500£_ |
| **a1f5[...]6c82**    |                                         |

(`c075[...]8b5d` is the expected digest of the last link)

---
## Changing an earlier log entry
| Previous link digest | Log entry                             |
|----------------------|---------------------------------------|
| \<nothing\>          | INFO: μBank process started           |
| f7d6[...]c280        | INFO: Alice deposit 1000€             |
| 2c11[...]7e26        | _INFO: Alice transfer 5000€ to Bob_   |
| **8705[...]d4b3**    | INFO: Alice's account balance is 500€ |
| **9dc6[...]4b21**    |                                       |

(`c075[...]8b5d` is the expected digest of the last link)

---
## Removing a log entry
| Previous link digest | Log entry                             |
|----------------------|---------------------------------------|
| \<nothing\>          | INFO: μBank process started           |
| f7d6[...]c280        | INFO: Alice deposit 1000€             |
| ~~2c11[...]7e26~~    | ~~INFO: Alice transfer 500€ to Bob~~  |
| 2c11[...]7e26        | INFO: Alice's account balance is 500€ |
| **9135[...]cc83**    |                                       |

(`c075[...]8b5d` is the expected digest of the last link)


---
What if we wanna append a new log entry?

```
$ echo "c075[...]8b5d + INFO: Alice transfer 250€ to Dan" \
  | sha256sum | cut -d ' ' -f 1

6a22[...]4F71
```

...and another one:

```
$ echo "6a22[...]4F71 + ERROR: Alice tried to transfer 1000€ to Eve" \
  | sha256sum | cut -d ' ' -f 1

34bf[...]aca1
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Why is this neat?

If we save/publish each link hash and
"replay" the log, we can tell if log
events have been removed, shuffled,
modified or added.

If we only choose to save a link hash
every hour/day/week, we can make sure
that nothing before point that has
been modified at a future date.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Any limitations with our approach?  
  
Can only prevent manipulation of
previous links in the chain,
a fraudulent transaction
could still be appended.  
  
Requires at least the last link digest
and all previous log entries for
proper validation.  

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
How could this help in a customer dispute
regarding account balance manipulation
by an evil bank insider?

The link hashes could be publicly available,
posted each day for everyone to see. 

The logs could be kept secret, but
relevant log events (draining transactions)
could be disclosed during a court trial.

By disclosing the plaintext log entry,
the chain position of its hash digest
may be proven without disclosing everything.

![bg right:30%](images/41-locks.jpg)


---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
...just be aware that someone may try
to crack our chain links to disclose
the transaction log entries.

![bg right:30%](images/41-locks.jpg)

---
```bash
#!/usr/bin/env bash
PREVIOUS_LINK_HASH="ac5b[...]fd0e"
CURRENT_LINK_HASH="c075[..]8b5d"

ATTEMPTS=0

for NAME in Ada Alice Bob Boris Charlie Connie; do
  AMOUNT=0

  while [[ ${AMOUNT} -le 5000 ]]; do
    (( ATTEMPTS++ ))

    CANDIDATE="INFO: ${NAME}'s account balance is ${AMOUNT}€"
    CANDIDATE_DATA="${PREVIOUS_LINK_HASH} + ${CANDIDATE}"

    CANDIDATE_HASH="$(echo "${CANDIDATE_DATA}" | sha256sum | cut -d ' ' -f 1)"

    if [[ "${CANDIDATE_HASH}" == "${CURRENT_LINK_HASH}" ]]; then
      echo "Cracked log entry after ${ATTEMPTS} attempts: ${CANDIDATE}"
      exit 0
    fi

    (( AMOUNT++ ))
  done
done
```

---
```
$ ./crack_that_log_entry.sh

Cracked log entry after 5502 attempts: INFO: Alice's account balance is 500€
```

---
| Log entry                             | Per-entry salt |
|---------------------------------------|----------------|
| INFO: μBank process started           | 13e61749       |
| INFO: Alice deposit 1000€             | fd3dd804       |
| INFO: Alice transfer 500€ to Bob      | 58a762cb       |
| INFO: Alice's account balance is 500€ | c004de54       |

To append new chain links,
`hash($PREVIOUS_LINK_HASH + hash($ENTRY_SALT + $LOG_ENTRY))`.  

The last link digests can be publicly available,
as they don't reveal any sensitive information.  

Anyone with access to a log entry, its associated salt
and the previous link digests can validate the log.

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
Can we make it more efficient so we
don't need go through every single
link digest to validate that a
log entry exist in the chain?
  
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

...oh, and "certificate transparency"!

![bg right:30%](images/41-locks.jpg)

<!-- https://dl.acm.org/cms/attachment/53f3a0fa-d90c-49e5-82bd-09e2ca003487/f3.jpg -->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
## Other use-cases
Efficient error detection and data replication.  
  
Cornerstone of [Git repositories](https://git-scm.com/).  

Used to provide "measured and attested boot" -
checkout [Joel's talk from SEC-T](https://youtu.be/vdj9Pr-6dq8) for details.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Christian Siedler (CC BY-SA 2.0)" -->
If you see the term
"trusted timestamping service/authority",
some type of hash chaining is likely used.

![bg right:30%](images/41-locks.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
## Wrapping up

![bg right:30%](images/41-one_world_trade.jpg)
