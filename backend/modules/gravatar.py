import hashlib
import json
import requests


def __get_gravatar_json(email):
    """
    This is a private helper function that takes an email address as input, generates the corresponding Gravatar URL,
    retrieves the JSON data from that URL, and returns it as a Python dictionary.
    """
    # Generate the Gravatar URL based on the email address
    chaine_bytes = email.encode('utf-8')
    hash_md5 = hashlib.md5(chaine_bytes).hexdigest()

    email_checker = 'https://en.gravatar.com/{}.json'.format(hash_md5)

    # Retrieve the JSON data from the Gravatar URL
    response = requests.get(
        email_checker,
    )

    # Convert the JSON data to a Python dictionary and return it
    json_data = response.json()
    json_data = json.dumps(json_data)
    data = json.loads(json_data)

    return data


def get_gravatar_id(email):
    """
    This function takes an email address as input, retrieves the corresponding Gravatar JSON data,
    and returns 'true' if the 'id' field in the data is not None, 'false' otherwise.
    """
    data = __get_gravatar_json(email)
    if "entry" not in data: return False

    # Extract the 'id' field from the JSON data
    entry = data["entry"][0]
    id = entry["id"]

    # Return 'true' if the 'id' field is not None, 'false' otherwise
    if id is not None:
        return f'true'
    else:
        return f'false'


def get_gravatar_info(email):
    data = __get_gravatar_json(email)
    if "entry" not in data: return "N/A", "N/A"
    try:
        entry = data['entry'][0]
        display_name = entry['displayName']
        photo_value = entry['photos'][0]["value"]
    except (KeyError, IndexError):
        display_name = None
        photo_value = None

    return display_name, photo_value
