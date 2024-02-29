#!/bin/bash
# Sends an http request to the passed host and display only the status code
curl -so /dev/null -w '%{response_code}'  "$1"
