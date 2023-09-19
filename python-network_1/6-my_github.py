#!/usr/bin/python3

"""import necessary modules"""
import requests
import sys

if __name__ == "__main__":
    """ Python script """
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )

    if response.status_code == 200:
        data = response.json()
        print(data.get("id"))
    else:
        print("None")
