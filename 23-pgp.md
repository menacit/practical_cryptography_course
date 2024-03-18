---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: PGP basics"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to OpenPGP in the practical cryptography course"
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
# OpenPGP basics
### Pretty Good Privacy since 1991

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## What is PGP?
Tool suite for asymmetric cryptography
developed by Phil Zimmermann
in the early 90s.  
  
"OpenPGP" acts as the umbrella for
attempts to standardize PGP.

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Common use-cases for PGP
Securing message-based communication
methods, such as E2E for email.  
  
File encryption.  
  
Software authenticity validation on Linux.

![bg right:30%](images/23-lamps.jpg)

---
## Used for package metadata signing
```
$ cat /etc/apt/sources.list.d/github-cli.list 

deb [signed-by=/etc/keys/github.pub] https://cli.github.com/packages stable main
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
OpenPGP certificates are signed ("**certified**")
by the key holder and potentially others.  
  
Pioneered the "**Web of Trust** model for
identity/certificate validation.

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Implementations
- **GnuPG**: Swiss army knife, AKA "GPG"
- **Sequoia**: Modern CLI tools and Rust libraries
- **GopenPGP**: PGP in your Go applications
- **OpenPGP.js**: Client- and server-side library

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## 'Nuff talk, more demos.

![bg right:30%](images/23-lamps.jpg)

---
### Let me introduce you to "sq"!
```
$ sq --help

sq 0.25.0 (sequoia-openpgp 1.7.0)
A command-line frontend for Sequoia, an implementation of OpenPGP
[...]
```

---
### Key / certificate generation
```
$ sq key generate \
	--userid 'Test Labsson <test@example.com>' \
	--export test.private \
	--expires-in 5y 

$ sq key extract-cert test.private --output test.cert 
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Basic file encryption
```
$ cat todo.md 

## My TODO list
- [X]: Learn about PGP
- [ ]: Conquer the world

$ cat todo.md | sq encrypt \
	--recipient-cert test.cert \
	> todo.md.pgp
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Basic file decryption
```
$ cat todo.md.pgp | \
	sq decrypt \
	--recipient-key test.private 

Encrypted using AES with 256-bit key
Compressed using ZIP

## My TODO list
- [X]: Learn about PGP
- [ ]: Conquer the world
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Digitally signing a message
```
$ cat proclamation.txt | \
	sq sign \
	--cleartext-signature \
	--signer-key test.private \
	> proclamation.txt.pgp
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Digitally signing a message
```
$ cat proclamation.txt.pgp

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

I hereby promise to never put
meatballs in my nose again!

-----BEGIN PGP SIGNATURE-----

wr0EARYKAG8FgmQX9m0JELNUBDJO1RxQAA
LnNlcXVvaWEtcGdwLm9yZzku8htwo/JCHZ
FiEEo62bZCb5bbX3wxfDs1QEOm7UAAHJnA
EY3QZRMCQZ8S5CwDUgEAqtSrWEvEa[...]
-----END PGP SIGNATURE-----
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Verifying signed message
```
$ cat proclamation.txt.pgp | \
	sq verify \
	--signer-cert test.cert 

Good signature from B354043A692893B5
1 good signature.

I hereby promise to never put
meatballs in my nose again!
```

![bg right:30%](images/23-lamps.jpg)

---
### Let's create some more test keys
```
$ for NAME in alice bob charlie; do 
	sq key generate \
		--userid "${NAME} <${NAME}@example.com>" \
		--expires-in 5y --export "${NAME}.private"

	sq key extract-cert \
		"${NAME}.private" \
		--output "${NAME}.cert"
done
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Multi-signing a message
```
$ cat the_truth.txt | \
	sq sign \
	--signer-key alice.private \
	> the_truth.txt.pgp

$ cat the_truth.txt.pgp | \
	sq sign \
	--signer-key bob.private \
	--append | \
	sponge the_truth.txt.pgp
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Verify multi-signed message
```
$ cat the_truth.txt.pgp | \
	sq verify \
	--signer-cert alice.cert \
	--signer-cert bob.cert \
	--signer-cert charlie.cert

Good signature from F89E9C4294F51777
Good signature from 5CF0C96FD9C6DC05
2 good signatures.

Oceania was at war with Eastasia
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Verify multi-signed message
```
$ cat the_truth.txt.pgp | \
	sq verify \
	--signer-cert alice.cert \
	--signer-cert bob.cert \
	--signer-cert charlie.cert \
	--signatures 3

Good signature from F89E9C4294F51777
Good signature from 5CF0C96FD9C6DC05
2 good signatures.
Error: Verification failed
```

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Certify third-party key
```
$ sq certify \
	alice.private \
	charlie.cert \
	'charlie <charlie@example.com>' | \
	sponge charlie.cert

$ sq certify \
	bob.private \
	charlie.cert \
	'charlie <charlie@example.com>' \
	--amount 60 | \
	sponge charlie.cert
```

![bg right:30%](images/23-lamps.jpg)

---
### Peaking at the certificate
```
$ sq inspect --certifications charlie.cert 

charlie.cert: OpenPGP Certificate.

Fingerprint: 63887435C2B865DBBA537AA0BC80AE1A45B83D65
Public-key algo: EdDSA Edwards-curve Digital Signature Algorithm
[...]
UserID: charlie <charlie@example.com>
Alleged certifier: D36E658BA221819AD35F80484047E2EF12270FAD
Alleged certifier: 06FE1C00440DD227E7EAE81B1B2D8E573AD890CF
Note: Certifications have NOT been verified!
```

---
### Create a keyring
```
$ sq keyring join --output alice.keyring *.cert

$ sq keyring list alice.keyring

0. 06FE1C0[...]573AD890CF alice@example.com
1. D36E658[...]EF12270FAD bob@example.com
2. 6388743[...]1A45B83D65 charlie@example.com
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
But wait a minute, how do I know
that a key for test@example.com
belongs to the real **Test Labsson**?

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Strategies for key verification 
- Praying / hoping for the best
- Key signing _parties_
- Web of Trust
- [DOIP / Keyoxide](https://docs.keyoxide.org/)

![bg right:30%](images/23-lamps.jpg)

---
![bg center 65%](images/23-keyoxide_example.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Just for cool cats/terminal dwellers?  
  
Let me introduce you to **Gpg4win**.

![bg right:30%](images/23-lamps.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Gpg4win
- **GnuPG**: Where the magic happens
- **Kleopatra**: GUI for management/encryption
- **GpgOL**: Integration for Outlook and Office
- **GpgEX**: Add-on for file explorer
  
FOSS with [professional support available](https://gnupg.com/gnupg-desktop.html).

![bg right:30%](images/23-lamps.jpg)

---
![bg center 70%](images/23-gpg4win_file_to_sign.png)

---
![bg center 55%](images/23-gpg4win_explorer_options.png)

---
![bg center 70%](images/23-gpg4win_explorer_options_zoomed.png)

---
![bg center 55%](images/23-gpg4win_sign_options.png)

---
![bg center 55%](images/23-gpg4win_explorer_verify.png)

---
![bg center 70%](images/23-gpg4win_verify_valid.png)

---
![bg center 70%](images/23-gpg4win_verify_invalid.png)

---
![bg center 70%](images/23-gpg4win_certs.png)

---
![bg center 70%](images/23-gpg4win_file_to_encrypt.png)

---
![bg center 55%](images/23-gpg4win_encrypt_options.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Hope this piqued your interest.  

All tools (_except the original PGP_) described
are freely available for you to play with.  

Grab a few classmates and set up a WoT.

![bg right:30%](images/23-lamps.jpg)
