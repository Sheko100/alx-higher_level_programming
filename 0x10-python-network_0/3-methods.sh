#!/bin/bash
# displays all HTTP methods the server will accept
curl -isX OPTIONS $1 | grep -e "Allow" | sed "s/Allow: //"
