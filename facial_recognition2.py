import cv2
import os
import numpy
data = "data_sets"
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
images = []
labels = []
names = {}
id = 0

for (subdirecteories,directeories,files) in os.walk(data):
    for subdirectory in directeories:
        names[id] = subdirectory
        subject_path = os.path.join(data,subdirectory)
        for filename in os.listdir(subject_path):
            path = os.path.join(subject_path,filename)
            image = cv2.imread(path)
            images.append(image)
            label = id
            labels.append(label)

        id+=1
(images,labels) = [numpy.array(lis) for lis in [images,labels]]

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)
while True:
     answer,frame = webcam.read()
     face_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(frame,1.3,4)
     for face in faces:
         x,y,w,h = face
         rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
         face = face_grey[y:y+h,x:x+w]
         face_resize = cv2.resize(face,(130,100))
         label,score = model.predict(face_resize)
         if score < 500:
             cv2.putText(frame,"%s-%.0f"%(names[label],score),(30,10),font = cv2.FONT_ITALIC,fontScale= 1,color= (255,0,0))
         else:
             cv2.putText(frame,"PERSON NOT IDENTIFIED",(30,10),font = cv2.FONT_ITALIC,fontScale= 1,color=(0,0,255))

     cv2.imshow("text",frame)
     key = cv2.waitKey(10)
     if key == 27:
         break
     
         
     
         
         
         

