import requests

def wordpress_email(email):

    params = {
        'http_envelope': '1',
    }

    response = requests.get(
        'https://public-api.wordpress.com/rest/v1.1/users/{}/auth-options'.format(email),
        params=params,
    )

    checker = response.text

    text = '"email_verified": true'

    if text in checker:
        return f'true'
    else:
        return f'false'
