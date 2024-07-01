import cv2

image=cv2.imread("Tiger.jfif")

imageGRAY=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#resmi grileştirme

imageRGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#BGR(blue,green,red)değerini RGB(red,green,blue) ye çevirir

imagehsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#BGR olan değeri HSV(Hue, Saturation, Value) ye çevirir
cv2.imshow("Orji",image)
cv2.imshow("Gray",imageGRAY)
cv2.imshow("RGB",imageRGB)
cv2.imshow("HSV",imagehsv)


cv2.waitKey(0)
cv2.destroyAllWindows()

