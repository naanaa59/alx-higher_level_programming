#!/bin/bash
# This script sets values on the body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
