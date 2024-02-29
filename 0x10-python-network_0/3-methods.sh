#!/bin/bash
# Sends an OPTIONS method http request to the passed host resource
curl -siX OPTIONS "$1" | grep 'Allow:' | sed 's/Allow: //'
