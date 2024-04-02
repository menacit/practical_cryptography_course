---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Key management and HSM"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Overview of secure usage and storage of cryptographic keys"
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
# Key management
### Protecting storage and usage of keys

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
We talk about Alice, Bob and Charlie.  
  
They are merely key holders
(and hopefully the only ones).

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Revocation is not perfect.  
  
May not be a practical option.  
  
How do you even know that a key has been compromised?

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Let's slap some symmetric encryption on the asymmetric private key!  
  
Key may still be stolen by malware
once decrypted.

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Should we change key every time a team member or sysadmin leaves/becomes untrusted?  
  
Should we really trust everyone equally?

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Meet the CAB!
[CA/Browser Forum](https://cabforum.org/).  
  
Sets baseline security/policy requirements for CAs that want to be included in trust stores.  
  
If you're a public CA and the forum doesn't like you, you're in big trouble.

![bg right:30%](images/36-monkey.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% CA/Browser Forum (CC BY-SA 4.0)" -->
![bg center 65%](images/36-cabforum_rules.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Some try to push things a bit further,
like Google with [Certificate Transparency](https://www.rfc-editor.org/rfc/rfc9162).

![bg right:30%](images/36-monkey.jpg)

---
![bg center 65%](images/36-ct_1.png)

---
![bg center 65%](images/36-ct_2.png)

---
## "Hardware Security Module"
Purpose designed hardware devices
for cryptographic operations.  
  
Typically used to generate/store keys
and sign/decrypt data.

Comes in many shapes and sizes:
- Rack units
- Key fobs
- Smart / SIM cards
  
![bg right:30%](images/36-crypto_keys.jpg)

---
## Security promise
**Keys that are generated and/or stored in HSM may never leave.**

![bg right:30%](images/36-crypto_keys.jpg)

---
## Secure key storage 
Device should be tamper resistant.  
  
Device should not leak key material through
side-channels (see ["TEMPEST"](https://en.wikipedia.org/wiki/Tempest_(codename))).

![bg right:30%](images/36-crypto_keys.jpg)

---
## Restricted key usage 
Key operations may be restricted by
authentication requirements,
rate limiting, datetime, etc.  
  
PIN code/password, biometrics, "two-man rule",
actual physical keys, etc.  
  
Logging of all usage.

![bg right:30%](images/36-crypto_keys.jpg)

---
### They may even be quite fast!

![bg right:30%](images/36-crypto_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Yubinerd (CC BY-SA 4.0)" -->
## YubiKey
Continuously improved for ~15 years.  
  
Built to survive on your keyring.

Manufactured in Sweden and USA.  
  
Well-supported by applications and community.

![bg right:30%](images/36-yubikey.jpg)

---
## Nitrokey
Open source SW and HW design.

Made in Germany.  
  
Upgradable firmware.

![bg right:30%](images/36-nitrokey.jpg)

---
## Let's try 'em out!

![bg right:30%](images/36-crypto_keys.jpg)

---
## Generate key on device
```
$ ykman piv keys generate 9a - | tee ada.pub

*BLINK BLINK BLINK BLINK*

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9[...]w0BAQEFyq/16vg95xrygi
JZ1//C5/06HCMJpNh[...]zplpr5oUBD3PLirNgCk+x
BEZb7ie5/EA5nU8TT[...]99w5e5MKthaFWFTPV6XIQ
kpapkPJ0cEkbryn+2[...]/30GwvHb5emaaS+fcllI/
APvi/+WqNLrR6H5WC[...]9mJ2hr+56w1RA+pJAIhmu
ZgJHnKUWq2NgDieVI[...]bNC7ps/Xuehjbsnxatj3v
-----END PUBLIC KEY-----
```

![bg right:30%](images/36-crypto_keys.jpg)

---
## Create a CSR
```
$ ykman \
	piv certificates request \
	--subject "ada" 9a ada.pub - \
	| tee ada.csr

? Enter PIN: ********

-----BEGIN CERTIFICATE REQUEST-----
MIICZDCCAUwCAQ[...]AwkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQ[...]EAJpNhzplpr5oqRUc
udwm0lg07JtlrH[...]SvU8TT99w5e5Mruvl
cAL8mWmuKqD6dH[...]CJyn+2/30GwvHts6d
nrTmp83Oj+ilIc[...]nvpQtueZ/BDzft+Ot
gGoUBZGw01hmq8[...]+ZxCLc2dmO7bTcYro
-----END CERTIFICATE REQUEST-----
```

![bg right:30%](images/36-crypto_keys.jpg)

---
### Import CSR and issue certificate
```
$ e import-req ada.csr ada

[...]
The request has been successfully
imported with a short name of: ada

$ e sign-req client ada

[...]
Request subject, to be signed as a
client certificate for 825 days:

subject=
  commonName = ada

[...]
Certificate created at:
/home/lab_user/pki/issued/ada.crt
```

![bg right:30%](images/36-crypto_keys.jpg)

---
### Import certificate in YubiKey
```
$ ykman \
	piv certificates import \
	9a pki/issued/ada.crt --verify

? Enter PIN: **********
```

![bg right:30%](images/36-crypto_keys.jpg)

---
### Show device / key slot information
```
$ ykman piv info

PIV version: 5.4.3
PIN tries remaining: 3/3
Management key algorithm: TDES
CHUID:	3019d4e73a[...]739ced39ce739d83
CCC: 	No data available.
Slot 9a:
  Algorithm:	RSA2048
  Subject DN:	CN=ada
  Issuer DN:	CN=Easy-RSA CA
  Serial:	231896777[...]612734602
  Fingerprint:	900b3b050[...]f0ebd65b9
  Not before:	2023-04-01 13:37:42
  Not after:	2025-07-01 13:37:42
```

![bg right:30%](images/36-crypto_keys.jpg)

---
## What just happened?

![bg right:30%](images/36-crypto_keys.jpg)

---
That's quite neat. But how do you use it?  
  
Several different "interfaces" and "protocols" exist for usage of a HSM/smart-card.  
  
In this case,
the application (or cryptography library) uses
the standardized [**PKCS #11**](https://en.wikipedia.org/wiki/PKCS_11) interface
for access to cryptographic operations.

![bg right:30%](images/36-crypto_keys.jpg)

---
### List available PKCS #11 tokens
```
$ p11tool --list-tokens

Token 0:
  URL: pkcs11:model=PKCS%231[...];token=ada
  Label: ada
  Type: Hardware token
  Flags: RNG, Requires login
  Manufacturer: piv_II
  Model: PKCS#15 emulated
  Serial: 75d007d3196b0e74
  Module: opensc-pkcs11.so
```

![bg right:30%](images/36-crypto_keys.jpg)

---
### Use YubiKey for HTTPS with curl
```
$ curl \
  --cacert pki/ca.crt \
  --cert "$(p11tool --list-token-urls | grep token=ada)" \
  https://nuke-mgmt.example.test/status.cgi

? Enter PKCS#11 token PIN for ada: *******

Status: NUKES ARMED AND READY! :-O
```

![bg right:30%](images/36-crypto_keys.jpg)

---
Works in many web browsers as well.  
  
Use PKCS #11 to store your CA/email signing key more securely.  
  
Play around with "ykman" to configure touch/physical interaction policies for key usage.  
  
Supports other cryptographic interfaces,
such as "[OpenPGP card](https://en.wikipedia.org/wiki/OpenPGP_card)".

![bg right:30%](images/36-crypto_keys.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pixelmenschen (CC BY 2.0)" -->
## Moving on...

![bg right:30%](images/36-lock_screen.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pixelmenschen (CC BY 2.0)" -->
## TPMs / Secure enclaves
Used for a wide variety of tasks,
including "verified boot" and FDE.

![bg right:30%](images/36-lock_screen.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jason Hall (CC BY 2.0)" -->
## HSMaaS
Offered in most public clouds.  
  
Some argue against its value, but usage is required by security standards such as
[PCI DSS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard).  
  
Some legal jurisdictions make it appealing.

![bg right:30%](images/36-arecibo.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% A. Gerst, ESA (CC BY-SA 2.0)" -->
## SoftHSM and emulated TPMs
Perhaps you want to play around without access to real hardware?  
  
Useful in CI/CD pipelines and for testing.

![bg right:30%](images/36-space_face.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% David Leo Veksler (CC BY-SA 2.0)" -->
### What are you signing right now?
Your HSM may require a PIN, physical interaction and/or biometrics to perform operations.  
  
But what are you actually
signing / decrypting / authenticating?  

![bg right:30%](images/36-crypto_wallets.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Should you trust
**"battle-hardened software"** or a
**"secure black box"**?  
  
What about malware, key backups and
[bad randomness](https://en.wikipedia.org/wiki/ROCA_vulnerability)?  
  
Mayhaps both or neither.

![bg right:30%](images/36-monkey.jpg)
