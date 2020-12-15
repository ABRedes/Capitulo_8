import requests
import json

baseUri = "http://localhost:58000/api/v1"

# API call to request service ticket
headers = {"Content-Type": "application/json"}
data = json.dumps({"username": "admin", "password": "admin123!"})
resp = requests.post(baseUri+"/ticket", data=data, headers=headers)

print(resp.status_code)
result = resp.json()
print(result)

ticket = result["response"]["serviceTicket"]
print(ticket)

# API call to request list of network devices
headers = {"X-Auth-Token": ticket }
resp = requests.get(baseUri+"/network-device", headers=headers)

print (resp.status_code)
result = resp.json()
print (json.dumps(result, indent=4))

for i in result["response"]:
    print(i["hostname"]+" "+i["serialNumber"]+" "+i["softwareVersion"])
