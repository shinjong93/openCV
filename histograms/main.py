import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img1 = cv2.imread('pseudo.jpg',cv2.IMREAD_GRAYSCALE)
#img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])

plt.subplot(221),plt.imshow(img1,'gray'),plt.title('Red Line')
plt.subplot(223),plt.plot(hist1,color='r')
plt.xlim([0,256])
plt.show()
