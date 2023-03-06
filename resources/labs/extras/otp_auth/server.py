# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password hashing lab

# Lab program to serve gift suggestions with password protection

# Import standard library modules for reading data from environment variables, logging and
# selecting random words for gift advice
import logging as log
import datetime
import hashlib
import random
import os

log.basicConfig(format='%(levelname)s: %(message)s', level=log.INFO)

# Import third-party Flask module (used as web application server)
try:
    from flask import Flask, request, abort
except:
    log.error('Failed to import required third-party module "flask"')
    exit(1)

# Configure application log level
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

# Read password used to protect server from environment variable
if not 'SERVER_PASSWORD' in os.environ:
    log.error('Required environment variable "SERVER_PASSWORD" is not set')
    exit(1)
else:
    password = os.environ['SERVER_PASSWORD']


# Function used to generate a OTP password based on current date-time and specified secret value
def generate_otp(secret_value):
    log.info('Generating OTP based on current date, time and a secret value')

    # Always get current date and time in the UTC timezone to enable correct validation of OTPs
    # regardless of which timezone the client happens to be in. Present datetime in ISO 8601 format
    # with minute precision to allow some time drift between clients and servers
    current_datetime = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='minutes')

    # Concatenate current datetime with secret value and hash it using the MD5 algorithm
    secret_string_to_hash = f'{current_datetime}_{secret_value}'
    log.debug(f'Secret UTF-8 string used to generate OTP (MD5 hash): "{secret_string_to_hash}"')
    otp = hashlib.md5(secret_string_to_hash.encode()).hexdigest()
    log.debug(f'Generated OTP: "{otp}"')

    return otp


# Silly function used to generate dynamic server responses
def generate_gift_advice():
    log.debug('Generating gift/present advice')

    adjectives = ['scary', 'yellow', 'dubious', 'depressed', 'cheap', 'flamboyant', 'sleepy']
    nouns = ['panda', 'teapot', 'AI', 'skyscraper', 'penguin', 'skateboard', 'quelest', 'ball']

    random_adjective = random.choice(adjectives)
    random_noun = random.choice(nouns)
    gift_advice = f'Algorithm says: You should buy a {random_adjective} {random_noun}!\n'
    log.debug(f'Generated gift advice: {gift_advice}')

    return gift_advice


# Setup Flask web application/server and configure actions for endpoints/URL paths
app = Flask('server')

# Answer with 200 OK if "/health-check" is requested, used to determine when the service is online 
@app.route('/health-check')
def health_endpoint():
    return 'The web server is responding - looks like we are online!'


# Provide gift suggestions if path is requested and password header is included
@app.route('/version-1')
def get_gift_advice_v1():
    log.debug('Processing HTTP request to gift advice endpoint version 1')

    # Check if authentication header is included in the request
    if not 'X-Secret-Password' in request.headers:
        log.warning('Got request without the password header "X-Secret-Password" included')
        abort(401)

    request_password = request.headers['X-Secret-Password']

    # Compare request password with stored password 
    if request_password != password:
        log.warning('Got request with header "X-Secret-Password" not matching the server password')
        log.debug(f'Value of request header "X-Secret-Password" was "{request_password}"')
        abort(401)

    log.info('Successfully authenticated request using password - returning gift advice!')
    return generate_gift_advice()


# Provide gift suggestions if path is requested and one-time password header is included
@app.route('/version-2')
def get_gift_advice_v2():
    log.debug('Processing HTTP request to gift advice endpoint version 2')

    # Check if one-time password authentication header is included in the request
    if not 'X-OTP' in request.headers:
        log.warning('Got request without the password header "X-OTP" included')
        abort(401)

    request_otp = request.headers['X-OTP']

    # Compare request OTP against OTP generated on server
    if request_otp != generate_otp(password):
        log.warning('Got request with header "X-OTP" not matching the server generated OTP')
        log.debug(f'Value of request header "X-OTP" was "{request_otp}"')
        abort(401)

    log.info('Successfully authenticated request using OTP - returning gift advice!')
    return generate_gift_advice()
