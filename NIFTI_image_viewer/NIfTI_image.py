# Import all the necessary packages
import numpy as np
import nibabel as nib                                                     # Read / write access to some common neuroimaging file formats
import matplotlib.pyplot as plt
import qimage2ndarray
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import sys


## will convert Nifti images to numpy arrays ##
class converter():
	def __init__(self, path="", Nifti_image=None):
		if(Nifti_image):
			self.image_obj = Nifti_image
		elif(path):
			self.image_obj = nib.load(path)
		else:
			self.image_obj = None

	## returns numpy array of Nifti image ##
	## uses qimage2ndarray to convert numpy array to QImage ##
	## this can be done without this library ##
	def toNumpyArray(self, path=None, Nifti_image=None):
		if(Nifti_image):
			return Nifti_image.get_fdata()
		elif(path):
			return nib.load(path).get_fdata
		else:
			return self.image_obj.get_fdata()

	## returns QImage of Nifti image ##
	def toQImageX(self, np_arr=None, section=100):
		if(np_arr):
			numpyImage = self.toNumpyArray(np_arr)
		else:
			numpyImage = self.toNumpyArray()
		numpyImage = numpyImage[:, section, :]
		return qimage2ndarray.array2qimage(numpyImage)

	def toQImageY(self, np_arr=None, section=100):
		if(np_arr):
			numpyImage = self.toNumpyArray(np_arr)
		else:
			numpyImage = self.toNumpyArray()
		numpyImage = numpyImage[:, section, :]
		return qimage2ndarray.array2qimage(numpyImage)

	def toQImageZ(self, np_arr=None, section=100):
		if(np_arr):
			numpyImage = self.toNumpyArray(np_arr)
		else:
			numpyImage = self.toNumpyArray()
		numpyImage = numpyImage[:, :, section]
		return qimage2ndarray.array2qimage(numpyImage)

## testing ##
if __name__ == "__main__":
	imag_obj = converter(path="./NIfTI images/training01_01_mprage_pp.nii.gz")
	image_obj_QImage = imag_obj.toQImageX()
	print(type(image_obj_QImage))
	image_obj_npArr = imag_obj.toNumpyArray()
	print(image_obj_npArr.shape)
	'''
	plt.imshow(image_obj_npArr[:, :, 100], cmap='gray')
	plt.axis('off');
	plt.show()
	'''
	app = QtWidgets.QApplication(sys.argv)
	label_imageDisplay = QtWidgets.QLabel()
	label_imageDisplay.setPixmap(QtGui.QPixmap(QtGui.QPixmap.fromImage(image_obj_QImage)))
	label_imageDisplay.setAlignment(QtCore.Qt.AlignCenter)
	label_imageDisplay.setScaledContents(True)
	label_imageDisplay.setMinimumSize(1,1)

	label_imageDisplay.show()
	sys.exit(app.exec_())