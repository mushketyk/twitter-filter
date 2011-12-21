from PyQt4 import QtGui
from PyQt4.QtGui import QScrollArea, QWidget, QVBoxLayout
from twitterFilter.tweetWidget import Ui_TweetWidget

__author__ = 'proger'

class SingleTweetWidget(Ui_TweetWidget):
    pass

class TweetsWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.scroll_area = QScrollArea()
        self.scroll_area.setParent(self)

        self.tweets_layout = QVBoxLayout()

        self.scroll_area.setLayout(self.tweets_layout)

    def add_tweet(self, tweet):
        new_tweet_widget = QtGui.QWidget()
        ui = Ui_TweetWidget()
        ui.setupUi(new_tweet_widget)

        self.tweets_layout.addWidget(new_tweet_widget)



