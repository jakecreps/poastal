import requests

def mewe_email(email):

    headers = {
    'accept': 'application/json, text/plain, */*',
    }

    response = requests.get('https://mewe.com/api/v2/auth/checkEmail?email={}'.format(email), headers=headers)

    checker = response.text

    text = "Email already taken"

    if text in checker:
        return f'true'
    else:
        return f'false'
