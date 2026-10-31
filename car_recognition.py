import cv2
import numpy

video = cv2.VideoCapture("Cars.mp4")
car_cascade = cv2.CascadeClassifier("cars.xml")
while video.isOpened():
    returnvalue,image = video.read()
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray_img,1.1,2)
    for car in cars:
        x,y,w,h = car
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)


    cv2.imshow("cars",image)
    key = cv2.waitKey(10)
    if key == 27:
        break