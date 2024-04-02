---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
# WebAuthn and FIDO2
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
  
One-time codes don't provide bulletproof protection against phishing.

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
### The heroes we need right now
[**FIDO Alliance**](https://fidoalliance.org/) is an industry association working
to ~~kill~~ reduce reliance on passwords.  
  
[**W3C**](https://www.w3.org/) is one of the main organizations working
on development of web standards.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### "FIDO2" consist of...
**WebAuthn** allows users to
cryptographically authenticate against sites/systems.  
  
**CTAP 2.0** acts as a standardised protocol for
applications/OSes to communicate with
external authentication devices.

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
## The promise 
Phishing-resistant authentication based on
hardware-backed cryptography **for everyone**!

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### Ehmm... less fluff, please.

![bg right:30%](images/38-cyberpunk.jpg)

---
![bg center 65%](images/38-webauthn.png)

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
### Not just for web browsing
```
$ ssh-keygen \
	-t ed25519-sk \
	-f ~/.ssh/my_fido2_key

Generating public/private ed25519-sk key pair.
You may need to touch your authenticator
to authorize key generation.

Enter passphrase (empty for no passphrase): ****
Enter same passphrase again: ****
```

![bg right:30%](images/38-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Austin Design (CC BY-SA 2.0)" -->
### A note about "passkeys"
Marketing term used by companies
like Google and Apple.  

Prioritizes multi-device synchronization
instead of the "HSM approach"
("the key may never leave!").  
  
Utilizes Webauthn under the hood.

![bg right:30%](images/38-cyberpunk.jpg)
