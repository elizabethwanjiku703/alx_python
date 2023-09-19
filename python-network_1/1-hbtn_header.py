#!/usr/bin/python3
""" Importing packages"""
import requests
import sys

if __name__ == "__main__":
    """ Write a Python script that shows X-Request_Id Header of an URL """
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


