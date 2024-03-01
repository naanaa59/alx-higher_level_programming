#!/usr/bin/python3
"""
    This script takes in a URL, sends a request to display a variable
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
