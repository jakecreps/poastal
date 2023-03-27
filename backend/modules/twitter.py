import requests
import json

def twitter_email(email):

    email_checker = 'https://api.twitter.com/i/users/email_available.json?email={}'.format(email)

    response = requests.get(
        email_checker,
    )

    check = response.json()

    if check["taken"]:
        return f'true'
    else:
        return f'false'
