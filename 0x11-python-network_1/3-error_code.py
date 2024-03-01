#!/usr/bin/python3
""" This is script that takes in a URL;
    sends a request to the URL
    displays the body of the response
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print('Error code:', err.code)
