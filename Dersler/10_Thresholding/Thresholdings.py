import cv2

image=cv2.imread("Rainy.jpg",0)
#SİMPLE THRESHOLDİNGS
ret1,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret2,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret3,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret4,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret5,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
ret6,thresh6=cv2.threshold(image,127,255,cv2.THRESH_MASK)

#ADAPTED THRESHOLDİNGS
Athresh1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                          cv2.THRESH_BINARY,11,2)
Athresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                          cv2.THRESH_BINARY,11,2)
#OTSU THRESHOLDİNGS
ret9,Othresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("Orjinal",image)
cv2.imshow("Binary",thresh1)
cv2.imshow("Binary İnv",thresh2)
cv2.imshow("Trunc",thresh3)
cv2.imshow("Tozero",thresh4)
cv2.imshow("Tozero İnv",thresh5)
cv2.imshow("Mask",thresh6)
cv2.imshow("Gassian",Athresh1)
cv2.imshow("Mean",Athresh2)
cv2.imshow("Binary+Otsu",Othresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

