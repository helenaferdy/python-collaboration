import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)


def login():
    client_id = "8smzjznfz8vmrm7qcft458x2"
    client_secret = "uqya83hAxn8R6S9vqZjMYW82"
    url = (f"https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}")
    headers = {"Accept": "application/json"}

    try:
        post = requests.post(url, headers=headers, timeout=3, verify=False)
        result = post.json()["access_token"]
        return result
    except:
        return "err"


def hello():
    token = "Bearer " + login()
    url = ("https://api.cisco.com/hello")
    headers = {"Accept": "application/json",
               "Authorization": token}

    try:
        post = requests.get(url, headers=headers, timeout=3, verify=False)
        result = post.json()["helloResponse"]["response"]
        return result
    except:
        return "err"

