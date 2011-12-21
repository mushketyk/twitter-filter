from PyQt4.QtGui import QVBoxLayout, QScrollArea, QPushButton
from twitterFilter.mainWindow import Ui_MainWindow
from twitterFilter.widgets import TweetsWidget

__author__ = 'proger'


class MainForm(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MainForm, self).setupUi(MainWindow)

        self.central_widget.setLayout(self.central_layout)

        for tab in [self.all_tweets_tab, self.recommended_tweets_tab]:
            layout = QVBoxLayout()
            #tweets_widget = TweetsWidget()
            #layout.addWidget(tweets_widget)
            sa = QScrollArea()
            sa.setWidgetResizable(True)

            tab.setLayout(layout)

