import requests

def adobe_email(email):

    headers = {
        'content-type': 'application/json',
        'x-ims-clientid': 'adobedotcom2',
    }

    json_data = {
        'username': email,
    }

    response = requests.post(
        'https://auth.services.adobe.com/signin/v2/users/accounts',
        headers=headers,
        json=json_data,
    )

    checker = response.text

    adobe = '"type"'

    if adobe in checker:
        return f'true'
    else:
        return f'false'

def adobe_facebook_email(email):

    headers = {
        'content-type': 'application/json',
        'x-ims-clientid': 'adobedotcom2',
    }

    json_data = {
        'username': email,
    }

    response = requests.post(
        'https://auth.services.adobe.com/signin/v2/users/accounts',
        headers=headers,
        json=json_data,
    )

    html = response.text

    facebook = 'facebook'

    if facebook in html:
        return f'true'
    else:
        return f'unknown'
