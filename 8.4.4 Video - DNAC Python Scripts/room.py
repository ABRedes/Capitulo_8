import requests

url = "https://webexapis.com/v1/rooms"

payload = {}
headers = {
  'Authorization': 'Bearer Y2IzMGFmOTItN2EzMC00ZDY3LTk0Y2QtNjQxZjc4ZDE2MWE2MjVmNDEyNWEtY2Rl_PF84_consumer'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))