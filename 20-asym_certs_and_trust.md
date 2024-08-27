---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Certificates and trust models"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Presentation about what certificates are and different trust models"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Certificates and trust models

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Asymmetric cryptography enables us
to share secrets/valid authenticity
without a shared key.  

But how do we get hold of the
public key of a peer?

![bg right:30%](images/20-dummy.jpg)

---
```
$ ssh 141.95.102.166

The authenticity of host '141.95.102.166 (141.95.102.166)' can't be established.
ED25519 key fingerprint is SHA256:wzzjNa+3VIhoxAEc1W9KfWzW8APaB3O6OSBFki66jEU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

---
```
$ for KEY in /etc/ssh/ssh_host_*_key.pub; do ssh-keygen -l -f "${KEY}"; done

1024 SHA256:IrBaPa6k+uPe1SMeshWaX8SMomgCxWthfjxtR0jjBfY root@w2 (DSA)
256 SHA256:VBBjYJyshoJU1x63APDVjTyzZu8TG4XUGGu1HxMEXSM root@w2 (ECDSA)
256 SHA256:wzzjNa+3VIhoxAEc1W9KfWzW8APaB3O6OSBFki66jEU root@w2 (ED25519)
3072 SHA256:4CiF9f8vMP2a8cGG5OjW0lmH1xWMXwgwjx9oUvPzYbI root@w2 (RSA
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
What does the "known\_hosts" file contain?  
  
Hostnames/IP addresses ("server identities")
and "key fingerprints" (hash of public key).

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Common "trust models"
- None ("YOLO!")
- **T**rust **O**n **F**irst **U**se (TOFU)
- Certificates and **C**ertificate **A**uthorities (CA)
- **W**eb **o**f **T**rust (WoT)

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## TOFU
```
$ ssh -o StrictHostKeyChecking=accept-new 141.95.102.166
```

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Common "trust models"
- None ("YOLO!")
- **T**rust **O**n **F**irst **U**se (TOFU)
- Certificates and **C**ertificate **A**uthorities (CA)
- **W**eb **o**f **T**rust (WoT)

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## What are "certificates"?
**Signed(public key + metadata)**

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Examples of metadata
- Identity (hostname, email, etc)
- Expiry
- Permitted usage
- ID photo

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Common standards
- X.509
- OpenPGP
- SSH certificates

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## CA
Trust store contains public keys which are blessed to sign other certificates.

## WoT
Any key can sign other certificates, users can choose how much risk they are willing to take.

![bg right:30%](images/20-dummy.jpg)

---
![bg center 70%](images/20-cert_store.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Certificate Authorities
Trust store contains public keys which are
blessed to sign other certificates.

## Web of Trust
Any key can sign other certificates,
users can choose how to "weight" keys
and how much risk they are willing to take.

![bg right:30%](images/20-dummy.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
We'll re-visit this topic and
take a deeper look into how X.509
utilize CAs for establishing trust.

![bg right:30%](images/20-dummy.jpg)
