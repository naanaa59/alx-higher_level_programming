#!/usr/bin/python3
"""
    This script fetches an URL with urllib
"""

import urllib.request


if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        type_c = type(content)
        utf = content.decode('utf-8')
    print(f"Body response:\n\t- type: {type_c}\n\t\
- content: {content}\n\t- utf8 content: {utf}")
