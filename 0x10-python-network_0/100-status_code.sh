#!/bin/bash
# This script takes in a URL, sends a request to that URL,  status code of the response
curl -s -w '%{http_code}\n' -o /dev/null "$1"
