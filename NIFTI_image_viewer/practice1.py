from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

## take properties of QMainWindow ##
class MyWindow(QMainWindow):
	def __init__(self):
		## Parent constructor called ##
		super(MyWindow, self).__init__()
		## window size with paramaters (xpos, ypos, width, height)
		self.setGeometry(200, 200, 300, 300)

		## window title ##
		self.setWindowTitle("Label and Button") 
		self.initUI()

	## put all the stuff in window ##
	def initUI(self):
		## create label ## 
		self.label = QtWidgets.QLabel(self)
		self.label.setText("label here")
		self.label.move(50, 50)

		## create button ##
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Button press")

		# set trigger #
		self.b1.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText("button clicked")
		self.update()

	def update(self):
		self.label.adjustSize()

## window ##
def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()
