import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
  pass
cv2.namedWindow('Colorbars')
hh='Max'
hl='Min'
wnd = 'Colorbars'
cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min", "Colorbars",0,255,nothing)
img = cv2.imread('../images/fourierHist2.jpg',0)
img = cv2.resize(img, (900,900))
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
while(1):
   hul=cv2.getTrackbarPos("Max", "Colorbars")
   huh=cv2.getTrackbarPos("Min", "Colorbars")
   ret,thresh1 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY)
   # cv2.imshow(wnd)
   cv2.imshow("thresh1",thresh1)
   k = cv2.waitKey(1) & 0xFF
   if k == ord('m'):
     mode = not mode
   elif k == 27:
     break
cv2.destroyAllWindows()
