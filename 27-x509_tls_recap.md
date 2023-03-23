---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Today's agenda
- Recap of X.509 and TLS basics
- Overview of network encryption solutions
- Quiz!
- Lab / Q&A time

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
**Thanks for the feedback!** _:person-bowing:_

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Suggested improvements
- Shorter/less presentations
- More activities - suggestions?
- Better way to handle course/lab material. Perhaps Git or any other ideas? 

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Clearer lab descriptions
Several requests for verbose lab descriptions.

Make sure to carefully go through **README.md**.  
  
When in doubt, ask the **teacher** for clarification.

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
### Excerpts from lab description
> Learning objectives:
> Practical knowledge of
> one-way hash functions for
> **storage/validation** of passwords.

> Tasks - Mandatory:
> Modify the web server code to use
> SHA384 for protection of the
> **stored password**

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
### Excerpts from lab description
> Lab report/documentation:
> Each student should submit
> a lab report containing
> **at least** the following information
[...]
> **Demonstration** of how the
> implemented changes
> **improve security** of the service
> (**"before and after"**)

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## Course pace and graded activities
**40 hours** per week for full-time studies.  
  
**~30 hours** available for labs / self-studies.  
   
**>=8 hours** of teacher assistance / Q&A time.

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Rick Harris (CC BY-SA 2.0)" -->
## End of rant. Let's recap!

![bg right:30%](images/27-car.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
**X.509** is a standard for
**cryptographic certificates ("PKI")**.  
  
These certificates contains a **public key**
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
**Mutual TLS ("mTLS")** is used to authenticated both **peers** in a session (client and server).

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
