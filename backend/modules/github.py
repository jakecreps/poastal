import requests
import json

headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'Authorization': 'Bearer <insert API token>', #Make sure you add your API token here for this module to work
}

def github_email(email):

    params = {
        'q': email,
    }

    response = requests.get('https://api.github.com/search/users', params=params, headers=headers)

    html = response.text

    text = '"total_count":0'

    if text in html:
        return f'false'
    else:
        return f'true'

def get_username(email):
    params = {
        'q': email,
    }
    response = requests.get('https://api.github.com/search/users', params=params, headers=headers)
    json_response = response.json()
    username = json_response["items"][0]["login"]
    return username

def githubname_email(email):

    params = {
        'q': email,
    }

    response = requests.get('https://api.github.com/search/users', params=params, headers=headers)

    # Extract the "login" value from the JSON response
    json_response = json.loads(response.text)
    try:
        login = json_response["items"][0]["login"]
    except:
        return f'N/A'

    # Make a new API request to get the user profile based on the login value
    response = requests.get(f'https://api.github.com/users/{login}', headers=headers)

    # Extract the "name" value from the JSON response
    json_response = json.loads(response.text)
    name = json_response["name"]

    if name:
        return name
    else:
        return f'N/A'

def githublocation_email(email):

    params = {
        'q': email,
    }

    response = requests.get('https://api.github.com/search/users', params=params, headers=headers)

    # Extract the "login" value from the JSON response
    json_response = json.loads(response.text)
    try:
        login = json_response["items"][0]["login"]
    except:
        return f'N/A'

    # Make a new API request to get the user profile based on the login value
    response = requests.get(f'https://api.github.com/users/{login}', headers=headers)

    # Extract the "location" value from the JSON response
    json_response = json.loads(response.text)
    location = json_response["location"]

    if location:
        return location
    else:
        return f'N/A'

def github_avatar_url(email):
    params = {
        'q': email,
    }

    response = requests.get('https://api.github.com/search/users', params=params, headers=headers)

    # Extract the "login" value from the JSON response
    json_response = json.loads(response.text)
    try:
        login = json_response["items"][0]["login"]
    except:
        return f'N/A'

    # Make a new API request to get the user profile based on the login value
    response = requests.get(f'https://api.github.com/users/{login}', headers=headers)

    # Extract the "avatar_url" value from the JSON response
    json_response = json.loads(response.text)
    avatar_url = json_response["avatar_url"]

    if avatar_url:
        return avatar_url
    else:
        return f'N/A'
