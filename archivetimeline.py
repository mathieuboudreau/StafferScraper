#!/usr/bin/env python3

import sys
from stafferscraper.twittersession import TwitterSession
from stafferscraper.config.loadconfig import load_config

def archivetimeline(userID, configFileName):
    config     = load_config(configFileName)
    API_KEY    = config['API_KEY']
    API_SECRET = config['API_SECRET']

    # Login
    twitter = TwitterSession()
    twitter.login(API_KEY, API_SECRET)

    # Set userID to scrape
    twitter.setUserID(userID)

    latestTweet = twitter.getLatestTweet()

    print(latestTweet['text'])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Archive Twitter timelines of a user in a SQLite3 database.')
    parser.add_argument('userID', help='Twitter user ID to be achived')
    parser.add_argument('--config', help='*.yml config file path', default = 'StafferScraper_config.yml')

    args = parser.parse_args()

    archivetimeline(args.userID, args.config)
