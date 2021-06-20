import Main_Window
from NIfTI_image import converter

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class Main(Main_Window.Ui_MainWindow):
	def __init__(self, MainWindow):
		self.setupUi(MainWindow)

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
			convertedX = QWidgets.QGraphicsPixmapItem(QtGui.QPixmap(QtGui.QPixmap.fromImage(self.X_image)))
			self.graphicsView_1.addItem(convertedX)
		'''
		if(Y):
			Y_image = self.image_obj_converter.toQImageY(section = Y)
			self.graphicsView_2.addPixmap(QtGui.QPixmap(QtGui.QPixmap.fromImage(Y_image)))
		
		if(Z):
			Z_image = self.image_obj_converter.toQImageZ(section = Z)
			self.graphicsView_3.addPixmap(QtGui.QPixmap(QtGui.QPixmap.fromImage(Z_image)))
		'''

	## slider value changed ##
	def changeValue(self, value, slider):
		value = int(self.images_npArray.shape[slider]*(value/100))
		if(slider == 0):
			self.show_images(X=value)
		elif(slider == 1):
			self.show_images(Y=value)
		elif(slider == 2):
			self.show_images(Z=value)

	## mouse press for zoom ##
	def mousePressEvent(self, event):
		pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
