from __future__ import unicode_literals
from requests_oauthlib import OAuth1
import requests
import pprint

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize"
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "xxxxxxxxxxxxxxxxxx"
CONSUMER_SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# request token
oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET_KEY)

endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=santaclara"
r = requests.get(endpoint, auth=oauth)

# Prettyprint to print in Json format
pretty_print = pprint.PrettyPrinter(indent=4)
pretty_print.pprint(r.json())







