---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Key attestation"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Demonstration of key attestation in practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
# Key attestation
### An adventure into X.509 and attestation

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
On an otherwise boring day, a new co-worker
ask you to sign a CSR.  
  
The certificate/key will be used for mTLS to
restrict access to The Super Sensitive Database.

You check the certificate subject/CN and
everything looks fine. Yet...

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
How can you be sure that another copy of the private key hasn't been saved/leaked?  
  
**Introducing key attestation.**

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
Method to validate that a (non-exportable)
key has been generated on the HSM.  
  
Vendor typically injects a key into HSM during manufacturing for signing of user generated keys.  
  
Third-parties can validate the
"attestation certificate"
(user generated public key signed by vendor key).

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
## Less talk, more demos!

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
## TODO list
- Ask co-worker to provide att. certificate
- Compare public key in CSR with public key in att. certificate
- Cryptographically validate att. certificate

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nikki Tysoe (CC BY 2.0)" -->
### Generating attestation certificate
```
$ ykman \
	piv keys attest 9a - \
	| tee bob_key_attest.crt

-----BEGIN CERTIFICATE-----
MIIDIDCCAg[...]igAwIBAgIQASCKKnz
MA0GCSqGSI[...]b3DQEBCwUAA4IBAQB
L2o5iekWDP[...]/fitZkP6L2xoF08Ss
qYr94bzO0e[...]i8pt+7XOA6GuvcTxK
IzMYtx270j[...]JCjZqOIzP52HLVuL3
CPqkcz0qen[...]WB9IMbjU8D1yCaj+1
-----END CERTIFICATE-----
```

![bg right:30%](images/40-space_invader.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nikki Tysoe (CC BY 2.0)" -->
### Exporting device-unique attestation CA
```
$ ykman \
	piv certificates export f9 - \
	| tee bob_yk_attest_ca.crt

-----BEGIN CERTIFICATE-----
MIIC+jCCAeKg[...]AwIBAgIJAPhUUgoBnzOkM
BAMMIFl1Ymlj[...]byBQSVYgUm9vdCBDQSBTZ
MDAwMFoYDzIw[...]NTIwNDE3MDAwMDAwWjAhM
dGVzdGF0aW9u[...]MIIBIjANBgkqhkiG9w0BA
Yuy5chbl+IiZ[...]j/3EviuaEaza/T2jnoWuS
0Ubv/FwK//RR[...]OjlBx6nuhxIZ9nomPVb57
-----END CERTIFICATE-----
```

![bg right:30%](images/40-space_invader.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
## TODO list
- ~~Ask co-worker to provide att. certificate~~
- Compare public key in CSR with public key in att. certificate
- Cryptographically validate att. certificate

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
### Comparing CSR with att. certificate
```
$ openssl \
	req -in bob.csr \
	-noout -pubkey \
	| sha256sum 

2cb1760a955ea5c4[...]f58b57cca15408bb

$ openssl \
	x509 -in bob_key_attest.crt \
	-noout -pubkey \
	| sha256sum

2cb1760a955ea5c4[...]f58b57cca15408bb
```

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
## TODO list
- ~~Ask co-worker to provide att. certificate~~
- ~~Compare public key in CSR with public key in att. certificate~~
- Cryptographically validate att. certificate

![bg right:30%](images/40-guard.jpg)

---
### Fetching root att. certificate
```
$ wget \
  --output-document root_yk_attest_ca.crt \
  https://developers.yubico.com/PIV/Introduction/piv-attestation-ca.pem
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
### Validating device-unique att. CA
```
$ openssl \
	verify \
	-CAfile root_yk_attest_ca.crt \
	bob_yk_attest_ca.crt 

bob_yk_attest_ca.crt: OK
```

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
### Validating att. certificate
```
$ cat \
	bob_yk_attest_ca.crt \
	root_yk_attest_ca.crt \
	> bob_yk_attest_ca_chain.crt

$ openssl \
	verify \
	-CAfile bob_yk_attest_ca_chain.crt \
	bob_key_attest.crt

bob_key_attest.crt: OK
```

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
## TODO list
- ~~Ask co-worker to provide att. certificate~~
- ~~Compare public key in CSR with public key in att. certificate~~
- ~~Cryptographically validate att. certificate~~

**Yatta yatta!**

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
If validation succeeded, it means:  
  
**A)** Key was generated on/by the YubiKey :D

**B)** Integrity of
attestation CAs, HSM or cryptography software
has been compromised :-/

![bg right:30%](images/40-abandoned_building.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
### Peaking into att. certificate
```
$ openssl x509 -in bob_key_attest.crt -text

[...]
Issuer: CN = Yubico PIV Attestation
Validity
    Not Before: Mar 14 00:00:00 2016 GMT
    Not After : Apr 17 00:00:00 2052 GMT
Subject: CN = YubiKey PIV Attestation 9a
[...]
X509v3 extensions:
    1.3.6.1.4.1.41482.3.3: 
        ...
    1.3.6.1.4.1.41482.3.7: 
        ...c..
    1.3.6.1.4.1.41482.3.8: 
        ..
[...]
```

![bg right:30%](images/40-abandoned_building.jpg)

---
> Extensions in the generated certificate:
> 1.3.6.1.4.1.41482.3.3:
> Firmware version, encoded as 3 bytes, like: 040300 for 4.3.0
> 1.3.6.1.4.1.41482.3.7:
> Serial number of the YubiKey, encoded as an integer.
> 1.3.6.1.4.1.41482.3.8:
> Two bytes, the first encoding pin policy and the second touch policy 
> [...]

— [YK PIV att. documentation](https://developers.yubico.com/PIV/Introduction/PIV_attestation.html).  

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
### Validating key usage restrictions
```
$ yk-attest-verify \
	piv \
	--allowed-pin-policies once,always \
	--allowed-touch-policies always \
	bob_key_attest.crt \
	bob_yk_attest_ca_chain.crt 

YubiKey PIV Attestation:
 - Key slot       : 9a
 - YubiKey Version: v5.4.3
 - Serial #       : 23316682
 - Formfactor     : USB-A Keychain
 - PIN Policy     : Once
 - Touch Policy   : Always

Attestation Policy Checks:
✔ All policy checks OK
```

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Johan Neven (CC BY 2.0)" -->
### Validating key usage restrictions
```
$ yk-attest-verify \
	piv \
	--allowed-pin-policies once,always \
	--allowed-touch-policies always \
	ada_key_attest.crt \
	ada_yk_attest_ca_chain.crt 

YubiKey PIV Attestation:
 - Key slot       : 9a
 - YubiKey Version: v5.4.3
 - Serial #       : 23316676
 - Formfactor     : USB-A Keychain
 - PIN Policy     : Once
 - Touch Policy   : Never

Attestation Policy Checks:
✖ Touch Policy 'Never' is not allowed
```

![bg right:30%](images/40-guard.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Nikki Tysoe (CC BY 2.0)" -->
### What if it was externally generated?
```
$ ykman \
	piv keys attest 9a - \
	| tee charlie_key_attest.crt

Error: Attestation failed.
```

![bg right:30%](images/40-space_invader.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Pelle Sten (CC BY 2.0)" -->
Many other use-cases for attestation.  
  
**Let this be a teaser.**

![bg right:30%](images/40-abandoned_building.jpg)
