import requests

uri = "https://devasc-dnacenter-1.cisco.com"

response = requests.get(uri, verify=False)

print(response.text)