#!/usr/bin/python3
"""
Send a request to a URL and display the body of the response
Handle urllib.error.HTTPError exceptions and print the HTTP status code
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')

            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
