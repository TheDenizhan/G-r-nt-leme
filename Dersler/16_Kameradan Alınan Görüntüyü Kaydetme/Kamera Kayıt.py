import cv2
import numpy as np

#Kameradan alınan canlı görüntünün kayıt edilmesi
camera=cv2.VideoCapture(0)
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)
fourcc=cv2.VideoWriter_fourcc(*'MP4V')
#Kameradan alınacak görüntünün hangi türde kayıt edileceğini belirler
writer=cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height))
#sayı küçüldükçe video hızı azalır,sayı büyükçe video hızı artar
while True:
    ret,frame=camera.read()
    writer.write(frame)
    cv2.imshow("Kamera",frame)

    if  cv2.waitKey(10)  & 0xFF == ord('q'):
        break

camera.release()
writer.release()
cv2.destroyAllWindows()
