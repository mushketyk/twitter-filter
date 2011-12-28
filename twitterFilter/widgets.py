from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QScrollArea, QWidget, QVBoxLayout
from twitterFilter.tweetWidget import Ui_TweetWidget

__author__ = 'proger'

class TweetWidget(Ui_TweetWidget):
    def setupUi(self, Widget):
        super(TweetWidget, self).setupUi(Widget)
        Widget.setLayout(self.root_layout)

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


    def add_tweet(self, tweet):
        new_tweet_widget = QtGui.QWidget()
        ui = TweetWidget()
        ui.setupUi(new_tweet_widget)

        self.scroll_box_layout.addWidget(new_tweet_widget)



