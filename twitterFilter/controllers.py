from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QVBoxLayout
from twitterFilter.mainForm import MainForm
from twitterFilter.widgets import TweetsWidget, TweetWidget

__author__ = 'proger'

class MainFormController:
    def __init__(self, main_form, tweet_loader_ctor):
        self.tweet_loader_ctor = tweet_loader_ctor
        self.main_form = main_form

        self.tweet_widget_controller = TweetWidgetController()

    def start(self):
        self.connect_signals()
        self.add_tweets_widgets()
        self.load_tweets()

    def connect_signals(self):
        pass

    def add_tweets_widgets(self):
        for tab in [self.main_form.all_tweets_tab, self.main_form.recommended_tweets_tab]:
            tab_layout = QVBoxLayout()
            tab.setLayout(tab_layout)

            tab.tweets_widget = TweetsWidget()
            tab_layout.addWidget(tab.tweets_widget)

    def load_tweets(self):
        api = self.tweet_loader_ctor("IvanMushketik")
        tweets = api.get_last_tweets()

        for tweet in tweets:
            tweet_widget = TweetWidget(tweet)
            self.connect_tweet_widget_signals(tweet_widget)
            self.main_form.all_tweets_tab.tweets_widget.add_tweet_widget(tweet_widget)

    def connect_tweet_widget_signals(self, tweet_widget):
        tweet_widget.connect(tweet_widget, SIGNAL("tweetSaving"), self.tweet_widget_controller.tweet_saved)


class TweetWidgetController:
    def __init__(self):
        pass

    def tweet_saved(self, tweet_widget):
        print tweet_widget.tweet.text



