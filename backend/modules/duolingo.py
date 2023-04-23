import requests
import json

def duolingo_name_check(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    response = requests.get('https://www.duolingo.com/2017-06-30/users', params=params, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    if len(data['users']) > 0:
        if 'name' in data['users'][0]:
            name = data['users'][0]['name']
            return name
        else:
            return f'N/A'
    else:
        return f'N/A'


def duolingo_email(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    response = requests.get('https://www.duolingo.com/2017-06-30/users', params=params, headers=headers)

    checker = response.text

    text = 'username'

    if text in checker:
        return f'true'
    else:
        return f'false'


def duolingo_image(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    response = requests.get('https://www.duolingo.com/2017-06-30/users', params=params, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    if len(data['users']) > 0:
        if 'picture' in data['users'][0]:
            picture = data['users'][0]['picture']
            return picture
        else:
            return f'false'
    else:
        return f'false'
