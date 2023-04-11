import os
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS

sys.path.append(os.path.abspath('./modules'))

# import modules
from twitter import twitter_email
from snapchat import snapchat_email
from parler import parler_email
from mewe import mewe_email
from rumble import rumble_email
from verify import *
from duolingo import duolingo_name_check, duolingo_email
from adobe import adobe_email, adobe_facebook_email
from wordpress import wordpress_email
from imgur import imgur_email
from hulu import hulu_email
from rubmaps import rubmaps_email
from gravatar import get_gravatar_id, get_gravatar_info

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


@app.route('/')
def poastal():
    email = request.args.get('email')
    if email:
        twitter_result = twitter_email(email)
        snapchat_result = snapchat_email(email)
        parler_result = parler_email(email)
        mewe_result = mewe_email(email)
        rumble_result = rumble_email(email)
        disposable_result = disposable(email)
        spam_result = spam(email)
        deliverable_result = deliverable(email)
        duolingo_result = duolingo_email(email)
        duolingo_name = duolingo_name_check(email)
        adobe_result = adobe_email(email)
        adobe_facebook_result = adobe_facebook_email(email)
        wordpress_result = wordpress_email(email)
        imgur_result = imgur_email(email)
        hulu_result = hulu_email(email)
        rubmaps_result = rubmaps_email(email)
        gravatar_result = get_gravatar_id(email)
        gravatar_info_result = get_gravatar_info(email)
        if not duolingo_name or duolingo_name == "N/A":
            name = gravatar_info_result[0]
        else:
            name = duolingo_name

        return jsonify(
            {
                'Name': name,
                'Photo': gravatar_info_result[1],
                'Deliverable': deliverable_result,
                'Disposable': disposable_result,
                'Spam': spam_result,
                # start profiles
                'profiles': {
                    'Facebook': adobe_facebook_result,
                    'Twitter': twitter_result,
                    'Snapchat': snapchat_result,
                    'Parler': parler_result,
                    'Rumble': rumble_result,
                    'MeWe': mewe_result,
                    'Imgur': imgur_result,
                    'Adobe': adobe_result,
                    'Wordpress': wordpress_result,
                    'Duolingo': duolingo_result,
                    'Hulu': hulu_result,
                    'Rubmaps': rubmaps_result,
                    'Gravatar': gravatar_result,
                },
            })
    else:
        return 'No email address provided.'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
