#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Symmetric file encryption lab

# Lab program to generate/copy example data for backup source directory

set -o pipefail -o errexit

TARGET_DIRECTORY="${1}"
if [[ -z "${TARGET_DIRECTORY}" ]]; then
	TARGET_DIRECTORY="$(dirname -- "${0}")/backup_source"
fi

if ! [[ -d "${TARGET_DIRECTORY}" ]]; then
	echo "ERROR: Can't find target directory for generated test files \"${TARGET_DIRECTORY}\""
	exit 1
fi

echo "INFO: Copying system manual pages as example files to target directory"
cp -pr -- /usr/share/man "${TARGET_DIRECTORY}/manual_pages"

for SIZE in 10M 50M 200M; do
	echo "INFO: Creating easily compressable example file of size ${SIZE}"
	head --bytes "${SIZE}" /dev/zero > "${TARGET_DIRECTORY}/easily_compressable-${SIZE}.data"
	echo "INFO: Creating very random example file of size ${SIZE}"
	head --bytes "${SIZE}" /dev/urandom > "${TARGET_DIRECTORY}/very_random-${SIZE}.data"
done
