---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Forward secrecy"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Presentation about forward secrey in practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
# Forward secrecy
### Long-term protection of confidentiality

![bg right:30%](images/46-squirrel_noms.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
When protecting network communication,
we typically combine symmetric and
asymmetric cryptography.

A client can connect to a target server,
extract public key from verified certificate,
generate a random symmetric key and
encrypt it against the extracted public key.

Once the symmetric key (AKA **"session key"**)
has been sent to the server, both peers can
use it to encrypt/decrypt transferred data.

![bg right:30%](images/46-squirrel_noms.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
The server's private key may be
accidentally leaked or stolen.  

How would it affect the confidentiality
of historic communication?

![bg right:30%](images/46-squirrel_noms.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
An attacker who has recorded historic
network traffic could use the private key
to decrypt the exchanged session keys.  
  
With access to the session keys,
they could decrypt all transferred data.   

The described method for key exchange does
not provide "**p**erfect **f**orward **s**ecrecy".
  
Yikes.... any ideas?

![bg right:30%](images/46-squirrel_noms.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
The server could generate a new asymmetric
key pair per connection and throw away the
private key once the connection is closed.

This key would be ephemeral and if leaked
only permit decryption of one session.

![bg right:30%](images/46-knippelsbro.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
...but the server's public key is
embedded in the certificate.

Without a verifiable certificate,
the connection is vulnerable against
active man-in-the-middle attacks.

(an attacker who can manipulate
network traffic, that is)  
  
Some suggestions?

![bg right:30%](images/46-knippelsbro.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
Let's generate a new key pair
per connection to the server.  
  
We could then use the private key
associated with the certificate
(let us call it "long-term key")
to sign our newly generated public key
before returning it to the client.

Client's could verify the signature
of the ephemeral public key using 
the server's trusted certificate.  

The long-term key is only used to
establish trust, not for confidentiality. 

![bg right:30%](images/46-knippelsbro.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Joel Rangsmo (CC BY-SA 4.0)" -->
In practice, we typically do this using
**E**phemeral **D**iffie-**H**ellman key exchange  
(sometimes turned around and called "**DHE**").
  
Algorithm specifically designed for...
well, key exchange!

Enable two parties to derive the same
key without sending it over the network.

![bg right:30%](images/46-orange_lens_on_rock.jpg)

<!--
https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## Wrapping up
The goal of forward secrecy is to protect
historic communication even if the server's
private key get leaked/stolen.

A cipher suites in TLS 1.3 provides
forward secrecy, yay!

Any questions? :-)

![bg right:30%](images/46-squirrel_noms.jpg)
