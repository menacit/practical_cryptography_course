---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Cryptography in Bitcoin"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Use-cases of cryptography in Bitcoin"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Bill Badzo (CC BY-SA 2.0)" -->
# Bitcoin
### Use-case study of cryptography

![bg right:30%](images/45-keenan_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bill Badzo (CC BY-SA 2.0)" -->
## What is Bitcoin?
Digital currency and
decentralized payment network.  
  
First widely used example of cryptocurrency.  

Released as FOSS in 2009 by the
mysterious pseudonym "Satoshi Nakamoto".

Let's have a peak at how it works
(and not discuss if it's the devil/our savior).

![bg right:30%](images/45-keenan_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
## Addresses and keys
No registration or
"**k**now **y**our **c**ustomer"-process is required
to perform transactions on the network.  

Relies on user-generated asymmetric key pairs.

The public key acts as the participant's
"account number", known in Bitcoin as "address".  

The private key is used to sign transactions.  
An analogy would be a physical wallet with cash.
  
![bg right:30%](images/45-tower.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Leo Veksler (CC BY-SA 2.0)" -->
## Key considerations
ECC is used due to its great performance and
small key size - no need for "fingerprints"
(hash digest of public key).

Parties with access to the private key
controls Bitcoins associated with
the public key/address.  

To minimize the risk of theft, utilize
"cold wallets" (offline key storage) or
"hardware wallets" (basically a HSM).

![bg right:30%](images/45-hardware_wallets.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nicholas A. Tonelli (CC0 1.0)" -->
## Initializing transactions
James wanna pay Ross for some "consulting".  

James gets hold of Ross' address
from an email/instant messaging chat,
by scanning a QR code or similar.  

James opens his "wallet application" and
commands it to sign a transaction:  

> Transfer 0.42 BTC from address
> bc1qmxje[...]54g3y7wp to
> bc1qa5wk[...]x9ek9hz6

And then what?

![bg right:30%](images/45-forest_road.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Carl Davies (CSIRO) (CC BY 3.0)" -->
## Distributing transactions
The signed transaction data is
distributed to all nodes in the network
using a peer-to-peer "gossip" protocol.  

Nodes are responsible for verifying that
transactions are signed by the private key
associated with the specified source address
and keep track of historic transactions to
validate "account balance".

Anyone can setup a node and monitor
current/historic transactions.

![bg right:30%](images/45-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## Validating transactions
Every \~few minutes, nodes save the
observed and validated transactions,
sorts them and calculates a hash of the data.  

The hash digest of transactions is hashed
together with the previous link
in a hash chain.  
  
In order to disincentivize attempts to
include fraudulent transactions in the
hash chain, nodes must provide a
proof of work.

![bg right:30%](images/45-numpad.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
## PoW in Bitcoin
Take SHA-2 256 hash of transaction data,
previous link hash and a few random bytes.  

Find a hash ending with **X** zeroes,
where X is dynamically and democratically
adjusted by nodes in the network to
account for available compute power.  

Once the challenge has been solved by a
node, it signs the solution and
distributes it to the network.  

![bg right:30%](images/45-resistors.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Mike Grauer Jr (CC BY 2.0)" -->
## Block creation
Nodes receive and validate the proof.  

If \~51% of nodes agree that the correct
transactions were included and that
the PoW challenge was solved,
the data ("called block") is
included in the hash chain.  

To incentivize nodes for properly
verifying transactions and PoW,
**X** Bitcoins are awarded to
the address (public key)
of the solving node.

![bg right:30%](images/45-cubes.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## Wrapping up
Bitcoin does not protect
confidentiality of transactions.  

Other cryptocurrencies use
["zero-knowledge proofs"](https://en.wikipedia.org/wiki/Zero-knowledge_proof) to solve this.  

I hope you learned something new!

![bg right:30%](images/45-gas_refinery.jpg)
