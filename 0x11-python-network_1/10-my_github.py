#!/usr/bin/python3
""" Module that takes your Github credentials (username and password)
    and uses the Github API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    try:
        response = requests.get(
            'https://api.github.com/user', auth=(username, password))
        json_data = response.json()

        if 'id' in json_data:
            print(json_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
