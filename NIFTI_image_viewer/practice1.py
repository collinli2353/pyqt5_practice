from PyQt5 import QtWidgets
from PyQt5.QtWidget import QApplication, QMainWindow
import sys

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()

	## window size with paramaters (xpos, ypos, width, height)
	win.setGeometry(200, 200, 300, 300)

	## window title ##
	win.setWindowTitle("NIFTI_image_viewer") 

	win.show()
	sys.exit(app.exec_())

window()
