#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    aut = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", aut=auth)
    print(r.json().get("id"))
