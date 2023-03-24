import requests
import json

def snapchat_email(email):

    headers = {
        'Content-Type': 'text/plain',
    }

    data = {}

    data.update(email=email)

    data = json.dumps(data)

    response = requests.post('https://bitmoji.api.snapchat.com/api/user/find', headers=headers, data=data)

    checker = response.text

    text = '{"account_type":"snapchat"}'

    if text in checker:
        return f'true'
    else:
        return f'false'
