import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('C:/Users/Rahul/Desktop/photoshoot/IMG.jpg', cv2.IMREAD_COLOR)
cam = cv2.VideoCapture('videos/Cam1.mp4')
#cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
low_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_lowerbody.xml')

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    low = low_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (12, 150, 100), 2)
    for (x, y, w, h) in low:
        cv2.rectangle(img, (x, y), (x + w, y + h), (12, 150, 100), 2)

    cv2.imshow('image', img)
    cv2.waitKey(1)  # If you don'tput this line,thenthe image windowis just a flash. If you put any number other than 0, the same happens.

cam.release()
cv2.destroyAllWindows()