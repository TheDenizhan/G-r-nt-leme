import cv2
import numpy as np

image=cv2.imread("Paint.png")
kernel=np.ones((3,3),np.uint8)

dilation=cv2.dilate(image,kernel,iterations=1)
#resimdeki hatları genişletme
erosion=cv2.erode(image,kernel,iterations=1)
#resimdeki hatları daraltma
dilation2=cv2.dilate(erosion,kernel,iterations=1)
#resimdeki hatları ilk önce daraltıp daha sonra elde edilen hatları genişletme
opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
#resimdeki hatları ilk önce daraltıp daha sonra elde edilen hatları genişletme
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
#resimdeki hatları ilk önce genişletip daha sonra elde edilen hatları daraltma
gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
#dilation işleminden erosion işlemini çıkartma
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
#orjinal resimden openning i çıkartma
blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)
#orjinal işlemden closing işlemini çıkartma



cross=cv2.morphologyEx(image,cv2.MORPH_CROSS,kernel)

ellipse=cv2.morphologyEx(image,cv2.MORPH_ELLIPSE,kernel)

#hitmiss=cv2.morphologyEx(image,cv2.MORPH_HITMISS,kernel)

rect=cv2.morphologyEx(image,cv2.MORPH_RECT,kernel)

cv2.imshow("orjinal",image)
cv2.imshow("dilation",dilation)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation2",dilation2)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradyan",gradyan)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)
cv2.imshow("cross",cross)
cv2.imshow("ellipse",ellipse)
#cv2.imshow("hitmiss",hitmiss)
cv2.imshow("rect",rect)




cv2.waitKey(0)
cv2.destroyAllWindows()