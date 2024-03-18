<!--
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course - X.509/TLS lab
-->

# Practical cryptography course - X.509/TLS lab

## Scenario description
Examplify Inc. has developed a web service that distributes inspiring and motivating quotes to
employees. Someone in HR claims that this will greatly boost their moral and productivity.
  
The wisdom provided by the service is considered a highly valuable company secret and the
potential consequences if leaked dire - yet the developers didn't think to implement authentication
nor network encryption. You've been tasked to harden the web service and ensure future prosperity.


## Learning objectives
Practical knowledge of using a X.509 certificate authority and TLS to secure network communication.


## Lab overview
The lab consist of a bash script that runs the [curl HTTP client](https://curl.se/) in a loop to
continuously request the quote page from a [nginx web server](https://nginx.org/en/). Both of these
software components (and a quote generation script) are packaged as Docker/OCI container images and
run using [Docker Compose](https://docs.docker.com/get-started/08_using_compose/).  
  
In order to complete the lab, the student should setup a X.509 certificate authority, modify the
client script/web server configuration to use HTTPS and mutual TLS authentication. All tools
required to complete the assignment should be pre-installed on the student's lab system. 


## Tasks

### Mandatory ("G")
- Setup a X.509 CA using the "easy-rsa" utility (version >3)
- Generate and sign a "server certificate" for the web server
- Generate and sign a "client certificate" for the client script
- Configure web server to support HTTPS, trust the CA and require client certificate authentication
- Configure client script to use HTTPS, trust the CA and authenticate using the client certificate


### Meritorious ("VG")
- Generate and configure usage of a certificate revocation list for the client/server
- Configure client and server to enforce usage of TLS version 1.2 or later
- Configure web server to log which client certificate ("CN") is used to request resources


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information ("G"):
- Description of which programs/commands were used to generate certificates
- Documentation of changes to the client script and server configuration 
- Demonstration of how the implemented changes improve security of the service ("before and after")
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.
In addition to the report, all lab files that have been changed (scripts, configuration sets, etc.)
should be provided as a ZIP or GZIP archive.  
  
Upload lab report and archive of changed files to %REPORT_TARGET%.


## Guidance and resources

### "easy-rsa" not included in path
The certificate authority utility "easy-rsa" should be pre-installed on the student's lab system.
It may however not be automatically included in the shell executable path. The utility can be used
by specifying the full script path, as seen in the example below:

```
$ /usr/share/easy-rsa/easyrsa help
```


### Sharing certificate files with containers
In order to enable sharing of files, like certificates and keys, with the client/server containers,
the directories "server\_share" and "client\_share" exist in the lab directory. These are
bind-mounted to "/share" in the containers, were they can be utilized by curl/nginx. For details,
check the "docker-compose.yml"-file.


### Testing changes with Docker Compose
The content generator, web server and client script are packaged as containers and executed using
[Docker Compose](https://docs.docker.com/get-started/08_using_compose/). In order to quickly test
changes and monitor execution status (logs, error codes, etc.) of scripts/configuration, students
can execute the "docker compose up --build" command, review output and press Ctrl+C to stop the
containers/exit.


### Validating compose file
Docker Compose declares its environment configuration in a file called "docker-compose.yml".
During the lab, students will be required to change this file in order to mount certificates/keys
in containers and similar.  
  
The [YAML format](https://en.wikipedia.org/wiki/YAML) used in the configuration file is notoriously
picky about indentation levels (tabs and spaces). In order to detect faulty syntax and formatting
issues, the "yamllint" program/command can be utilized. A text editor that helps with indentation
is also highly recommended.


### Monitoring network traffic
In order to aid the process of debugging or producing demonstrations of implement changes, network
traffic between the client and bridge can be sniffed/intercepted. Docker Compose creates a
dedicated network bridge called "lab-x509\_tls". Traffic on the bridge can be displayed using CLI
tools or recorded for analysis in a GUI program such as [Wireshark](https://www.wireshark.org/).


### Links
- [Documentation - Easy-RSA 3](https://easy-rsa.readthedocs.io/en/latest/)
- [Compose file V3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
- [Tutorial - tcpdump HOWTO](https://danielmiessler.com/study/tcpdump/)
- [nginx "http\_ssl\_module" reference](https://nginx.org/en/docs/http/ngx_http_ssl_module.html)
