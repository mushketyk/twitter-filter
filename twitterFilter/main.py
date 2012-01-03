from twitterFilter.mainForm import MainForm
from twitterFilter.mainWindow import Ui_MainWindow

__author__ = 'proger'

from PyQt4.QtGui import QApplication
from mainWindow import *
from twitterFilter.twitter import Tweet, TwitterUser



import sys
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainForm()

    #MainWindow.setMaximumSize(400, 400)
    MainWindow.show()
    sys.exit(app.exec_())
