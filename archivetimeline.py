#!/usr/bin/env python3

import sys, datetime
from stafferscraper.twittersession import TwitterSession
from stafferscraper.tweetdb import TweetDB
from stafferscraper.config.loadconfig import load_config

def twitterTimeTo_ISO_8601(twitterTime):
    timeValue = datetime.datetime.strptime(twitterTime, '%a %b %d %H:%M:%S +0000 %Y')
    return timeValue.isoformat('T')

def archivetimeline(userID, configFileName):
    config     = load_config(configFileName)
    API_KEY    = config['API_KEY']
    API_SECRET = config['API_SECRET']

    # Login
    twitter = TwitterSession()
    twitter.login(API_KEY, API_SECRET)

    # Set userID to scrape, and create the database
    twitter.setUserID(userID)
    userDB = TweetDB(userID)

    # Fetch the latest tweet to set it as the initial max ID

    latestTweet = twitter.getLatestTweet()
    idLT = [latestTweet['id']]

    for jj in range(0, 30):
        # Fetch batch of 200 (or less) tweets
        tweetBatch=twitter.getTweetBatch(idLT[-1])

        # Set time that tweets were fetched
        fetchedTime = datetime.datetime.now()
        fetchedTime_ISO_8601 = fetchedTime.isoformat('T')

        # Insert tweets in database
        for tweet in tweetBatch:
            idLT.append(tweet['id'])
            userDB.insertRow((tweet['id'], twitterTimeTo_ISO_8601(tweet['created_at']), tweet['text'], fetchedTime_ISO_8601))

        userDB.commit() # Only commit to the database at the end of every batch

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Archive Twitter timelines of a user in a SQLite3 database.')
    parser.add_argument('userID', help='Twitter user ID to be achived')
    parser.add_argument('--config', help='*.yml config file path', default = 'StafferScraper_config.yml')

    args = parser.parse_args()

    archivetimeline(args.userID, args.config)
