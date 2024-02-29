#!/bin/bash
# This script display all the methods supported by the server
curl *s --head "$1" | grep "Allow" | cut -c 8-
