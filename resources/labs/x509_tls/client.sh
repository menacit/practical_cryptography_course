#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - X.509/TLS lab

# Lab program to continuously request sensitive secret data from a web server and display it

# Read runtime options from environment variables and validate that they are set correctly
if [[ -z "${TARGET_SERVER_ADDRESS}" ]]; then
	echo 'ERROR: Required environment variable "TARGET_SERVER_ADDRESS" is not configured'
	exit 1
else
	TARGET_URL="http://${TARGET_SERVER_ADDRESS}:8080/"
fi

if [[ -z "${REQUEST_DELAY_SECONDS}" ]]; then
	REQUEST_DELAY_SECONDS='5'
fi

# Main application logic - continuously perform requests to get information from a web server
echo "INFO: Requesting top-secret data from ${TARGET_URL} every ${REQUEST_DELAY_SECONDS} second(s)"

REQUEST_COUNTER='0'
while true; do
	REQUEST_COUNTER="$(( REQUEST_COUNTER + 1 ))"
	echo "INFO: Requesting top-secret quote number ${REQUEST_COUNTER}..."

	# Perform request against HTTP server and print the response
	curl \
		--fail --silent --show-error \
		--connect-timeout 3 \
		"${TARGET_URL}"

	# Display error message if curl executed unsuccessfully (exit code other than 0)
	if [[ "${?}" == "0" ]]; then
		echo 'INFO: Successfully fetched top-secret quote!'
	else
		echo "ERROR: Failed to request a top-secret quote from ${TARGET_URL}"
	fi

	sleep "${REQUEST_DELAY_SECONDS}"
done
