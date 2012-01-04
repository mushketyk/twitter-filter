from twitterFilter.controllers import MainFormController
from twitterFilter.mainForm import MainForm
from twitterFilter.mainWindow import Ui_MainWindow

__author__ = 'proger'

from PyQt4.QtGui import QApplication
from mainWindow import *
from twitterFilter.twitter import Tweet, TwitterUser, DumbTwitterAPI

import sys
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    main_form = MainForm()
    main_form.show()

    main_form_controller = MainFormController(main_form, DumbTwitterAPI)
    main_form_controller.start()


    sys.exit(app.exec_())
