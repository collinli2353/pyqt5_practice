# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 791, 491))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("practice4_images/thorloki.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setOpenExternalLinks(False)
        self.photo.setObjectName("photo")
        self.Thor = QtWidgets.QPushButton(self.centralwidget)
        self.Thor.setGeometry(QtCore.QRect(0, 489, 381, 51))
        self.Thor.setObjectName("Thor")
        self.Loki = QtWidgets.QPushButton(self.centralwidget)
        self.Loki.setGeometry(QtCore.QRect(420, 490, 381, 51))
        self.Loki.setObjectName("Loki")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## setup buttons ##
        self.Thor.clicked.connect(self.show_thor)
        self.Loki.clicked.connect(self.show_loki)

    def show_thor(self):
        self.photo.setPixmap(QtGui.QPixmap("practice4_images/thor.jpg"))

    def show_loki(self):
        self.photo.setPixmap(QtGui.QPixmap("practice4_images/loki.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Thor.setText(_translate("MainWindow", "Thor"))
        self.Loki.setText(_translate("MainWindow", "Loki"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

