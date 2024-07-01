import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

esh = cv2.imread('img/eshabil.jpg',cv2.IMREAD_COLOR)
leo = cv2.imread('img/leonel.jpg',cv2.IMREAD_COLOR)
has= cv2.imread('img/hasan.jpg',cv2.IMREAD_COLOR)
ibr= cv2.imread('img/ibrahim.jpg',cv2.IMREAD_COLOR)
kad= cv2.imread('img/kadir.jpg',cv2.IMREAD_COLOR)
meh= cv2.imread('img/mehemet.jpg',cv2.IMREAD_COLOR)
muh= cv2.imread('img/muhammet.jpg',cv2.IMREAD_COLOR)
pel= cv2.imread('img/pelin.jpg',cv2.IMREAD_COLOR)
rek= cv2.imread('img/rektor.jpg',cv2.IMREAD_COLOR)
yav= cv2.imread('img/yavuz.jpg',cv2.IMREAD_COLOR)
zek= cv2.imread('img/zekeria.jpg',cv2.IMREAD_COLOR)
cag= cv2.imread('img/cagri.jpg',cv2.IMREAD_COLOR)



# Load a sample picture and learn how to recognize it.
eshabil_image = face_recognition.load_image_file("dataset_image/eshabil.jpg")
eshabil_face_encoding = face_recognition.face_encodings(eshabil_image)[0]

hasan_image = face_recognition.load_image_file("dataset_image/hasan.jpg")
hasan_face_encoding = face_recognition.face_encodings(hasan_image)[0]

leonel_image = face_recognition.load_image_file("dataset_image/leonel.jpg")
leonel_face_encoding = face_recognition.face_encodings(leonel_image)[0]

cagri_image = face_recognition.load_image_file("dataset_image/cagri.jpg")
cagri_face_encoding = face_recognition.face_encodings(cagri_image)[0]

ibrahim_image = face_recognition.load_image_file("dataset_image/ibrahim.jpg")
ibrahim_face_encoding = face_recognition.face_encodings(ibrahim_image)[0]

kadir_image = face_recognition.load_image_file("dataset_image/kadir.jpg")
kadir_face_encoding = face_recognition.face_encodings(kadir_image)[0]

mehemet_image = face_recognition.load_image_file("dataset_image/mehemet.jpg")
mehemet_face_encoding = face_recognition.face_encodings(mehemet_image)[0]

muhammet_image = face_recognition.load_image_file("dataset_image/muhammet.jpg")
muhammet_face_encoding = face_recognition.face_encodings(muhammet_image)[0]

pelin_image = face_recognition.load_image_file("dataset_image/pelin.jpg")
pelin_face_encoding = face_recognition.face_encodings(pelin_image)[0]

rektor_image = face_recognition.load_image_file("dataset_image/rektor.jpg")
rektor_face_encoding = face_recognition.face_encodings(rektor_image)[0]

yavuz_image = face_recognition.load_image_file("dataset_image/yavuz.jpg")
yavuz_face_encoding = face_recognition.face_encodings(yavuz_image)[0]

zekeria_image = face_recognition.load_image_file("dataset_image/zekeria.jpg")
zekeria_face_encoding = face_recognition.face_encodings(zekeria_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    leonel_face_encoding,
    hasan_face_encoding,
    cagri_face_encoding,
    ibrahim_face_encoding,
    kadir_face_encoding,
    mehemet_face_encoding,
    muhammet_face_encoding,
    pelin_face_encoding,
    rektor_face_encoding,
    yavuz_face_encoding,
    zekeria_face_encoding,
    eshabil_face_encoding
]
known_face_names = [
    "leonel",
    "hasan",
    "cagri",
    "ibrahim",
    "kadir",
    "mehemet",
    "muhammet",
    "pelin",
    "rektor",
    "yavuz",
    "zekeria",
    "eshabil"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        if name == "leonel":
            cv2.imshow('photo', leo)
        if name == "hasan" :
            cv2.imshow('photo', has)
        if name == "cagri" :
            cv2.imshow('photo', cag)
        if name == "ibrahim" :
            cv2.imshow('photo',ibr)
        if name == "kadir" :
            cv2.imshow('photo',kad)
        if name == "mehemed" :
            cv2.imshow('photo',meh)
        if name == "muhammet" :
            cv2.imshow('photo',muh)
        if name == "pelin" :
            cv2.imshow('photo',pel)
        if name == "rektor" :
            cv2.imshow('photo',rek)
        if name == "yavuz" :
            cv2.imshow('photo',yav)
        if name == "zekaria" :
            cv2.imshow('photo',zek)
        if name == "eshabil" :
            cv2.imshow('photo',esh)


    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()