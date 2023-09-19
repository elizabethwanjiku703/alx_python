#!/usr/bin/python3

"""import packages"""
import requests
import sys

if __name__ == "__main__":
    """ Get url and email command line argument"""
    url = sys.argv[1]
    email = sys.argv[2]

    """Create a dictionary with the email as a parameter"""
    data = {"email": email}

    """Send the POST request to the specified URL with the email parameter"""
    response = requests.post(url, data=data)

    """Display the body of the response"""
    print(response.text)
