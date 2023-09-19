#!/usr/bin/python3
""" Importing the Packages"""
import requests
import sys

url = sys.argv[1]
""" The url to connect to the Packages"""
response = requests.get(url)
request_id = response.headers["X-Request-Id"]
print(request_id)
