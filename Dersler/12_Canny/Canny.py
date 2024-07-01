import cv2
import numpy as np

def auto_canny(blur,sigma=0.33):

    v=np.median(blur)
    lower=int(max(0,(1.0-sigma)*v))
    upper =int(min(255,(1.0+sigma)*v))
    edged=cv2.Canny(blur,lower,upper)

    return edged;

image=cv2.imread("Rocks.jfif")
imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(imgray,(3,3),0)

canny=cv2.Canny(blur,100,1)
wide=cv2.Canny(blur,10,220)
tight=cv2.Canny(blur,200,230)
auto=auto_canny(blur)

cv2.imshow("orjinal",image)
cv2.imshow("gray",imgray)
cv2.imshow("blur",blur)
cv2.imshow("Canny",canny)

cv2.imshow("wide-tight-auto",np.hstack([wide,tight,auto]))

cv2.waitKey(0)
cv2.destroyAllWindows()

