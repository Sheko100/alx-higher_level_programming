#!/bin/bash
# displays the body of the response
curl -sX POST -H "Content-Type: application/json" $1 -d $2 
