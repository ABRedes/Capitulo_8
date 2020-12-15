device_url = base_url + '/dataservice/device'

device_list = session.get(url=device_url, verify=False)
if device_list.status_code == 200:
    json_data = device_list.json()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint (json_data)
else:
    print (device_list.status_code)
    exit(1)
