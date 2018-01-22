#!/bin/bash -e

TOKEN_DIR="/tmp/token"
TOKEN_FILE="/tmp/token/api_token"
OXIDIZED_CONFIG_FILE="/root/.config/oxidized/config"

# Check if there is a token file location.
if [ -d ${TOKEN_DIR} ]; then
    # If so.  Wait until the token file has been created
    while [ ! -f "$TOKEN_FILE" ]
    do
        sleep 1
    done
    # Read the token file
    for line in $(cat ${TOKEN_FILE})
    do
        break
    done
    # Write the token file to the config file
    sed -i "s/REPLACE WITH VALID TOKEN/$line/g" "${OXIDIZED_CONFIG_FILE}"
fi
