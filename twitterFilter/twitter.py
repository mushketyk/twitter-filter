import pickle
import urlparse

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

class DumbTwitterAPI:

    def __init__(self, user_name):
        pass

    def get_last_tweets(self):
        fd = open("tweets.test", "rb")
        tweets = pickle.load(open("/home/proger/tweets.test", "rb"))
        fd.close()

        return tweets

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

        return sorted(result, key = lambda tweet: tweet.created_at, reverse=True)

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

def format_tweet_text(text):
    result = ""

    for word in text.split():
        append = word

        res = urlparse.urlparse(word)
        # This is url
        if res.scheme and res.hostname:
            append = "<a href='" + word + "'>" + word + "</a>"
        elif word.startswith('#'):
            append = "<font color='blue'>" + word + "</font>"
        elif word.startswith('@'):
            append = "<font color='blue'>" + word + "</font>"

        result += ' ' + append

    return result

if __name__ == "__main__":
    api = TwitterAPI("IvanMushketik")
    tweets = api.get_last_tweets()

    fd = open("/home/proger/tweets.test", "wb")
    pickle.dump(tweets, fd)
    fd.close()
