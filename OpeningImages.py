import cv2

img1=cv2.imread('./RefernceImage/image1.jpeg')

img2=cv2.imread('./RefernceImage/image2.jpeg',cv2.IMREAD_COLOR)

# img=cv2.imread('project3.jpeg',cv2.IMREAD_GRAYSCALE)
if img1 is None:
	print "Object Doesnot exist!"
else:
	# print img
	cv2.imshow('first Image',img1)

	cv2.waitKey(0) #until ny key is pressed
	cv2.destroyAllWindows()

