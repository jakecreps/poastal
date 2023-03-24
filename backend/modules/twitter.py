import requests

def twitter_email(email):

    email_checker = 'https://api.twitter.com/i/users/email_available.json?email={}'.format(email)

    response = requests.get(
        email_checker,
    )

    checker = response.text

    text = '{"valid":false,"msg":"Email has already been taken.","taken":true}'

    if text in checker:
        return f'true'
    else:
        return f'false'
