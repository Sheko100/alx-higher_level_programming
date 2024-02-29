#!/bin/bash
# Prints the Content-Length header value of the passed host root doc
curl -sI "$1" | grep 'Content-Length: ' | grep -o '[0-9]*'
