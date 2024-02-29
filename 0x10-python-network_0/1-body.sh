#!/bin/bash
# Prints the content of the host resource path passed if the status code is 200
curl -sIL "$1" | grep -q '200 OK' && curl -sL "$1"
