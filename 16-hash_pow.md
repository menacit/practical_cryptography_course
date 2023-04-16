---
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Proof of Work"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Usage of cryptographic hashing for PoW"
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
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
# Proof of Work
### An introduction of hashing for PoW

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
Why is email spam a problem?  
  
Anyone can send anyone a message at (almost) zero cost.

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
Couldn't we just charge a tiny fee per message?  
  
How would you even implement that?  
  
Any other ways we could introduce cost?

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
Computations require processing.  
  
Processing requires harwdare and electricity.  
  
Hardware and electricity ain't free!

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
Cryptographic hash functions require quite a bit of CPU cycles.  
  
How can we prove that the user has wasted processing power on hashing?

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
Let's steal a few tricks from hash-based authentication!

![bg right:30%](images/16-server_rack.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
**Sender:** I got some email for you!  
  
**Receiver:** Hmm, hash some text prefixed with "fiskburk" that results in a hash ending with "ff".
  
**Sender:** If I hash "fiskburk24077-29047-32326" I get a hash ending with "ff".  

**Receiver:** I get the same result - handover that email, will you?

![bg right:30%](images/16-server_rack.jpg)

---
### resources/misc/pow.sh
```
#!/usr/bin/env bash

# Validate that at least two command line arguments are provided
if [[ -z "${2}" ]]; then
	echo "Usage: ${0} <PREFIX_SEED> <EXPECTED_SUFFIX>"
	exit 1
fi

PREFIX_SEED="${1}"
EXPECTED_SUFFIX="${2}"

# Loop until solution for PoW is found
time while true; do
	# Grab some random data to include in hash calculation
	INPUT_DATA="${RANDOM}-${RANDOM}-${RANDOM}"

	# Hash specified seed together with random input data, only include hash from output
	HASH="$(echo -n ${PREFIX_SEED} ${INPUT_DATA} | sha256sum | cut -d ' ' -f 1)"

	# If the suffix of the generated hash matches the specified suffix, challenge is solved
	if [[ "${HASH}" == *${EXPECTED_SUFFIX} ]]; then
		echo "${EXPECTED_SUFFIX}: sha256(${PREFIX_SEED} + ${INPUT_DATA}) == ${HASH}"
		# Stop loop once finished
		break
	fi
done
```

---
```
$ resources/misc/pow.sh
Usage: resources/misc/pow.sh <PREFIX_SEED> <EXPECTED_SUFFIX>

$ resources/misc/pow.sh "asdasdasdasd" "ff"

ff: sha256(asdasdasdasd + 16083-12281-837) == d60ee[...]3b13e1ff
real	0m0.138s

$ resources/misc/pow.sh "asdasdasdasd" "fff"

fff: sha256(asdasdasdasd + 22132-31048-7135) == 3be[...]37371fff
real	0m22.333s

$ resources/misc/pow.sh "asdasdasdasd" "ffff"

ffff: sha256(asdasdasdasd + 19378-5998-4075) == fb8[...]370ffff
real	1m23.770s
```

---
<!-- _footer: "%ATTRIBUTION_PREFIX% ORNL (CC BY 2.0)" -->
## Other use-cases
- Online bruteforce prevention
- Alternative to captcha
- Crypto currencies

Whatever you can imagine!

![bg right:30%](images/16-server_rack.jpg)

