#!/usr/bin/python3

"""import necessary modules"""
import requests
import sys

if __name__ == "__main__":
    """requests library to send a POST request and the sys 
    library to read the command-line argument"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
