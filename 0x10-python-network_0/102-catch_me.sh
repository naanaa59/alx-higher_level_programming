#!/bin/bash
# This script makes a request to a URL that causes the server to respond a message "You got me!"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
