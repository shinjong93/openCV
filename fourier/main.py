import cv2
import numpy as np
import matplotlib.pyplot as plt

def fourier():
	img = cv2.imread('../images/histPseudo.jpg', cv2.IMREAD_GRAYSCALE)
	
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)

	rows , cols = img.shape
	crow, ccol = int(rows/2), int(cols/2)

	ranges = 5

	fshift[crow-ranges:crow+ranges, ccol-ranges:ccol+ranges] = 0

	f_ishift = np.fft.ifftshift(fshift)
	img_back = np.fft.ifft2(f_ishift)
	img_back = np.abs(img_back) 


	plt.subplot(131), plt.imshow(img,cmap = 'gray')
	plt.title('input image'), plt.xticks([]), plt.yticks([])

	plt.subplot(132), plt.imshow(img_back, cmap = 'gray')
	plt.title('after HRF'), plt.xticks([]), plt.yticks([])

	plt.subplot(133), plt.imshow(img_back)
	plt.title('result in JET'), plt.xticks([]), plt.yticks([])

	plt.show()

	cv2.imwrite('../images/fourierHist2.jpg',img_back)

fourier()
