# SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
# SPDX-License-Identifier: CC-BY-SA-4.0
# X-Context: Practical cryptography course - Password hashing lab

# Lab program to serve gift suggestions with password protection

# Import standard library modules for reading data from environment variables, logging and
# selecting random words for gift advice
import logging as log
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

# Load and configure password used to protect server
log.info('Reading password from "/etc/server_password.txt"')
try:
    with open('/etc/server_password.txt', 'r') as file_handle:
        # If there are white-space characters before or after the password string, remove them
        password = file_handle.readline().strip()
    if not password:
        raise Exception('Password file/first line is empty')

    log.debug(f'Password read from "/etc/server_password.txt" was "{password}"')

except Exception as error_message:
    log.error(f'Failed to read password from "/etc/server_password.txt": {error_message}')
    exit(1)


# Silly function used to generate dynamic server responses
def generate_gift_advice():
    log.debug('Generating gift/present advice')

    adjectives = ['scary', 'yellow', 'dubious', 'depressed', 'cheap', 'flamboyant', 'sleepy']
    nouns = ['panda', 'teapot', 'AI', 'skyscraper', 'penguin', 'skateboard', 'quelest', 'ball']

    random_adjective = random.choice(adjectives)
    random_noun = random.choice(nouns)
    gift_advice = f'{random_adjective} {random_noun}'
    log.debug(f'Generated gift advice: {gift_advice}')

    return gift_advice


# Setup Flask web application/server and configure actions for endpoints/URL paths
app = Flask('server')

# Answer with 200 OK if "/health-check" is requested, used to determine when the service is online 
@app.route('/health-check')
def health_endpoint():
    return 'The web server is responding - looks like we are online!'


# Provide gift suggestions if root of the web server is requested (URL path "/")
@app.route('/version-1')
def get_gift_advice():
    log.debug('Processing HTTP request to gift advice endpoint')

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

    log.info('Successfully authenticated request - returning gift advice!')
    return generate_gift_advice()
