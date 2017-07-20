
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import sys
from header1_1_ws import *
from grid1_1 import *


def run():
	if __name__ == '__main__':
	    app = QtWidgets.QApplication(sys.argv)
	    ex = Grid_Ui()
	    ex.showMaximized()
	    sys.exit(app.exec())
run()