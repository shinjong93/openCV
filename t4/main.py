import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pseudo.jpg',cv2.IMREAD_COLOR)
copy_img = img.copy()
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img2,(3,3),0)
cv2.imwrite('blur.jpg',blur)

canny = cv2.Canny(blur,100,200)
cv2.imwrite('canny.jpg',canny)

box1=[]
f_count=0
select=0
plate_width=0

cnts,contours,hierarchy = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    rect_area = w*h
    aspect_ratio = float(w)/h

    if(aspect_ratio >= 0.2) and (aspect_ratio <= 1.0) and (rect_area >= 100) and (rect_area <= 700):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        box1.append(cv2.boundingRect(cnt))

for i in range(len(box1)): ##Buble Sort on python
     for j in range(len(box1)-(i+1)):
          if box1[j][0]>box1[j+1][0]:
               temp=box1[j]
               box1[j]=box1[j+1]
               box1[j+1]=temp

#to find number plate measureing length between rectangles
for m in range(len(box1)):
     count=0
     for n in range(m+1,(len(box1)-1)):
          delta_x=abs(box1[n+1][0]-box1[m][0])
          if delta_x > 150:
               break
          delta_y =abs(box1[n+1][1]-box1[m][1])
          if delta_x ==0:
               delta_x=1
          if delta_y ==0:
               delta_y=1
          gradient =float(delta_y) /float(delta_x)
          if gradient<0.25:
              count=count+1
     #measure number plate size
     if count > f_count:
          select = m
          f_count = count;
          plate_width=delta_x
cv2.imwrite('snake.jpg',img)
