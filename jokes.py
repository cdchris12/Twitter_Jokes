#!/usr/bin/env python
import json
import os
import sys

# Try loading the config file and die if not found
try:
    os.stat("config.json")
except Exception:
    print ("Config file missing!!!", flush=True)
    sys.exit(1)
else:
    with open('config.json', 'r') as infile:
        config = json.load(infile)
    # End with
# End try/except block

import arrow
import twitter

def setup(config):
    api = twitter.Api(
        consumer_key=config.c_key,
        consumer_secret=config.c_secret,
        access_token_key=config.t_key,
        access_token_secret=config.t_secret
    )

    return api
# End def

def search(api):
    _search = api.GetSearch("#joke")
    return _search
# End def

def getJoke(_search):
    for i, tweet in enumerate(_search):
        print i
        #print(tweet.id, tweet.text)
    # End for

    return 0
# End def

def main():
    api = setup()
    _search = search(api)
    joke = getJoke(_search)
# End def

if __name__ = "__main__":
    main()
# End def
