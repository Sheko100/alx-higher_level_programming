#!/bin/bash
# Counts the http request body bytes
host=$1
curl -s "$host" | wc -c;
