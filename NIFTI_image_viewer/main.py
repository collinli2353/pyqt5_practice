import Main_Window
from NIfTI_image import NIFTI_converter
from QGS_sections import QGraphicsView_image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

## implement MainWindowUI ##
class Main(Main_Window.Ui_MainWindow):
	def __init__(self, MainWindow):
		self.setupUi(MainWindow)

		## COPIED FROM MAIN_WINDOW.py ##
		self.graphicsView_1 = QGraphicsView_image(self.centralwidget)
		self.graphicsView_1.setGeometry(QtCore.QRect(460, 10, 351, 341))
		self.graphicsView_1.setObjectName("graphicsView_1")
		self.graphicsView_2 = QGraphicsView_image(self.centralwidget)
		self.graphicsView_2.setGeometry(QtCore.QRect(830, 10, 351, 341))
		self.graphicsView_2.setObjectName("graphicsView_2")
		self.graphicsView_3 = QGraphicsView_image(self.centralwidget)
		self.graphicsView_3.setGeometry(QtCore.QRect(460, 390, 351, 341))
		self.graphicsView_3.setObjectName("graphicsView_3")
		self.graphicsView_4 = QGraphicsView_image(self.centralwidget)
		self.graphicsView_4.setGeometry(QtCore.QRect(830, 390, 351, 341))
		self.graphicsView_4.setObjectName("graphicsView_4")

		## QGraphicsView ##
		self.graphicsView = [self.graphicsView_1, self.graphicsView_2, self.graphicsView_3, self.graphicsView_4]

		## QGraphicsPixmapItem ##
		self.image = [None, None, None, None]

		## triggers ##
		### Open file trigger ###
		self.actionOpen.triggered.connect(self.browse)

		### Horizontal Slider trigger ###
		self.horizontalSlider_1.valueChanged.connect(lambda value: self.changeValue(value, slider=0))
		self.horizontalSlider_2.valueChanged.connect(lambda value: self.changeValue(value, slider=1))
		self.horizontalSlider_3.valueChanged.connect(lambda value: self.changeValue(value, slider=2))


	## Opens finder to get NIFTI image path ##
	def browse(self):
		## set filter to open only files ending in specific types ##
		filter = "nii(*.nii);nii.gz(*nii.gz)"
		fname = QFileDialog.getOpenFileName(filter=filter)

		## will store the numpy arrays of the image using the NIfTI_image.converter class##
		self.image_obj_converter = NIFTI_converter(path = fname[0])
		self.images_npArray = self.image_obj_converter.toNumpyArray()

		## display images ##
		self.show_images(X = 100, Y = 100, Z = 100)

	## Displays X_image, Y_image, Z_image based on slice ##
	def show_images(self, X = None, Y = None, Z = None):
		if(X):
			self.X_image = self.image_obj_converter.toQImageX(section = X)
			convertedX = QtGui.QPixmap.fromImage(self.X_image)
			self.graphicsView[0].setPhoto(convertedX)
		
		if(Y):
			self.Y_image = self.image_obj_converter.toQImageY(section = Y)
			convertedY = QtGui.QPixmap.fromImage(self.Y_image)
			self.graphicsView[1].setPhoto(convertedY)
		
		if(Z):
			self.Z_image = self.image_obj_converter.toQImageZ(section = Z)
			convertedZ = QtGui.QPixmap.fromImage(self.Z_image)
			self.graphicsView[2].setPhoto(convertedZ)
		

	## slider value changed ##
	def changeValue(self, value, slider):
		## Scale Value ##
		value = int(self.images_npArray.shape[slider]*(value/100))
		if(slider == 0):
			self.show_images(X=value)
		elif(slider == 1):
			self.show_images(Y=value)
		elif(slider == 2):
			self.show_images(Z=value)



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Main(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
