import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)

plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

"""
cv2.nameWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('inamge',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
