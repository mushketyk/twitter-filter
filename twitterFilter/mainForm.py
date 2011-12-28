from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QVBoxLayout, QScrollArea, QPushButton, QListWidget, QWidget, QLabel
from twitterFilter.mainWindow import Ui_MainWindow
from twitterFilter.tweetWidget import Ui_TweetWidget

from twitterFilter.widgets import TweetsWidget, TweetWidget

__author__ = 'proger'


class MainForm(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MainForm, self).setupUi(MainWindow)

        self.central_widget.setLayout(self.central_layout)

        for tab in [self.all_tweets_tab, self.recommended_tweets_tab]:
            tab_layout = QVBoxLayout()
            tab.setLayout(tab_layout)

            tweets_widget = TweetsWidget()
            tab_layout.addWidget(tweets_widget)
            #scroll_box = QScrollArea()
            #scroll_box.setWidgetResizable(True)
            #tab_layout.addWidget(scroll_box)

            #scroll_widget = QWidget()
            #scroll_box_layout = QVBoxLayout(scroll_widget)
            #scroll_box.setWidget(scroll_widget)

            #scroll_box_layout.setSpacing(2)
            #scroll_box_layout.setMargin(2)

            #scroll_box_layout.setAlignment(Qt.AlignTop)
            #scroll_box_layout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)

            for i in range(10):
                #new_tweet_widget = QtGui.QWidget()
                #ui = TweetWidget()
                #ui.setupUi(new_tweet_widget)

                #scroll_box_layout.addWidget(new_tweet_widget)
                tweets_widget.add_tweet(None)




