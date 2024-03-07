#!/bin/bash

# Check if a file name is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <requirements.txt>"
    exit 1
fi

# Assign the file name to a variable
FILENAME="$1"

# Check if the file exists
if [ ! -f "$FILENAME" ]; then
    echo "File not found: $FILENAME"
    exit 2
fi

# Extract packages and versions, then find duplicates
awk -F'==' '{print $1}' "$FILENAME" | uniq -d | while read -r package; do
    echo "Duplicate package found: $package"
    grep "^$package==" "$FILENAME"
    echo ""
done
