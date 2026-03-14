#!/usr/bin/python3
import requests
from sys import argv

username = argv[1]
password = argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, password))

data = response.json()

print(data.get("id"))