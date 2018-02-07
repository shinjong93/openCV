from PIL import Image
import pytesseract as pyt
import argparse
import cv2
import os

img = cv2.imread('../images/fourierHist1.jpg',0)

text = pyt.image_to_string(Image.open('../images/bluredFouier2.jpg'))

print(text)
