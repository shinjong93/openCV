import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pseudo2.jpg',cv2.IMREAD_GRAYSCALE)

thresholder = 160
whiteValue = 255

blur = cv2.GaussianBlur(img,(5,5),0)

# global thresholding
ret1,th1 = cv2.threshold(img,thresholder,whiteValue,cv2.THRESH_BINARY)

images = [img, 0, th1]
titles = ['Original Noisy Image','Histogram','Threshold (v=' + str(thresholder) + ')']

for i in range(1):
    plt.subplot(1,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(1,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])


plt.show()
