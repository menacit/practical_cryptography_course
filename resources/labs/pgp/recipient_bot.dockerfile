# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - PGP and HSM lab

# Install sq PGP CLI utility
FROM docker.io/library/ubuntu:22.04
RUN apt-get update \
	&& apt-get install --assume-yes --no-install-recommends sq \
	&& rm -rf /var/lib/apt-get/lists/* \
	&& apt-get autoremove --assume-yes
RUN mkdir -p /lab/recipient_private_keys /lab/recipient_certificates /lab/student_data/messages
VOLUME ["/lab/recipient_private_keys"]
COPY recipient_bot.sh /usr/local/bin
CMD ["/usr/bin/bash", "/usr/local/bin/recipient_bot.sh"]
