#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password hashing lab

# Lab program to continuously request sensitive secret data from a web server and display it

# Import standard library modules for reading data from environment variables, logging and sleeping
import logging as log
import time
import os

log.basicConfig(format='%(levelname)s: %(message)s', level=log.INFO)

# Import third-party requests module (used for HTTP requests to the server)
try:
    import requests
except:
    log.error('Failed to import required third-party module "requests"')
    exit(1)

# Configure target address for HTTP requests
if not 'TARGET_SERVER_ADDRESS' in os.environ:
    log.error('Required environment variable "TARGET_SERVER_ADDRESS" is not set')
    exit(1)
else:
    target_url = 'http://{host}:5000/version-1'.format(host=os.environ['TARGET_SERVER_ADDRESS'])

# Configure password to include in HTTP header "X-Secret-Password"
if not 'SERVER_PASSWORD' in os.environ:
    log.error('Required environment variable "SERVER_PASSWORD" is not set')
    exit(1)
else:
    password = os.environ['SERVER_PASSWORD']

# Configure delay time between HTTP requests
if not 'REQUEST_DELAY_SECONDS' in os.environ:
    request_delay_seconds = 5
else:
    request_delay_seconds = int(os.environ['REQUEST_DELAY_SECONDS'])

# Configure script log level
if 'LOG_LEVEL' in os.environ and os.environ['LOG_LEVEL'] == 'INFO':
    log_level = log.INFO
elif 'LOG_LEVEL' in os.environ and os.environ['LOG_LEVEL'] == 'DEBUG':
    log_level = log.DEBUG
elif 'LOG_LEVEL' in os.environ:
    log.error('Value for environment variable "LOG_LEVEL" must be either "INFO" or "DEBUG"')
    exit(1)
else:
    log_level = log.INFO

log.getLogger().setLevel(log_level)

# Main application logic
log.info(f'Requesting gift advise from {target_url} every {request_delay_seconds} second(s)')
log.debug(f'Using password "{password}" for authenticating requests')

request_counter = 0
while True:
    request_counter += 1
    log.debug(f'Sending request number {request_counter} to {target_url}')

    try:
        # Perform HTTP GET request with the custom header "X-Secret-Password" set
        response = requests.get(target_url, headers={'X-Secret-Password': password}, timeout=3)
        if response.status_code != 200:
            raise Exception('Web server did not return status code 200 OK')
        # Assume that response body contains gift advice if server returns status code OK
        gift_advice = response.text

    except Exception as error_message:
        log.warning(f'Failed to request secret gift advice: {error_message} ({request_counter})')
    else:
        log.info(f'Got advice from server to buy a {gift_advice} as a present ({request_counter})')

    time.sleep(request_delay_seconds)
