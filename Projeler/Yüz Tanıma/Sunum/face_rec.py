from cv2 import*
from numpy import *

recognizer =cv2.face.LBPHFaceRecognizer_create()

recognizer.read('code/code.yml')
cascadePath="haarcascade_frontalface_default.xml"
faceCascade=CascadeClassifier(cascadePath);

font=FONT_HERSHEY_SIMPLEX
cam2=VideoCapture(0)



while(True):
    ret,img2=cam2.read()
    gray =cvtColor(img2,COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.2,5)

    for(x,y,w,h) in faces:
        rectangle(img2,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),4)
        Id,confidence= recognizer.predict(gray[y:y+h,x:x+w])

        if(0<Id and 51>Id):
            Id = "hasan"
            print(Id)
        elif(52<Id and 102>Id):
            Id = "mert"
            print(Id)
        elif (0<Id and 51>Id):
            Id = "hasan2"
            print(Id)
        elif (0<Id and 51>Id):
            Id = "mert22"
            print(Id)
        else:
            Id = "else"
            print(Id)

        rectangle(img2, (x - 22, y - 90), (x + w + 22, y - 22), (255,0, 0), -1)
        putText(img2, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)

    imshow('img2',img2)

    if waitKey(10)& 0xFF == ord('q'):
            break

cam2.release()
destroyAllWindows()