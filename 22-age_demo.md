---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: age tool demo"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Demonstration of asymmetric encryption tool age"
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

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Miske (CC BY-SA 2.0)" -->
# Tool demonstration: age
### Lean and mean file encryption

![bg right:30%](images/22-silo.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Miske (CC BY-SA 2.0)" -->
## What is ["age"](https://age-encryption.org/)?
- FOSS tool (and format) for symmetric and **asymmetric file encryption**
- Fast and modern (\~secure)
- Compatible with (some) SSH keys
- Support for [key storage on hardware token](https://github.com/str4d/age-plugin-yubikey)

![bg right:30%](images/22-silo.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Stig Nygaard (CC BY 2.0)" -->
## Generate key pair
```
$ age-keygen | tee my_private.key

AGE-SECRET-KEY-1MQ5U9HTKKAP[...]Y92RTHKH7ASQ5LVL2Q
```

```
$ age-keygen -y my_private.key | tee my_public.key

age14z423we7r3ze5rkjy4[...]uwfy9pxxvmnxy2yrq6rr74p
```

![bg right:30%](images/22-grey_heron.jpg)

---
## Let's encrypt some data
```
$ cat secret.txt

I shot the sheriff :-/
```

```
$ cat secret.txt | \
	age --encrypt --recipients-file my_public.key \
	> secret.txt.age
```

---
## ...and decrypt it
```
$ cat secret.txt.age | \
	age --decrypt --identity my_private.key \
	> secret.txt
```

```
$ cat secret.txt

I shot the sheriff :-/
```

---
## Encrypt to multiple keys
```
$ cat alice.key.pub bob.key.pub | tee friends.keys

age1uw4mjkc9ma5tvs5[...]2ywm69kru2rspacst0jdnczqacx2s5
age1eut64dvujqfmw6e[...]uuddd7hdxsrw3csu3dzh6amswhyr3v
```

```
$ cat secret.txt | \
	age --encrypt --recipients-file friends.keys \
	> secret.txt.age
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yubinerd (CC BY-SA 4.0)" -->
## Generate / store key on YubiKey
```
$ age-plugin-yubikey \
	--generate \
	--pin-policy never \
	--touch-policy always \
	> my_yubikey.plugin

[...]

! Please touch the YubiKey
Recipient: age1yubikey1q0[...]q6
```

![bg right:30%](images/22-yubikey.jpg)

---
## Encrypt and decrypt data using YubiKey
```
$ age-keygen -y my_yubikey.plugin > my_yubikey.pub

$ cat secret.txt | \
	age --encrypt --recipients-file my_yubikey.pub \
	> secret.txt.age
```

```
$ cat secret.txt.age | \
	age --decrypt --identity my_yubikey.plugin \
	> secret.txt
	
! Please touch the YubiKey
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Miske (CC BY-SA 2.0)" -->
## Wanna give it a spin?
Try replacing tar/7-Zip in the
"sym\_crypt" lab backup script with age!

Take it a step further and use your
YubiKey for storing the private key.
  
**[courses+crypto_012201@%EMAIL_DOMAIN%](mailto:courses+crypto_012201@%EMAIL_DOMAIN%)**

![bg right:30%](images/22-silo.jpg)
