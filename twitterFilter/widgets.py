from PyQt4 import QtGui
from PyQt4.QtGui import QScrollArea, QWidget, QVBoxLayout
from twitterFilter.tweetWidget import Ui_TweetWidget

__author__ = 'proger'

class SingleTweetWidget(Ui_TweetWidget):
    pass


class TweetsWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.scroll_area = QScrollArea(self)
        #self.scroll_area.setParent(self)
        self.scroll_area.setWidgetResizable(True)

        tweets_container = QWidget()
        self.scroll_area.setWidget(tweets_container)
        self.tweets_layout = QVBoxLayout(tweets_container)

        #self.scroll_area.setLayout(self.tweets_layout)


    def add_tweet(self, tweet):
        new_tweet_widget = QtGui.QWidget()
        ui = SingleTweetWidget()
        ui.setupUi(new_tweet_widget)

        #ui.setGeometry()

        self.tweets_layout.addWidget(new_tweet_widget)



