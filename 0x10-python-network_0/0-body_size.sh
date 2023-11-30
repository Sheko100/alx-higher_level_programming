#!/bin/bash
# Counts the http request body bytes
curl -s "$1" | wc -c;
