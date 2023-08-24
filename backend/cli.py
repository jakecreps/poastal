import argparse
import os
import sys
import json

sys.path.append(os.path.abspath('./modules'))

#import modules
from twitter import twitter_email
from snapchat import snapchat_email
# from parler import parler_email
from mewe import mewe_email
from rumble import rumble_email
from verify import *
from duolingo import duolingo_name_check, duolingo_email, duolingo_image
from adobe import adobe_email, adobe_facebook_email
from wordpress import wordpress_email
from imgur import imgur_email
from hulu import hulu_email
from rubmaps import rubmaps_email
from github import *
from gravatar import *
from discord import *

def check_email(email):
    twitter_result = twitter_email(email)
    snapchat_result = snapchat_email(email)
    # parler_result = parler_email(email)
    mewe_result = mewe_email(email)
    rumble_result = rumble_email(email)
    disposable_result = disposable(email)
    spam_result = spam(email)
    deliverable_result = deliverable(email)
    duolingo_result = duolingo_email(email)
    duolingo_name = duolingo_name_check(email)
    duolingo_image_url = duolingo_image(email)
    adobe_result = adobe_email(email)
    adobe_facebook_result = adobe_facebook_email(email)
    wordpress_result = wordpress_email(email)
    imgur_result = imgur_email(email)
    hulu_result = hulu_email(email)
    rubmaps_result = rubmaps_email(email)
    github_result = github_email(email)
    github_name = githubname_email(email)
    github_location = githublocation_email(email)
    github_image = github_avatar_url(email)
    gravatar_response = hash_email(email)
    gravatar_image = parse_json(gravatar_response, 'thumbnailUrl')
    gravatar_result = gravatar_email(email)
    discord_result = discord_email(email)

    result = {
        'Duolingo Name': duolingo_name,
        'GitHub Name': github_name,  # Add GitHub Name to the table
        'Location': github_location,  # Add GitHub Location to the table
        'Image': {
            'Duolingo': duolingo_image_url,
            'GitHub': github_image,
            'Gravatar': gravatar_image,
        },
        'Deliverable': deliverable_result,
        'Disposable': disposable_result,
        'Spam': spam_result,
        #start profiles
        'Profiles':{
            'Facebook': adobe_facebook_result,
            'Twitter': twitter_result,
            'Snapchat': snapchat_result,
            # 'Parler': parler_result,
            'Rumble': rumble_result,
            'MeWe': mewe_result,
            'Imgur': imgur_result,
            'Adobe': adobe_result,
            'Wordpress': wordpress_result,
            'Duolingo': duolingo_result,
            'Hulu': hulu_result,
            'Rubmaps': rubmaps_result,
            'Github': github_result,
            'Gravatar': gravatar_result,
            'Discord': discord_result,
        },
    }

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', help='email address to check')
    args = parser.parse_args()

    email = args.email
    result = check_email(email)
    print(json.dumps(result, indent=4))
