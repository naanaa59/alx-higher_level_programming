#!/bin/bash
# This script takes in a URL, sends a request to that URL, size of the body of the response
curl -s -w '%{size_download}\n' -o /dev/null "$1"
