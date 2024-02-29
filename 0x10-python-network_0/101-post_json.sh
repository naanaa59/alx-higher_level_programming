#!/bin/bash
# This script POST the content of a json file
curl -s -d @"$2" "$1"
