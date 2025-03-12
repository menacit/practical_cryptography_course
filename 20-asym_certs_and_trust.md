---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
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
Asymmetric cryptography enables us to
share secrets and sign/validate data
without a shared secret key.  

But how do we get hold of the
public key of our peer?

_(both other humans and network services)_

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
<!-- _footer: "%ATTRIBUTION_PREFIX% Egill Egilsson (CC BY 2.0)" -->
What does the "known\_hosts" file 
created by our SSH client contain?  
  
Hostnames/IP addresses ("server identities")
and "key fingerprints" (hash of public key).

_(the "server identities" are often hashed
to minimize information disclosure if
file is stolen/leaked)_

![bg right:30%](images/20-esbjerg.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Cory Doctorow (CC BY-SA 2.0)" -->
We can't go around and ask everyone/everything
on the Internet what their public key is.  

Mayhaps your bank could write it on a sign
in their lobby, but what about
a random web shop?  

There must be a better way...

![bg right:30%](images/20-paper_bag_man.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
## Common "trust models"
- None ("YOLO!")
- **T**rust **O**n **F**irst **U**se (TOFU)
- Certificates and **C**ertificate **A**uthorities (CA)
- **W**eb **o**f **T**rust (WoT)

![bg right:30%](images/20-koto_greenhouse.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
## TOFU
```
$ ssh -o StrictHostKeyChecking=accept-new 141.95.102.166
```

![bg right:30%](images/20-gunver.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
## Common "trust models"
- None ("YOLO!")
- **T**rust **O**n **F**irst **U**se (TOFU)
- Certificates and **C**ertificate **A**uthorities (CA)
- **W**eb **o**f **T**rust (WoT)

![bg right:30%](images/20-koto_greenhouse.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Elly Jonez (CC BY 2.0)" -->
## What are "certificates"?
`sign(public key + metadata)`

Only requires us to know the
signer's public key in advance.

Examples of metadata:

- Identity (hostname, email, etc)
- Portrait photo
- Expiry date

![bg right:30%](images/20-window_computer.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## Common standards
- X.509
- SSH certificates
- OpenPGP

![bg right:30%](images/20-longmoor_cab.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## Certificate Authorities
Trust store contains public keys which are
blessed to sign other certificates.

## Web of Trust
Any key can sign others certificates,
users can choose how to "weight" keys
and how much risk they are willing to take.

![bg right:30%](images/20-longmoor_cab.jpg)

---
![bg center 70%](images/20-cert_store.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
We'll re-visit this topic and
take a deeper look at how X.509
utilize certificate authorities
to establish trust.

![bg right:30%](images/20-dummy.jpg)
