import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from header1_1_ws import *
from buttons1_1 import *

 
class Grid_Ui(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Switcher'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 100
        self.var = 0
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        #self.show()
 
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        module_1 = Ui_Form()
        module_2 = Ui_Form()
        module_3 = Ui_Form()
        module_4 = Ui_Form()
        buttons = ui_buttons()
        #scaled_module = module.resize(300,150)
        layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 10)
        #layout.setColumnStretch(0,2)
        
        #buttons.scanButton.clicked.connect(self.scan_module)
        
        layout.addWidget(buttons,0,0)

        layout.addWidget(module_1,0,1)
        layout.addWidget(module_2,0,2)
        layout.addWidget(module_3,1,1)
        layout.addWidget(module_4,1,2) 
 
        self.horizontalGroupBox.setLayout(layout)

        buttons.powerAllOnButton.clicked.connect(module_1.power_all_on)
        buttons.powerAllOnButton.clicked.connect(module_2.power_all_on)
        buttons.powerAllOnButton.clicked.connect(module_3.power_all_on)
        buttons.powerAllOnButton.clicked.connect(module_4.power_all_on)

        buttons.powerAllOffButton.clicked.connect(module_1.power_all_off)
        buttons.powerAllOffButton.clicked.connect(module_2.power_all_off)
        buttons.powerAllOffButton.clicked.connect(module_3.power_all_off)
        buttons.powerAllOffButton.clicked.connect(module_4.power_all_off)

        buttons.lineAllOnButton.clicked.connect(module_1.line_all_on)
        buttons.lineAllOnButton.clicked.connect(module_2.line_all_on)
        buttons.lineAllOnButton.clicked.connect(module_3.line_all_on)
        buttons.lineAllOnButton.clicked.connect(module_4.line_all_on)

        buttons.lineAllOffButton.clicked.connect(module_1.line_all_off)
        buttons.lineAllOffButton.clicked.connect(module_2.line_all_off)
        buttons.lineAllOffButton.clicked.connect(module_3.line_all_off)
        buttons.lineAllOffButton.clicked.connect(module_4.line_all_off)

    #def scan_module(self):
        #number = scan()
        #if number == 49:
        #    self.layout.addWidget(module_1,0,1)

