#!/usr/bin/python3

"""import packages"""
import requests
import sys

if __name__ == "__main__":
    """Get the url from the command line argument"""
    url = sys.argv[1]

    """Send the request to the specified url and display body of the resposonse"""
    response = requests.get(url)
    print(response.text)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
