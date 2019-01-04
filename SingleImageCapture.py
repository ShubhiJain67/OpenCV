import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# print "Hello"
# print cam.get(cv2.CAP_PROP_FRAME_WIDTH)

tf,frame=cam.read()
count=0
#(true/false,)

if frame is None:
	print "None"
else:
		
	cv2.imshow('Single frame',frame)
	key=cv2.waitKey(0)
	if key==ord('c'):
		cv2.imwrite("frame{}.png".format(count),frame)
		count+=1
		print "Frame is saved!"
		print "Exited"
	elif key==ord('q'):
		print "You pressed the Quit button"


	
	cam.release()
	cv2.destroyAllWindows()