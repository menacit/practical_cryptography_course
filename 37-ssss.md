---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: SSSS"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to Shamir's Secret Sharing Scheme"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
# Introduction to SSS(S)
### Shamir's Secret Sharing (Scheme)

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
We've talked about multi-signing in OpenPGP and some of its use-cases.  
  
Wouldn't it be cool if we could do the same thing for encryption?

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
But we can already encrypt a message
to several recipients?  
  
Yes, but every single one of them can
decrypt the message on their own.

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
Let's say that you write a will.  
Maybe you do have a favorite child?  
  
You sign it and symmetrically encrypt it.  
  
**Now what?**

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
Perhaps we could use a **HSM**?  
  
Hmmm, yes - but there is another option...

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
## Shamir got you covered!
With _SSS_, a secret (such as a password)
can be encrypted and split into
several **shares**.  
  
In order to decrypt the secret,
a configurable number of shares must be known.  
  
An analogy would be RAID5/6.

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
You have four children and a lawyer.  
  
You use _SSS_ to encrypt a passphrase
into five shares.  

You set a requirement that three shares
are required to decrypt the passphrase.  
  
In order to decrypt the passphrase/will,
at least/any three of the shareholders
must collaborate.

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Steve Jurvetson (CC BY 2.0)" -->
Sounds like a neat trick,
but does anyone use it?  
  
[HashiCorp Vault](https://www.hashicorp.com/products/vault) is one example.  
  
Useful for many
"break glass in case of emergency"-solutions.

![bg right:30%](images/37-drones.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Warren LeMay (CC BY-SA 2.0)" -->
## Exercise: Hidden treasure
Use the tool ["ssss-split"](http://point-at-infinity.org/ssss/) to encrypt:
> My gold is buried under the dog house
  
Split secret into three shares and require two of them for decryption.  
  
Send a share each and
**decryption instructions** to:
  
**[courses+crypto_ssss-1@%EMAIL_DOMAIN%](mailto:courses+crypto_ssss-1@%EMAIL_DOMAIN%)**,
**[courses+crypto_ssss-2@%EMAIL_DOMAIN%](mailto:courses+crypto_ssss-2@%EMAIL_DOMAIN%)** and
**[courses+crypto_ssss-3@%EMAIL_DOMAIN%](mailto:courses+crypto_ssss-3@%EMAIL_DOMAIN%)**.

![bg right:30%](images/37-vault_door.jpg)
