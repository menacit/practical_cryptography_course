---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Attacking Net-NTLM"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "An introduction to techniques for attacking Net-NTLM authentication"
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
# Attacking Net-NTLM
### Abusing protocol design flaws 

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Proof of Knowledge is used in many network authentication proctols.  
  
Was especially popular before SSL/TLS became commonly used.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
## Meet NTLMv1 / NTLMv2
Authentication mechanism popular in
Windows environments.  
  
Provides seamless authentication for access to file shares, internal web applications, etc.  
  
Relies on challenge/response to avoid sending credentials in cleartext.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
**Wait a second - wasn't "NTLM"**
**used for password hashing?**

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Well, yes. It's confusing.  
  
**NTMLM / NTHash**: Password storage.  
  
**NTLMv1 / NTLMv2**: Network authenticaiton.  
  
To keep things simple, usually called
**Net-NTLMv1 / Net-NTLMv2**.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Authentication flow:  Net-NTLMv1
1. User connects to network server
2. Server responds with eight random bytes as an authentication challenge 
3. User takes their password hash, splits it up and use it as keys to DES encrypt the challenge
4. Server takes stored password hash for user and performs the same procedure
5. If client challenge response matches server generated result, consider user authenticated

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### Authentication flow:  Net-NTLMv2
1. User connects to network server
2. Server responds with eight random bytes as a "server challenge"
3. User generates eight random bytes as a "client challenge" 
3. User responds with ~md5(password hash + server/client challenge) and client challenge
4. Server calculate ~md5(stored password hash + server/client challenge)
5. If client response matches server generated result, consider user authenticated

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
**Hmmm, doesn't seem right?**

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
We just turned the password hash into a
password equivalent.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Furthermore, eight random bytes, DES and MD5 doesn't sound like a solid foundation.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
At least we can't just sniff network traffic and reuse the client response for impersonation.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Let me introduce you to
**"NTLM relaying attacks"**.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
I mentioned the
**seamless authentication** thing, right?  
  
Server challenge doesn't actually contain any information about the server's identity.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### NTLM relaying attack
1. Attacker sets up malicious website
2. Victim user connects to malicious site
3. Attacker connects to target server
4. Target server returns challenge

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
### NTLM relaying attack
5. Attacker website returns the same challenge to the victim user
6. Victim user generates challenge response
7. Attacker takes response from victim user and reuse it against the target server
8. Target server validates that challenge response, attacker is authenticated as victim user.

![bg right:30%](images/33-mural.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% William Warby (CC BY 2.0)" -->
Doesn't necessarily require user interaction -
Windows ~~loves~~ likes to do it by itself!  
  
If you wanna play around, check out
["responder" on GitHub](https://github.com/lgandx/Responder).

![bg right:30%](images/33-mural.jpg)
