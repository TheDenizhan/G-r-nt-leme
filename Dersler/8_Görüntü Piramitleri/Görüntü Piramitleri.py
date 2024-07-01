import cv2

image=cv2.imread("butterfly.jfif")

ikikatB=cv2.pyrUp(image)
#iki kat büyük
ikikatK=cv2.pyrDown(image)
#iki kat küçük

print("orji",image.shape)
print("ikiKB",ikikatB.shape)
print("ikiKK",ikikatK.shape)

cv2.imshow("orj",image)
cv2.imshow("ikiKB",ikikatB)
cv2.imshow("ikiKk",ikikatK)

cv2.waitKey(0)
cv2.destroyAllWindows()
