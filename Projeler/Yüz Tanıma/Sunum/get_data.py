
from cv2 import*

vid_cam = cv2.VideoCapture(0)


face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


face_id = 2


count = 52

while(True):

    _,img_frame=vid_cam.read()
    gray=cvtColor(img_frame,COLOR_BGR2GRAY)

    faces=face_detector.detectMultiScale(gray,1.2,5)

    for(x,y,w,h) in faces:
        rectangle(img_frame,(x,y),(x+w,y+h),(0,0,255),2)

        count+=1

        imwrite("pic/veri"+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
        imshow("frame",img_frame)

    if waitKey(50)& 0xFF == ord('q'):
        break

    elif count>100:
        break


vid_cam.release()
destroyAllWindows()