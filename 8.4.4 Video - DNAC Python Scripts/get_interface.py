import requests

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
