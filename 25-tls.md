---
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Introduction to TLS"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to TLS in the practical cryptography course"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
# Transport Layer Security
### An introduction to SSL / TLS

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
Network traffic may be intercepted.  
  
Malicious actors can manipulate and
spy on sensitive communication.  
  
How can we protect it?

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Marcin Wichary (CC BY 2.0)" -->
**S**ecure **S**ockets **L**ayer was
introduced by Netscape in the late 90s
to enable e-commerce/"exciting things".  

Wraps existing clear text TCP protocols,
like HTTP and SMTP, with a layer of encryption.

Replaced by **T**ransport **L**ayer **S**ecurity,
properly standardized by the IETF.
  
Protects confidentiality and integrity
of network communication at the
OSI model's ["presentation layer"](https://en.wikipedia.org/wiki/OSI_model)
("application layer" in TCP/IP).

![bg right:30%](images/25-90s_tv.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## TLS typically use...
- X.509 for "identity validation"
- Asymmetric cryptography for key exchange
- Symmetric encryption for confidentiality
- Hashing for integrity protection

Different combinations algorithms
are known as "**cipher suites**".  

TLS 1.2 supports 37 different ones,
TLS 1.3 merely 5.

![bg right:30%](images/25-lake_street_bridge.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Adam Lusch (CC BY-SA 2.0)" -->
## Example cipher suites
```
TLS_RSA_EXPORT_WITH_RC4_40_MD5

TLS_DHE_RSA_WITH_AES_128_CBC_SHA256

TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305

TLS_GOSTR341112_256_WITH_NULL_GOSTR3411
```

![bg right:30%](images/25-lake_street_bridge.jpg)

---
## Configuring a web server
```
$ cat /etc/caddy/Caddyfile 

https://localhost {
  tls /etc/caddy/my_server.pem /etc/caddy/my_server-key.pem
  respond "Let me tell you a secret, friend!"
}
```

---
## Configuring a client
```python
#!/usr/bin/env python3
import requests

response = requests.get('https://localhost', verify='ca.pem')

print(response.text)
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
## What is "mTLS"?
In TLS, both connection peers
(client and server) may
present certificates.  

We call this "**m**utual **TLS**", AKA
"client-certificate authentication".

Can be used as replacement
for username \+ password login,
application can grab user identifier
from the certificate's **c**ommon **n**ame.

_(similar to "key authentication" in SSH)_

![bg right:30%](images/25-le_foron.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
### my\_ca/config.json
```json
[...]
"profiles": {
  "server": {
    "expiry": "2160h",
    "usages": [
      "signing",
      "key encipherment",
      "server auth"
    ]
  },
  "client": {
    "expiry": "8760h",
    "usages": [
      "signing",
      "key encipherment",
      "client auth"
    ]
  }
}
[...]
```

![bg right:30%](images/25-le_foron.jpg)

---
### Reconfigure Caddy for mTLS
```
$ cat /etc/caddy/Caddyfile 

https://localhost {
  tls /etc/caddy/my_server.pem /etc/caddy/my_server-key.pem {
    client_auth {
      mode require_and_verify
      trusted_ca_cert_file /etc/caddy/ca.pem
    }
  }
  respond "Let me tell you a secret, {tls_client_subject}!"
}
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
## Access denied!
```python
#!/usr/bin/env python3
import requests

response = requests.get(
    'https://localhost',
    verify='ca.pem'
)

print(response.text)
```

```
$ ./app.py

[...]
SSL: SSLV3_ALERT_BAD_CERTIFICATE
```

![bg right:30%](images/25-le_foron.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
### Configure client certificate
```python
#!/usr/bin/env python3
import requests

response = requests.get(
    'https://localhost',
    verify='ca.pem',
    cert=(
        'my_client.pem',
        'my_client-key.pem'
    )
)

print(response.text)
```

![bg right:30%](images/25-le_foron.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Guilhem Vellut (CC BY 2.0)" -->
## Access granted!
```
$ ./app.py

Let me tell you a secret,
CN=my_client,OU=User Support Team,
O=Department Of Labs,L=Stockholm,C=SE!
```

![bg right:30%](images/25-le_foron.jpg)

---
![bg center 60%](images/25-firefox_no_client_cert.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
Unfortunately, browsers typically don't
support directly importing PEM files
with the client certificate/key.

We need to package them into a
[PKCS #12 archive](https://en.wikipedia.org/wiki/PKCS_12) first.  
  
```
$ openssl pkcs12 \
	-in my_client.pem \
	-inkey my_client-key.pem \
	-export -out my_client.p12
```

![bg right:30%](images/25-battersea_power_station.jpg)

---
![bg center 65%](images/25-firefox_client_cert_list.png)

---
![bg center 75%](images/25-firefox_client_cert_imported.png)

---
![bg center 65%](images/25-firefox_client_cert_auth_select.png)

---
![bg center 65%](images/25-firefox_client_cert_authed.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
## Wrapping up
TLS provides a relatively simple method
for wrapping clear text protocols
in a "layer of encryption" and
enables mutual authentication.  

Supports different combinations of
algorithms using "cipher suites".

Several different versions exist,
avoid SSL and TLS version \<1.2.

Designed for TCP, use **DTLS** for UDP.  

![bg right:30%](images/25-cyberpunk.jpg)
