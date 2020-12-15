# The requests library is used to communicate with vManage.
import requests
# pprint is used to make the output more readable.  It is mainly used for
# illustration, but is also uses for for debugging and verbose presentation.
import pprint
import urllib3

# disable_warning from urllib3 disables the warnings from using the self-signed
# certificate used in vManage by default.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# This is the information that we need to get to vManage and authenticate.  Although
# the port can be assumed, the username and password is needed to get an API token.
vmanage_host = 'devasc-sdwan-1.cisco.com'
vmanage_port = '443'
vmanage_username = 'devnetuser'
vmanage_password = 'RE!_Yw519_27'

# The base URL is simply the vManage's IP address/hostname in URL format with
# optional port number
base_url = 'https://%s:%s'%(vmanage_host, vmanage_port)

# The session token is retrieved from the path '/j_security_check'. Since we are using
# the requests library, the token is added to subsequent calls
login_action = '/j_security_check'

# The username and password are passed in as part of the payload of the API call.
login_data = {'j_username' : vmanage_username, 'j_password' : vmanage_password}

# Combining the base URL with the path renders the end point from when we get
# and API token.
login_url = base_url + login_action

