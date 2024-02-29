#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me using PUT method
curl -LX PUT -b "user_id=989" http://0.0.0.0:5000/catch_me
