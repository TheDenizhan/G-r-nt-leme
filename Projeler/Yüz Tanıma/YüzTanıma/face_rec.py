from cv2 import*
from numpy import *
import time
import serial
#ardunio = serial.Serial(port='COM5',baudrate=115200,timeout=1)
recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read('code/code.yml')
cascadePath="haarcascade_frontalface_alt2.xml"
faceCascade=CascadeClassifier(cascadePath);

font=FONT_HERSHEY_SIMPLEX
cam2=VideoCapture(0)
#scale=10


while(True):
    ret,img2=cam2.read()

    #img2=flip(img2,1)
    #height, width, channels = img2.shape

    #centerX, centerY = int(height / 3), int(width / 3)
   #radiusX, radiusY = int(scale * height / 200), int(scale * width / 200)

#    minX, maxX = centerX - radiusX, centerX + radiusX
 #   minY, maxY = centerY - radiusY, centerY + radiusY

  #  cropped = img2[minX:maxX, minY:maxY]
   # resized_cropped = cv2.resize(cropped, (width, height))

    gray =cvtColor(img2,COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.5,4)

    for(x,y,w,h) in faces:
        rectangle(img2,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),4)
        Id,conf= recognizer.predict(gray[y:y+h,x:x+w])

        if   (Id == 1 and conf < 70):
                Id = "Hasan"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 2 and conf < 70):
                Id = "Leonel"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 3 and conf < 70):
                Id = "Furkan"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 4 and conf < 70):
                Id = "Umut"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 5 and conf < 70):
                Id = "Mert"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 6 and conf < 70):
                Id = "Erdal"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        elif   (Id == 7 and conf < 70):
                Id = "Cigdem"
                print(Id, conf)
                # ardunio.write(bytes('1','utf-8'))
        else:


                    Id = "Unknown"
                    print(Id, conf)
                    #ardunio.write(bytes('0', 'utf-8'))



        rectangle(img2, (x - 22, y - 90), (x + w + 22, y - 22), (0,255,0),-1)
        putText(img2, str(Id), (x, y - 40), font, 2, (0,0,0), 3)

    imshow('Yuz Tanima', img2)

    if waitKey(1)& 0xFF == ord('q'):
            break

cam2.release()
destroyAllWindows()