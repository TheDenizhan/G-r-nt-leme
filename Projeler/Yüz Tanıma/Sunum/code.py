
from cv2 import*
from os import*
from face_recognition import*
from numpy import*
from PIL import Image
path="pic"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector=CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLaabels(path):

    imagePath=[os.path.join(path,f) for f in listdir(path)]

    faceSamples =[]

    ids =[]

    for imagePath in imagePath:

        PIL_img = Image.open(imagePath).convert('L')

        img_numpy=array(PIL_img,'uint8')

        id =int(os.path.split(imagePath)[-1].split(".")[1])
        print(id)

        faces =detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:

            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

faces,ids=getImagesAndLaabels('pic')
recognizer.train(faces,array(ids))
recognizer.write('code/code.yml')