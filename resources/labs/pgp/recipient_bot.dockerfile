# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - PGP and HSM lab

# Install sq PGP CLI and tool to verify Yubikey attestation certificates
FROM docker.io/library/ubuntu:22.04
ARG ATTEST_VERSION=0.0.9 
ARG ATTEST_URL=https://github.com/joemiller/yk-attest-verify/releases/download/v${ATTEST_VERSION}
ARG ATTEST_CHECKSUM=24d08e59c62dee8d42f8853719d1e7bb1496239e0de030b4a0bfab9dde90955b

ADD ${ATTEST_URL}/yk-attest-verify_${ATTEST_VERSION}_linux_amd64.deb /tmp/yk-attest-verify.deb
RUN echo "${ATTEST_CHECKSUM} /tmp/yk-attest-verify.deb" | sha256sum --check
RUN apt-get update \
	&& apt-get install --assume-yes --no-install-recommends sq /tmp/yk-attest-verify.deb \
	&& rm -rf /var/lib/apt-get/lists/* \
	&& apt-get autoremove --assume-yes

RUN mkdir -p /lab/recipient_private_keys /lab/recipient_certificates /lab/student_data/messages
VOLUME ["/lab/recipient_private_keys"]
COPY recipient_bot.sh /usr/local/bin
CMD ["/usr/bin/bash", "/usr/local/bin/recipient_bot.sh"]
