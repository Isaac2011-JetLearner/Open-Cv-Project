import cv2
import os

imgs  = "data_sets"
person = "isaac"
path = os.path.join(imgs,person)
if not os.path.isdir(path):
    os.mkdir(path)

webcam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in range(30):
    answer,frame = webcam.read()
    if answer == False:
        break
    faces = face_cascade.detectmultiscale(frame,1.3,4)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),"green",1)
        face = frame[y:y+h,x:x+w]
        cv2.imwrite("%s/%s.png"%(path,i+1),face)
        
    cv2.imshow("picture",frame)
    key = cv2.waitKey(0)
    if key == 27:
        break



    
