#!/bin/bash
# Description: Makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a message.
curl -sX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
