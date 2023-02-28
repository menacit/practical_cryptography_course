<!--
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course - Password hashing lab
-->

# Practical cryptography course - Password hashing lab

## Scenario description
Birthday presents for minions... ehm... coworkers, I mean, are every managers' worst nightmare.
Flowers? Chocolate? No no, that could be misinterpreted. A trip to Bali? Finance would go bonkers.  
  
In order to save its C-level staff from this recurring trauma, Xample Industries have created a web
service that provides appropriate gift advice by, allegedly, using "advanced AI machine learning".
During a last minute code review, security auditors found that the password used to protect this
highly sensitive information was stored in plain-text on the server's hard drive.  
  
Someone needs to fix this issue and that someone seems to be you.


## Learning objectives
Practical knowledge of one-way hash functions for storage/validation of passwords.


## Lab overview
The lab consist of two Python scripts that acts as a password protect web server and HTTP client.
The web server is a basic [Flask application](https://flask.palletsprojects.com/) that reads a
password from a text file. The client script uses the popular third-party Python module
["requests"](https://requests.readthedocs.io) to fetch data ("gift advice") from the server.  
  
Both of these software components are packaged as Docker/OCI container images and run using
[Docker Compose](https://docs.docker.com/get-started/08_using_compose/).  
  
In order to complete the lab, the student should implement password hashing in the web server.
All tools required to complete the assignment should be pre-installed on the student's lab system.


## Tasks

### Mandatory ("G")
- Modify the web server code to use SHA384 for protection of the stored password


### Meritorious ("VG")
- Implement some form of "password salting" 
- Add additional rounds of hashing in the server code to strengthen password protection


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information ("G"):
- Documentation of changes made in the web server's source code to implement password hashing
- Demonstration of how the implemented changes improve security of the service ("before and after")

Optionally, describe the security benefits of password salting in 500 characters or more ("VG)".  
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.
In addition to the report, all lab files that have been changed (scripts, configuration sets, etc.)
should be provided as a ZIP or GZIP archive.  
  
Send lab report and archive of changed files in an email to:  
[courses+crypto-pwd\_hash\_lab@%EMAIL_DOMAIN%](mailto:courses+pwd_hash_lab@%EMAIL_DOMAIN%)


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
dedicated network bridge called "lab-pwd\_hash". Traffic on the bridge can be displayed using CLI
tools or recorded for analysis in a GUI program such as [Wireshark](https://www.wireshark.org/).


### Links
- [Compose file V3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
- [Python documentation: "hashlib" module](https://docs.python.org/3.11/library/hashlib.html)
- [Tutorial - tcpdump HOWTO](https://danielmiessler.com/study/tcpdump/)
