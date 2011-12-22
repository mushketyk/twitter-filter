__author__ = 'proger'

import tweepy

class Tweet:
    def __init__(self, tweepy_tweet):
        self.text = tweepy_tweet.text
        self.created_at = tweepy_tweet.created_at
        self.author = TwitterUser(tweepy_tweet.author)

class TwitterUser:
    def __init__(self, tweepy_user):
        self.name = tweepy_user.name

class TwitterAPI:
    def __init__(self, user_name):
        self.user_name = user_name
        self.twitter_user = tweepy.api.get_user(user_name)

        self.friends = None

    def get_last_tweets(self, last_ids=dict()):

        result = []
        for friend in self._get_friends_list():
            print("Checking " + friend.name)
            for message in tweepy.api.user_timeline(friend.id, count = 10):
                result.append(Tweet(message))

        return sorted(result, key = lambda tweet: tweet.created_at)

    def _get_followers_list(self):
        if not self.followers:
            self.followers = self.twitter_user.followers()

        return self.followers

    def _get_friends_list(self):
        if not self.friends:
            self.friends = self.twitter_user.friends()

        return self.friends

    def _convert_to_users(self, tweepy_users):
        users = []

        for tweepy_user in tweepy_users:
            user = TwitterUser(tweepy_user.name)
            users.append(user)

if __name__ == "__main__":
    api = TwitterAPI("kakabuka")
    tweets = api.get_last_tweets()

    for tweet in tweets:
        print "Created by: " + str(tweet.author.name) + "; Created at: " + str(tweet.created_at) + "; Text: " + str(tweet.text)
