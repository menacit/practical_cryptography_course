# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password hashing lab

# Install required dependencies for client script
FROM docker.io/library/python:3.11.2-alpine
RUN pip install --no-cache-dir requests==2.28.2
COPY client.py /usr/src/
CMD ["/usr/local/bin/python", "-u", "/usr/src/client.py"]
