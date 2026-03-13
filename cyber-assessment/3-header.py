#!/usr/bin/python3

from urllib import request
from sys import argv

response = request.urlopen(argv[1])

print(response.headers.get("X-Request-Id"))