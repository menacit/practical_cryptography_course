#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password cracking lab

# Simple wrapper script to execute John The Ripper using Docker.

# If image is not already available locally, build it before running it.
if [[ -z "$(docker image ls --quiet jtr_image)" ]]; then
	docker build -t jtr_image:v1 -f jtr_image.dockerfile .
fi

# Mount current working directory (hopefully containing shadow file, word list etc.)
# to "/data" inside the container. Also specify JtR configuration file as "/data/john.conf".
docker run --rm --tty --interactive --volume "${PWD}:/data" jtr_image:v1 --config=john.conf ${@}
