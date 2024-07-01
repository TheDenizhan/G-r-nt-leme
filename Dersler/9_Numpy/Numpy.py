import cv2
import numpy as np

image=np.zeros((450,450,3),"uint8")
#np.zeros((yükseklik,genişlik,kanal),veritipi)
print(image)
#zeros ile boş bir resim oluşturuyoruz

cv2.imshow("Boş",image)

cv2.waitKey(0)
cv2.destroyAllWindows()