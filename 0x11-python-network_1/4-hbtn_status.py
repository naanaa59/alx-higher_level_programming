#!/usr/bin/python3
"""
    requests model
"""

import requests


if __name__ == '__main__':
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {html.text.__class__}")
    print(f"\t- content: {html.text}")
