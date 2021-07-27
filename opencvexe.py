import cv2 as cv
face_cascade=cv.CascadeClassifier("..\libs\haarscade_frontalface_default.xml")
face_cascade_eye = cv.CascadeClassifier('..\libs\haarcascade_eye.xml')
cap=cv.VideoCapture(0)
