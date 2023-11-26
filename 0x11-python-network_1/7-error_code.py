#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and
displays the body of the response. If the HTTP status code is greater
than or equal to 400, prints: "Error code:" followed by the value of
the HTTP status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Error code: {errh.response.status_code}")
    except Exception as err:
        print(err)
