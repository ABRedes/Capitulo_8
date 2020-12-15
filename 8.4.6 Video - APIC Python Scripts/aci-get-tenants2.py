
def get_tenants():
    """ Get Tenants """

    token = apic_login()
    try:
        response = requests.get(
            url=APIC_URL+"/api/node/class/fvTenant.json",
            headers={
                "Cookie": "APIC-cookie=" + token,
                "Content-Type": "application/json; charset=utf-8",
            },
            verify=False
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print("HTTP Request failed")
