---
SPDX-FileCopyrightText: © 2026 Menacit AB <foss@menacit.se>
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
truststore containing CA certificates.  

The **CA**/**B**rowser Forum agree on
what it takes to be included\*.  

How do we get our CSR signed by
a publicly-trusted CA?

Furthermore, how do they validate the
"identity" (hostname, for example)
in our submitted CSR?

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## The dark ages
Upload your CSR to their website.
  
Fork up a few (hundred) USD
and specify the email address
(admin|administrator|webmaster|
hostmaster|postmaster)@\$YOUR\_DOMAIN.
  
Take the random code they emailed
you and enter it on their website.

Download a signed certificate!

(Once expired, repeat process)

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
Sounds annoying, quite expensive
and not all that secure!

No wonder most web sites weren't
available over HTTPS.

(which hackers and spooks loved!)

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## Introducing "Let's Encrypt"
Publicly-trusted CA launched in 2014
with the goal of providing certificates
to every website for free (as in beer).  

Developed and run by the nonprofit
**I**nternet **S**ecurity **R**esearch **G**roup.  
  
Invented and uses the
[ACME protocol](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment) to
validate CSRs and issue certificates.

![bg right:30%](images/44-cave_stairs.jpg)

<!--
https://www.manageengine.com/key-manager/what-is-automated-certificate-management-environment-acme.html
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
The limitation: Just server certificates
with 90 days expiry time (soon 45 days).
  
Need software to automatically handle
renewal, like [Certbot](https://certbot.eff.org/), or a web server
that has built-in support, such as [Caddy](https://caddyserver.com/).

![bg right:30%](images/44-cave_stairs.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
The certificate aims to
prove control over a domain/email address,
not a brand/company/organization.  

"**E**xtended **V**alidation certificates"
were introduced in 2005 to
address the problem.

Required for code-signing of drivers
in Microsoft Windows and similar.

![bg right:30%](images/44-cave_stairs.jpg)

<!--
https://en.wikipedia.org/wiki/Extended_Validation_Certificate
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kurayba (CC BY-SA 2.0)" -->
## Wrapping up

![bg right:30%](images/44-cave_stairs.jpg)
