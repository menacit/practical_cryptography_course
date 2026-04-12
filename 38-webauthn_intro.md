---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: WebAuthn and FIDO2"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to WebAuthn and FIDO2"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## FIDO2, WebAuthn and Passkeys
### A somewhat gentle introduction

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## Passwords suck
Choosing a ~~good~~ decent one seems tricky.  
  
Avoiding reusal (unique per site/systems).  
  
Constantly worrying about where you write it.

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Let's throw in some 2FA, you may say.  
  
One-time codes don't provide bulletproof
protection against credential phishing.

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
What about "client certificates"
and enforcement of mutual TLS -
it is resistant to phishing, right?

Yes, but everyone would need manage
site-specific certs or rely on publicly
trusted CAs to issue them - doesn't
really work at "Internet scale".

(you also enable "linkability",
tricky for users to stay anonymous)

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Shame that we'll never get rid of them.

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
Wait a second, what is that shining beacon?

![bg right:30%](images/38-pillars.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
## Meet our saviors
[**FIDO Alliance**](https://fidoalliance.org/) is an industry association
working to ~~kill~~ reduce reliance on passwords.  
  
[**W3C**](https://www.w3.org/) is one of the main organizations
working on development of web standards.

Together, they promise phishing-resistant
authentication based on trustworthy
cryptography **for everyone**!

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### "FIDO2" consist of...
**WebAuthn** is an interface for
authenticate against sites/systems
(provided by web browsers through JavaScript).  
  
**CTAP 2.0** acts as a standardised protocol for
applications/OSes to communicate with
external authentication devices,
like a TPM or YubiKey.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### How it works: Registration
User registers on "https://example.com"
with the username "Bob".
  
JavaScript in user's browser utilize
the WebAuthn API to generate a new
asymmetric keypair for the origin
("https://example.com"). 
  
The web browser speaks CTAP to forward
the request to the YubiKey over USB/NFC,
which returns the matching public key.
  
The browser sends the public key to
the web server on "www.example.com".

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### How it works: Login
User tries logging in as "Bob".
  
The web server provides a challenge
(a few random bytes).

The browser forwards the challenge
and web site origin to the YubiKey.

YubiKey uses the private key associated
with the origin ("https://example.com")  
to sign the challenge.

The server validates the challenge
signature using the stored public key
associated with "Bob".

![bg right:30%](images/38-cyberpunk.jpg)

---
![bg center 65%](images/38-webauthn.png)

<!--
https://webauthn.io/
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
That's quite smooth, but a bit annoying
that we still need to enter a username.

No worries, **discoverable credentials**
are here to remove that friction!

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### Login with "discoverable credentials"
User tries to login at "example.com".
  
The browser asks the YubiKey if it has
any private key for the origin - if so,
it returns the matching public key.

Once sent to the web server, it checks
which user it's associated with ("Bob")
and returns a challenge.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
Neat! But do anyone support it?

Yes, all major browsers/OSes and
most big web sites.

Some password managers and OSes
offer it without requiring a dedicated
security token like the YubiKey
(which has some pros/cons).

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
**How is this different from mTLS + HSM?**  
  
No CA/X.509 required, generates unique
keypair per site ("origin").  
  
Simpler and provides better privacy.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
**What makes it "phishing-resistant"?**  
  
Unique key for each site/origin.  
  
Browser/application includes origin in authentication request against (hardware) token.  
  
You may not be able to tell the different,
but "g00Ige.com" isn't "google.com".

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### A note about "passkeys"
Marketing term initially used by
companies like Google and Apple.  
  
Most people agree that it's better
than "FIDO2 with discoverable keys",
so even the alliance us it these days.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### Extending the standard
WebAuthn is mutating into a generalized
interface for performing hardware-backed
cryptographic operations in web browsers,
not just authentication!

Extensions like "hmac-secret" (AKA "PRF")
may be used to derive a symmetric key
based on the origin - super useful for
client-side encryption in web apps!

The "raw signing extension" will enable
signing of arbitrary data, like
documents or votes.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Quinn Dombrowski (CC BY-SA 2.0)" -->
## Wrapping up
Thanks to passkeys, we are closer than
ever before to get rid of lousy passwords
without sacrificing the user experience!

(Makes it a bit [tricky to change domain](https://www.theverge.com/news/807011/twitter-com-x-com-login-security-key-passkey-domain))

Wanna give it a try? Checkout demo sites
like ["WebAuthn.io"](https://webauthn.io/) or build something
yourself using ["py_webauthn"](https://duo-labs.github.io/py_webauthn/).

![bg right:30%](images/38-pillars.jpg)
