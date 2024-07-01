import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()

    cv2.rectangle(goruntu,(200,100),(462,450),(0,0,255),3)
    cv2.putText(goruntu, "TheDenizhan", (160,85), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (25, 25, 255), 2)

    cv2.imshow("goruntu",goruntu)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()