from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QVBoxLayout, QScrollArea, QPushButton, QListWidget, QWidget, QLabel, QMainWindow
from twitterFilter.mainWindow import Ui_MainWindow
from twitterFilter.tweetWidget import Ui_TweetWidget
from twitterFilter.twitter import TwitterAPI, DumbTwitterAPI, Tweet

from twitterFilter.widgets import TweetsWidget, TweetWidget

__author__ = 'proger'


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)

    def setupUi(self, form):
        super(MainForm, self).setupUi(form)

        self.central_widget.setLayout(self.central_layout)











