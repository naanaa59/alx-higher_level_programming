#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -W '%{size_download}\n' -o /dev/null "$1"

