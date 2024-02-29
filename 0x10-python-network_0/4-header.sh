#!/bin/bash
# Sends 'X-School-User-Id' header with 98 as a value to the passed host
curl -sH "X-School-User-Id: 98" "$1"
