---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
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
  
Malicious actors can manipulate and spy on sensitive communication.  

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
SSL was introduced by Netscape to enable e-commerce.  
  
Replaced by properly standardised TLS after SSLv3.  
  
Ensures confidentiality and integrity of network communication at the "session layer".  
  
Used to secure cleartext protocols such as HTTP, SMTP, FTP, etc.

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
## TLS typically use...
- X.509 for "identity validation"
- Asymmetric encryption for key exchange
- Symmetric encryption for confidentiality
- Hashing for integrity protection

Different combinations of these are known as "cipher suites".

![bg right:30%](images/25-cyberpunk.jpg)

---
## Example cipher suites
```
TLS_RSA_WITH_AES_128_CBC_SHA256

TLS_RSA_WITH_AES_256_GCM_SHA384

SSL_CK_DES_192_EDE3_CBC_WITH_SHA
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
## What is "mTLS"?
Mutual TLS.  

Both connection peers (client and server) may present certificates.  
  
Sloppily called "client certificate authentication".

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Bret Bernhoft (CC0 1.0)" -->
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

![bg right:30%](images/25-cyberpunk.jpg)

---
### Reconfigure Caddy for mTLS
```
$ ls /etc/caddy
Caddyfile  ca.pem  my_server-key.pem  my_server.pem

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

$ sudo systemctl restart caddy.service
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kristoffer Trolle (CC BY 2.0)" -->
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

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kristoffer Trolle (CC BY 2.0)" -->
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

![bg right:30%](images/25-cyberpunk.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kristoffer Trolle (CC BY 2.0)" -->
## Access granted!
```
$ ./app.py

Let me tell you a secret, CN=my_client,
OU=User Support Team, O=Department Of Labs,
L=Stockholm,C=SE!
```

![bg right:30%](images/25-cyberpunk.jpg)

---
![bg center 60%](images/25-firefox_no_client_cert.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Kristoffer Trolle (CC BY 2.0)" -->
Hold onto your horses! We need to package the certificate and key into a
[PKCS #12 archive](https://en.wikipedia.org/wiki/PKCS_12).  
  
```
$ openssl pkcs12 \
	-in my_client.pem \
	-inkey my_client-key.pem \
	-export -out my_client.p12
```

![bg right:30%](images/25-cyberpunk.jpg)

---
![bg center 65%](images/25-firefox_client_cert_list.png)

---
![bg center 75%](images/25-firefox_client_cert_imported.png)

---
![bg center 65%](images/25-firefox_client_cert_auth_select.png)

---
![bg center 65%](images/25-firefox_client_cert_authed.png)
