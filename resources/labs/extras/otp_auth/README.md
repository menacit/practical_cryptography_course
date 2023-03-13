<!--
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course - One-time password authentication lab
-->

# Practical cryptography course - One-time password authentication lab

## Learning objectives
Practical knowledge of one-way hash functions for proof of knowledge.


## Lab overview
The lab consist of a Python web application that exposes sensitive information and a client bash
script that continuously tries to fetch it using the [curl HTTP client](https://curl.se/).  
  
Both of these software components are packaged as Docker/OCI container images and run using
[Docker Compose](https://docs.docker.com/get-started/08_using_compose/).  
  
In order to complete the lab, the student should modify the client script to support authenticated
requests against the "/version-2" endpoint.


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information:
- Documentation of changes made in the client script source code to use "version-2" authentication
- Demonstration of how the implemented changes improve security of the service ("before and after")

Optionally, describe security weaknesses/attacks/design flaws affecting the "version-2"
authentication mechanism.  
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.
In addition to the report, all lab files that have been changed (scripts, configuration sets, etc.)
should be provided as a ZIP or GZIP archive.  
  
Send lab report and archive of changed files in an email to:  
[courses+crypto-otp\_auth\_lab@%EMAIL_DOMAIN%](mailto:courses+crypto-otp_auth_lab@%EMAIL_DOMAIN%)


## Guidance and resources

### Hash representation and comparison
Cryptographic hashes can be represented in several different ways, but the most common method is as
hexadecimal encoded strings ("hexdigest"). When hashing user input for comparison against a stored
password hash, make sure that the same representation is used.  
  
In order for two cryptographic hashes to be equal, exactly the same data should be provided as
input to the hash function. When hashes are produced using text files/command output as input,
hidden characters such as spaces, tabs and trailing newlines/carriage return will affect resulting
hash value.


### Testing changes with Docker Compose
The web server and client application are packaged as containers and executed using
[Docker Compose](https://docs.docker.com/get-started/08_using_compose/). In order to quickly test
changes and monitor execution status (logs, error codes, etc.) of code/configuration, students can
execute the "docker compose up --build" command, review output and press Ctrl+C to stop the
containers/exit.


### Monitoring network traffic
In order to aid the process of debugging or producing demonstrations of implement changes, network
traffic between the client and bridge can be sniffed/intercepted. Docker Compose creates a
dedicated network bridge called "lab-otp\_auth". Traffic on the bridge can be displayed using CLI
tools or recorded for analysis in a GUI program such as [Wireshark](https://www.wireshark.org/).


### Links
- [Compose file V3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
- [Python documentation: "hashlib" module](https://docs.python.org/3.11/library/hashlib.html)
- [Tutorial - tcpdump HOWTO](https://danielmiessler.com/study/tcpdump/)
