# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice6.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("practice6.ui", self)
        self.browse_button.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "/home/pi/Desktop/pyqt5_practice/NIFTI_image_viewer/practice6.ui")
        self.filename.setText(fname[0])

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())