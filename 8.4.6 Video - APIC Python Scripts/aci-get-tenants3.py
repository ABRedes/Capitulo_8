def get_devices():
    """ Get Devices """

    token = apic_login()
    try:
        response = requests.get(
                  url=APIC_URL+"/api/node/class/topology/pod-1/topSystem.json",
                  headers={
                    "Cookie": "APIC-cookie=" + token,
                    "Content-Type": "application/json; charset=utf-8"
                          },
                  verify=False)
        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print("HTTP Request failed")

