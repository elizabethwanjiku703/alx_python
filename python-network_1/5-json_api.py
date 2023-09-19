#!/usr/bin/python3

"""import necessary modules"""
import requests
import sys

def search_user(letter):
    """Parameter - search_user function"""
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, params=params)
    
    try:
        """Display id and name is json is valid"""
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

search_user(letter)


if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

search_user(letter)



