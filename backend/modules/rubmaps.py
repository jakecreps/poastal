import requests

def rubmaps_email(email):

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = {
        'email': email,
        'ajax': '1',
    }

    response = requests.post('https://www.rubmaps.ch/signup', headers=headers, data=data)

    checker = response.text

    text = '0'

    if text in checker:
        return f'false'
    else:
        return f'true'
