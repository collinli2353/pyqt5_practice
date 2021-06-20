import Main_Window
from NIfTI_image import converter

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *


class Main(Main_Window.Ui_MainWindow):
	def __init__(self, MainWindow):
		self.setupUi(MainWindow)

		## QGraphicsView scenes (use .scene() to get scene) ##
		self.graphicsView_1.setScene(QGraphicsScene())
		self.graphicsView_2.setScene(QGraphicsScene())
		self.graphicsView_3.setScene(QGraphicsScene())
		self.graphicsView_4.setScene(QGraphicsScene())

		self.graphicsView_1.wheelEvent(self.event)

		## QGraphicsPixmapItem ##
		self.image = [None, None, None, None]

		## triggers ##
		self.actionOpen.triggered.connect(self.browse)

		self.horizontalSlider_1.valueChanged.connect(lambda value: self.changeValue(value, slider=0))
		self.horizontalSlider_2.valueChanged.connect(lambda value: self.changeValue(value, slider=1))
		self.horizontalSlider_3.valueChanged.connect(lambda value: self.changeValue(value, slider=2))


	## gets file location ##
	def browse(self):
		## set filter to open only files ending in specific types ##
		filter = "nii(*.nii);nii.gz(*nii.gz)"
		fname = QFileDialog.getOpenFileName(filter=filter)

		## will store the numpy arrays of the image
		self.image_obj_converter = converter(path = fname[0])
		self.images_npArray = self.image_obj_converter.toNumpyArray()

		## display images ##
		self.show_images(X = 100, Y = 100, Z = 100)

	def show_images(self, X = None, Y = None, Z = None):
		if(X):
			self.X_image = self.image_obj_converter.toQImageX(section = X)
			convertedX = QtGui.QPixmap.fromImage(self.X_image)
			if(self.image[0]):
				self.image[0].setPixmap(convertedX)
			else:
				self.image[0] = self.graphicsView_1.scene().addPixmap(convertedX)


			self.image[0].setFlag(QGraphicsItem.ItemIsMovable)
		
		if(Y):
			self.Y_image = self.image_obj_converter.toQImageY(section = Y)
			convertedY = QtGui.QPixmap.fromImage(self.Y_image)
			if(self.image[1]):
				self.image[1].setPixmap(convertedY)
			else:
				self.image[1] = self.graphicsView_2.scene().addPixmap(convertedY)
			self.image[1].setFlag(QGraphicsItem.ItemIsMovable)
		
		if(Z):
			self.Z_image = self.image_obj_converter.toQImageZ(section = Z)
			convertedZ = QtGui.QPixmap.fromImage(self.Z_image)
			if(self.image[3]):
				self.image[3].setPixmap(convertedZ)
			else:
				self.image[3] = self.graphicsView_3.scene().addPixmap(convertedZ)
			self.image[3].setFlag(QGraphicsItem.ItemIsMovable)
		

	## slider value changed ##
	def changeValue(self, value, slider):
		value = int(self.images_npArray.shape[slider]*(value/100))
		if(slider == 0):
			self.show_images(X=value)
		elif(slider == 1):
			self.show_images(Y=value)
		elif(slider == 2):
			self.show_images(Z=value)

	## wheel event for zoom ##
	def event(self, event: QWheelEvent):
		print("fda")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
