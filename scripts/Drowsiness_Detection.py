#src is:https://github.com/akshaybahadur21/Drowsiness_Detection
#which is based on https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/
import cv2
import dlib
import time
import imutils
import threading
import numpy as np
from imutils import face_utils
from flask import Flask, render_template, Response

def eye_aspect_ratio(eye):
	A = np.linalg.norm(eye[1]-eye[5])
	B = np.linalg.norm(eye[2]-eye[4])
	C = np.linalg.norm(eye[0]-eye[3])
	ear = (A + B) / (2.0 * C)
	return ear
	
thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0) #"../data/glasses.mp4")
flag=0
eye_flag=0
last_eyes=time.time()
seconds_with_no_eyes=2.5

while True:
	ret, frame=cap.read()
	if not ret:
		print("failed to read cap")
		continue
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	if not subjects:
		if (time.time()-last_eyes)>seconds_with_no_eyes:
			print("Show me those eyes")
			cv2.putText(frame, "********Show Me those Eyes********", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
			cv2.putText(frame, "****************ALERT!****************", (10,325),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0,0), 2)
	else:  
		last_eyes=time.time()
              
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		print(ear)
		if ear < thresh:
			flag += 1
			print(flag)
			if flag >= frame_check:
				print("Alert")
				cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		else:
			flag = 0
cap.stop()
