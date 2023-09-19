"""importing request package"""
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")
"""return response object"""

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
