import requests

def parler_email(email):

    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'email': email,
    }

    response = requests.post('https://api.parler.com/v0/public/user/email/check', headers=headers, json=json_data)

    checker = response.text

    text = '{"message":"email exists"}'

    if text in response.text:
        return f'true'
    else:
        return f'false'
