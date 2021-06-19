# Import all the necessary packages
import numpy as np
import nibabel as nib                                                     # Read / write access to some common neuroimaging file formats
import matplotlib.pyplot as plt


## will convert Nifti images to numpy arrays ##
class image():
	def __init__(self, path="", Nifti_image=None):
		if(Nifti_image):
			self.image_obj = Nifti_image
		elif(path):
			self.image_obj = nib.load(path)
		else:
			self.image_obj = None

	## returns numpy array of Nifti image ##
	def toNumpyArray(self, path="", Nifti_image=None):
		if(Nifti_image):
			return Nifti_image.get_fdata()
		elif(path):
			return nib.load(path).get_fdata
		else:
			return self.image_obj.get_fdata()

## testing ##
if __name__ == "__main__":
	imag_obj = image(path="./NIfTI images/training01_01_mprage_pp.nii.gz")
	image_obj_npArr = imag_obj.toNumpyArray()
	plt.imshow(image_obj_npArr[:, :, 100], cmap='gray')
	plt.axis('off');
	plt.show()
