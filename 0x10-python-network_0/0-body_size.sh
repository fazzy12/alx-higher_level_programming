#!/bin/bash
# Script to send a request to a URL and display the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
