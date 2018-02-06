import cv2
import numpy as np
from matplotlib import pyplot as plt

def onMouse(x):
	pass

def control():
	img = cv2.imread('../images/fourierHist1.jpg')

	cv2.namedWindow('threshold')
	cv2.createTrackbar('value','threshold',0,255,onMouse)

	val = cv2.getTrackbarPos('value','threshold')
	whiteValue = 255

	while True:
		thsimg  = cv2.threshold(img,val,whiteValue,cv2.THRESH_BINARY)
			

		ret1,th1 = cv2.threshold(img,val,whiteValue,cv2.THRESH_BINARY)
		images = [img, 0, th1]
		titles = ['Original Noisy Image','Histogram','Threshold (v=' + str(val) + ')']

		for i in range(1):
			plt.subplot(1,3,i*3+1),plt.imshow(images[i*3],'gray')
			plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
			plt.subplot(1,3,i*3+2),plt.hist(images[i*3].ravel(),256)
			plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
			plt.subplot(1,3,i*3+3),plt.imshow(images[i*3+2],'gray')
			plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

		plt.show()

		#cv2.imshow('threshold',thsimg)

		#cv2.waitKey(0)		

		val = cv2.getTrackbarPos('value','threshold')
	
	cv2.destroyAllWindows()

control()
