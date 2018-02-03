import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

img[100,100] = [255,255,255]
"""
print(img.item(10,10,2))
"""

print(img.dtype)
