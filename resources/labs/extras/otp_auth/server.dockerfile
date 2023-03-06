# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password hashing lab

# Install required dependencies for runtime healthcheck and web server application
FROM docker.io/library/python:3.11.2-alpine
RUN apk add --update-cache curl
RUN pip install --no-cache-dir Flask==2.2.2 
COPY server.py /usr/src/
CMD ["/usr/local/bin/flask", "--app", "/usr/src/server.py", "run", "--host", "0.0.0.0"]
HEALTHCHECK \
	--interval=5s --timeout=2s --retries=10 \
	CMD ["/usr/bin/curl", "--fail", "http://127.0.0.1:5000/health-check"]
