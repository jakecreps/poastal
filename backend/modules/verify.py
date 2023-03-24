import requests

def deliverable(email):
    params = {
        'email': email,
    }

    response = requests.get('http://api.eva.pingutil.com/email', params=params)

    checker = response.text
    deliverable = '"deliverable":true'

    if deliverable in checker:
        return f'true'
    else:
        return f'false'

def spam(email):
    params = {
        'email': email,
    }

    response = requests.get('http://api.eva.pingutil.com/email', params=params)

    checker = response.text
    spam = '"spam":true'

    if spam in checker:
        return f'true'
    else:
        return f'false'

def disposable(email):
    params = {
        'email': email,
    }

    response = requests.get('http://api.eva.pingutil.com/email', params=params)

    checker = response.text
    disposable = '"disposable":true'

    if disposable in checker:
        return f'true'
    else:
        return f'false'
