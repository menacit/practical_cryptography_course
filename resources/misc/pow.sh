#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Proof of Work

# Lab program to demonstrate Proof of Work (PoW)

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
