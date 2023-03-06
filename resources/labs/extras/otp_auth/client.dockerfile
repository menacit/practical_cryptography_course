# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - One-time password authentication lab

# Install required dependencies for client script
FROM docker.io/library/alpine:3.17.1
RUN apk add --update-cache bash coreutils curl curl-doc mandoc
COPY client.sh /root/
CMD ["/bin/bash", "/root/client.sh"]
