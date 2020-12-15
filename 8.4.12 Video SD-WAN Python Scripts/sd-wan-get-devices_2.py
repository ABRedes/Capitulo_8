# Create the requests session object
session = requests.session()

# We make a POST call of the URL and data from above.  If the response is in
# HTML, it means that a login error has occurred
login_response = session.post(url=login_url, data=login_data, verify=False)
if b'<html>' in login_response.content:
    print ("Login Failed")
    exit(1)

# The XSRF Token is used to prevent cross-site request forgery attacks and is
# required in vManage 19.X
xsrf_token_url = base_url + '/dataservice/client/token'
print(xsrf_token_url)
# Now GET the URL constructed above to retrieve the token.  If a successful
# return code is not received (i.e. 200), then an error was encountered
login_token = session.get(url=xsrf_token_url, verify=False)
if login_token.status_code == 200:
    if b'<html>' in login_token.content:
        print ("Login Token Failed")
        exit(1)

    session.headers['X-XSRF-TOKEN'] = login_token.content
