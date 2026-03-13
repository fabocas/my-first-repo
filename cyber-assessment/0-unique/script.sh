#!/bin/bash
file="$1"
sort "$1" | uniq -u