#!/usr/bin/python3
"""
    This script takes in a URL and an email, sends a POST request
    to the passed URL
    with the email as a parameter, and displays the body of the response
"""
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
