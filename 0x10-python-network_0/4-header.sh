#!/bin/bash
# Send a GET request with custom header using curl and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
