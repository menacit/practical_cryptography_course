---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: X.509/TLS recap"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Quick recap of X.509/TLS presentations in the practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% ESA (CC BY 3.0 IGO)" -->
# X.509 / TLS recap

![bg right:30%](images/27-tarso.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
**X.509** is a standard for
**cryptographic certificates ("PKI")**.  
  
These certificates contain a **public key**
and **metadata**, such as expiry time
and "identity information" like a
**hostname** or **email address**.  
  
Relies on **certificate authorities**
to sign/certify certificates.

![bg right:30%](images/27-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
Certificates for **root CAs** are typically included
in OS/application **trust stores**.  

![bg right:30%](images/27-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
Used for encrypted/signed email ("S/MIME"),
securing key exchange in network protocols,
validating software authenticity and similar.

![bg right:30%](images/27-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kuhnmi (CC BY 2.0)" -->
**TLS** is used to secure
**network communication**
between client and server
**applications**.  
  
Replaces the outdated **SSL protocol**,
an acronym that has become a synonym.  
  
Commonly used to wrap/tunnel
cleartext protocols like
HTTP(S) and SMTP(S).

![bg right:30%](images/27-birds.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kuhnmi (CC BY 2.0)" -->
**Mutual TLS ("mTLS")** is used to
authenticate both **peers** in
a session (client and server).

![bg right:30%](images/27-birds.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kuhnmi (CC BY 2.0)" -->
## TLS typically use...
- X.509 for "identity validation"
- Asymmetric encryption for key exchange
- Symmetric encryption for confidentiality
- Hashing for integrity protection

Different combinations of these
(symmetric, asymmetric and hashing algorithms)
are known as **"cipher suites"**.

![bg right:30%](images/27-birds.jpg)
