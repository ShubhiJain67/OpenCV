import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# print "Hello"
# print cam.get(cv2.CAP_PROP_FRAME_WIDTH)
while(True):

	tf,frame=cam.read()
	# print tf
	#(true/false,)
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Single frame',frame)
	#waitkey(1) is for video and (0) is for images
	key= cv2.waitKey(1)
	if key ==ord('c'):
		print "You have asked to quit"
		break
	elif key==ord('x'):
		print "Hello you hae presed x"
		
cam.release()
cv2.destroyAllWindows()