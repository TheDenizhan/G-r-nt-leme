import cv2

image=cv2.imread("Cizim.jpg")
#MEAN FILTER

meanfilter1=cv2.blur(image,(3,3))
meanfilter2=cv2.blur(image,(7,7))
meanfilter3=cv2.blur(image,(25,25))

#MEDİAN FİLTER

medianfilter=cv2.medianBlur(image,3)
medianfilter2=cv2.medianBlur(image,7)
medianfilter3=cv2.medianBlur(image,25)

#GAUSS FİLTER

gausfilter=cv2.GaussianBlur(image,(3,3),0)
gausfilter2=cv2.GaussianBlur(image,(7,7),0)
gausfilter3=cv2.GaussianBlur(image,(25,25),0)

cv2.imshow("orjinal",image)
cv2.imshow("MF(3,3)",meanfilter1)
cv2.imshow("MF(7,7)",meanfilter2)
cv2.imshow("MF(25,25)",meanfilter3)

cv2.imshow("MdF(3)",medianfilter)
cv2.imshow("MdF(7)",medianfilter2)
cv2.imshow("MdF(25)",medianfilter3)

cv2.imshow("GF(3,3)",gausfilter)
cv2.imshow("GF(7,7)",gausfilter2)
cv2.imshow("GF(25,25)",gausfilter3)

cv2.waitKey(0)
cv2.destroyAllWindows()