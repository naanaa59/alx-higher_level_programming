#!/bin/bash
# This script POST the content of a json file
curl -s --json @"$2" "$1"
