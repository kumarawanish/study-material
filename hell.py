import requests
import json

print(4444444444)
post_url = "https://cac-api.cashfree.com/cac/v1/authorize"
PROXY_URL = "http://10.1.3.22/proxy"
CLIENTID = 'CF64427YUUYMGV6PSYIUMI'
CLIENTSECRET = 'a695dd78344705a655522b9ec7c3af46d6443d7d'
headers = {'X-Client-Id': CLIENTID, 'X-Client-Secret' : CLIENTSECRET}
req = None
#        req = requests.post(post_url, headers=headers)
try:
    req = requests.post(
        url = PROXY_URL,
        data = json.dumps(dict(
            url = post_url,
            method = "POST",
            headers = headers,
            body = {},
        )
    )
    )
except Exception as e:
    pass

print(11111)
if req and req.status_code == 200:
    print(2222)
    data = json.loads(req.text)
    if data.get('subCode') == '200':
        auth_token = data['data']['token']
        print(auth_token)
    else:
        raise Exception(data.get('message'))
else:
    raise Exception("There is some error in geting auth token")