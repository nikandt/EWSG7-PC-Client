import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from header1_1_ws import *
from grid1_1 import *

class ui_buttons(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)


	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(50,20)

		self.scanButton = QtWidgets.QPushButton(Form)
		self.scanButton.setGeometry(QtCore.QRect(0,0,95,20))
		self.scanButton.setObjectName("Scan")

		self.powerAllOnButton = QtWidgets.QPushButton(Form)
		self.powerAllOnButton.setGeometry(QtCore.QRect(0,40, 95,20))
		self.powerAllOnButton.setObjectName("Power All On")

		self.powerAllOffButton = QtWidgets.QPushButton(Form)
		self.powerAllOffButton.setGeometry(QtCore.QRect(0,60, 95,20))
		self.powerAllOffButton.setObjectName("Power All Off")

		self.lineAllOnButton = QtWidgets.QPushButton(Form)
		self.lineAllOnButton.setGeometry(QtCore.QRect(0,100, 95,20))
		self.lineAllOnButton.setObjectName("Line All On")

		self.lineAllOffButton = QtWidgets.QPushButton(Form)
		self.lineAllOffButton.setGeometry(QtCore.QRect(0,120, 95,20))
		self.lineAllOffButton.setObjectName("Line All Off")

		self.flashButton = QtWidgets.QPushButton(Form)
		self.flashButton.setGeometry(QtCore.QRect(0,160, 95,20))
		self.flashButton.setObjectName("Flash")


		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		self.scanButton.setText(_translate("Forn", "Scan"))
		self.powerAllOnButton.setText(_translate("Form", "Power All On"))
		self.powerAllOffButton.setText(_translate("Form", "Power All Off"))
		self.lineAllOnButton.setText(_translate("Form", "Line All On"))
		self.lineAllOffButton.setText(_translate("Form", "Line All Off"))
		self.flashButton.setText(_translate("Form", "Flash..."))
