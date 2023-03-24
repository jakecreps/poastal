import requests

def rumble_email(email):

    email = email

    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    params = {
        'a': 'check_email',
        'origin': '',
    }

    data = 'format=json&check_email={}'.format(email)

    response = requests.post('https://rumble.com/register.php', params=params, headers=headers, data=data)

    checker = response.text

    text = "There's already a Rumble account with this email."

    if text in checker:
        return f'true'
    else:
        return f'false'
