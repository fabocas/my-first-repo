#!/bin/bash

if [ $# -eq 0]; then
	echo "Usage: $0 list"
	exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
	echo "file doesnt exist: $file"
	exit 1
fi




sort "$file" | uniq -u