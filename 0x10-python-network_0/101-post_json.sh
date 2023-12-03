#!/bin/bash
# displays the body of the response
curl -s -H "Content-Type: application/json" -H "Accept: application/json" "$1" -d @"$2"
