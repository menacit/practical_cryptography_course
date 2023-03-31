# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password cracking lab

# Install John The Ripper package from Kali Linux repository
FROM docker.io/kalilinux/kali-last-release

RUN apt-get update \
	&& apt-get install --assume-yes --no-install-recommends john \
	&& rm -rf /var/lib/apt-get/lists/* \
	&& apt-get autoremove -y

RUN useradd --home-dir /data --create-home --shell /usr/bin/bash cracker
VOLUME ["/data"]
WORKDIR /data

USER cracker
ENTRYPOINT ["/usr/sbin/john"]
