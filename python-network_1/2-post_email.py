#!/usr/bin/python3
"""Import the packages"""
import requests
import sys

"""Send a POST request"""
def send_post_request(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

if __name__ ==  '__main__':
    """passed URL with the email as a parameter"""
    url = sys.argv[1]
    email = sys.argv[2]
    print(f"Your email is: {email}")
    
    """displays the body of the response"""
    response_body = send_post_request(url, email)
    print(response_body)
