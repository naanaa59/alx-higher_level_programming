#!/bin/bash
# This script POST the content of a json file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
