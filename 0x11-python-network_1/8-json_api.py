#!/usr/bin/python3
"""
    Takes in a letter, sends POST request to url with letter as param
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {"q": letter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print(f"[{resp.get('id')}] {resp.get('name')}")
    except ValueError:
        print("Not a valid JSON")
