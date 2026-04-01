---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
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
and "identity information" like
a hostname or email address.  
  
Relies on **Certificate Authorities**
to sign/issue certificates based on
**Certificate Signing Requests**.

![bg right:30%](images/27-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
Certificates for **root CAs** are typically included
in OS/application **trust stores**.  
  
An **intermediate CA** is signed by a root CA
and permitted to issue other certificates
_(for clients, servers, code signing, etc!)_.  
  
Used to minimize usage the super sensitive
root CA private key and thereby protect it.

**CRLs** and **OCSP** may be used to check if
an issued certificate has been revoked.

![bg right:30%](images/27-satellite_dish.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Peter Black (CC BY-SA 2.0)" -->
A client connects to "www.example.com".

The server returns its certificate and the
certificate for the intermediate CA which signed it.

The client uses the public key from a trusted
root CA to validate the signature of the
intermediate CA.

The client uses the public key from the
intermediate CA to validate the signature of
the server's certificate.

If the server certificate's identity metadata
("CN" or "SAN") matches "www.example.com", the
client extracts the embedded public key and uses
it to establish an encrypted connection.

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
  
Provides a more secure alternative
to password authentication.

![bg right:30%](images/27-birds.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kuhnmi (CC BY 2.0)" -->
## TLS typically use...
- X.509 for "identity validation"
- Asymmetric encryption for "key exchange"
- Symmetric encryption for confidentiality
- Hashing for integrity protection

Different combinations of these
(symmetric, asymmetric and hashing algorithms)
are known as **"cipher suites"**.

![bg right:30%](images/27-birds.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ESA (CC BY 3.0 IGO)" -->
Any questions before we move on?

![bg right:30%](images/27-tarso.jpg)
