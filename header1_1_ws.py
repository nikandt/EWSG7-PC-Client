import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import sys
import serial
import time


#ser = serial.Serial('COM3', 9600, timeout=0)
class FakeSerial(object):
    def write(self, data):
        pass
ser = FakeSerial()

class Ui_Form(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.powerAllClicks = 0
        self.lineAllClicks = 0
        self.clicks1 = 0
        self.clicks2 = 0
        self.clicks3 = 0
        self.clicks4 = 0
        self.clicks5 = 0
        self.clicks6 = 0
        self.clicks7 = 0
        self.clicks8 = 0

        self.testclick1 = 0
        self.testclick2 = 0
        self.testclick3 = 0
        self.testclick4 = 0



        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        self.box = QtWidgets.QLabel(Form)
        self.box.setGeometry(QtCore.QRect(0, 0, 600, 300))

        self.powerAllOnButton = QtWidgets.QPushButton(Form)
        self.powerAllOnButton.setGeometry(QtCore.QRect(450,100,70,20))

        self.powerAllOffButton = QtWidgets.QPushButton(Form)
        self.powerAllOffButton.setGeometry(QtCore.QRect(520,100,70,20))

        self.lineAllOnButton = QtWidgets.QPushButton(Form)
        self.lineAllOnButton.setGeometry(QtCore.QRect(450,120,70,20))

        self.lineAllOffButton = QtWidgets.QPushButton(Form)
        self.lineAllOffButton.setGeometry(QtCore.QRect(520,120,70,20))

        #self.flashButton = QtWidgets.QPushButton(Form)
        #self.flashButton.setGeometry(QtCore.QRect(450,140,140,20))

        self.testButton1 = QtWidgets.QPushButton(Form)
        self.testButton1.setGeometry(QtCore.QRect(20, 20, 110, 50))
        self.testButton2 = QtWidgets.QPushButton(Form)
        self.testButton2.setGeometry(QtCore.QRect(170, 20, 110, 50))
        self.testButton3 = QtWidgets.QPushButton(Form)
        self.testButton3.setGeometry(QtCore.QRect(320, 20, 110, 50))
        self.testButton4 = QtWidgets.QPushButton(Form)
        self.testButton4.setGeometry(QtCore.QRect(470, 20, 110, 50))

        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(12,250,66,50))
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(72,250,66,50))
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(162,250,66,50))
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(222,250,66,50))
        self.pushButton5 = QtWidgets.QPushButton(Form)
        self.pushButton5.setGeometry(QtCore.QRect(312,250,66,50))
        self.pushButton6 = QtWidgets.QPushButton(Form)
        self.pushButton6.setGeometry(QtCore.QRect(372,250,66,50))
        self.pushButton7 = QtWidgets.QPushButton(Form)
        self.pushButton7.setGeometry(QtCore.QRect(462,250,66,50))
        self.pushButton8 = QtWidgets.QPushButton(Form)
        self.pushButton8.setGeometry(QtCore.QRect(522,250,66,50))
        #170, 40, 75, 23
        self.powerAllOnButton.setObjectName("Power On")
        self.powerAllOffButton.setObjectName("Power Off")
        self.lineAllOnButton.setObjectName("Line On")
        self.lineAllOffButton.setObjectName("Line Off")
        #self.flashButton.setObjectName("Flash")

        self.testButton1.setObjectName("Recognize")
        self.testButton2.setObjectName("Recognize")
        self.testButton3.setObjectName("Recognize")
        self.testButton4.setObjectName("Recognize")

        self.pushButton1.setObjectName("Power 1")
        self.pushButton2.setObjectName("Line 1")
        self.pushButton3.setObjectName("Power 2")
        self.pushButton4.setObjectName("Line 2")
        self.pushButton5.setObjectName("Power 3")
        self.pushButton6.setObjectName("Line 3")
        self.pushButton7.setObjectName("Power 4")
        self.pushButton7.setObjectName("Line 4")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 200, 50, 50))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 50, 50))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 200, 50, 50))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 200, 50, 50))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(320, 200, 50, 50))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(380, 200, 50, 50))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(470, 200, 50, 50))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(530, 200, 50, 50))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        pixmap_box = QPixmap('box2.jpeg')
        scaled_box = pixmap_box.scaled(800,400,QtCore.Qt.KeepAspectRatio)
        self.box.setPixmap(pixmap_box)

        pixmap_black = QPixmap('led_black.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(scaled_black)
        self.label_2.setPixmap(scaled_black)
        self.label_3.setPixmap(scaled_black)
        self.label_4.setPixmap(scaled_black)
        self.label_5.setPixmap(scaled_black)
        self.label_6.setPixmap(scaled_black)
        self.label_7.setPixmap(scaled_black)
        self.label_8.setPixmap(scaled_black)

        Form.setWindowTitle(_translate("Form", "Form"))

        #pixmap_button = QPixmap('black_button.jpeg')
        #self.pushButton.setIcon(QIcon(pixmap_button))
        self.powerAllOnButton.setText(_translate("Form", "Power On"))
        self.powerAllOffButton.setText(_translate("Form", "Power Off"))
        self.lineAllOnButton.setText(_translate("Form", "Line on"))
        self.lineAllOffButton.setText(_translate("Form", "Line Off"))
        #self.flashButton.setText(_translate("Form", "Flash"))

        self.testButton1.setText(_translate("From", "Recognize"))
        self.testButton2.setText(_translate("From", "Recognize"))
        self.testButton3.setText(_translate("From", "Recognize"))
        self.testButton4.setText(_translate("From", "Recognize"))

        self.pushButton1.setText(_translate("Form", "Power"))
        self.pushButton2.setText(_translate("Form", "Line"))
        self.pushButton3.setText(_translate("Form", "Power"))
        self.pushButton4.setText(_translate("Form", "Line"))
        self.pushButton5.setText(_translate("Form", "Power"))
        self.pushButton6.setText(_translate("Form", "Line"))
        self.pushButton7.setText(_translate("Form", "Power"))
        self.pushButton8.setText(_translate("Form", "Line"))

        self.powerAllOnButton.clicked.connect(self.power_all_on)
        self.powerAllOffButton.clicked.connect(self.power_all_off)

        self.lineAllOnButton.clicked.connect(self.line_all_on)
        self.lineAllOffButton.clicked.connect(self.line_all_off)

        self.testButton1.clicked.connect(self.test1)
        self.testButton2.clicked.connect(self.test2)
        self.testButton3.clicked.connect(self.test3)
        self.testButton4.clicked.connect(self.test4)

        self.pushButton1.clicked.connect(self.click1)
        #self.label.mousePressEvent = self.click1()
        self.pushButton2.clicked.connect(self.click2)
        self.pushButton3.clicked.connect(self.click3)
        self.pushButton4.clicked.connect(self.click4)
        self.pushButton5.clicked.connect(self.click5)
        self.pushButton6.clicked.connect(self.click6)
        self.pushButton7.clicked.connect(self.click7)
        self.pushButton8.clicked.connect(self.click8)

    def power_all_on(self):
        pixmap_red = QPixmap('led_red.png')
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        ser.write(b'1')
        self.label.setPixmap(scaled_red)
        self.label_3.setPixmap(scaled_red)
        self.label_5.setPixmap(scaled_red)
        self.label_7.setPixmap(scaled_red)
        self.powerAllClicks = 1
        self.clicks1 = 1
        self.clicks3 = 1
        self.clicks5 = 1
        self.clicks7 = 1

    def power_all_off(self):
        pixmap_black = QPixmap('led_black.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        ser.write(b'0')
        self.label.setPixmap(scaled_black)
        self.label_3.setPixmap(scaled_black)
        self.label_5.setPixmap(scaled_black)
        self.label_7.setPixmap(scaled_black)
        self.powerAllClicks = 0
        self.clicks1 = 0
        self.clicks3 = 0
        self.clicks5 = 0
        self.clicks7 = 0

    def line_all_on(self):
        pixmap_green = QPixmap('led_green.png')
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        ser.write(b'1')
        self.label_2.setPixmap(scaled_green)
        self.label_4.setPixmap(scaled_green)
        self.label_6.setPixmap(scaled_green)
        self.label_8.setPixmap(scaled_green)
        self.lineAllClicks = 1
        self.clicks2 = 1
        self.clicks4 = 1
        self.clicks6 = 1
        self.clicks8 = 1

    def line_all_off(self):
        pixmap_black = QPixmap('led_black.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        ser.write(b'0')
        self.label_2.setPixmap(scaled_black)
        self.label_4.setPixmap(scaled_black)
        self.label_6.setPixmap(scaled_black)
        self.label_8.setPixmap(scaled_black)
        self.lineAllClicks = 0
        self.clicks2 = 0
        self.clicks4 = 0
        self.clicks6 = 0
        self.clicks8 = 0

    def test1(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_yellow = QPixmap('led_yellow.png')
        pixmap_red = QPixmap('led_red.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_yellow = pixmap_yellow.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        if self.testclick1 == 0:
            self.label.setPixmap(scaled_yellow)
            self.label_2.setPixmap(scaled_yellow)
            self.testclick1 = 1
        else:
            if self.clicks1 == 1:
                self.label.setPixmap(scaled_red)
                if self.clicks2 == 1:
                    self.label_2.setPixmap(scaled_green)
                else:
                    self.label_2.setPixmap(scaled_black)
            else:
                if self.clicks2 == 1:
                    self.label_2.setPixmap(scaled_green)
                else:
                    self.label_2.setPixmap(scaled_black)
                self.label.setPixmap(scaled_black)

            self.testclick1 = 0

    def test2(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_yellow = QPixmap('led_yellow.png')
        pixmap_red = QPixmap('led_red.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_yellow = pixmap_yellow.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        if self.testclick2 == 0:
            self.label_3.setPixmap(scaled_yellow)
            self.label_4.setPixmap(scaled_yellow)
            self.testclick2 = 1
        else:
            if self.clicks3 == 1:
                self.label_3.setPixmap(scaled_red)
                if self.clicks4 == 1:
                    self.label_4.setPixmap(scaled_green)
                else:
                    self.label_4.setPixmap(scaled_black)
            else:
                if self.clicks4 == 1:
                    self.label_4.setPixmap(scaled_green)
                else:
                    self.label_4.setPixmap(scaled_black)
                self.label_3.setPixmap(scaled_black)

            self.testclick2 = 0

    def test3(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_yellow = QPixmap('led_yellow.png')
        pixmap_red = QPixmap('led_red.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_yellow = pixmap_yellow.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        if self.testclick3 == 0:
            self.label_5.setPixmap(scaled_yellow)
            self.label_6.setPixmap(scaled_yellow)
            self.testclick3 = 1
        else:
            if self.clicks5 == 1:
                self.label_5.setPixmap(scaled_red)
                if self.clicks6 == 1:
                    self.label_6.setPixmap(scaled_green)
                else:
                    self.label_6.setPixmap(scaled_black)
            else:
                if self.clicks6 == 1:
                    self.label_6.setPixmap(scaled_green)
                else:
                    self.label_6.setPixmap(scaled_black)
                self.label_5.setPixmap(scaled_black)

            self.testclick3 = 0

    def test4(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_yellow = QPixmap('led_yellow.png')
        pixmap_red = QPixmap('led_red.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_yellow = pixmap_yellow.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)

        if self.testclick4 == 0:
            self.label_7.setPixmap(scaled_yellow)
            self.label_8.setPixmap(scaled_yellow)
            self.testclick4 = 1
        else:
            if self.clicks7 == 1:
                self.label_7.setPixmap(scaled_red)
                if self.clicks8 == 1:
                    self.label_8.setPixmap(scaled_green)
                else:
                    self.label_8.setPixmap(scaled_black)
            else:
                if self.clicks8 == 1:
                    self.label_8.setPixmap(scaled_green)
                else:
                    self.label_8.setPixmap(scaled_black)
                self.label_7.setPixmap(scaled_black)

            self.testclick4 = 0

    def click1(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_red = QPixmap('led_red.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks1 == 0:
            ser.write(b'1')
            self.label.setPixmap(scaled_red)
            self.clicks1 = 1
        else:
            ser.write(b'0')
            self.label.setPixmap(scaled_black)
            self.clicks1 = 0


    def click2(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks2 == 0:
            ser.write(b'1')
            self.label_2.setPixmap(scaled_green)
            self.clicks2 = 1
        else:
            ser.write(b'0')
            self.label_2.setPixmap(scaled_black)
            self.clicks2 = 0

    def click3(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_red = QPixmap('led_red.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks3 == 0:
            ser.write(b'1')
            self.label_3.setPixmap(scaled_red)
            self.clicks3 = 1
        else:
            ser.write(b'0')
            self.label_3.setPixmap(scaled_black)
            self.clicks3 = 0

    def click4(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks4 == 0:
            ser.write(b'1')
            self.label_4.setPixmap(scaled_green)
            self.clicks4 = 1
        else:
            ser.write(b'0')
            self.label_4.setPixmap(scaled_black)
            self.clicks4 = 0

    def click5(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_red = QPixmap('led_red.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks5 == 0:
            ser.write(b'1')
            self.label_5.setPixmap(scaled_red)
            self.clicks5 = 1
        else:
            ser.write(b'0')
            self.label_5.setPixmap(scaled_black)
            self.clicks5 = 0


    def click6(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks6 == 0:
            ser.write(b'1')
            self.label_6.setPixmap(scaled_green)
            self.clicks6 = 1
        else:
            ser.write(b'0')
            self.label_6.setPixmap(scaled_black)
            self.clicks6 = 0

    def click7(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_red = QPixmap('led_red.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_red = pixmap_red.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks7 == 0:
            ser.write(b'1')
            self.label_7.setPixmap(scaled_red)
            self.clicks7 = 1
        else:
            ser.write(b'0')
            self.label_7.setPixmap(scaled_black)
            self.clicks7 = 0

    def click8(self):
        pixmap_black = QPixmap('led_black.png')
        pixmap_green = QPixmap('led_green.png')
        scaled_black = pixmap_black.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        scaled_green = pixmap_green.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        #line = ser.read()
        #line = int(int.from_bytes(line,byteorder = 'big'))
        
        if self.clicks8 == 0:
            ser.write(b'1')
            self.label_8.setPixmap(scaled_green)
            self.clicks8 = 1
        else:
            ser.write(b'0')
            self.label_8.setPixmap(scaled_black)
            self.clicks8 = 0

def scan():
    assert False
    ser.write(b'2')
    time.sleep(0.1)
    number = ser.readline()
    number = int(int.from_bytes(number,byteorder = 'big'))
    print(number)
    return number

