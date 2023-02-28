# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - X.509/TLS lab

# Install the "fortune" utility and setup a loop to generate a Startrek quote every second
FROM docker.io/library/alpine:3.17.1
RUN apk add --update-cache fortune
CMD \
	echo "Starting top-secret content generation loop..."; \
	while sleep 1; do \
		fortune startrek | tr '\t' ' ' | tr '\n' ' ' | tr -s ' ' > /output/secret.txt; \
		echo >> /output/secret.txt; \
	done
