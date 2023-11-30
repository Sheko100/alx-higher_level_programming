#!/bin/bash
# displays only the status code of the response
curl -sw '%{http_code}\n' -o /dev/null "$1"
