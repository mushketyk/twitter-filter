from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QScrollArea, QWidget, QVBoxLayout
from twitterFilter import twitter
from twitterFilter.tweetWidget import Ui_TweetWidget

__author__ = 'proger'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TweetWidget(QWidget, Ui_TweetWidget):
    def __init__(self, tweet):
        QWidget.__init__(self)

        self.setupUi(self)
        self.tweet = tweet

        self.display_author_name(self.tweet.author.name)
        self.display_publishing_date(self.tweet.created_at)
        self.display_tweet_text(self.tweet.text)

        self.connect(self.save_button, SIGNAL("clicked(bool)"), self.save_button_clicked)

    def save_button_clicked(self):
        self.emit(SIGNAL("tweetSaving"), self)

    def setupUi(self, Widget):
        super(TweetWidget, self).setupUi(Widget)
        self.setLayout(self.root_layout)

    def display_author_name(self, author_name):
        self.author_name.setText(_fromUtf8("Author: " + author_name))

    def display_publishing_date(self, publishing_date):
        self.publishing_date.setText(_fromUtf8("Date: " + str(publishing_date)))

    def display_tweet_text(self, tweet_text):
        formated_text = twitter.format_tweet_text(tweet_text)
        self.tweet_text.setText(_fromUtf8(formated_text))


class TweetsWidget(QScrollArea):
    def __init__(self):
        QScrollArea.__init__(self)

        self.setWidgetResizable(True)

        scroll_widget = QWidget()
        self.scroll_box_layout = QVBoxLayout(scroll_widget)
        self.setWidget(scroll_widget)

        self.scroll_box_layout.setSpacing(2)
        self.scroll_box_layout.setMargin(2)

        self.scroll_box_layout.setAlignment(Qt.AlignTop)
        self.scroll_box_layout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)


    def add_tweet_widget(self, tweet_widget):
        self.scroll_box_layout.addWidget(tweet_widget)





