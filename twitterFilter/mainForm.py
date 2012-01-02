from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QVBoxLayout, QScrollArea, QPushButton, QListWidget, QWidget, QLabel
from twitterFilter.mainWindow import Ui_MainWindow
from twitterFilter.tweetWidget import Ui_TweetWidget
from twitterFilter.twitter import TwitterAPI, DumbTwitterAPI, Tweet

from twitterFilter.widgets import TweetsWidget, TweetWidget

__author__ = 'proger'


class MainForm(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MainForm, self).setupUi(MainWindow)

        self.central_widget.setLayout(self.central_layout)

        for tab in [self.all_tweets_tab, self.recommended_tweets_tab]:
            tab_layout = QVBoxLayout()
            tab.setLayout(tab_layout)

            tab.tweets_widget = TweetsWidget()
            tab_layout.addWidget(tab.tweets_widget)


        api = DumbTwitterAPI("IvanMushketik")
        tweets = api.get_last_tweets()

        for tweet in tweets:
            self.all_tweets_tab.tweets_widget.add_tweet(tweet)






