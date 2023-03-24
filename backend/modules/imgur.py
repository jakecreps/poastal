import requests

def imgur_email(email):
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = 'email={}'.format(email)

    response = requests.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data)

    checker = response.text

    text = '{"data":{"available":false},"success":true,"status":200}'

    if text in checker:
        return f'true'
    else:
        return f'false'
