import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# print "Hello"
# print cam.get(cv2.CAP_PROP_FRAME_WIDTH)
count=0
gray=False
normal=True
while(True):

	tf,frame=cam.read()
	# print tf
	if gray:
		frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# if normal:
	# 	frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
	cv2.imshow('Single frame',frame)
	
	key= cv2.waitKey(1)
	if key ==ord('q'):
		print "You have asked to quit"
		break
	elif key==ord('x'):
		print "Hello you hae pressed X"
	elif key==ord('s'):
		cv2.imwrite("./CaptureFrame/frame{}.png".format(count),frame)
		count+=1
		print "Frame saved with the name frame",count-1
	elif key==ord('g'):
		gray=True
		normal=False
		print "Changed to Gray Mode"
	elif key==ord('n'):
		normal=True
		gray=False
		print "Changed to Normal Mode"
		
		
cam.release()
cv2.destroyAllWindows()