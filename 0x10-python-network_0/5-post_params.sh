#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the respons
curl -sX POST -H "Content-Type: application/json" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' $1