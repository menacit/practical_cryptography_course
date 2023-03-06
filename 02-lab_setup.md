---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Lab setup"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Guidance for setup of lab systems for the practical cryptography course"
keywords:
  - "cryptology"
  - "cryptography"
  - "practical"
  - "encryption"
  - "course"
  - "lab"
  - "setup"
color: "#ffffff"
class:
  - "invert"
style: |
  section.center {
    text-align: center;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bill Smith (CC BY 2.0)" -->
# Lab setup
### What you need to know to get started

![bg right:30%](images/02-sphere.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yubinerd (CC BY-SA 4.0)" -->
**You'll need a [YubiKey in the "5 Series"](https://www.yubico.com/products/yubikey-5-overview/).**

![bg right:30%](images/02-yubikey.jpg)

<!--
- For labs and experiments, students will need a Yubikey

- Thankfully, Yubico has provided them to the in-class students

- A nimble device that can be used to increase cryptographic security, more about it later!
-->

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## You need to setup...
- [HashiCorp Vagrant](https://developer.hashicorp.com/vagrant/downloads) on your host machine
- [Virtualbox](https://www.virtualbox.org/) or other Vagrant provider

Connect YubiKey via USB, open a terminal in ["resources/labs"](%RESOURCES_ARCHIVE%) and run:

```
$ vagrant up
$ vagrant ssh
$ vagrant ssh -- ykman info
```
  
See "resources/labs/README.md" for details!

![bg right:30%](images/02-owl.jpg)

<!--
- We'll need some software and a lab environments for the course

- For now, just make sure that the software is installed and seem to be working.

- Check out the presentation links: I will however not provide a step-by-step guide, you won't get
it in real life.

- Have a look at the README.md, contains several tips for solving common issues
-->
