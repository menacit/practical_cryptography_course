---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Obtaining certificates"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Introduction to obtaining publicly signed certificates"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
# Obtaining certificates
### Getting 'em signed by public CAs

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Setting up your own CA
is not that hard.  

Getting users to trust it
is a whole other deal.

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Most operating systems ship with a 
trust store containing CA certificates.  

The **CA/B**rowser Forum agree on
what it takes to be included\*.  

How do we get our CSR signed by
a publicly-trusted CA?

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## The dark ages
Fork up a few (hundred) USD
and specify the email address
(admin|administrator|webmaster|
hostmaster|postmaster)@\$YOUR\_DOMAIN.  

Wait...  

Here is (hopefully) a certificate!

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## Introducing "Let's Encrypt"
Publicly-trusted CA launched in 2014
with the goal of providing certificates
to every website for free (as in beer).  

Developed and run by the nonprofit
**I**nternet **S**ecurity **R**esearch **G**roup.  
  
Supports wild-card certificates
(\*.example.com).  

Invented and uses the
[ACME protocol](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment) to
validate CSRs.

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## The limitations
No email (S/MIME) or
code signing certificates (yet).  

Not trusted in very old/outdated
trust stores (which you probably
shouldn't be trusting anyway!).

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
The certificate aims to
prove control over a domain,
not a brand/company/organization.  

"**E**xtended **V**alidation certificates"
were introduced in 2005 to
address the problem.

![bg right:30%](images/44-cave_stairs.jpg)
