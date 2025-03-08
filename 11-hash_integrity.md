---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Hashing for integrity validation"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Usage of cryptographic hashing for integrity validation"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Kojach (CC BY 2.0)" -->
## Hashing for integrity validation

![bg right:30%](images/11-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kojach (CC BY 2.0)" -->
Running "shasum" to get file hashes - is that it?  
  
Let's take a look at some example use-cases.

![bg right:30%](images/11-face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jeena Paradies (CC BY 2.0)" -->
## FIM
Background services continuously checking hashes of executables, configuration files, etc.  
  
Commonly used as a detection mechanism for malicious/unapproved systems changes.  
  
Wanna give it a try? Take a look at:

- [Samhain](https://www.la-samhna.de/samhain/manual/)
- [osquery](https://osquery.readthedocs.io/en/stable/deployment/file-integrity-monitoring/)
- [IMA](https://www.redhat.com/en/blog/how-use-linux-kernels-integrity-measurement-architecture)

![bg right:30%](images/11-lion.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Wolfgang Stief (CC0 1.0)" -->
## Runtime allow-listing
Let's take it one step further - block execution of binaries that doesn't match permitted hashes.  
  
Enables enforcement of computer usage policies and several forms of malware.  
  
Checkout [Airlock Digital](https://www.airlockdigital.com/) and
[fapolicyd](https://novalug.org/docs/fapolicyd.thurston.pdf).

![bg right:30%](images/11-chips.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Martin Fisch (CC BY 2.0)" -->
## Software download mirrors
Lots of FOSS projects rely on third-party mirror sites for downloads as bandwidth is not free.  
  
Mirrors may be compromised or run by a malicious actor that modifies executables.  
  
Hashes can be published on a project's official website to mitigate the problem.

![bg right:30%](images/11-albatross.jpg)

---
![bg center 70%](images/11-ubuntu_download.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Revoy (CC BY 3.0)" -->
## Supply-chain security
Most systems/code bases rely on software published by a vendor or FOSS project.  
  
Remote modification of dependencies could lead malicious code being baked into the application.  
  
Pinning using hashes is common solution:

```
$ docker pull hashicorp/vault:1.12.4@sha256:03d1[...]5cda
```

![bg right:30%](images/11-astronaut.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kojach (CC BY 2.0)" -->
A small sample of how cryptographic hashing
can be utilized to protect data integrity.

Questions? :-)

![bg right:30%](images/11-face.jpg)
