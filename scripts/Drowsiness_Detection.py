#src is:https://github.com/akshaybahadur21/Drowsiness_Detection
#which is based on https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/
import cv2
import dlib
import time
import imutils
import threading
import numpy as np
from imutils import face_utils
from blink import  blue1,blue0,buzz1,buzz0,red1,red0,dbg

def eye_aspect_ratio(eye):
	A = np.linalg.norm(eye[1]-eye[5])
	B = np.linalg.norm(eye[2]-eye[4])
	C = np.linalg.norm(eye[0]-eye[3])
	ear = (A + B) / (2.0 * C)
	return ear
	
ear_thresh = 0.25
seconds_with_no_eyes=2.5
seconds_with_sub_ear=1.5

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0) #"../data/glasses.mp4")

last_eyes=time.time()
last_ear_uncritical=time.time()

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
			blue1()
			buzz1()
			cv2.putText(frame, "********Show Me those Eyes********", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
			cv2.putText(frame, "****************ALERT!****************", (10,325),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0,0), 2)
	else:  
		blue0()
		buzz0()
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
		if ear < ear_thresh:
			if (time.time()-last_ear_uncritical)>seconds_with_sub_ear:
				print("Alert")
				buzz1()
				red1()
				cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		else:
			buzz0()
			red0()
			last_ear_uncritical=time.time()
	if dbg:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break
if dbg:
    cv2.destroyAllWindows()
cap.stop()
